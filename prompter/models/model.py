class Model:
    def call(self, prompt: str) -> str:
        raise NotImplementedError('Call must be implemented')
