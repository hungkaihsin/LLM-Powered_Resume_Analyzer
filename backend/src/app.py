import os
from flask import Flask
from flask_cors import CORS
from src.api.routes import api_blueprint

app = Flask(__name__)

# Allow requests from the frontend's domain
CORS(app, resources={r"/api/*": {"origins": "*"}})
app.register_blueprint(api_blueprint, url_prefix="/api")

if __name__ == "__main__":
    # Get port from environment variable or default to 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
