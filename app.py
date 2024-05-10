from flask import Flask
from flask_cors import CORS
from image_routes import image_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(image_bp, url_prefix='/images')


@app.route('/')
def hello():
    return 'Hello, World!'


# Custom 500 Internal Server Error handler
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal Server Error'}), 500


if __name__ == '__main__':
    app.run(debug=True)