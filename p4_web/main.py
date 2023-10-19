# 맥에서 실행: export FLASK_APP=main.py && flask run

from flask import Flask, flash, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/user_prf', methods=['GET', 'POST'])
def user_prf():
    if request.method == 'GET':
        return render_template('user_prf.html')
    elif request.method == 'POST':
        login_id = request.form['login_id']
        login_pwd = request.form['login_pwd']
        if login_id=='admin' and login_pwd=='1234':
            nickname = '슈니'
            return render_template('user_prf.html', nickname = nickname)
        else:
            flash('다시 입력해주세요.')
            return render_template('login.html')

@app.route('/main', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('main.html')
    elif request.method == 'POST':
        return render_template('main.html')

@app.route('/search1', methods=['GET', 'POST'])
def search1():
    if request.method == 'GET':
        return render_template('search1.html')
    elif request.method == 'POST':
        keyword = request.form['search_keyword']
        if keyword == '편스토랑':
            return render_template('search1.html')

if __name__ == '__main__':
    app.run(port=80, debug=True)