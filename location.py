# pip install locationsharinglib
# pip install Flask


import json

from locationsharinglib import Service
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})

@app.route("/location", methods=["GET"])
def translate():
    
    cookies_file = 'www.google.com_cookies.txt'
    google_email = 'chagai95@gmail.com'
    service = Service(cookies_file=cookies_file, authenticating_account=google_email)
    nickname = "Chagai"
    person = service.get_person_by_nickname(nickname)
    return json.dumps({"accuracy": person.accuracy, "address": person.address, "battery_level": person.battery_level, "charging": person.charging, "latitude": person.latitude, "longitude": person.longitude, "timestamp": person.timestamp}).encode("ascii"), 200


if __name__ == "__main__":
    context = ('certificate.crt', 'privatekey.key') #certificate and key files
    app.run(host="0.0.0.0", port=4400, ssl_context=context)