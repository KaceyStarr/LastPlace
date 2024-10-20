from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def db_connect():
    db = sqlite3.connect("expenses.sqlite")
    db.row_factory = sqlite3.Row
    return db


@app.route('/login', methods=['POST'])
def login():
    return render_template('signin.html')


#new rounte output the loans on the database.
@app.route('/loans')
def loans():
    conn = db_connect()
    cur = conn.cursor()
    cur.execute('SELECT * FROM people')
    people = cur.fetchall()
    conn.close()

    return render_template('loans.html', people=people)


@app.route('/budget/')
def budget():
    conn = db_connect()
    cur = conn.cursor()
    cur.execute('SELECT * FROM people')
    people = cur.fetchall()
    conn.close()
    
    return render_template('budget.html', people=people)


@app.route('/credit')
def credit():
    conn = db_connect()
    cur = conn.cursor()
    cur.execute('SELECT * FROM people')
    people = cur.fetchall()
    conn.close()

    return render_template('credit.html', people=people)

if __name__ == '__main__':
    app.run(debug=True)

# @app.route('/credit')
# def 


# @app.route('/budget', methods=['POST'])
# def budget():
#     user = request.form['user']

# @app.route('/savings', methods=['POST'])
# def saving():
#     user = request.form['user']

# @app.route('/credit', methods=['POST'])
# def credit():
#     user = request.form['user']
#     credit_scores = int(request.form['credit_score'])
#     credit_scores[user] = credit_scores

if __name__ == '__main__':
    app.run(debug=True)