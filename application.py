from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import database


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def home():
    return "Home"

# Test API request
@app.route("/get-user/<user_id>")
@cross_origin()
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "email@email.com"
    }
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200

# Get all wells with existing well types
@app.route("/get-wells")
@cross_origin()
def get_all_wells():
    get_wells_request = database.select_all_wells()
    features = []
    for well in get_wells_request:
        if (well['WellType'] != None):
            features.append({"type": "Feature", "properties": well, "geometry": {"type": "Point", "coordinates": [well['Longitude'], well['Latitude']]}})
    wells_json = {
        "type": "FeatureCollection", 
        "name": "OrphanWellsOklahoma_3",
        "amount": len(features),
        "crs": {
            "type": "name", 
            "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } 
            },
        "features": features}

    return jsonify(wells_json), 200

if (__name__) == "__main__":
    app.run(debug=True)