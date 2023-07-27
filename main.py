from repository.repository import Repository
from service.service import Service
from service.encrypt import Encrypter
from loguru import logger
from typing import Tuple

from flask import Flask
from flask import request
from models import models

repos = Repository()
service = Service(repos)

app = Flask(__name__)

@app.route("/reinit", methods=["POST"])
def reinit() -> Tuple[str, int]:
    repos.reinit()
    return "migrations applied", 200

@app.route("/addlink", methods=["POST"])
def add_link() -> Tuple[str, int]:
    inp = models.LinkRequest.model_validate_json(request.data)
    
    # TODO: check whether link is valid
    # TODO: check whether custom_code isn't used before

    code = service.add_link(inp.link)
    resp = models.CodeResponse(code=code, \
                               msg="Link has been added,").model_dump_json()
    return resp, 200

app.run(host="localhost", port=8000, debug=True)
repos.close_db()
