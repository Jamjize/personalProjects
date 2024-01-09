from flask import Flask, render_template, redirect, url_for
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play/<game>')
def play_game(game):
    game_file = f'static/games/{game}.swf'
    subprocess.run(['static/games/FlashPlayer.exe', game_file])

    # Después de jugar el juego, redirige a la página de juego
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
