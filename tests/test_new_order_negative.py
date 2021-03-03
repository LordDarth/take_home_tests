import requests
import json
import base64
import hmac
import hashlib
import datetime, time
import unittest
import pytest
from helper import *


#default order values
request= "/v1/order/new"
symbol= "btcusd"
price= "18000"
stop_price= "17000"
amount= "1"
side= "buy"
order_type= "exchange limit"
options= "maker-or-limit"

base_url = "https://api.sandbox.gemini.com"
endpoint = "/v1/order/new"
url = base_url + endpoint

gemini_api_key = "account-iDp4LehhNXFOebUikonS"
gemini_api_secret = "CFG4EiSa4bKunGvyrABawKagpGf".encode()




class TestNewOrderNegative(unittest.TestCase):


#test buy order invalid symbol
	def test_new_order_buy_invalid_symbol(self):

		time.sleep(1)
		payload_nonce = generate_nonce()


		payload = {
			"request": request,
			"nonce": payload_nonce,
			"symbol": "eth2usd",
			"amount": amount,
			"price": "3633.00",
			"side": side,
			"type": "exchange limit",
			#"options": ["maker-or-cancel"]
			}

		signature,b64=generate_signature(payload,gemini_api_secret)

		request_headers=generate_request_header(signature,b64,gemini_api_key)

		response = requests.post(url,
						data=None,
						headers=request_headers)

		new_order = response.json()
		print(new_order)

		errors=[]

		#check if order details are what we expect

		if len(new_order)<=3:
			if new_order["result"]=='error':
				if "unsupported symbol" in new_order["message"]:
					errors.append("order rejected")
					errors.append(new_order["message"])
		assert errors, "order rejected:\n{}".format("\n".join(errors))



#test sell order invalid symbol
	def test_new_order_sell_invalid_symbol(self):
		#sleep for 1 second to get a different nonce
		time.sleep(1)

		payload_nonce = generate_nonce()

		payload = {
			"request": request,
			"nonce": payload_nonce,
			"symbol": "eth2usd",
			"amount": amount,
			"price": "1500.00",
			"side": "sell",
			"type": "exchange limit",
			#"options": ["maker-or-cancel"]
			}

		signature,b64=generate_signature(payload,gemini_api_secret)

		request_headers=generate_request_header(signature,b64,gemini_api_key)

		response = requests.post(url,
						data=None,
						headers=request_headers)

		new_order = response.json()
		print(new_order)


		errors=[]

		#check if order details are what we expect

		if len(new_order)<=3:
			if new_order["result"]=='error':
				if "unsupported symbol" in new_order["message"]:
					errors.append("order rejected")
					errors.append(new_order["message"])
		assert errors, "order rejected:\n{}".format("\n".join(errors))



#test buy order invalid order type
	def test_new_order_buy_invalid_type(self):
		time.sleep(1)

		payload_nonce = generate_nonce()


		payload = {
			"request": request,
			"nonce": payload_nonce,
			"symbol": symbol,
			"amount": amount,
			"price": "3633.00",
			"side": side,
			"type": "invalid type",
			#"options": ["maker-or-cancel"]
			}

		signature,b64=generate_signature(payload,gemini_api_secret)

		request_headers=generate_request_header(signature,b64,gemini_api_key)

		response = requests.post(url,
						data=None,
						headers=request_headers)

		new_order = response.json()
		print(new_order)

		errors=[]

		#check if order details are what we expect

		if len(new_order)<=3:
			if new_order["result"]=='error':
				if "Invalid order type" in new_order["message"]:
					errors.append("order rejected")
					errors.append(new_order["message"])
		assert errors, "order rejected:\n{}".format("\n".join(errors))



#test sell order invalid order type
	def test_new_order_sell_invalid_type(self):
		#sleep for 1 second to get a different nonce
		time.sleep(1)

		payload_nonce = generate_nonce()

		payload = {
			"request": request,
			"nonce": payload_nonce,
			"symbol": "ethusd",
			"amount": amount,
			"price": "1500.00",
			"side": "sell",
			"type": "invalid type",
			#"options": ["maker-or-cancel"]
			}

		signature,b64=generate_signature(payload,gemini_api_secret)

		request_headers=generate_request_header(signature,b64,gemini_api_key)

		response = requests.post(url,
						data=None,
						headers=request_headers)

		new_order = response.json()
		print(new_order)


		errors=[]

		#check if order details are what we expect

		if len(new_order)<=3:
			if new_order["result"]=='error':
				if "Invalid order type" in new_order["message"]:
					errors.append("order rejected")
					errors.append(new_order["message"])
		assert errors, "order rejected:\n{}".format("\n".join(errors))




#test buy order invalid side
	def test_new_order_buy_invalid_side(self):

		time.sleep(1)
		payload_nonce = generate_nonce()


		payload = {
			"request": request,
			"nonce": payload_nonce,
			"symbol": symbol,
			"amount": amount,
			"price": "3633.00",
			"side": "buyer",
			"type": order_type,
			#"options": ["maker-or-cancel"]
			}

		signature,b64=generate_signature(payload,gemini_api_secret)

		request_headers=generate_request_header(signature,b64,gemini_api_key)

		response = requests.post(url,
						data=None,
						headers=request_headers)

		new_order = response.json()
		print(new_order)

		errors=[]

		#check if order details are what we expect

		if len(new_order)<=3:
			if new_order["result"]=='error':
				if "Invalid side" in new_order["message"]:
					errors.append("order rejected")
					errors.append(new_order["message"])
		assert errors, "order rejected:\n{}".format("\n".join(errors))



#test sell order invalid side
	def test_new_order_sell_invalid_side(self):
		#sleep for 1 second to get a different nonce
		time.sleep(1)

		payload_nonce = generate_nonce()

		payload = {
			"request": request,
			"nonce": payload_nonce,
			"symbol": "ethusd",
			"amount": amount,
			"price": "1500.00",
			"side": "seller",
			"type": order_type,
			#"options": ["maker-or-cancel"]
			}

		signature,b64=generate_signature(payload,gemini_api_secret)

		request_headers=generate_request_header(signature,b64,gemini_api_key)

		response = requests.post(url,
						data=None,
						headers=request_headers)

		new_order = response.json()
		print(new_order)


		errors=[]

		#check if order details are what we expect

		if len(new_order)<=3:
			if new_order["result"]=='error':
				if "Invalid side" in new_order["message"]:
					errors.append("order rejected")
					errors.append(new_order["message"])
		assert errors, "order rejected:\n{}".format("\n".join(errors))



#test stop limit sell order invalid stop price
	def test_new_order_stop_limit_sell_invalid_stop_price(self):
		#sleep for 1 second to get a different nonce
		time.sleep(1)


		payload_nonce = generate_nonce()

		payload = {
			"request": request,
			"nonce": payload_nonce,
			"symbol": symbol,
			"amount": amount,
			"price": "15000.00",
			"side": "sell",
			"type": "exchange stop limit",
			"stop_price":"14000.00",
			#"options": ["maker-or-cancel"]
			}

		signature,b64=generate_signature(payload,gemini_api_secret)

		request_headers=generate_request_header(signature,b64,gemini_api_key)

		response = requests.post(url,
						data=None,
						headers=request_headers)

		new_order = response.json()
		print(new_order)


		errors=[]

		#check if order details are what we expect

		if len(new_order)<=3:
			if new_order["result"]=='error':
				if "must be greater" in new_order["message"]:
					errors.append("order rejected")
					errors.append(new_order["message"])
		assert errors, "order rejected:\n{}".format("\n".join(errors))



#test stop limit buy order invalid stop price
	def test_new_order_stop_limit_buy_invalid_stop_price(self):
		#sleep for 1 second to get a different nonce
		time.sleep(1)


		payload_nonce = generate_nonce()

		payload = {
			"request": request,
			"nonce": payload_nonce,
			"symbol": symbol,
			"amount": amount,
			"price": "3600.00",
			"side": side,
			"type": "exchange stop limit",
			"stop_price":"3800.00",
			#"options": ["maker-or-cancel"]
			}

		signature,b64=generate_signature(payload,gemini_api_secret)

		request_headers=generate_request_header(signature,b64,gemini_api_key)

		response = requests.post(url,
						data=None,
						headers=request_headers)

		new_order = response.json()
		print(new_order)


		errors=[]

		#check if order details are what we expect

		if len(new_order)<=3:
			if new_order["result"]=='error':
				if "must be lower" in new_order["message"]:
					errors.append("order rejected")
					errors.append(new_order["message"])
		assert errors, "order rejected:\n{}".format("\n".join(errors))



#test stop limit sell order invalid option
	def test_new_order_stop_limit_sell_invalid_option(self):
		#sleep for 1 second to get a different nonce
		time.sleep(1)


		payload_nonce = generate_nonce()

		payload = {
			"request": request,
			"nonce": payload_nonce,
			"symbol": symbol,
			"amount": amount,
			"price": "15000.00",
			"side": "sell",
			"type": "exchange stop limit",
			"stop_price":stop_price,
			"options": ["maker-or-cancel"]
			}

		signature,b64=generate_signature(payload,gemini_api_secret)

		request_headers=generate_request_header(signature,b64,gemini_api_key)

		response = requests.post(url,
						data=None,
						headers=request_headers)

		new_order = response.json()
		print(new_order)


		errors=[]

		#check if order details are what we expect

		if len(new_order)<=3:
			if new_order["result"]=='error':
				if "Stop Limit orders only support Standard order behavior" in new_order["message"]:
					errors.append("order rejected")
					errors.append(new_order["message"])
		assert errors, "order rejected:\n{}".format("\n".join(errors))



#test stop limit buy order invalid option
	def test_new_order_stop_limit_buy_invalid_option(self):
		#sleep for 1 second to get a different nonce
		time.sleep(1)


		payload_nonce = generate_nonce()

		payload = {
			"request": request,
			"nonce": payload_nonce,
			"symbol": symbol,
			"amount": amount,
			"price": "3600.00",
			"side": side,
			"type": "exchange stop limit",
			"stop_price":"3500.00",
			"options": ["immediate-or-cancel"]
			}

		signature,b64=generate_signature(payload,gemini_api_secret)

		request_headers=generate_request_header(signature,b64,gemini_api_key)

		response = requests.post(url,
						data=None,
						headers=request_headers)

		new_order = response.json()
		print(new_order)


		errors=[]

		#check if order details are what we expect

		if len(new_order)<=3:
			if new_order["result"]=='error':
				if "Stop Limit orders only support Standard order behavior" in new_order["message"]:
					errors.append("order rejected")
					errors.append(new_order["message"])
		assert errors, "order rejected:\n{}".format("\n".join(errors))


