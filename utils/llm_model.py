from transformers import AutoModelForCausalLM, AutoTokenizer
from huggingface_hub import InferenceClient, login

from settings import config_parameters


class LLModel:
    def __init__(self):
        self.client = None

    async def _load_model(self):
        login(token=config_parameters.HF_TOKEN)
        self.client = InferenceClient(model='Qwen/Qwen2.5-1.5B-Instruct')

    async def predict(self, prompt: str) -> str:
        if not self.client:
            await self._load_model()

        response = self.client.text_generation(prompt, max_new_tokens=100)

        return response
