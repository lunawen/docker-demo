from flask import Flask
import os
import socket

app = Flask(__name__)


@app.route("/")
def hello():
    html = "<h3>Hello {name}!</h3>" \
           "<h4>This is a simple project to demonstrate how Docker works.</h4>" \
           "<b>Container ID:</b> {hostname}<br/>"
    return html.format(name=os.getenv("NAME"), hostname=socket.gethostname())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
