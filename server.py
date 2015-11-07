from flask import Flask
import fiscalnote as fn
from keys import fiscalnotekey
import json


app = Flask(__name__)
fn_client = fn.FiscalNoteClient(fiscalnotekey)


@app.route("/")
def hello():
    return json.dumps(fn_client.legislators(q="kevin", legislature="NY"))

if __name__ == "__main__":
    app.run()
