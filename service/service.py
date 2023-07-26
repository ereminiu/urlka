from repository.repository import Repository
from service.encrypt import Encrypter
from typing import Optional

class Service:
    def __init__(self, repos: Optional[Repository]) -> None:
        self.repos = repos
        self.encrypter = Encrypter()
    
    def add_link(self, link: str) -> None:
        """ Relaiton one-to-one, links duplicatets"""
        link_id = self.repos.insert_link(link)
        code = self.get_code(link)
        code_id = self.repos.insert_code(code)
        self.repos.insert_link_to_code(link_id, code_id)
    
    def get_link(self, code: str) -> str:
        return self.repos.select_link(code)
    
    def get_code(self, s: str) -> str:
        return self.encrypter.get_code(s)

    def reinit(self) -> None:
        self.repos.reinit()
