from flask import Flask
from src.app.routes import routes

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(routes)

if __name__ == "__main__":
    app.run(debug=True)
