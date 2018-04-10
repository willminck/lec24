from flask import Flask, render_template, request
import model

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <img src="/static/blockM.png"/>
        <h1>Michigan Sports Info!</h1>
        <ul>
            <li><a href="/fball"> Men's Football </a></li>
        </ul>
    '''

@app.route('/fball', methods=['GET', 'POST'])
def fball():
    if request.method == 'POST':
        sortby = request.form['sortby']
        sortorder = request.form['sortorder']
        seasons = model.get_fball_seasons(sortby, sortorder)
    else:
        seasons = model.get_fball_seasons()

    return render_template("seasons.html", seasons=seasons)

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    return render_template("hello.html", firstname=firstname, lastname=lastname)

if __name__ == '__main__':
    model.init_fball()
    app.run(debug=True)
