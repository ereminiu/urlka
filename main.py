from repository import Repository
from service import Service

def main() -> None:
    repos = Repository()
    service = Service(repos)

main()