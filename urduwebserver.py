from flask import Flask, redirect, url_for, request
from graphitequery import query
app = Flask(__name__)


@app.route('/qe_results/<name>')
def qe_results(name):
    return list(query(name))


@app.route('/qe', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['query']
        return redirect(url_for('qe_results', name=user))
    else:
        user = request.args.get('query')
        return redirect(url_for('qe_results', name=user))
  
    
if __name__ == '__main__':
    app.run(debug=True)
