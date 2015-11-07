from flask import Flask
import fiscalnote as fn
from keys import fiscalnotekey
import json


app = Flask(__name__)
fn_client = fn.FiscalNoteClient(fiscalnotekey)


@app.route("/")
def hello():
    return json.dumps(fn_client.legislators(q="kevin", legislature="NY"))

@app.route("/person/<mem_id>")
def viewprofile(mem_id):
    viewProfile(mem_id)
    
@app.route("/Person/<mem_id>")
def viewProfile(mem_id):
    ret = fn_client.getPersonFromID(mem_id)
    strs = ""
    for i in ret:
        strs += str(i)
    return strs

if __name__ == "__main__":
    app.run()
