from app import app
import json

@app.route('/')
def index():
    data = json.dumps({"in":11111111})
    return data