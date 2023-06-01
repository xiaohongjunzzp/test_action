from flask import Flask, request, redirect, url_for
import os
import urllib.request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html>
        <body>
        <form action="/upload" method="post" enctype="multipart/form-data">
            <input type="file" name="file"><br>
            <input type="submit" value="上传">
        </form>
        </body>
        </html>
    '''

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    filename = file.filename
    file.save(os.path.join(r'C:\Users\Administrator\Desktop\test', filename))
    url = 'http://example.com/file.txt'
    urllib.request.urlretrieve(url, os.path.join(r'C:\Users\Administrator\Desktop\test', 'file.txt'))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
