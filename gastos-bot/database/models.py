# database/models.py
class Expense:
    def __init__(self, id, amount, category, date, description=None):
        self.id = id
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description
