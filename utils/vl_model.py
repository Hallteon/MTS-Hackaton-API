import base64
import torch
import requests

import numpy as np
import matplotlib.pyplot as plt

from io import BytesIO

from transformers import AutoModelForCausalLM, AutoTokenizer
from PIL import Image
from typing import Union, Optional

from settings import config_parameters

# Попросил накидать DeepSeek (чтобы шаблон для vl на основе чего-то хотя-бы сделать)

class VLModel:
    def __init__(self):
        self.model_name = "qwen/qwen-2.5-vl-7b-instruct"
        self.headers = {
            "Authorization": f"Bearer {config_parameters.OPEN_ROUTER_KEY}",
            "HTTP-Referer": "https://github.com/",
            "X-Title": "MTS HACK",
        }

    async def predict(self, image_base64: str,
                      prompt: str) -> str:
        data = {
            "model": self.model_name,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Детально опиши это изображение:"},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"}}
                    ]
                }
            ],
            "max_tokens": 500
        }

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=self.headers,
            json=data
        )

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f'Ошибка {response.status_code}'


if __name__ == "__main__":
    import cv2

    # Инициализация модели
    model = VLModel()

    # Загрузка изображения (пример)
    image_path = "example.jpg"
    image_np = cv2.imread(image_path)
    image_np = cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB)  # Конвертация в RGB

    # Запрос к изображению
    query = "Опиши, что изображено на картинке?"

    # Получение ответа
    answer = model.predict(image_np, query)
    print("Ответ модели:", answer)