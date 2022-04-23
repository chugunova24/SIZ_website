import os
from flask_dropzone import Dropzone
from flask import Flask, render_template, request

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)


# папка с шаблонами теперь по умолчанию app
app = Flask(__name__)
app.config.update(
    # UPLOADED_PATH=os.path.join(basedir, 'uploads'),
    UPLOADED_PATH=os.path.join(basedir, 'uploads'),
    DROPZONE_MAX_FILE=1024,
    DROPZONE_TIMEOUT=5*60*1000)

# app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'video'
# app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
# app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image/*, .pdf, .txt'

# файлы сохраняются в папку uploads.
# файлы с одинаковыми названиями сохраняются один раз, так что всё ок вроде
dropzone = Dropzone(app)
@app.route('/', methods=['GET', 'POST'])
def upload():

    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join(app.config['UPLOADED_PATH'],f.filename))
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)


