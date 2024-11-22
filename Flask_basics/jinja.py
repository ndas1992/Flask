'''
{{}} expression to print output in html
{%.....%} conditions, for loops
{#...#} this is for comments
'''



from flask import Flask, render_template, request, redirect, url_for
'''
Itcreates an instance of the flask class
which will be your WSGI (Web Server Gateway Interface) application.

'''
##### WSGI Application
app = Flask(__name__)

@app.route("/")
def Welcome():
    return "<html><H1>Welcome to this best Flask course. This should be an amazing course</H1></html>"

@app.route('/about')
def about():
    return render_template('about.html')


# @app.route('/submit', methods=['GET', 'POST'])
# def submit():
#     if request.method=='POST':
#         name = request.form['name']# request.form[id from form in form.html]
#         return f'Hello {name}!'
#     return render_template('form.html')

## Variable Rule
@app.route('/success/<int:score>')
def success(score):
    res = ''
    if score>=50:
        res = 'PASS'
    else:
        res = 'FAIL'
    return render_template('result.html', resultss=res)


## Variable Rule
@app.route('/successres/<int:score>')
def successres(score):
    res = ''
    if score>=50:
        res = 'PASS'
    else:
        res = 'FAIL'
    exp = {'score':score, 'res':res}
    return render_template('result1.html', resultss=exp)

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method=='POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['C'])
        data_science = float(request.form['data_science'])

        total_score = (science + maths + c + data_science)/4
    else:
        return render_template('getresults.html')
    return redirect(url_for('successres', score=total_score))


if __name__ == "__main__":
    app.run(debug=True)