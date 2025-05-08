#!/usr/bin/env python3
from argparse import ArgumentParser, Namespace
import os
from expense import *

def main():
    """Main function to handle CLI commands."""
    parser = ArgumentParser(description="Expense Tracker CLI")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    add_parser = subparsers.add_parser("add", help="A new expense")
    add_parser.add_argument("--description",type=str, required=True, help="Expense description")
    add_parser.add_argument("--amount", type=float, required=True, help="Expense amount")

    args: Namespace = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    commands = {
        "add": lambda: add_expense(args.description, args.amount),
    }

    command_function = commands.get(args.command, parser.print_help)
    command_function()


if __name__ == "__main__":
    main()