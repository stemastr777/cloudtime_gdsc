# import the Flask class from the flask module
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import requests
import json

# create the application object
app = Flask(__name__)
CORS(app)

# use decorators to link the function to a url
@app.route('/')
def home():
    return render_template('index.html')  # return main page

@app.route('/questions')
def questions():
    args = request.args
    q_list = requests.get("https://quiz-gen-1-4riej3ojca-et.a.run.app", params={'topic': args['topic'], 'diff': args['diff'], 'num_q': args['num_q']}).content
    return render_template('quiz.html', questions=json.loads(q_list))

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8081)
