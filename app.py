# -*- coding: utf-8 -*-
from flask import Flask, render_template, send_from_directory, request, redirect, url_for, session
import json
app = Flask(__name__, static_folder='res', static_url_path='')
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import random

cred = credentials.Certificate('eleusiscg-firebase-adminsdk-jeb4f-b498a90783.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route('/')
def homePage():
    return render_template("main_page_template.html")

maxSize=8#Hardcode

cardvalues=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
cardsuits=["D","H","C","S"]
allcards=[]
for i in cardsuits:
	for j in cardvalues:
		allcards.append(i+j)

@app.route('/testing')
def testFunc():
	db.collection(u'currentgames').document(u'1'.zfill(maxSize)).collection(u'users').document("b").set({})
	o=""
	copyofcards=allcards*3
	while(len(copyofcards)>0):
		randindex=random.randint(0,len(copyofcards)-1)
		o+=copyofcards[randindex]
		copyofcards.pop(randindex)
		if(len(copyofcards) != 0):
			o+=" "
	db.collection(u'currentgames').document(u'1'.zfill(maxSize)).set({"cards":o.decode('utf_8'),"started":"no"})
	return 'Success!'

@app.route("/verify", methods=["POST"])
def validate():
	data = request.form
	ids=[doc.id.zfill(maxSize) for doc in db.collection(u'currentgames').get()]
	if(data['id'].zfill(maxSize) in ids):
		doc_ref=db.collection(u'currentgames').document(data['id'].zfill(maxSize)).collection(u'users').document(str(data['name']))
		exists = True
		try:
			doc_ref.get()
		except Exception as e:
			exists = False
		if(len(data['name'])>1 and exists):
			doc_ref=db.collection(u'currentgames').document(data["id"].zfill(maxSize)).collection(u'users').document(str(data['name']))
			if(doc_ref.get().to_dict()['pass']==data["pass"]):
				session['name']=data['name']
				session['password']=data['pass']
				session['id']=data['id']
				return redirect(url_for("startGame"))
			else:
				return redirect("/")
		elif(len(data['name'])>1):
			doc_ref=db.collection(u'currentgames').document(data["id"].zfill(maxSize)).collection(u'users').document(data['name'])
			doc_ref.set({"pass":data["pass"]})
			session['name']=data['name']
			session['password']=data['pass']
			session['id']=data['id']
			return redirect(url_for("startGame"))
		else:
			return redirect("/")
	return redirect("/")

@app.route('/game', methods=["GET","POST"])
def startGame():
	data = session
	if(request.method=="GET" and db.collection(u'currentgames').document(data['id'].zfill(maxSize)).get()['started']=='no'):
		return render_template("game_page_template.html", users=[doc.id for doc in db.collection(u'currentgames').document(data['id'].zfill(maxSize)).collection(u'users').get() if doc.id != 'b'], you=data['name'])
	elif(request.method=="POST"):
		db.collection(u'currentgames').document(data['id'].zfill(maxSize)).update({"started":"yes"})
		db.collection(u'currentgames').document(data['id'].zfill(maxSize)).update({"dealer":data['user']})
		return redirect(url_for("startGame"))
	else:
		dealer=db.collection(u'currentgames').document(data['id'].zfill(maxSize)).get()['dealer']
		return render_template("game_page_template.html", users=[doc.id for doc in db.collection(u'currentgames').document(data['id'].zfill(maxSize)).collection(u'users').get() if doc.id != 'b'], you=data['name'], dealer=dealer)

app.secret_key="LOLASDGJIET@%$^)NDLKJEH435646TLIUSBRgadfkhsdt346 IJVHTILU"
if __name__ == '__main__':
   app.run(host = '0.0.0.0', port = '5053', debug = True)