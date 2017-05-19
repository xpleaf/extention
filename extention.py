# coding: utf-8
from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/download/<path:filename>')
def downloader(filename):
    print filename
    path = os.path.join(app.root_path, 'logs')
    return send_from_directory(path, filename=filename, as_attachment=True)  # as_attachment=True 一定要写，不然会变成打开，而不是下载


if __name__ == '__main__':
    app.run(port=8080, debug=True)
