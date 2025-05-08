from datetime import datetime
import json
import os

EXPENSE_FILE = os.path.join(os.path.dirname(__file__), 'tasks.json')

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
            amount=data["status"],
            created_at=datetime.fromisoformat(data["created_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
        )

"""Load tasks to a JSON file."""