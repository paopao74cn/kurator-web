import os
from flask import Flask, request, redirect, url_for,send_from_directory, render_template, jsonify
from werkzeug import secure_filename
import sqlite3

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['csv','yaml', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files.getlist['file[]']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print file
            return redirect(url_for('uploaded_file',filename=filename))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)           
           
@app.route('/')
def hello_kurator():
    return 'Hello Kurator!'
    
@app.route('/index')
def index_page():
    user = {'nickname': 'Miguel'}  # fake user
    return render_template('index.html', user = user)

#     return "index page!"

@app.route('/user')
def hello():
    return 'Hello user!'

# returns an HTML webpage
@app.route('/user/<username>')
def hello_user(username):
    return render_template('profile.html', name = username)
    # return 'Hello ' + username + '!'
    
# returns a piece of data in JSON format
@app.route('/outputdata')
#def people():
#    my_people = {'Alice': 25, 'Bob': 21, 'Charlie': 20, 'Doug': 28}
#    return jsonify(my_people)
    # wf_output = ka -f 
def hellowf():
    wf_output = {'bib_id':23, 'bib_title': "Agassiz, L.", 'bib_year':1839, 'bib_pub': 'Soc.Sci.Nat. Helvetica Mem.'}
    return jsonify(wf_output)


if __name__ == '__main__':
    app.run(debug=True)
