from drask import app
from flask import jsonify

print(app)

@app.route('/')
def home():
    return "Index page"


@app.route('/api/test')
def test():
    return jsonify(
        message="hello world"
    )
