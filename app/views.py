from flask import render_template, jsonify
from app import app
 
 
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('app.html')
 
 
@app.route('/endpoint', methods=['GET'])
def endpoint():
    payload = {'result': 123}
    return jsonify(payload)