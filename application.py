from flask import Flask
from flask import render_template
import secrets

app = Flask(__name__)

def random_quote:
	quote_list = ["Bite my shiny, metal ass!"]
	quote_list.append = ["Hey sexy mama, wanna kill all humans?"]
	quote_list.append = ["You know what cheers me up? Other people's misfortune."]
	quote_list.append = ["I'm so embarrassed. I wish everyone else was dead!"]
	return secrets.choice(quote_list)

@app.route("/")
def index():
	return render_template("bender.html", quote = random_quote())

'''
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
'''
