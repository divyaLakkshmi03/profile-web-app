import os
import mysql.connector
from flask import Flask, request, redirect

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST", "mysql-service"),
    user="root",
    password=os.getenv("MYSQL_ROOT_PASSWORD"),
    database="flaskdb"
)

cursor = db.cursor(dictionary=True)

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS profile (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    bio TEXT
)
""")
db.commit()


@app.route("/")
def home():
    cursor.execute("SELECT * FROM profile LIMIT 1")
    data = cursor.fetchone()

    if data:
        profile_html = f"""
        <h2>Profile</h2>
        <p><b>Name:</b> {data['name']}</p>
        <p><b>Email:</b> {data['email']}</p>
        <p><b>Bio:</b> {data['bio']}</p>
        <a href='/edit'>Edit Profile</a>
        """
    else:
        profile_html = "<a href='/edit'>Create Profile</a>"

    return f"""
    <html>
    <body style="font-family: Arial; margin: 40px;">
        <h1>Divya's Profile App 🚀</h1>
        {profile_html}
    </body>
    </html>
    """


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        bio = request.form["bio"]

        cursor.execute("SELECT * FROM profile LIMIT 1")
        existing = cursor.fetchone()

        if existing:
            cursor.execute("""
                UPDATE profile
                SET name=%s, email=%s, bio=%s
                WHERE id=%s
            """, (name, email, bio, existing["id"]))
        else:
            cursor.execute("""
                INSERT INTO profile (name, email, bio)
                VALUES (%s, %s, %s)
            """, (name, email, bio))

        db.commit()
        return redirect("/")

    # GET request (show form with existing values)
    cursor.execute("SELECT * FROM profile LIMIT 1")
    user = cursor.fetchone()

    name = user["name"] if user else ""
    email = user["email"] if user else ""
    bio = user["bio"] if user else ""

    return f"""
    <html>
    <body style="font-family: Arial; margin: 40px;">
        <h2>Edit Profile</h2>
        <form method="POST">
            Name:<br>
            <input type="text" name="name" value="{name}" required><br><br>

            Email:<br>
            <input type="email" name="email" value="{email}" required><br><br>

            Bio:<br>
            <textarea name="bio" rows="4" cols="40">{bio}</textarea><br><br>

            <button type="submit">Update</button>
        </form>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

