from datetime import datetime, date
import json
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

EXPENSE_FILE = os.path.join(os.path.dirname(__file__), 'expenses.json')

# Expense class to represent a task
class Expense:
    def __init__(self, id, description, amount, expense_date=None):
        self.id             = id
        self.description    = description
        self.amount         = float(amount)
        self.date           = (
            date.fromisoformat(expense_date)
            if expense_date else
            date.today()
        )

    # String representation of the task
    def to_dict(self):
        return {
            "id": self.id,
            "Date": self.date.isoformat(),
            "description": self.description,
            "amount": self.amount,

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
def add_expense(description, amount, expense_date=None):
    expenses = load_expenses()
    new_expense = {
        "id": len(expenses) + 1,
        "Date": expense_date or date.today().isoformat(),
        "Description": description,
        "Amount": amount,
    }
    expenses.append(new_expense)
    save_expenses(expenses)
    print(f"Expense added: {new_expense}")


def list_expenses():
    """List all expenses"""
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return []

    # Set fields and headers
    fields = ['id', 'Date', 'Description','Amount']
    headers = ['ID', 'Date', 'Description', 'Amount']

    # Compute max width for each column
    widths = []
    for fld, hdr in zip(fields, headers):
        max_data = max(len(str(expense.get(fld, ''))) for expense in expenses)
        widths.append(max(max_data, len(hdr)))

    # print the header row
    header_row = " ".join(hdr.ljust(w) for hdr, w in zip(headers, widths))
    print(header_row)
    print(" ".join('-' * w for w in widths))

    # print each expense row
    for expense in expenses:
        row_cells = []
        for fld, w in zip(fields, widths):
            cell = str(expense.get(fld, ''))

            if fld in ('id', 'Amount'):
                row_cells.append(cell.rjust(w))
            else:
                row_cells.append(cell.ljust(w))
        print(" ".join(row_cells))

    return expenses

"""update an expense"""
def update_expense(expense_id, amount):
    expenses = load_expenses()
    for expense in expenses:
        if expense["id"] == expense_id:
            expense["Amount"] = amount
            save_expenses(expenses)
            print(f"Expense {expense_id} updated amount to {amount}")
            return
    print(f"Expense {expense_id} not found")

"""Delete an expense"""
def delete_expense(expense_id):
    expenses = load_expenses()
    expenses = [expense for expense in expenses if expense["id"] != expense_id]
    save_expenses(expenses)
    print(f"Expense {expense_id} deleted")

def view_summary():
    expenses = load_expenses()
    for expense in expenses:
        total += expenses

    return total