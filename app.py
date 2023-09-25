from flask import Flask, render_template, request, redirect, url_for, send_file
from translate_speech import translate_speech


app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/translate', methods=['GET', 'POST'])
def translate():
    if request.method == 'POST':
        english_speech = request.form['english_speech']
        konkani_speech = translate_speech(english_speech)
        return render_template('index.html', konkani_speech=konkani_speech)
    return render_template('index.html')

@app.route('/get_started')
def get_started():
    return render_template('second.html')

@app.route('/Home')
def Home():
    return render_template('homepage.html')

@app.route('/Dictionary')
def Dictionary():
    return render_template('choice.html')

@app.route('/Days')
def Days():
    return render_template('days.html')

@app.route('/Colors')
def Colors():
    return render_template('colors.html')

@app.route('/Fruits')
def Fruits():
    return render_template('fruits.html')

@app.route('/Vegetables')
def Vegetables():
    return render_template('vegetables.html')

@app.route('/Parts')
def Parts():
    return render_template('bodyparts.html')

@app.route('/Family')
def Family():
    return render_template('family.html')

@app.route('/Trans')
def Trans():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/audio')
def serve_audio():
    return send_file('static/captured_voice.mp3', as_attachment=True)




if __name__ == '__main__':
    app.run()