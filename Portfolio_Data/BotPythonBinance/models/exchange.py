from datetime import datetime

from api import utils
from models.model import AbstractModel

class Exchange(AbstractModel):
    ressource_name = 'exchange'

    id:str = ''
    name: str = ''

    def __init__(self, **kwargs):
        super.__init__(**kwargs)