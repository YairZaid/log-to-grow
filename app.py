from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "log-to-grow: אפליקציית מעקב אימונים!"

if __name__ == "__main__":
    app.run(debug=True)