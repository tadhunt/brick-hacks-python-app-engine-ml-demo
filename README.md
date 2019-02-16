
This application is an example app that does sentiment analysis, and it
can be uploaded to App Engine and run there, or locally in your python
environment

To run locally, from this directory do Do this to verify it works.
This is the fastest way to make sure you've got the app working correctly.

  virtualenv env
  source env/bin/activate
  pip install -r requirements.txt
  python main.py

To install onto App Engine, from this directory do:

  gcloud components install app-engine-python # you need to do this once
  gcloud app deploy                           # do this every time you make a change
