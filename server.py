# Flask
from flask import Flask, render_template, request, redirect, url_for, session, abort, make_response
import urllib
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

@app.route("/friends/<mem_id>")
def friends(mem_id):
    ret = fn_client.getPersonFromID(mem_id)
    if(ret is None):
        return "Incorrect ID"
    return render_template('friends.html', data=ret)

@app.route("/search")
def search():
    name = request.args.get('name')
    if(name is None):
        return render_template('search.html')
    else:
        print("Search for " + name)
        id_n = fn_client.getIDFromName(name)
        print("ID found: " + id_n)
        uu = "localhost:5000/Person/"+str(id_n)
        return redirect(uu, 200)

@app.route("/person/<mem_id>")
def viewProfile(mem_id):
    ret = fn_client.getPersonFromID(mem_id)
    if(ret is None):
        return "Incorrect ID"
    print(ret['first_name'])
    return render_template('person.html', data=ret)


@app.errorhandler(500)
def internal_server(e):
    return render_template('error.html', template_folder=tmpl_dir, error=500, error_msg="Internal Server Error", 
        return_home="Something went wrong! Let us know if it happens again!"    
    )
    
@app.route("/friends/")
@app.route("/person/")
def page_not_found():
    return render_template('error.html', template_folder=tmpl_dir, error=404, error_msg="Page Not Found",
            return_home="We can't find what you're looking for."
        )
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', template_folder=tmpl_dir, error=404, error_msg="Page Not Found",
        return_home="We can't find what you're looking for."
    )


if __name__ == "__main__":
    app.run(debug=True)