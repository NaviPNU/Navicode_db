from flask import Flask, request, jsonify
import pandas as pd
import numpy as np

app = Flask(__name__)

df = pd.read_csv('starbucks.csv', encoding='cp949')

@app.route('/coord_type', methods=['GET'])
def coord_type():
    navicode = request.args.get('navicode')
    if navicode.isdigit():
        result = df[df['navicode'].str.startswith(navicode)]
        type = result.iloc[0, 4]
        return jsonify({'type': str(type)})
    else:
        return jsonify({'type': '2'}) # 1 dynamic, 2 static

@app.route('/get_coord_dynamic', methods=['GET'])
def get_coord_dynamic():
    navicode = request.args.get('navicode')
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    lati = float(latitude)
    long = float(longitude)

    if navicode is None or latitude is None or longitude is None:
        return jsonify({'error': 'Missing parameters'}), 400

    result = df[df['navicode'].str.startswith(navicode)]

    if result.empty:
        return jsonify({'error': 'No matching navicode'}), 404

    result['distance'] = result.apply(
        lambda row: calculate_distance(lati, long, row[2], row[3]), axis=1
    )

    nearest = result.sort_values(by='distance').head(5)

    output = []
    for _, row in nearest.iterrows():
        output.append({
        'name': row[0],
        'latitude': row[2],
        'longitude': row[3]
        })

    return jsonify(output)

@app.route('/get_coord_static', methods=['GET'])
def get_coord_static():
    navicode = request.args.get('navicode')
    result = df[df['navicode'] == navicode]

    if result.empty:
        return jsonify({'error': '404'}), 404
    else:
        name = result.iloc[0, 0]
        gps_coord_y = result.iloc[0, 2]
        gps_coord_x = result.iloc[0, 3]
        return jsonify({'name' : name, 'longitude': gps_coord_x, 'latitude': gps_coord_y})


@app.route('/add_coord_location', methods=['POST'])
def add_coord_loaction():
    try:
        data = request.json
        required_fields = ["name", 'navicode', 'latitude', 'longitude', 'type']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'{field} is required'}), 400
        new_row = {
            'name': data['name'],
            'navicode': data['navicode'],
            'latitude': data['latitude'],
            'longitude': data['longitude'],
            'type': data['type']
        }
        global df
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv('starbucks.csv', index=False)

        return jsonify({'message': 'location added success'}), 200

    except Exception as e:
        return jsonify({'error': str(e)})

def calculate_distance(lat1, lon1, lat2, lon2):
    return np.sqrt((lat1 - lat2) ** 2 + (lon1 - lon2) ** 2)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # bash -> netsh advfirewall firewall add rule name="FlaskApp" dir=in action=allow protocol=TCP localport=5000