from flask import Flask
app = Flask(__name__)

@app.route('/login/<username>')
def show_welcome(username):
	return 'Hi %s ' % username

@app.route('/add/<int:number>')
def add_one(number):
	return '%d' % (number+1)

@app.route('/school/')
def schools():
	return 'The school page'

@app.route('/student')
def students():
	return 'The student page'

if __name__ == '__main__':
	app.run()