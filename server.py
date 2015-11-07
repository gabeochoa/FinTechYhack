from flask import Flask
import fiscalnote as fn
from keys import fiscalnotekey
import json
import os 

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__)
fn_client = fn.FiscalNoteClient(fiscalnotekey)

@app.route("/")
def hello():
    return render_template('index.html', template_folder=tmpl_dir)
#    return json.dumps(fn_client.legislators(q="kevin", legislature="NY"))

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
