from typing import Union, List
from pydantic import BaseModel


class HuggingFaceConfigsModel(BaseModel):
    HF_TOKEN: Union[str]


class OpenRouterConfigsModel(BaseModel):
    OPEN_ROUTER_KEY: Union[str]


class APIConfigsModel(BaseModel):
    API_HOST: Union[str]
    API_PORT: Union[int]
    API_URL: Union[str, None] = None

    SECRET_KEY: Union[str]

    DOMAIN: Union[str]

    ROOT_DIR: Union[str]
    IS_PROD: Union[bool]


class ConfigsValidator(APIConfigsModel, OpenRouterConfigsModel,
                       HuggingFaceConfigsModel):
    pass