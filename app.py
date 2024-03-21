from flask import Flask, render_template, request, send_file
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/navigate', methods=['POST'])
def navigate():
    page = request.form['page']
    if page == 'home':
        return '<h2>Home Page Content Goes Here</h2>'
    elif page == 'login':
        return '<h2>Login Page Content Goes Here</h2>'
    elif page == 'register':
        return '<h2>Registration Page Content Goes Here</h2>'
    else:
        return 'Invalid page'

@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    text = request.form['text']
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save('static/output.mp3')
    return send_file('static/output.mp3', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

