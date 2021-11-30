from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/jobs")
def jobs():
    # return "Hello World!"
    return render_template('index.html')

