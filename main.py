from repository.repository import Repository
from service.service import Service
from loguru import logger

def main() -> None:
    repos = Repository()
    service = Service(repos)

    repos.close_db()

main()