#!/usr/bin/env python3

from flask import Flask, request, render_template, \
                  redirect

from model_sqlite import save_doc_as_file, \
                         read_doc_as_file, \
                         get_last_entries_from_files


app = Flask(__name__)

@app.route('/')
def index():
    #d = { 'last_added':[ { 'uid':'testuid', 'code':'testcode' } ] }
    d = { 'last_added':get_last_entries_from_files() }
    return render_template('index.html',**d)

@app.route('/create')
def create():
    uid = save_doc_as_file()
    return redirect("{}edit/{}".format(request.host_url,uid))
    
@app.route('/edit/<string:uid>/')
def edit(uid):
    val = read_doc_as_file(uid)
    if val is None:
        return render_template('error.html',uid=uid)
    d = dict( uid=uid, code=val[1], language =val[2],
              url="{}view/{}".format(request.host_url,uid))
    return render_template('edit.html', **d) 

@app.route('/publish',methods=['POST'])
def publish():
    code = request.form['code']
    uid  = request.form['uid']
    language = request.form['language']
    uid = save_doc_as_file(uid,code,language)
    return redirect("{}{}/{}".format(request.host_url,
                                     request.form['submit'],
                                     uid))

@app.route('/view/<string:uid>/')
def view(uid):
    val = read_doc_as_file(uid)
    if val is None:
        return render_template('error.html',uid=uid)
    d = dict( uid=uid, code=val[1],language=val[2],
              url="{}view/{}".format(request.host_url,uid))
    return render_template('view.html', **d)

@app.route('/admin/')
def admin():
    pass

if __name__ == '__main__':
    app.run()

