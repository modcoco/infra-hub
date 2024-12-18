from flask import Flask
import os

from app.logger import log
from app.config import ProductionConfig
from app.routes import routes

app = Flask(__name__)

app.config.from_object(ProductionConfig)
os.makedirs(app.config["TASKS_DIR"], exist_ok=True)
app.register_blueprint(routes)

log.info("Home endpoint accessed.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)
