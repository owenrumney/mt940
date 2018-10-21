#!/bin/python

import mt940
import json
from pprint import pprint as pretty_print

def default(value):
    if isinstance(value, mt940.models.Transactions):
        data = value.data.copy()
        data['transactions'] = value.transactions
        return data

    elif hasattr(value, 'data'):
        return value.data



# load the transactions
rabo_transactions = mt940.parse('rabobank.txt')
print("Final Opening Balance: ", rabo_transactions.data.get('final_opening_balance'))
print("Final Closing Balance: ", rabo_transactions.data.get('final_closing_balance'))
print("Transactions:")
for transaction in rabo_transactions:
    pretty_print(transaction.data)

# write to a json file
with open('rabobank.json', 'w') as w:
    w.write(json.dumps(rabo_transactions, default=default, indent=4))
