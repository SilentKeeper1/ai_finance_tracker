import os

class Advisor:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")

    def get_advice(self, user_data, prompt):

        return (
            f"Базуючись на ваших даних ({user_data}), ось порада щодо '{prompt}':\n"
            "Спробуйте оптимізувати витрати у категорії, яка найбільша. "
            "Для детальнішої поради інтегруйте LLM."
        )