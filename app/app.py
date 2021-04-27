from flask import Flask, redirect, url_for, render_template, request, send_file
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

uploads_path = 'app/uploads/' 

@app.route('/')
def index():
    if os.path.exists("app/uploads/seqs.fasta"):
        os.remove('app/uploads/seqs.fasta')
    if os.path.exists("app/uploads/taxonomy.txt"):
        os.remove('app/uploads/taxonomy.txt')
    return redirect(url_for('main'))

@app.route('/main')
def main():
    if os.path.exists("app/uploads/seqs.fasta"):
        os.remove('app/uploads/seqs.fasta')
    if os.path.exists("app/uploads/taxonomy.txt"):
        os.remove('app/uploads/taxonomy.txt')
    return render_template('main.html')

@app.route('/addItem', methods=['POST'])
def addItem():
    id = request.form['id']
    seq = request.form['seq']
    tax = request.form['tax']
    addSeqLine(id, seq)
    addTaxLine(id, tax)
    return {}

@app.route('/export_seqs')
def export_seqs():
    return send_file('uploads/seqs.fasta', as_attachment=True)
    
@app.route('/export_tax')
def export_tax():
    return send_file('uploads/taxonomy.txt', as_attachment=True)

def addSeqLine(id, seq):
    seq = seq.replace('\n', '')
    f_seq = open(uploads_path + 'seqs.fasta', 'a')
    f_seq.write('>' + id + '\n' + seq + '\n')
    f_seq.close()

def addTaxLine(id, tax):
    tax = tax.replace(';', '; ').replace('  ', ' ').replace('.', '')
    f_tax = open(uploads_path + 'taxonomy.txt', 'a')
    f_tax.write(id + '\t' + tax + '\n')
    f_tax.close()