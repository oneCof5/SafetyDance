from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/ip', methods=['GET'])
def get_ip():
    try:
        # Get the public IP address by querying an external service
        public_ip = requests.get('https://api.ipify.org?format=json').json()['ip']
    except requests.RequestException as e:
        public_ip = "Error fetching IP"
    return jsonify(ip=public_ip)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
