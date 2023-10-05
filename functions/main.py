# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

from firebase_functions import https_fn
from firebase_admin import initialize_app

import testfns
# import googleops

initialize_app()
#
#
@https_fn.on_request()
def on_request_example(req: https_fn.Request) -> https_fn.Response:
    retval = testfns.hello()
    return https_fn.Response(retval)

@https_fn.on_request()
def on_get_creds(req: https_fn.Request) -> https_fn.Response:
    # retval = googleops.get_creds()
    return https_fn.Response('That worked??')
