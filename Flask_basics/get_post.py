from flask import Flask, render_template, request
'''
Itcreates an instance of the flask class
which will be your WSGI (Web Server Gateway Interface) application.

'''
##### WSGI Application
app = Flask(__name__)

@app.route("/")
def Welcome():
    return "<html><H1>Welcome to this best Flask course. This should be an amazing course</H1></html>"

@app.route('/form', methods=['GET', 'POST'])
def form():
    return render_template('form.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method=='POST':
        name = request.form['name']# request.form[id from form in form.html]
        return f'Hello {name}!'
    return render_template('form.html')




if __name__ == "__main__":
    app.run(debug=True)