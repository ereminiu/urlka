from repository.repository import Repository
from service.service import Service
from service.encrypt import Encrypter
from loguru import logger
from typing import Tuple

from flask import Flask

repos = Repository()
Service = Service(repos)

app = Flask(__name__)

@app.route("/reinit", methods=["POST"])
def reinit() -> Tuple[str, int]:
    repos.reinit()
    return "migrations applied", 200

repos.close_db()