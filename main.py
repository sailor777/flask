import flask

from forms import LoginForm
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask('flask_app')
app.config.from_object('config')
db = SQLAlchemy(app)

#db.create_all()

admin_user = {'username': 'admin', 'password': 'admin'}

@app.route('/')
@app.route('/index')
def main():
    #return('Hello NEW World!')
    title = 'Bla-Bla!'
    user = {'nickname': 'Sailor'}
    return flask.render_template('index.html',
                                title='Home',
                                user=user)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.data['username'] == admin_user['username'] \
            and form.data['password'] == admin_user['password']:
                return flask.redirect('/')
        else:
            return flask.flash('Wrong username or password')
    return flask.render_template('login.html',title='Sign In',form=form)

import models
'''
if __name__ == '__main__':
    app.run(debug=True)'''
