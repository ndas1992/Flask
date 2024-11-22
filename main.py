from flask import Flask, render_template
'''
Itcreates an instance of the flask class
which will be your WSGI (Web Server Gateway Interface) application.

'''
##### WSGI Application
app = Flask(__name__)

@app.route("/")
def Welcome():
    return "<html><H1>Welcome to this best Flask course. This should be an amazing course</H1></html>"

@app.route("/index")
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)