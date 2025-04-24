import base64
import numpy as np

from utils.vl_model import VLModel
from io import BytesIO
from PIL import Image


class VLModelService:
    def __init__(self):
        self.model = None

    async def _image_to_base64(self, image: Image) -> str:
        buffered = BytesIO()
        image.save(buffered, format='JPEG')

        return base64.b64encode(buffered.getvalue()).decode('utf-8')

    async def model_predict(self, image: Image, prompt: str) -> str:
        if not self.model:
            self.model = VLModel()

        image_base64 = await self._image_to_base64(image)
        vl_answer = await self.model.predict(image_base64=image_base64, prompt=prompt)

        return vl_answer