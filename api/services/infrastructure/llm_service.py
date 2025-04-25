from utils.llm_model import LLModel


class LLModelService:
    def __init__(self, context: str):
        self.context = context
        self.model = None

    async def model_predict(self, prompt: str) -> str:
        if not self.model:
            self.model = LLModel()

        llm_answer = await self.model.predict(prompt=prompt, context=self.context)

        return llm_answer
