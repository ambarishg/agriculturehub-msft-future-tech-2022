import flaskr

if __name__ == "__main__":
       app = flaskr.create_app()
       app.run(host='0.0.0.0', debug=True)