from flask import Flask
from flask import request, jsonify
from flask_cors import CORS
from app import lemmatisoi
app = Flask(__name__)
CORS(app)

@app.route("/api", methods=['POST'])
def post_voikko():
    lemmatized = lemmatisoi( request.json.get('lemmat') )
    return jsonify({'data': lemmatized })

if __name__ == "__main__":
    app.run(port=5000)
