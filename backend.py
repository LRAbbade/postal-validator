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
        error = None
    except Exception as e:
        res = False
        error = str(e)

    return jsonify({
        'cep': cep,
        'result': res,
        'error': error
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0')
