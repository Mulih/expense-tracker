# Expense Tracker

The **Expense Tracker** is a command-line application that helps you manage your expenses. You can add, list, update, delete, and view summaries of your expenses. The data is stored in a JSON file for persistence.

---

## Features

- **Add Expenses**: Add a new expense with a description, amount, and optional date.
- **List Expenses**: View all recorded expenses in a tabular format.
- **Update Expenses**: Update the amount of an expense by its ID.
- **Delete Expenses**: Remove an expense by its ID.
- **View Summary**: View the total expenses, optionally filtered by a specific month.

---

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd expense-tracker

2. Create a virtual environment and activate it:

```python
python3 -m venv venv
source venv/bin/activate
```

1. Install dependencies (if any):

```python
pip install -r requirements.txt
```

Usage
Run the application using the following command:

```python
./expense_tracker <command> [options]
```

### Commands

1. Add an Expense
Add a new expense with a description and amount:

```python
./expense_tracker add --description "lunch" --amount 20
```

2. List All Expenses
List all recorded expenses in a tabular format:

```python
./expense_tracker list
```

3. Update an Expense
Update the amount of an expense by its ID:

```python
./expense_tracker update --id 1 --amount 25
```

4. Delete an Expense
Delete an expense by its ID:

```python
./expense_tracker delete --id 1
```

5. View Summary
View the total expenses:

```python
./expense_tracker summary
```

View the total expenses for a specific month:

```python
./expense_tracker summary --month 5
```

Data Storage
Expenses are stored in a JSON file located at:

```python
[expenses.json]
```

Example JSON Structure:

```python
[
    {
        "id": 1,
        "Date": "2025-05-08",
        "Description": "lunch",
        "Amount": 20.0
    },
    {
        "id": 2,
        "Date": "2025-05-08",
        "Description": "WiFi",
        "Amount": 4000.0
    }
]
```

Project Structure
expense-tracker/
├── expense_tracker_py/
│   ├── __init__.py
│   ├── expense.py
│   ├── expense_tracker
│   ├── expenses.json
├── [README.md]

Future Enhancements
Add support for exporting expenses to CSV or Excel.
Implement category-based expense tracking.
Add support for recurring expenses.
License
This project is licensed under the MIT License. See the LICENSE file for details.
