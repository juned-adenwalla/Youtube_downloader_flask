from flask import *
from pytube import YouTube

app = Flask(__name__)

def download(url):
    video = url.streams.first()
    filepath = video.download()
    return filepath

@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = YouTube(request.form.get('url'))
        filepath = download(url)
        return render_template("video.html", filetitle = url.title, filepath = filepath)
    return render_template("index.html")

@app.route("/download", methods = ['GET', 'POST'])
def download_video():
    if request.method == "POST":
        filepath = request.form.get('filepath')
        return send_file(filepath, as_attachment=True)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(port=80, debug=True)