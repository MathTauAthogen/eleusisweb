from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def homePage():
    return render_template("main_page_template.html")

ids=[0,1,2,3,4,5,6,78,9,10]

maxSize=8

@app.route('/ajax/<string:typeof>')
def ajaxRequest(typeof):
	if(typeof == "id"):
		print("LOL")
		if(request.data['id'].zfill(maxSize) in ids):
			return True
		else:
			return False

@app.route('/res/<string:name>')
def resRequest(name):
	if(typeof == "id"):
		print("LOL")
		if(request.data['id'].zfill(maxSize) in ids):
			return True
		else:
			return False

if __name__ == '__main__':
   app.run('127.0.0.1', '5000', debug = True)