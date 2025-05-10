import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/linreg', methods=['POST'])
def linreg():
    data = request.json
    xdata = data.get('xdata')
    ydata = data.get('ydata')
    x = data.get('x')
    xn = np.array(x)

    if xdata is None or ydata is None or x is None or len(xdata) != len(ydata):
        return jsonify({'error': 'Invalid input'}), 400

    m, b = np.polyfit(xdata, ydata, 1)

    y = m * x + b

    return jsonify({'y': y.tolist()})  


    app.run(host="0.0.0.0", port=8000)

