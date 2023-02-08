from flask import Flask, render_template,request
from babel import numbers, dates
from datetime import date, datetime, time
from flask_babel import Babel,format_date,gettext


app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE']='en'
babel=Babel(app)

@babel.localeselector
def get_locale():
    return 'es'
    # return request.accept_languages.best_match(['en','es','de'])

@app.route('/')
def index():
    return render_template('index.html')

if __name__ =='__main__':
    app.run(debug=True)
