# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

from firebase_functions import https_fn, options, firestore_fn
from firebase_admin import initialize_app, firestore
import google.cloud.firestore

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

@https_fn.on_request(cors=cors)
def on_request_example(req: https_fn.Request) -> https_fn.Response:
    print(req)
    retval = testfns.hello() 
    return https_fn.Response(retval)

@https_fn.on_request(cors=cors)
def login(req: https_fn.Request) -> https_fn.Response:
    try: 
        service = googleops.drive_auth()
        user = service.about().get(fields='user').execute()
        retval = {"user": user, "status":"success"}
        return https_fn.Response(json.dumps(retval),mimetype='application/json')
    except:
        e = sys.exc_info()[0]
        # TODO(developer) - Handle errors individually
        print(f'An error occurred: {e}')
        return https_fn.Exception(500,e,None)


# --------------------------------------------------------------------------------------

@https_fn.on_request()
def addmessage(req: https_fn.Request) -> https_fn.Response:
    """Take the text parameter passed to this HTTP endpoint and insert it into
    a new document in the messages collection."""
    # Grab the text parameter.
    original = req.args.get("text")
    if original is None:
        return https_fn.Response("No text parameter provided", status=400)

    firestore_client: google.cloud.firestore.Client = firestore.client()

    # Push the new message into Cloud Firestore using the Firebase Admin SDK.
    _, doc_ref = firestore_client.collection("messages").add(
        {"original": original}
    )

    # Send back a message that we've successfully written the message
    return https_fn.Response(f"Message with ID {doc_ref.id} added.")


@firestore_fn.on_document_created(document="messages/{pushId}")
def makeuppercase(
    event: firestore_fn.Event[firestore_fn.DocumentSnapshot | None],
) -> None:
    """Listens for new documents to be added to /messages. If the document has
    an "original" field, creates an "uppercase" field containg the contents of
    "original" in upper case."""

    # Get the value of "original" if it exists.
    if event.data is None:
        return
    try:
        original = event.data.get("original")
    except KeyError:
        # No "original" field, so do nothing.
        return

    # Set the "uppercase" field.
    print(f"Uppercasing {event.params['pushId']}: {original}")
    upper = original.upper()
    event.data.reference.update({"uppercase": upper})

@https_fn.on_request()
def movephotos(req: https_fn.Request) -> https_fn.Response:
    """This will kick off the process of moving photos and videos from Drive 
    to Photos, based on the Firebase database"""

    firestore_client: google.cloud.firestore.Client = firestore.client()

    folders_ref = firestore_client.collection('folders')
    folders = folders_ref.get()

    response = ""
    for folder in folders:
        response += f'{folder} \n'

    # Send back a message that we've successfully written the message
    return https_fn.Response(f"{response}")
