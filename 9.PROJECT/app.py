from flask import Flask, render_template, redirect, url_for, request
import sqlite3

app = Flask(__name__)

DATABASE = "./newcrmdb.db"

@app.route('/')
def index():
    return redirect(url_for('user'))

@app.route('/user')
def user():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    offset = (page - 1) * per_page
    
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    
    cur.execute("SELECT COUNT(*) FROM users")
    total_count = cur.fetchone()[0]
    
    cur.execute("SELECT * FROM users LIMIT ? OFFSET ?", (per_page, offset))
    users = cur.fetchall()
    users2 = [dict(row) for row in users]
    conn.close()
    
    total_pages = (total_count // per_page) + (1 if total_count % per_page > 0 else 0)

    return render_template('user.html', users2=users2, page=page, total_pages=total_pages)
  

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)