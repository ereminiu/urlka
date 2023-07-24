from repository.repository import Repository
from typing import Optional

class Service:
    def __init__(self, repos: Optional[Repository]) -> None:
        self.repos = repos