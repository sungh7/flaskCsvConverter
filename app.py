import os
from flask import Flask, render_template, request, flash, url_for, redirect, send_file, Response, send_from_directory
from flask_restful import reqparse, abort, Api, Resource
from werkzeug.utils import secure_filename
import sys, json
import csv
import model
import model2

ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.secret_key = b'qim,dbicuzj;ljkj193$%!4kl1'
app.config['UPLOAD_FOLDER'] = './static/img_DB'
app.config['csv_DB'] = './static/csv_DB'
app.config['MAX_CONTENT_LENGTH'] = 16*1024*1024
api = Api(app)


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
                     
# 메인 페이지 라우팅
@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route('/csv')
def csvTemplate():
    return render_template('csv.html')

@app.route('/api')
def apiTemplate():
    return render_template('api.html')

@app.route("/test", methods=['GET', 'POST'])
def test():
    select = request.form.get('comp_select')
    return (str(select))

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            model.make_table(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            uploads = os.path.join(app.config['csv_DB'])
            return send_from_directory(directory=uploads, filename='{}.csv'.format(filename), as_attachment=True)
    return render_template('index.html', label='Done')

@app.route('/upload2', methods=['GET', 'POST'])
def upload_file2():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            model2.make_table(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            uploads = os.path.join(app.config['csv_DB'])
            return send_from_directory(directory=uploads, filename='{}.csv'.format(filename), as_attachment=True)
    return render_template('index.html', label='Done')

if __name__ == '__main__':
    #app.secret_key = 'super secret key'
    app.run(host='0.0.0.0', port=5000, debug=True)
