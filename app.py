import sqlite3
from flask import Flask,render_template,jsonify,request

app = Flask(__name__)
app.secret_key="super_secret_key"

def get_db_connection():
    conn = sqlite3.connect("users.db")
    conn.row_factory=sqlite3.row
    return conn
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS users(id INTERGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,email TEXT NOT NULL,password TEXT NOT NULL,dob TEXT NOT NULL,gender TEXT NOT NULL,course TEXT NOT NULL)""")
    conn.commit()
    conn.close()
init_db()
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/courses")
def courses():
    return render_template("courses.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/trainers")
def trainers():
    return render_template("trainers.html")

@app.route("/login")
def  login():
    return render_template("login.html")




@app.route('/api/register',methods=["POST"])
def api_register():
    data = request.get_json()
    email = data.get("email")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT*FROM users WHERE email = ?",(email,))
    user = cursor.fetchone()
    if user:
        return jsonify({"status":"error","message":"user already exists with this email"}),400
        cursor.execute("INSERT INTO users(name,email,password,dob,gender,course)VALUES(?,?,?,?,?,?)",data["name"],data[    ])


    if email in users_db:
        return jsonify({"status":"error","message":"user already exists with this email"}),400

    users_db[email]=data
    return jsonify({"status":"success","message":"Registration successful!"})

@app.route('/api/login',methods=["POST"])
def api_login():
    data = request.get_json()
    email = data.get("email")
    password=data.get("password")


    user = users_db.get(email)
    if user and user.get("password")==password:
        return jsonify({"status": "success","message": "login sucessful! Welcome back."})
    else:
        return jsonify({"status":"error","message":"invalid email or password!"}),401

if __name__=='__main__':
    app.run(debug=True)

