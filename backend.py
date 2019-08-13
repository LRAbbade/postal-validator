from flask import Flask, render_template, request, jsonify
from main import Validate

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validate')
def validate_cep():
    cep = str(request.args.get('cep'))
    try:
        res = Validate(cep)
    except Exception as e:
        res = str(e)

    return jsonify({
        'cep': cep,
        'result': res
    })
