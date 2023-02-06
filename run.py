from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/index")
@app.route('/')
def index_template():
	return render_template('index.html', title='Vegas Tracker')

@app.route('/about')
def about_template():
	return render_template('about.html', title='About')

@app.route('/future')
def future_template():
	return render_template('future.html', title='Futures')

if __name__ =='__main__':
	app.run(debug=True)