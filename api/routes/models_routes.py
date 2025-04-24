import io
import numpy as np

from fastapi import (APIRouter, Header, HTTPException, UploadFile,
                     File)
from fastapi.responses import JSONResponse
from PIL import Image

from api.schemas.models_schemas import VLModelSchema, LLModelSchema

from api.services.infrastructure.vl_service import VLModelService
from api.services.infrastructure.llm_service import LLModelService


router = APIRouter(prefix='/models',
                   tags=['NER']) # Итоговый путь /api/models/...


@router.post('/llm/predict')
async def lmm_prompt_answer(llm_data: LLModelSchema):
    llm_answer = await LLModelService(context=llm_data.context_text).model_predict(prompt=llm_data.query_text)

    return llm_answer


@router.post('/vl/predict')
async def vl_query_answer(query: str,
                          image: UploadFile = File(...)):
    image_bytes = await image.read()
    pil_image = Image.open(io.BytesIO(image_bytes))

    if pil_image.mode != 'RGB':
        pil_image = pil_image.convert('RGB')

    vl_answer = await VLModelService().model_predict(image=pil_image, prompt=query)

    return vl_answer

