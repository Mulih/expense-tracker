#!/usr/bin/env python3
from argparse import ArgumentParser
import os
from expense import *

def main():
    """Main function to handle CLI commands."""
    parser = ArgumentParser(description="Expense Tracker CLI")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    