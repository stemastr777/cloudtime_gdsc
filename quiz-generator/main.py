from flask import Flask
from flask import request
from flask import Response                                #<-CHANGED
from flask_cors import CORS, cross_origin
import string
import random

import vertexai                                           #<-CHANGED
from vertexai.language_models import TextGenerationModel  #<-CHANGED
import os

# Default model settings                                  #<-CHANGED
MODEL = "text-bison"                                      #<-CHANGED
MAX_TOKENS = 1024                                         #<-CHANGED
TOP_P = 0.8                                               #<-CHANGED
TOP_K = 40                                                #<-CHANGED
TEMP = 0.5                                                #<-CHANGED

# Default quiz settings
TOPIC = "GCP"
NUM_Q = 2
DIFF = "advanced"
KEY = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 5))  

PROMPT = """
Generate a quiz according to the following specifications:

- topic: {topic}
- num_q: {num_q}
- diff:  {diff}

Output should be (only) an unquoted json array of objects with keys "question", "responses", and "correct".
Randomize the questions and dont use (') notation
{key}
"""


app = Flask(__name__)  # Create a Flask object.
CORS(app)
PORT = os.environ.get("PORT")  # Get PORT setting from environment.
if not PORT:
    PORT = 8080


# Initialize Vertex AI access.
vertexai.init(project="<YOUR PROJECT ID>", location="us-central1")  #<-CHANGED
parameters = {                                                 #<-CHANGED
    "candidate_count": 1,                                      #<-CHANGED
    "max_output_tokens": 1024,                                 #<-CHANGED
    "temperature": 0.2,                                        #<-CHANGED
    "top_p": 0.8,                                              #<-CHANGED
    "top_k": 40,                                               #<-CHANGED
}                                                              #<-CHANGED
model = TextGenerationModel.from_pretrained(MODEL)             #<-CHANGED


# This function takes a dictionary, a name, and a default value.
# If the name exists as a key in the dictionary, the corresponding
# value is returned. Otherwise, the default value is returned.
def check(args, name, default):
    if name in args:
        return args[name]
    return default


# The app.route decorator routes any GET requests sent to the /generate
# path to this function, which responds with "Generating:" followed by
# the body of the request.
@app.route("/", methods=["GET", "OPTIONS"])
# This function generates a quiz using Vertex AI.
def generate():
    args = request.args
    topic = check(args, "topic", TOPIC)
    num_q = check(args, "num_q", NUM_Q)
    diff = check(args, "diff", DIFF)
    prompt = PROMPT.format(topic=topic, num_q=num_q, diff=diff, key=KEY)
    response = model.predict(prompt, **parameters)      #<-CHANGED
    print(f"Response from Model: {response.text}")      #<-CHANGED
    html = f"{response.text}"                           #<-CHANGED
    response = Response(html, mimetype="application/json")  #<-CHANGED
    return response

# def _build_cors_preflight_response(preflight_response):
#     preflight_response.headers.add("Access-Control-Allow-Origin", "*")
#     preflight_response.headers.add('Access-Control-Allow-Headers', "*")
#     preflight_response.headers.add('Access-Control-Allow-Methods', "*")
#     return preflight_response

# def _corsify_actual_response(actual_response):
#     actual_response = preflight_response
#     actual_response.headers.add("Access-Control-Allow-Origin", "*")
#     return actual_response



# This code ensures that your Flask app is started and listens for
# incoming connections on the local interface and port 8080.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=True)
