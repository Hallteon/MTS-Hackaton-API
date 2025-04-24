from fastapi import APIRouter
from api.routes.models_routes import router as nn_router


router = APIRouter()

router.include_router(nn_router)
