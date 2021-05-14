from tool import app, UPLOAD_FOLDER
import os
from zipfile import ZipFile
from flask import (Flask, jsonify, request, session, g, redirect, send_file, send_from_directory,
                   url_for, abort, render_template, flash)
from werkzeug.utils import secure_filename
from tool.functions import taking_Attendance


# routes
# home route

@app.route('/', methods=['GET', 'POST'])
def attendance_upload():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'day_file' not in request.files:
            print('no file')
            return redirect(request.url)
        day_file = request.files['day_file']
        register_file = request.files['register_file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if day_file.filename == '' and register_file.filename == '':
            print('no filename')
            return redirect(request.url)
        else:
            print("saved file successfully")
            print(day_file)
            filename = taking_Attendance(
                app.config['UPLOAD_FOLDER'], day_file, register_file)
            # os.remove(UPLOAD_FOLDER+day_file)
            # os.remove(UPLOAD_FOLDER+register_file)
            return redirect('/attendance/downloadfile/' + filename)
        return render_template('attendance_upload_file.html')
    else:
        return render_template('attendance_upload_file.html')


@app.route("/attendance/downloadfile/<filename>", methods=['GET'])
def attendance_download_file(filename):
    return render_template('attendance_download.html', value=filename)


@app.route('/attendance/return-files/<filename>')
def attendance_return_files(filename):
    print(UPLOAD_FOLDER+filename)
    return send_from_directory('uploads/', filename, as_attachment=True, cache_timeout=0)
