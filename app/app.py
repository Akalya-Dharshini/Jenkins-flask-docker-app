from flask import Flask, render_template
import datetime
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html",
        hostname=socket.gethostname(),
        time=datetime.datetime.now()
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
