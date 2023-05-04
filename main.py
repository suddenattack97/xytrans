from flask import Flask, render_template, jsonify, Response
from flask import request, redirect, url_for, session, send_file ,abort
from datetime import datetime
from io import BytesIO
from pyproj import Proj, Transformer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trans', methods=['POST'])
def trans():
    data = request.json

    input_coords = (float(data['input_x_coordinate']), float(data['input_y_coordinate']))
    input_proj = Proj(data['input_coordinate_system'])  # 현재 좌표계
    output_proj = Proj(data['output_coordinate_system'])  # 변경하려는 좌표계

    transformer = Transformer.from_proj(input_proj, output_proj)
    new_x, new_y = transformer.transform(input_coords[0], input_coords[1])

    return jsonify({'new_x': new_x, 'new_y': new_y})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6001)