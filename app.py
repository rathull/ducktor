from flask import Flask
import os
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return 'heroku server tracking repo'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))