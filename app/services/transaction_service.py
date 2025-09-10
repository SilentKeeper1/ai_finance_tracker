from .analytics_service import AnalyticsService

class TransactionService:
    """
    Сервіс для роботи з транзакціями користувача та аналітикою.
    """

    @staticmethod
    def add_transaction(transactions, tx):
        """
        Додає нову транзакцію до списку.
        :param transactions: список існуючих транзакцій
        :param tx: dict з даними транзакції (type, category, amount)
        :return: оновлений список транзакцій
        """
        transactions.append(tx)
        return transactions

    @staticmethod
    def get_transactions_by_type(transactions, tx_type):
        """
        Повертає транзакції певного типу (income/expense).
        """
        return [tx for tx in transactions if tx.get("type") == tx_type]

    @staticmethod
    def get_transactions_by_category(transactions, category):
        """
        Повертає транзакції певної категорії.
        """
        return [tx for tx in transactions if tx.get("category") == category]

    @staticmethod
    def get_total_amount(transactions, tx_type=None):
        """
        Рахує загальну суму транзакцій (за типом або всі).
        """
        if tx_type:
            return sum(tx.get("amount", 0) for tx in transactions if tx.get("type") == tx_type)
        return sum(tx.get("amount", 0) for tx in transactions)

    @staticmethod
    def get_analytics(transactions):
        """
        Повертає аналітику по транзакціях через AnalyticsService.
        """
        return AnalyticsService.get_summary(transactions)