#Сервіс для генерації AI-порад на основі фінансових даних користувача.
from ai_models import Advisor
from .analytics_service import AnalyticsService

class AIService:
    

    def __init__(self, advisor=None):
        self.advisor = advisor or Advisor()

    def get_advice(self, transactions, prompt):

        user_data = AnalyticsService.get_summary(transactions)
        advice = self.advisor.get_advice(user_data, prompt)
        return advice
    

#Генерує пораду на основі транзакцій та запиту користувача.
#:param transactions: список транзакцій
#:param prompt: текстовий запит
#:return: текст поради
