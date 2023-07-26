from repository.repository import Repository
from service.service import Service
from service.encrypt import Encrypter
from loguru import logger

def main() -> None:
    repos = Repository()
    service = Service(repos)

    link = r'https://github.com/avito-tech/auto-backend-trainee-assignment'
    service.add_link(link)

    # service.reinit()

    repos.close_db()

main()