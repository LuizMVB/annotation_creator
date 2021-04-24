from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('main'))

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/export')
def export():
    return "export"