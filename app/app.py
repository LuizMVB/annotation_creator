from flask import Flask, redirect, url_for, render_template, request, send_file

app = Flask(__name__)
uploads_path = 'app/uploads/'
table = []

@app.route('/')
def index():
    return redirect(url_for('main'))

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/addItem/<id>/<seq>/<tax>')
def addItem(id, seq, tax):
    table.append({'id': id, 'seq': seq, 'tax': tax})
    return {}

@app.route('/export_seqs')
def export_seqs():
    f_seq = open(uploads_path + 'seqs.fasta', 'w')
    for item in table:
        f_seq.write('>' + str(item['id']) + '\n' + item['seq'] + '\n')
    f_seq.close()
    return send_file('uploads/seqs.fasta', as_attachment=True)
    
@app.route('/export_tax')
def export_tax():
    f_tax = open(uploads_path + 'taxonomy.txt', 'w')
    for item in table:
        f_tax.write(str(item['id']) + '\t' + item['tax'] + '\n')
    f_tax.close()
    return send_file('uploads/taxonomy.txt', as_attachment=True)