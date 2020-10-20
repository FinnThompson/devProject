from flask import Flask, render_template, json

app = Flask(__name__)

@app.route('/')
def helloWorld():
	return render_template("index.html")

@app.route('/hello/')
@app.route('/hello/<name>')
def helloName(name = None):
	return render_template("hello.html", name=name)

@app.route('/parks/')
def parks():
	with open('parks.json', 'r') as f:
		parks = json.load(f)
	return render_template("parks.html", parks = parks)

@app.route('/hand/')
@app.route('/hand/<name>')
def washHands(name = None):
	return render_template("hand.html", name = name)

if __name__ == "__main__":
	app.run()