# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

from firebase_functions import https_fn, options
from firebase_admin import initialize_app

initialize_app()

import sys
import json

import testfns
import googleops

# globals
success = 'success'
failure = 'failure'

# Disable CORS
cors = options.CorsOptions('*',['POST','GET'])

@https_fn.on_request()
def on_request_example(req: https_fn.Request) -> https_fn.Response:
    print(req)
    retval = testfns.hello() 
    return https_fn.Response(retval)

@https_fn.on_request(cors=cors)
def login(req: https_fn.Request) -> https_fn.Response:
    try: 
        googleops.get_creds()
        retval = {"status":"success"}
        return https_fn.Response(json.dumps(retval),mimetype='application/json')
    except:
        e = sys.exc_info()[0]
        # TODO(developer) - Handle errors individually
        print(f'An error occurred: {e}')
        return https_fn.Exception(500,e,None)

