from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello"

@app.route('/test')
def index():
   return render_template('bender.html')
	
#if __name__ == "__main__":
#    app.run(host="0.0.0.0", port=int("5000"), debug=True)
