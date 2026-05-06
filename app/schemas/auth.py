# TODO: Escrever docstrings

# DEPENDENCIES IMPORTS
from pydantic import BaseModel



# SCHEMAS
class Token(BaseModel):
    """
    """
    access_token: str
    token_type: str



class TokenData(BaseModel):
    """
    """
    user_id: int | None = None