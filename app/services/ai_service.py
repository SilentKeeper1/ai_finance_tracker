#Модель для аналітики витрат і генерації креативних рішень для бізнесу та приватних користувачів.
class BudgetAdvisorModel:

    @staticmethod
    def analyze(transactions, user_type="personal"):
        expenses = {}
        income = 0
        for tx in transactions:
            if tx.get("type") == "income":
                income += tx.get("amount", 0)
            elif tx.get("type") == "expense":
                cat = tx.get("category")
                amt = tx.get("amount", 0)
                expenses[cat] = expenses.get(cat, 0) + amt

        top_cat = max(expenses, key=expenses.get) if expenses else None
        budget = income - sum(expenses.values())
        analysis = {
            "total_income": income,
            "total_expenses": sum(expenses.values()),
            "budget": budget,
            "top_expense_category": top_cat,
            "top_expense_amount": expenses.get(top_cat, 0) if top_cat else 0,
            "expenses_by_category": expenses,
        }
        return analysis

    @staticmethod
    def get_recommendation(analysis, user_type="personal"):
        recs = []
        # Загальні поради
        if analysis["budget"] < 0:
            recs.append("Ви витрачаєте більше, ніж заробляєте. Спробуйте скоротити витрати або збільшити доходи.")
        else:
            recs.append("Ваш бюджет позитивний. Можна розглянути варіанти для інвестування чи заощаджень.")

        # Поради для найбільшої категорії витрат
        if analysis["top_expense_category"]:
            recs.append(
                f"Найбільше ви витрачаєте на '{analysis['top_expense_category']}' ({analysis['top_expense_amount']} грн). "
                "Спробуйте знайти альтернативи або оптимізувати витрати у цій категорії."
            )

        # Креативні рішення для бізнесу
        if user_type == "business":
            if analysis["budget"] < 0:
                recs.append(
                    "Для бізнесу: оптимізуйте операційні витрати, автоматизуйте процеси, "
                    "перегляньте контракти з постачальниками, впровадьте бюджетування проектів."
                )
            else:
                recs.append(
                    "Для бізнесу: розгляньте інвестування у розвиток, маркетинг або нові продукти."
                )
            if "маркетинг" in analysis["expenses_by_category"]:
                recs.append(
                    "Перевірте ефективність маркетингових витрат: використовуйте аналітику для оптимізації каналів."
                )
        # Креативні рішення для приватних користувачів
        else:
            if analysis["budget"] < 0:
                recs.append(
                    "Спробуйте вести щоденник витрат, встановіть ліміти на покупки, "
                    "шукайте акції та знижки, використовуйте кешбек-сервіси."
                )
            else:
                recs.append(
                    "Відкладіть частину доходу у фонд заощаджень або інвестуйте у власний розвиток."
                )
        return "\n".join(recs)

# Приклад використання:
# transactions = [
#     {"type": "income", "category": "зарплата", "amount": 40000},
#     {"type": "expense", "category": "їжа", "amount": 200},
#     {"type": "expense", "category": "оренда", "amount": 20000},
#     {"type": "expense", "category": "маркетинг", "amount": 5000},
# ]
# analysis = BudgetAdvisorModel.analyze(transactions, user_type="business")
# advice = BudgetAdvisorModel.get_recommendation(analysis, user_type="business")