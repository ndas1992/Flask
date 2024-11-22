from flask import Flask, jsonify, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/', method=["GET"])
def welcome():
    return render_template('welcome.html')

if __name__ == "__main__":
    app.run(debug=True)

