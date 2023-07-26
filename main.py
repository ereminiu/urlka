from repository.repository import Repository
from service.service import Service
from service.encrypt import Encrypter
from loguru import logger

def main() -> None:
    repos = Repository()
    service = Service(repos)

    # service.reinit()

    repos.close_db()

main()