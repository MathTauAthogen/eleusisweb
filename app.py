from flask import Flask, render_template, send_from_directory, request
import json
app = Flask(__name__, static_folder='res', static_url_path='')
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('eleusiscg-firebase-adminsdk-jeb4f-b498a90783.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route('/')
def homePage():
    return render_template("main_page_template.html")

maxSize=8#Hardcode

@app.route('/testing')
def testFunc():
	db.collection(u'currentgames').document(u'1'.zfill(maxSize)).collection(u'users')
	return 'Success!'

@app.route('/ajax/<string:typeof>', methods=["POST"])
def ajaxRequest(typeof):
	if(typeof == "id"):
		if(str(request.get_json(force=True)['id']).zfill(maxSize) in ids):
			return json.dumps({'valid': 'true'})
		else:
			return json.dumps({'valid': 'false'})
	#if(typeof == "user"):
	#if(typeof == "id"):
	#if(typeof == "id"):

if __name__ == '__main__':
   app.run(host = '0.0.0.0', port = '5050', debug = True)
