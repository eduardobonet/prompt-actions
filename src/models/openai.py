from .model_fetcher import ModelFetcher as BaseFetcher
from .model import Model
import os
import requests


class OpenAiModel(Model):
    def __init__(self, model_name):
        self.model_name = model_name
        self.api_key = os.environ['OPENAI_API_KEY']
        self.open_ai_url = 'https://api.openai.com/v1/completions'

    def call(self, prompt: str) -> str:
        request_params = {
            'model': self.model_name,
            'prompt': prompt,
            'max_tokens': 500,
            'echo': True
        }

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f"Bearer {self.api_key}"
        }
        print(request_params)
        response = requests.post(self.open_ai_url, json=request_params, headers=headers)

        return response.json()


class ModelFetcher(BaseFetcher):
    def fetch_model(self, model_name: str) -> OpenAiModel:
        return OpenAiModel(model_name)
