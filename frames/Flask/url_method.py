from flask import Flask
app = Flask(__name__)

@app.route('/Message', methods = ['POST'])
def do_send():
	return "This is for POST method"

@app.route('/Message', methods = ['GET'])
def show_the_send_form():
	return "This is for GET method"

if __name__ == '__main__':
	app.run()