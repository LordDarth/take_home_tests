import json
import base64
import hmac
import hashlib
import datetime, time

def generate_signature(payload,gemini_api_secret):

		encoded_payload = json.dumps(payload).encode()
		b64 = base64.b64encode(encoded_payload)
		signature = hmac.new(gemini_api_secret, b64, hashlib.sha384).hexdigest()

		return signature,b64


def generate_request_header(signature,b64,gemini_api_key):

		request_headers = { 'Content-Type': "text/plain",
				'Content-Length': "0",
				'X-GEMINI-APIKEY': gemini_api_key,
				'X-GEMINI-PAYLOAD': b64,
				'X-GEMINI-SIGNATURE': signature,
				'Cache-Control': "no-cache" }

		return request_headers


def generate_nonce():
		t = datetime.datetime.now()
		payload_nonce =  str(int(time.mktime(t.timetuple())*1000))

		return payload_nonce

