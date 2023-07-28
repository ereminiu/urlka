from repository.repository import Repository
from service.encrypt import Encrypter
from typing import Optional
import service.url_validator

class Service:
    def __init__(self, repos: Repository) -> None:
        self.repos = repos
        self.encrypter = Encrypter()
    
    # TODO: modify retreiving values
    def add_link(self, link: str) -> str:
        """ Relaiton one-to-one, links duplicatets"""
        link_id = self.repos.insert_link(link)
        code = self.get_code(link)
        code_id = self.repos.insert_code(code)
        self.repos.insert_link_to_code(link_id, code_id)
        return code
    
    def get_link(self, code: str) -> str:
        return self.repos.select_link(code)
    
    def get_code(self, s: str) -> str:
        return self.encrypter.get_code(s)
    
    def check_code(self, code: str) -> bool:
        return self.repos.exists_code(code)
    
    def check_url(self, link: str) -> bool:
        return service.url_validator.check_url(link)

    def reinit(self) -> None:
        self.repos.reinit()
