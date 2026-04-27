from flask import Flask

app = Flask(__name__)

# Hardcoded secret (SAST finding)
password = "hardcoded_password"

@app.route("/")
def home():
    return "Hello Vulnerable App"

@app.route("/login")
def login():
    return "Login endpoint (insecure)"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
