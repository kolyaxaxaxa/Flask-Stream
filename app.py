from flask import Flask, render_template
from functions import *

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def page_index():
    return render_template('index.html')

@app.route('/profile')
def page_profile():
    # first_name = getUsersInfo.first_name
    # last_name = getUsersInfo.last_name
    # bdate = getUsersInfo.bdate
    # city = getUsersInfo.city
    return render_template('profile.html')

@app.route('/friends')
def page_friends():
    return render_template('friends.html')

if __name__ == '__main__':
    app.run(debug=True)