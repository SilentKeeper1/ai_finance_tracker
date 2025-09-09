#Сервіс для фінансової аналітики користувача.
class AnalyticsService:

    @staticmethod
    def aggregate_expenses(transactions):
        expenses = {}
        for tx in transactions:
            cat = tx.get('category')
            amt = tx.get('amount', 0)
            expenses[cat] = expenses.get(cat, 0) + amt
        return expenses
    
#Агрегує витрати по категоріях.
#:param transactions: список транзакцій (dict з 'category' та 'amount')
#:return: dict {category: total_amount}

    @staticmethod
    def get_top_expense_category(expenses):
        if not expenses:
            return None, 0
        top_cat = max(expenses, key=expenses.get)
        return top_cat, expenses[top_cat]
    
#Знаходить категорію з найбільшими витратами.
#:param expenses: dict {category: total_amount}
#:return: (category, amount)

    @staticmethod
    def aggregate_income(transactions):

            income = {}
            for tx in transactions:
                if tx.get('type') == 'income':
                    cat = tx.get('category')
                    amt = tx.get('amount', 0)
                    income[cat] = income.get(cat, 0) + amt
            return income
    

#Агрегує доходи по категоріях.
#:param transactions: список транзакцій (dict з 'category', 'amount', 'type')
#:return: dict {category: total_income}


    @staticmethod
    def get_summary(transactions):

            expenses = AnalyticsService.aggregate_expenses(transactions)
            income = AnalyticsService.aggregate_income(transactions)
            top_cat, top_amt = AnalyticsService.get_top_expense_category(expenses)
            return {
                "total_expenses": sum(expenses.values()),
                "total_income": sum(income.values()),
                "top_expense_category": top_cat,
                "top_expense_amount": top_amt,
                "expenses_by_category": expenses,
                "income_by_category": income,
            }
#Повертає коротку аналітику по транзакціях.
#:param transactions: список транзакцій
#:return: dict з агрегованими даними