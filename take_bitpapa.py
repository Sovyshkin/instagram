import requests
import json


def parce_bitpapa(side, amount, currency_cod, fiat, pay_method): 

    sort = 'price'
    if str(side) == '0':
        side = 'sell'
        sort = 'price'

    if str(side) == '1':
        side = 'buy'
        sort = '-price'

    params = {
        'type': side,
        'page': '1',
        'sort': sort,#'-price',
        'currency_code': currency_cod,#'RUB',
        'previous_currency_code': currency_cod,#'RUB',
        'crypto_currency_code': fiat,#'BTC',
        'with_correct_limits': 'false',
        'limit': '10',
        'pages': '15',
    }
    #side, amount, currency_cod, fiat, pay_method
    #'sell', '10000', 'USD', 'BTC', 'SPECIFIC_BANK'   
    if amount != '':
        params['amount'] = str(amount)
    if pay_method != '':
        params['payment_method_code'] = str(pay_method)

    r = requests.get('https://bitpapa.com/api/v1/pro/search', params=params)
    json_string = r.text
    data = r.json()
    #print(json_string)
    data_papa_p2p = []
    for i in data['ads']:
        #print(i['user']['user_name'], i['price'], 'Limit: ', i['limit_min'], '-' ,i['limit_max'])
        a = {'user': i['user']['user_name'], 'price': i['price'], 'min': i['limit_min'], 'max': i['limit_max']}
        data_papa_p2p.append(a)

    return data_papa_p2p


def bitpapa_spot():
    r = requests.get('https://bitpapa.com/api/v1/exchange_rates/all')

    data = r.json()
    spot_papa = []
    for i in data['rates']:
        print(i, data['rates'][i])
        symbol = i.replace("_", "")
        a = {'symbol': symbol, 'price': str(data['rates'][i])}
        spot_papa.append(a)
        
    return spot_papa

#def only_bank_papa():


# side = '0'
# amount = ''
# currency_cod = 'RUB'
# fiat = 'USDT'
# pay_method = ''
##'sell', '10000', 'USD', 'BTC', 'SPECIFIC_BANK'
# d = parce_bitpapa(side, amount, currency_cod, fiat, pay_method)
#print(d)


# info = bitpapa_spot()
# #print(info)