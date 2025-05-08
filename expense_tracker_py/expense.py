from datetime import datetime
import json
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

EXPENSE_FILE = os.path.join(os.path.dirname(__file__), 'expenses.json')

# Expense class to represent a task
class Expense:
    def __init__(self, id, description, amount, created_at=None, updated_at=None):
        self.id = id
        self.description = description
        self.amount = amount
        self.created_at = created_at if created_at else datetime.now()
        self.updated_at = updated_at if updated_at else datetime.now()

    # String representation of the task
    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "amount": self.amount,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            description=data["description"],
            amount=data["amount"],
            created_at=datetime.fromisoformat(data["created_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
        )

"""Load expenses to a JSON file"""
def load_expenses():
    # load tasks from the JSON file
    if not os.path.exists(EXPENSE_FILE):
        return [] # return empty file
    with open(EXPENSE_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            print("Error opening file, starting with empty expense list")
            return []

"""Save expenses to a expenses.json file"""
def save_expenses(expenses):
    with open(EXPENSE_FILE, 'w') as f:
        json.dump(expenses, f, indent=4)

"""Add a new expense"""
def add_expense(description, amount):
    expenses = load_expenses()
    new_expense = {
        "id": len(expenses) + 1,
        "Description": description,
        "Amount": amount,
    }
    expenses.append(new_expense)
    save_expenses(expenses)
    print(f"Expense added: {new_expense}")
