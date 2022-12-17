from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from werkzeug.exceptions import abort

import os, time, uuid
from . import kvutils
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials

from . import cosmosdbwithoutasync
import asyncio
import json


bp = Blueprint('predictions', __name__)

@bp.route('/', methods=('GET', 'POST'))
def predict():
    if request.method == 'POST':
        local_file_name =  request.files["filename"].filename
        bytes_data = request.files["filename"].read()

        credential = kvutils.credential
        account_url = kvutils.account_url 
        container_name = kvutils.container_name 
        blob_service_client = BlobServiceClient(account_url, 
    credential=credential)
        blob_client = blob_service_client.get_blob_client(container=container_name, 
        blob=local_file_name)
        blob_client.upload_blob(bytes_data,overwrite = True)

        full_file_name = account_url + "/" + container_name + "/" + local_file_name

        ENDPOINT = kvutils.ENDPOINT
        prediction_key = kvutils.prediction_key
        prediction_resource_id = "paddy"
        project_id = kvutils.project_id
        publish_iteration_name = kvutils.publish_iteration_name

         # Now there is a trained endpoint that can be used to make a prediction
        prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
        predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)

        results = predictor.classify_image(
                project_id, publish_iteration_name, bytes_data)

        result_dict ={}
        result_dict["category"] = "cassava"
        result_dict["filename"] = local_file_name
        result_dict["id"] = 'cassava_' + str(uuid.uuid4())

        for prediction in results.predictions:
            result_dict[prediction.tag_name] = round(prediction.probability * 100,3)

        cosmosdbwithoutasync.create_item(result_dict)
        

        return render_template('predictions/index.html',
        filename = local_file_name,
        predictionresults = results.predictions,
        fullfilename = full_file_name)

    return render_template('predictions/predict.html')

@bp.route('/predictions')
def index():
    return render_template('predictions/index.html')

@bp.route('/allitems', methods=('GET', 'POST'))
def allitems():

    if request.method == 'POST':
        qry =  request.form["filename"]
        results = cosmosdbwithoutasync.get_items(qry)
        return render_template('predictions/allitems.html',allitems = results)
   
    results = cosmosdbwithoutasync.get_all_items()
    return render_template('predictions/allitems.html',allitems = results)