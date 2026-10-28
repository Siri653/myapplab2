from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register():
    name = request.form["name"]
    roll = request.form["roll"]
    email = request.form["email"]
    phone = request.form["phone"]
    return render_template(
        "success.html",
        name=name,
        roll=roll,
        email=email,
        phone=phone,
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)