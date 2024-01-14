from flask import Flask, request
import os
from dotenv import load_dotenv
from helpers.get_diagnosis import get_diagnosis


app = Flask(__name__)

@app.route('/')
def index():
    return 'heroku server tracking repo'
    
'''
    Takes in input text from GET request in the "text" field
    Return a string of the predicted diagnosis
'''
@app.route('/get_diagnosis/', methods = ['GET'])
def diagnose():
    # input_text = 'i have a headache and stomach pain i also have a severe cough and have lost a lot of weight recently what do i do'
    input_text = request.args.get('text')
    return get_diagnosis(input_text, os.environ.get('OPENAI_API_KEY'))

if __name__ == '__main__':    
    load_dotenv()
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
    