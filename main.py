from flask import Flask, render_template, request
from werkzeug.exceptions import HTTPException


app = Flask("app")

@app.route("/")
def index():
	return render_template("index.html")

@app.errorhandler(Exception)
def error(e):
  code = 500
  if isinstance(e, HTTPException):
    code = e.code
    return render_template("error.html", e=str(e)), code

@app.route("/api", methods=["GET", "POST"])
def api():
	data = request.args.get("data")

	if data is None:
		return {"type": "Error", "content": "No data requested"}
	elif data == "1":
		return {"type": "Data", "content": "Yay! Request successful!"}
	else:
		return {"type": "Error", "content": "Data specified does not exist"}

@app.route("/docs")
def docs():
  global hits
  hits += 1
  return render_template("docs.html")

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8000)