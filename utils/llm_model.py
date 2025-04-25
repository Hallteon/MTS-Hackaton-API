import torch
import requests

from settings import config_parameters


class LLModel:
    def __init__(self):
        self.model_name = "qwen/qwen-2.5-7b-instruct:free"
        self.headers = {
            "Authorization": f"Bearer {config_parameters.OPEN_ROUTER_KEY}",
            "HTTP-Referer": "https://github.com/",
            "X-Title": "MTS HACK",
        }

    async def predict(self, context: str,
                      prompt: str) -> str:
        data = {
            "model": self.model_name,
            "messages": [
                {"role": "user",
                 "content": context},
                {"role": "system",
                 "content": prompt},
            ],
            "temperature": 0.7,
            "max_tokens": 100
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