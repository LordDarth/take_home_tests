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

gemini_api_key = "account"
gemini_api_secret = "secret".encode()




class TestNewOrderPositive(unittest.TestCase):



#test buy order
	def test_new_order_buy(self):


		payload_nonce = generate_nonce()


		payload = {
			"request": request,
			"nonce": payload_nonce,
			"symbol": symbol,
			"amount": amount,
			"price": "3633.00",
			"side": side,
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

		errors=[] #popupate with order data mismatch

		#check if order details are what we expect
		if len(new_order)<=3:
			if new_order["result"]=='error':
				errors.append("order rejected")
				errors.append(new_order["message"])
				assert not errors, "order rejected:\n{}".format("\n".join(errors))

		if not (new_order["side"] == 'buy'):
			errors.append("side did not match")

		if not (new_order["symbol"]=="btcusd"):
			errors.append("symbol did not match")

		if not (new_order["type"]=="exchange limit"):
			errors.append("type did not match")

		if not (new_order["is_cancelled"]==False):
			errors.append("order state did not match")

		if not (new_order["price"]=="3633.00"):
			errors.append("price did not match")

		if not (new_order["original_amount"]=="1"):
			errors.append("original amount did not match")


		assert not errors, "errors occured:\n{}".format("\n".join(errors))

#test sell order
	def test_new_order_sell(self):
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


		errors=[] #popupate with order data mismatch

		#check if order details are what we expect
		if len(new_order)<=3:
			if new_order["result"]=='error':
				errors.append("order rejected")
				errors.append(new_order["message"])
				assert not errors, "order rejected:\n{}".format("\n".join(errors))

		if not (new_order["side"] == 'sell'):
			errors.append("side did not match")

		if not (new_order["symbol"]=="ethusd"):
			errors.append("symbol idid not match")

		if not (new_order["type"]=="exchange limit"):
			errors.append("type did not match")

		if not (new_order["is_cancelled"]==False):
			errors.append("order state did not match")

		if not (new_order["price"]=="1500.00"):
			errors.append("price did not match")

		if not (new_order["original_amount"]=="1"):
			errors.append("original amount is not did not match")


		assert not errors, "errors occured:\n{}".format("\n".join(errors))



#test stop limit sell order
	def test_new_order_stop_limit_sell(self):
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
			#"options": ["maker-or-cancel"]
			}

		signature,b64=generate_signature(payload,gemini_api_secret)

		request_headers=generate_request_header(signature,b64,gemini_api_key)

		response = requests.post(url,
						data=None,
						headers=request_headers)

		new_order = response.json()
		print(new_order)


		errors=[] #popupate with order data mismatch

		#check if order details are what we expect
		if len(new_order)<=3:
			if new_order["result"]=='error':
				errors.append("order rejected")
				errors.append(new_order["message"])
				assert not errors, "order rejected:\n{}".format("\n".join(errors))

		if not (new_order["side"] == 'sell'):
			errors.append("side did not match")

		if not (new_order["symbol"]=="btcusd"):
			errors.append("symbol did not match")

		if not (new_order["type"]=="stop-limit"):
			errors.append("type did not match")

		if not (new_order["is_cancelled"]==False):
			errors.append("order state did not match")

		if not (new_order["price"]=="15000.00"):
			errors.append("price did not match")

		if not (new_order["original_amount"]=="1"):
			errors.append("original amount did not match")

		if not (new_order["stop_price"]=="17000.00"):
			errors.append("stop_price did not match")

		assert not errors, "errors occured:\n{}".format("\n".join(errors))


#test stop limit buy order
	def test_new_order_stop_limit_buy(self):
		#sleep for 1 second to get a different nonce
		time.sleep(1)


		payload_nonce = generate_nonce()

		payload = {
			"request": request,
			"nonce": payload_nonce,
			"symbol": symbol,
			"amount": amount,
			"price": "19500.00",
			"side": side,
			"type": "exchange stop limit",
			"stop_price":"19000.00",
			#"options": ["maker-or-cancel"]
			}

		signature,b64=generate_signature(payload,gemini_api_secret)

		request_headers=generate_request_header(signature,b64,gemini_api_key)

		response = requests.post(url,
						data=None,
						headers=request_headers)

		new_order = response.json()
		print(new_order)


		errors=[] #popupate with order data mismatch

		#check if order details are what we expect
		if len(new_order)<=3:
			if new_order["result"]=='error':
				errors.append("order rejected")
				errors.append(new_order["message"])
				assert not errors, "order rejected:\n{}".format("\n".join(errors))

		if not (new_order["side"] == "buy"):
			errors.append("side did not match")

		if not (new_order["symbol"]=="btcusd"):
			errors.append("symbol did not match")

		if not (new_order["type"]=="stop-limit"):
			errors.append("type is not limit")

		if not (new_order["is_cancelled"]==False):
			errors.append("order stae did not match")

		if not (new_order["price"]=="19500.00"):
			errors.append("price did not match")

		if not (new_order["original_amount"]=="1"):
			errors.append("original amount did not match")

		if not (new_order["stop_price"]=="19000.00"):
			errors.append("stop_price did not match")

		assert not errors, "errors occured:\n{}".format("\n".join(errors))


#test  limit maker or cancel buy order
	def test_new_order_limit_maker_or_cancel_buy(self):
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
			"type": "exchange limit",
			"options": ["maker-or-cancel"],
			}

		signature,b64=generate_signature(payload,gemini_api_secret)

		request_headers=generate_request_header(signature,b64,gemini_api_key)

		response = requests.post(url,
						data=None,
						headers=request_headers)

		new_order = response.json()
		print(new_order)


		errors=[] #popupate with order data mismatch

		#check if order details are what we expect
		if len(new_order)<=3:
			if new_order["result"]=='error':
				errors.append("order rejected")
				errors.append(new_order["message"])
				assert not errors, "order rejected:\n{}".format("\n".join(errors))

		if not (new_order["side"] == "buy"):
			errors.append("side did not match")

		if not (new_order["symbol"]=="btcusd"):
			errors.append("symbol did not match")

		if not (new_order["type"]=="exchange limit"):
			errors.append("type did not match")

		if not (new_order["is_cancelled"]==False):
			errors.append("order state did not match")

		if not (new_order["price"]=="3600.00"):
			errors.append("price did not match")

		if not (new_order["original_amount"]=="1"):
			errors.append("original amount did not match")

		if  not(new_order["options"][0]=="maker-or-cancel"):
			errors.append("option did not match")


		assert not errors, "errors occured:\n{}".format("\n".join(errors))

#test  limit maker or cancel sell order
	def test_new_order_limit_maker_or_cancel_sell(self):
		#sleep for 1 second to get a different nonce
		time.sleep(1)


		payload_nonce = generate_nonce()

		payload = {
			"request": request,
			"nonce": payload_nonce,
			"symbol": symbol,
			"amount": amount,
			"price": "3600.00",
			"side": "sell",
			"type": "exchange limit",
			"options": ["maker-or-cancel"],
			}

		signature,b64=generate_signature(payload,gemini_api_secret)

		request_headers=generate_request_header(signature,b64,gemini_api_key)

		response = requests.post(url,
						data=None,
						headers=request_headers)

		new_order = response.json()
		print(new_order)


		errors=[] #popupate with order data mismatch

		#check if order details are what we expect
		if len(new_order)<=3:
			if new_order["result"]=='error':
				errors.append("order rejected")
				errors.append(new_order["message"])
				assert not errors, "order rejected:\n{}".format("\n".join(errors))

		if not (new_order["side"] == "sell"):
			errors.append("side did not match")

		if not (new_order["symbol"]=="btcusd"):
			errors.append("symbol did not match")

		if not (new_order["type"]=="exchange limit"):
			errors.append("type did not match")

		if not (new_order["is_cancelled"]==True): #if trade possible then order cancelled
			errors.append("order state did not match")

		if not (new_order["price"]=="3600.00"):
			errors.append("price did not match")

		if not (new_order["original_amount"]=="1"):
			errors.append("original amount did not match")

		if  not(new_order["options"][0]=="maker-or-cancel"):
			errors.append("option did not match")


		assert not errors, "errors occured:\n{}".format("\n".join(errors))

#test  limit immediate or cancel buy order
	def test_new_order_limit_immediate_or_cancel_buy(self):
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
			"type": "exchange limit",
			"options": ["immediate-or-cancel"],
			}

		signature,b64=generate_signature(payload,gemini_api_secret)

		request_headers=generate_request_header(signature,b64,gemini_api_key)

		response = requests.post(url,
						data=None,
						headers=request_headers)

		new_order = response.json()
		print(new_order)


		errors=[] #popupate with order data mismatch

		#check if order details are what we expect
		if len(new_order)<=3:
			if new_order["result"]=='error':
				errors.append("order rejected")
				errors.append(new_order["message"])
				assert not errors, "order rejected:\n{}".format("\n".join(errors))

		if not (new_order["side"] == "buy"):
			errors.append("side did not match")

		if not (new_order["symbol"]=="btcusd"):
			errors.append("symbol did not match")

		if not (new_order["type"]=="exchange limit"):
			errors.append("type did not match")

		if not (new_order["is_cancelled"]==True):
			errors.append("order state did not match")

		if not (new_order["price"]=="3600.00"):
			errors.append("price did not match")

		if not (new_order["original_amount"]=="1"):
			errors.append("original amount did not match")

		if  not(new_order["options"][0]=="immediate-or-cancel"):
			errors.append("order option did not match")



		assert not errors, "errors occured:\n{}".format("\n".join(errors))

#test  limit immediate or cancel sell order
	def test_new_order_limit_immediate_or_cancel_sell(self):
		#sleep for 1 second to get a different nonce
		time.sleep(1)


		payload_nonce = generate_nonce()

		payload = {
			"request": request,
			"nonce": payload_nonce,
			"symbol": symbol,
			"amount": amount,
			"price": "3600.00",
			"side": "sell",
			"type": "exchange limit",
			"options": ["immediate-or-cancel"],
			}

		signature,b64=generate_signature(payload,gemini_api_secret)

		request_headers=generate_request_header(signature,b64,gemini_api_key)

		response = requests.post(url,
						data=None,
						headers=request_headers)

		new_order = response.json()
		print(new_order)


		errors=[] #popupate with order data mismatch

		#check if order details are what we expect
		if len(new_order)<=3:
			if new_order["result"]=='error':
				errors.append("order rejected")
				errors.append(new_order["message"])
				assert not errors, "order rejected:\n{}".format("\n".join(errors))

		if not (new_order["side"] == "sell"):
			errors.append("side did not match")

		if not (new_order["symbol"]=="btcusd"):
			errors.append("symbol did not match")

		if not (new_order["type"]=="exchange limit"):
			errors.append("type did not match")

		if not (new_order["is_cancelled"]==False):
			errors.append("order state did not match")

		if not (new_order["price"]=="3600.00"):
			errors.append("price did not match")

		if not (new_order["original_amount"]=="1"):
			errors.append("original amount did not match")

		if  not(new_order["options"][0]=="immediate-or-cancel"):
			errors.append("option did not match")

		if  not(new_order["original_amount"]=="1"):
			errors.append("original amount did not match")

		if  not(new_order["remaining_amount"]=="0"):
			errors.append("remaining did not match")


		assert not errors, "errors occured:\n{}".format("\n".join(errors))


#test  limit fill or kill buy order
	def test_new_order_limit_fill_or_kill_buy(self):
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
			"type": "exchange limit",
			"options": ["fill-or-kill"],
			}

		signature,b64=generate_signature(payload,gemini_api_secret)

		request_headers=generate_request_header(signature,b64,gemini_api_key)

		response = requests.post(url,
						data=None,
						headers=request_headers)

		new_order = response.json()
		print(new_order)


		errors=[] #popupate with order data mismatch

		#check if order details are what we expect
		if len(new_order)<=3:
			if new_order["result"]=='error':
				errors.append("order rejected")
				errors.append(new_order["message"])
				assert not errors, "order rejected:\n{}".format("\n".join(errors))

		if not (new_order["side"] == "buy"):
			errors.append("side did not match")

		if not (new_order["symbol"]=="btcusd"):
			errors.append("symbol did not match")

		if not (new_order["type"]=="exchange limit"):
			errors.append("type did not match")

		if (new_order["executed_amount"]=="0"):
			if not (new_order["is_cancelled"]==True):
				errors.append("order state did not match")

		if not (new_order["price"]=="3600.00"):
			errors.append("price did not match")

		if not (new_order["original_amount"]=="1"):
			errors.append("original amount did not match")

		if  not(new_order["options"][0]=="fill-or-kill"):
			errors.append("option did not match")


		assert not errors, "errors occured:\n{}".format("\n".join(errors))

#test  limit fill or kill sell order
	def test_new_order_limit_fill_or_kill_sell(self):
		#sleep for 1 second to get a different nonce
		time.sleep(1)


		payload_nonce = generate_nonce()

		payload = {
			"request": request,
			"nonce": payload_nonce,
			"symbol": symbol,
			"amount": amount,
			"price": "3600.00",
			"side": "sell",
			"type": "exchange limit",
			"options": ["fill-or-kill"],
			}

		signature,b64=generate_signature(payload,gemini_api_secret)

		request_headers=generate_request_header(signature,b64,gemini_api_key)

		response = requests.post(url,
						data=None,
						headers=request_headers)

		new_order = response.json()
		print(new_order)


		errors=[] #popupate with order data mismatch

		#check if order details are what we expect
		if len(new_order)<=3:
			if new_order["result"]=='error':
				errors.append("order rejected")
				errors.append(new_order["message"])
				assert not errors, "order rejected:\n{}".format("\n".join(errors))

		if not (new_order["side"] == "sell"):
			errors.append("side did not match")

		if not (new_order["symbol"]=="btcusd"):
			errors.append("symbol did not match")

		if not (new_order["type"]=="exchange limit"):
			errors.append("type did not match")

		if (new_order["executed_amount"]=="0"):
			if not (new_order["is_cancelled"]==True):
				errors.append("order state did not match")

		if not (new_order["price"]=="3600.00"):
			errors.append("price did not match")

		if not (new_order["original_amount"]=="1"):
			errors.append("original amount did not match")

		if  not(new_order["options"][0]=="fill-or-kill"):
			errors.append("option did not match")


		assert not errors, "errors occured:\n{}".format("\n".join(errors))

###
#test  limit indication-of-interest buy order
	def test_new_order_limit_indication_of_interest_buy(self):
		#sleep for 1 second to get a different nonce
		time.sleep(1)


		payload_nonce = generate_nonce()

		payload = {
			"request": request,
			"nonce": payload_nonce,
			"symbol": symbol,
			"amount": "100",
			"price": "19633.00",
			"side": side,
			"type": "exchange limit",
			"options": ["indication-of-interest"],
			}

		signature,b64=generate_signature(payload,gemini_api_secret)

		request_headers=generate_request_header(signature,b64,gemini_api_key)

		response = requests.post(url,
						data=None,
						headers=request_headers)

		new_order = response.json()
		print(new_order)


		errors=[] #popupate with order data mismatch

		#check if order details are what we expect
		if len(new_order)<=3:
			if new_order["result"]=='error':
				errors.append("order rejected")
				errors.append(new_order["message"])
				assert not errors, "order rejected:\n{}".format("\n".join(errors))

		if not (new_order["side"] == "buy"):
			errors.append("side did not match")

		if not (new_order["symbol"]=="btcusd"):
			errors.append("symbol did not match")

		if not (new_order["type"]=="indication-of-interest limit"):
			errors.append("type did not match")

		if (new_order["executed_amount"]=="0"):
			if not (new_order["is_cancelled"]==False):
				errors.append("order state did not match")

		if not (new_order["price"]=="19633.00"):
			errors.append("price did not match")

		if not (new_order["original_amount"]=="100"):
			errors.append("original amount did not match")

		if  not(new_order["options"][0]=="indication-of-interest"):
			errors.append("option did not match")

		if not (new_order["is_hidden"]) == True:
			errors.append("is hidden did not match")


		assert not errors, "errors occured:\n{}".format("\n".join(errors))

#test  limit indication of interest sell order
	def test_new_order_limit_indication_of_interest_sell(self):
		#sleep for 1 second to get a different nonce
		time.sleep(1)


		payload_nonce = generate_nonce()

		payload = {
			"request": request,
			"nonce": payload_nonce,
			"symbol": symbol,
			"amount": "100",
			"price": "19600.00",
			"side": "sell",
			"type": "exchange limit",
			"options": ["indication-of-interest"],
			}

		signature,b64=generate_signature(payload,gemini_api_secret)

		request_headers=generate_request_header(signature,b64,gemini_api_key)

		response = requests.post(url,
						data=None,
						headers=request_headers)

		new_order = response.json()
		print(new_order)


		errors=[] #popupate with order data mismatch

		#check if order details are what we expect
		if len(new_order)<=3:
			if new_order["result"]=='error':
				errors.append("order rejected")
				errors.append(new_order["message"])
				assert not errors, "order rejected:\n{}".format("\n".join(errors))

		if not (new_order["side"] == "sell"):
			errors.append("side did not match")

		if not (new_order["symbol"]=="btcusd"):
			errors.append("symbol did not match")

		if not (new_order["type"]=="indication-of-interest limit"):
			errors.append("type did not match")

		if (new_order["executed_amount"]=="0"):
			if not (new_order["is_cancelled"]==False):
				errors.append("order state did not match")

		if not (new_order["price"]=="19600.00"):
			errors.append("price did not match")

		if not (new_order["original_amount"]=="100"):
			errors.append("original amount did not match")

		if  not(new_order["options"][0]=="indication-of-interest"):
			errors.append("option did not match")

		if not (new_order["is_hidden"]) == True:
			errors.append("is_hidden did not match")


		assert not errors, "errors occured:\n{}".format("\n".join(errors))


#test buy and sell orders to trade
	def test_new_orders_trade(self):
		#sleep for 1 second to get a different nonce
		time.sleep(1)

		payload_nonce = generate_nonce()


		payload = {
			"request": request,
			"nonce": payload_nonce,
			"symbol": symbol,
			"amount": amount,
			"price": "3633.00",
			"side": side,
			"type": order_type,
			#"options": ["maker-or-cancel"]
			}

		signature,b64=generate_signature(payload,gemini_api_secret)

		request_headers=generate_request_header(signature,b64,gemini_api_key)

		response = requests.post(url,
						data=None,
						headers=request_headers)

		new_order_buy = response.json()
		print(new_order_buy)



		#sleep for 1 second to get a different nonce
		time.sleep(1)

		payload_nonce = generate_nonce()


		payload = {
			"request": request,
			"nonce": payload_nonce,
			"symbol": symbol,
			"amount": amount,
			"price": "3633.00",
			"side": "sell",
			"type": order_type,
			#"options": ["maker-or-cancel"]
			}

		signature,b64=generate_signature(payload,gemini_api_secret)

		request_headers=generate_request_header(signature,b64,gemini_api_key)

		response = requests.post(url,
						data=None,
						headers=request_headers)

		new_order_sell = response.json()
		print(new_order_sell)
		errors=[] #popupate with order data mismatch

		#check if buy order details are what we expect
		if len(new_order_buy)<=3:
			if new_order_buy["result"]=='error':
				errors.append("order rejected")
				errors.append(new_order_buy["message"])
				assert not errors, "order rejected:\n{}".format("\n".join(errors))

		if not (new_order_buy["side"] == 'buy'):
			errors.append("buy side did not match")

		if not (new_order_buy["symbol"]=="btcusd"):
			errors.append(" buy symbol did not match")

		if not (new_order_buy["type"]=="exchange limit"):
			errors.append("buy type did not match")

		if not (new_order_buy["is_cancelled"]==False):
			errors.append("buy order state did not match")

		if not (new_order_buy["price"]=="3633.00"):
			errors.append("buy price did not match")

		if not (new_order_buy["original_amount"]=="1"):
			errors.append("buy original amount did not match")

		if not (new_order_buy["executed_amount"]=="1"):
			errors.append("buy executed amount did not match")


		#check if sell order details are what we expect
		if len(new_order_sell)<=3:
			if new_order_sell["result"]=='error':
				errors.append("order rejected")
				errors.append(new_order_sell["message"])
				assert not errors, "order rejected:\n{}".format("\n".join(errors))

		if not (new_order_sell["side"] == 'sell'):
			errors.append("sell side did not match")

		if not (new_order_sell["symbol"]=="btcusd"):
			errors.append("sell symbol did not match")

		if not (new_order_sell["type"]=="exchange limit"):
			errors.append("sell type did not match")

		if not (new_order_sell["is_cancelled"]==False):
			errors.append("sell order state did not match")

		if not (new_order_sell["price"]=="3633.00"):
			errors.append("sell price did not match")

		if not (new_order_sell["original_amount"]=="1"):
			errors.append("sell original amount did not match")

		if not (new_order_sell["executed_amount"]=="1"):
			errors.append("sell executed amount did not match")

		assert not errors, "errors occured:\n{}".format("\n".join(errors))


#test triggering stop limit sell order
	def test_new_order_stop_limit_trigger_sell(self):
		#sleep for 1 second to get a different nonce
		time.sleep(1)


		payload_nonce = generate_nonce()

		#create stop limit order
		payload = {
			"request": request,
			"nonce": payload_nonce,
			"symbol": symbol,
			"amount": amount,
			"price": "15000.00",
			"side": "sell",
			"type": "exchange stop limit",
			"stop_price":stop_price,
			#"options": ["maker-or-cancel"]
			}

		signature,b64=generate_signature(payload,gemini_api_secret)

		request_headers=generate_request_header(signature,b64,gemini_api_key)

		response = requests.post(url,
						data=None,
						headers=request_headers)

		new_order = response.json()
		print(new_order)

		#create  limit buy order
		#sleep for 1 second to get a different nonce
		time.sleep(1)

		payload_nonce_b = generate_nonce()


		payload_b = {
			"request": request,
			"nonce": payload_nonce_b,
			"symbol": symbol,
			"amount": amount,
			"price": "17000.00",
			"side": side,
			"type": "exchange limit",
			#"stop_price":stop_price,
			#"options": ["maker-or-cancel"]
			}

		signature_b,b64_b=generate_signature(payload_b,gemini_api_secret)

		request_headers_b=generate_request_header(signature_b,b64_b,gemini_api_key)

		response_b = requests.post(url,
						data=None,
						headers=request_headers_b)

		new_order_b = response_b.json()
		print(new_order_b)

		##creare opposite order to trade

		#sleep for 1 second to get a different nonce
		time.sleep(1)

		payload_nonce_s = generate_nonce()

		#create  limit sell order
		payload_s = {
			"request": request,
			"nonce": payload_nonce_s,
			"symbol": symbol,
			"amount": amount,
			"price": "17000.00",
			"side": "sell",
			"type": "exchange limit",
			#"stop_price":stop_price,
			#"options": ["maker-or-cancel"]
			}

		signature_s,b64_s=generate_signature(payload_s,gemini_api_secret)

		request_headers_s=generate_request_header(signature_s,b64_s,gemini_api_key)

		response_s = requests.post(url,
						data=None,
						headers=request_headers_s)

		new_order_s = response_s.json()
		print(new_order_s)

		##start verification of order responses
		errors=[] #popupate with order data mismatch

		#check if order details are what we expect
		if len(new_order)<=3:
			if new_order["result"]=='error':
				errors.append("order rejected")
				errors.append(new_order["message"])
				assert not errors, "order rejected:\n{}".format("\n".join(errors))

		if not (new_order["side"] == 'sell'):
			errors.append("side did not match")

		if not (new_order["symbol"]=="btcusd"):
			errors.append("symbol did not match")

		if not (new_order["type"]=="stop-limit"):
			errors.append("type did not match")

		if not (new_order["is_cancelled"]==False):
			errors.append("order state did not match")

		if not (new_order["price"]=="15000.00"):
			errors.append("price did not match")

		if not (new_order["original_amount"]=="1"):
			errors.append("original amount did not match")

		if not (new_order["stop_price"]=="17000.00"):
			errors.append("stop_price did not match")

		assert not errors, "errors occured:\n{}".format("\n".join(errors))


#test triggering stop limit buy order
	def test_new_order_stop_limit_trigger_buy(self):
		#sleep for 1 second to get a different nonce
		time.sleep(1)
		payload_nonce = generate_nonce()

		payload = {
			"request": request,
			"nonce": payload_nonce,
			"symbol": symbol,
			"amount": amount,
			"price": "19150.00",
			"side": side,
			"type": "exchange stop limit",
			"stop_price":"19000.00",
			#"options": ["maker-or-cancel"]
			}

		signature,b64=generate_signature(payload,gemini_api_secret)

		request_headers=generate_request_header(signature,b64,gemini_api_key)

		response = requests.post(url,
						data=None,
						headers=request_headers)

		new_order = response.json()
		print(new_order)

		##create buy order
				#sleep for 1 second to get a different nonce
		time.sleep(1)
		payload_nonce_b = generate_nonce()

		payload_b = {
			"request": request,
			"nonce": payload_nonce_b,
			"symbol": symbol,
			"amount": amount,
			"price": "19000.00",
			"side": side,
			"type": "exchange limit",
			#"stop_price":"19000.00",
			#"options": ["maker-or-cancel"]
			}

		signature_b,b64_b=generate_signature(payload_b,gemini_api_secret)

		request_headers_b=generate_request_header(signature_b,b64_b,gemini_api_key)

		response_b = requests.post(url,
						data=None,
						headers=request_headers_b)

		new_order_b = response_b.json()
		print(new_order_b)

		##create opposite order to trade
				#sleep for 1 second to get a different nonce
		time.sleep(1)
		payload_nonce_s = generate_nonce()

		payload_s = {
			"request": request,
			"nonce": payload_nonce_s,
			"symbol": symbol,
			"amount": amount,
			"price": "19000.00",
			"side": "sell",
			"type": "exchange limit",
			#"stop_price":"19000.00",
			#"options": ["maker-or-cancel"]
			}

		signature_s,b64_s=generate_signature(payload_s,gemini_api_secret)

		request_headers_s=generate_request_header(signature_s,b64_s,gemini_api_key)

		response_s = requests.post(url,
						data=None,
						headers=request_headers_s)

		new_order_s = response_s.json()
		new_order = response.json()
		print(new_order_s)
		print("trade----")
		print(new_order)


		errors=[] #popupate with order data mismatch

		#check if order details are what we expect
		if len(new_order)<=3:
			if new_order["result"]=='error':
				errors.append("order rejected")
				errors.append(new_order["message"])
				assert not errors, "order rejected:\n{}".format("\n".join(errors))

		if not (new_order["side"] == "buy"):
			errors.append("side did not match")

		if not (new_order["symbol"]=="btcusd"):
			errors.append("symbol did not match")

		if not (new_order["type"]=="stop-limit"):
			errors.append("type is not limit")

		if not (new_order["is_cancelled"]==False):
			errors.append("order stae did not match")

		if not (new_order["price"]=="19500.00"):
			errors.append("price did not match")

		if not (new_order["original_amount"]=="1"):
			errors.append("original amount did not match")

		if not (new_order["stop_price"]=="19000.00"):
			errors.append("stop_price did not match")

		assert not errors, "errors occured:\n{}".format("\n".join(errors))


#test optional tag client order id new order
	def test_new_order_client_order_id_buy(self):

		time.sleep(1)

		payload_nonce = generate_nonce()
		time1 = str(datetime.datetime.now())
		client_order_id="lakulish"+time1

		payload = {
			"request": request,
			"nonce": payload_nonce,
			"client_order_id": client_order_id,
			"symbol": symbol,
			"amount": amount,
			"price": "3633.00",
			"side": side,
			"type": order_type,
			"options": ["maker-or-cancel"]
			}

		signature,b64=generate_signature(payload,gemini_api_secret)

		request_headers=generate_request_header(signature,b64,gemini_api_key)

		response = requests.post(url,
						data=None,
						headers=request_headers)

		new_order = response.json()
		print(new_order)

		errors=[] #popupate with order data mismatch

		#check if order details are what we expect
		if len(new_order)<=3:
			if new_order["result"]=='error':
				errors.append("order rejected")
				errors.append(new_order["message"])
				assert not errors, "order rejected:\n{}".format("\n".join(errors))

		if not (new_order["side"] == 'buy'):
			errors.append("side did not match")

		if not (new_order["symbol"]=="btcusd"):
			errors.append("symbol did not match")

		if not (new_order["type"]=="exchange limit"):
			errors.append("type did not match")

		if not (new_order["is_cancelled"]==False):
			errors.append("order state did not match")

		if not (new_order["price"]=="3633.00"):
			errors.append("price did not match")

		if not (new_order["original_amount"]=="1"):
			errors.append("original amount did not match")

		if not (new_order["client_order_id"]==client_order_id):
			errors.append("client ord id did not match")


		assert not errors, "errors occured:\n{}".format("\n".join(errors))
