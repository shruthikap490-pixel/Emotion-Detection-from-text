from flask import Flask, render_template, request
import random

app = Flask(__name__)

emotions = {
    "happy": "😊",
    "sad": "😢",
    "angry": "😡",
    "love": "😍",
    "fear": "😨",
    "surprise": "😲",
    "confused": "😕",
    "excited": "🤩",
    "bored": "🥱",
    "shy": "☺️",
    "crying": "😭",
    "sleepy": "😴",
    "cool": "😎",
    "sick": "🤒",
    "thinking": "🤔",
    "nervous": "😬",
    "disappointed": "😞",
    "motivated": "💪",
    "hungry": "🍔",
    "party": "🥳",
    "laugh": "😂",
    "jealous": "😒",
    "relaxed": "😌",
    "stress": "😫",
    "romantic": "❤️"
    }

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html', emotions=emotions)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/animation')
def animation():
    return render_template('animation.html')

@app.route('/detect', methods=['GET', 'POST'])
def detect():
    detected = ''
    emoji = ''

    if request.method == 'POST':
        text = request.form['text'].lower()

        detected = 'happy'

        for emotion in emotions:
            if emotion in text:
                detected = emotion
                emoji = emotions[detected]

    return render_template('detect.html', detected=detected, emoji=emoji)

if __name__ == '__main__':
    app.run(debug=True)