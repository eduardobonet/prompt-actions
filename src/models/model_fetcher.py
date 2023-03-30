from .model import Model
import importlib


class ModelFetcher:
    def fetch_model(self, model_name: str) -> Model:
        module_name, model_name = model_name.split("__")

        module = importlib.import_module(f"models.{module_name}")
        fetcher: ModelFetcher = module.ModelFetcher()

        return fetcher.fetch_model(model_name)
