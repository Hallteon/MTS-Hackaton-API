from pydantic import BaseModel


class LLModelSchema(BaseModel):
    context_text: str
    query_text: str


class VLModelSchema(BaseModel):
    query_text: str


