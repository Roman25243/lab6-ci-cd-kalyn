from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return {"message": "Github CI/CD Actions"}


@app.route("/info")
def info():
    return {"version": "1.0", "status": "running"}


@app.route("/page")
def page():
    return "<h1>Welcome to CI/CD Demo</h1>"


if __name__ == "__main__":
    app.run()
