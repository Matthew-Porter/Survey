from flask import Flask, render_template, request, redirect 
app= Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
	
	print "Got Post Info"

	user = request.form['user']
	location = request.form['location']
	languages = request.form['languages']
	comment = request.form['comment']

	return render_template('result.html', user = user, location = location, languages = languages, comment = comment)
	return request('/', )
app.run(debug=True)

