from pydantic import BaseModel

class LinkRequest(BaseModel):
    link: str
    custom_code: str

class CodeResponse(BaseModel):
    code: str
    msg: str

class CodeRequest(BaseModel):
    code: str

class Messenge(BaseModel):
    msg: str