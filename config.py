import os
from typing import Literal

import pydantic_settings

BASE_DIR = os.path.dirname(__file__)

EnvType = Literal['local', 'remote']


class Settings(pydantic_settings.BaseSettings):
    ENVIRONMENT: EnvType = 'local'
    LOGIN: str
    PASSWORD: str


settings = Settings(_env_file=os.path.join(BASE_DIR, '.env'))
