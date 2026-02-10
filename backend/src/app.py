import os
from flask import Flask, jsonify
from flask_cors import CORS
from src.api.routes import api_blueprint

app = Flask(__name__)
# Disable strict slashes globally BEFORE registering blueprints
app.url_map.strict_slashes = False

# Allow requests from any origin for all routes
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def index():
    return jsonify(status="healthy", message="JobFit-AI Backend API"), 200

@app.errorhandler(Exception)
def handle_exception(e):
    # Pass through HTTP errors
    if hasattr(e, 'code'):
        return jsonify(error=str(e)), e.code
    # Handle non-HTTP exceptions only
    return jsonify(error="Internal Server Error"), 500

app.register_blueprint(api_blueprint, url_prefix="/api")

if __name__ == "__main__":
    # Get port from environment variable or default to 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
