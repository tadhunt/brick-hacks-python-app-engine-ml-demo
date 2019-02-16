# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_app]

#
# This application is an example app that does sentiment analysis,
# and it can be uploaded to App Engine and run there, or locally in your
# python environment
#
# To run locally, from this directory do:
#   virtualenv env
#   source env/bin/activate
#   pip install -r requirements.txt
#   python main.py

#
# To install onto App Engine, from this directory do:
#   gcloud components install app-engine-python # you need to do this once
#   gcloud app deploy                           # do this every time you make a change

import os
import json
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from google.oauth2 import service_account
from flask import Flask
from flask import request

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

#
# Before this app will work, you will need to provide a private key for a service account
#
# To get the private key:
# 1. browse to: https://console.cloud.google.com/apis/credentials
# 2. select Create Credentials -> Service Account Key
# 3. Select "New Service Account" on the service account dropdown
# 4. Give your service account a name, and set the role to "Owner"
# 5. Select the "JSON" radio button
# 6. Press the download button, and download the key
# 7. copy-paste the content of the downloaded file between the """'s in the private-key variable definiton below
#
private_key = """
"""

#print(private_key)

project_id = 'rit-brick-hacks-feb-2019'
info = json.loads(private_key, strict=False)
credentials = service_account.Credentials.from_service_account_info(info)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return '<p style="font-size:40px">Hello Brick Hacks!!</p>'

#
# To do sentiment analysis using the language service client, you'll need to enable the language API in your project.
# When you run the app locally (python main.py)
@app.route('/sentiment')
def sentiment():
    """do a sentiment analysis on the fragment."""

    # The text to analyze
    text = request.args.get('text')
    if text == None:
            return "Missing query"

    # Instantiates a client
    client = language.LanguageServiceClient(credentials=credentials)

    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment

    return '<p style="font-size:40px">Text: {}<br>\nSentiment {}, {}</p>'.format(text, sentiment.score, sentiment.magnitude)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
