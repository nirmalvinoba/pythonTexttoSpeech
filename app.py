
from flask import Flask,request,render_template,send_file
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    text = request.form.get('text')
    lan = request.form.get('lan')
    tts = gTTS(text, lang='lan')
    tts.save('output.mp3')
    return send_file('output.mp3',as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)    