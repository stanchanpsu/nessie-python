#!/usr/bin/env python
import json
import requests
import credentials

# /atms
atm_payload = {'lat': "", 'long': "", 'key': credentials.api_key}
r = requests.get(credentials.base_url + "atms", params=atm_payload)

print "ATM GET: " + str(r.status_code)

# /Customer
key_payload = {'key': credentials.api_key}
r = requests.get(credentials.base_url + "customers", params=key_payload)

print "Customer GET: " + str(r.status_code)

# /Account
account_payload = {'type': "Credit Card", 'nickname': "Steve", 'balance': 12, 'rewards': 12}
account_url = credentials.base_url + "customers/" + credentials.customer_id + "/accounts?key=" + credentials.api_key
r = requests.post(account_url, json=account_payload)

print "Account POST: " + str(r.status_code)

# /Bills
bills_payload = {
  "status": "pending",
  "payee": "string",
  "nickname": "string",
  "payment_date": "2017-01-12",
  "recurring_date": 1,
  "payment_amount": 0.01
}

bills_url = credentials.base_url + "accounts/" + credentials.account_id + "/bills?key=" + credentials.api_key
r = requests.post(bills_url, json=bills_payload)

print "Bills POST: " + str(r.status_code)

# /Purchase
purchase_url = credentials.base_url + "accounts/" + credentials.account_id + "/purchases"
r = requests.get(purchase_url,params=key_payload)

print "Purchase GET: " + str(r.status_code)

# /Transfer
transfer_payload = {
  "medium": "balance",
  "payee_id": credentials.second_account_id,
  "amount": 0.01,
  "transaction_date": "2017-01-12",
  "description": "string"
}
transfer_url = credentials.base_url + "accounts/" + credentials.account_id + "/transfers?key=" + credentials.api_key
r = requests.post(transfer_url, json=transfer_payload)

print "Transfer POST: " + str(r.status_code)

# /Enterprise
enterprise_url = credentials.base_url + "enterprise/customers/" + credentials.customer_id
r = requests.get(enterprise_url, params = key_payload)

print "Enterprise Customer GET: " + str(r.status_code)