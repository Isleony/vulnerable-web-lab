from flask import Flask, request, render_template_string, redirect
import sqlite3

app = Flask(__name__)

# ----------------------------
# Banco de dados (vulnerável)
# ----------------------------
def get_db():
    return sqlite3.connect("users.db")

# ----------------------------
# Página de login (SQLi)
# ----------------------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        pwd = request.form["password"]

        conn = get_db()
        cursor = conn.cursor()

        # VULNERÁVEL A SQL INJECTION
        query = f"SELECT id, username FROM users WHERE username = '{user}' AND password = '{pwd}'"
        cursor.execute(query)

        result = cursor.fetchone()
        conn.close()

        if result:
            return redirect(f"/profile?id={result[0]}")
        else:
            return "Login inválido"

    return '''
        <h2>Login</h2>
        <form method="POST">
            <input name="username" placeholder="username"><br>
            <input name="password" placeholder="password"><br>
            <button type="submit">Login</button>
        </form>
    '''

# ----------------------------
# IDOR – Broken Access Control
# ----------------------------
@app.route("/profile")
def profile():
    user_id = request.args.get("id")

    conn = get_db()
    cursor = conn.cursor()

    # SEM validação de sessão
    cursor.execute(f"SELECT id, username, email FROM users WHERE id = {user_id}")
    user = cursor.fetchone()
    conn.close()

    if user:
        return f"""
        <h2>Perfil do Usuário</h2>
        <p>ID: {user[0]}</p>
        <p>Username: {user[1]}</p>
        <p>Email: {user[2]}</p>
        """
    else:
        return "Usuário não encontrado"

if __name__ == "__main__":
    app.run(debug=True)
