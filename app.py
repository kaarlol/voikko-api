from flask import Flask
from flask import request, jsonify, render_template
#from voikko import lemmatisoi
app = Flask(__name__)


@app.route("/api", methods=['POST'])
def post_voikko():
#    lemmatized = lemmatisoi( request.json.get('lemmat') )
    return jsonify({'data': lemmatized })

@app.route('/')
@app.route('/<name>')
def index(name=None):
    return render_template('index.html', name=name)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
