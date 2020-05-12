# -*- encoding=utf8 -*-
__author__ = "Morrow"
#python 2.7
import time
import hmac
import hashlib
import base64
import urllib

timestamp = round(time.time() * 1000)
secret = 'SEC1ac91279ff67130f7929abfb142bf29df9bd9b057efda56661543cf583e6f180'
secret_enc = bytes(secret).encode('utf-8')
string_to_sign = '{}\n{}'.format(timestamp, secret)
string_to_sign_enc = bytes(string_to_sign).encode("UTF-8")
hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
sign = urllib.quote_plus(base64.b64encode(hmac_code))
print(timestamp)
print(sign)






