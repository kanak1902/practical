from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Serverless Computing!"

@app.route("/hello")
def hello():
    return f"Hello {request.args.get('name', 'Student')}!"

app.run(host="0.0.0.0", port=10000)
