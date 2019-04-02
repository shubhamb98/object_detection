from flask import Flask
from flask import Flask,redirect, url_for, request,render_template,flash,send_from_directory
import pandas as pd
from werkzeug.utils import secure_filename
import os
import random
import object_detection.aa as aa
import object_detection.bb as bb
app = Flask(__name__)

current_path=os.getcwd()
UPLOAD_FOLDER = current_path+'/test_images'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
ALLOWED_EXTENSIONS = set(['mp3', 'wav', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/', methods=['GET', 'POST'])
def upload_file():

    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            message='No file part'
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            message='No selected file'
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filename = 'image1.jpg'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            message='file Uploaded Successfully!'
            #str(os.path.splitext(filename)[0])
            return redirect(url_for('result',filename=filename))
    return render_template('upload.html')

@app.route('/result')
def result():
    scores,classes,category_index,image_np=bb.detectt()
    topic=aa.object_detect_lables(scores,classes,category_index,image_np)
    print("Detected object is :"+ topic)
    x=aa.quote(topic)
    img="C:/Users/HP/Desktop/out.bmp"
    return render_template('user_rec.html', tables=x, show_table=1, image=img)



if __name__ == '__main__':
    app.run()
