from flask import Flask, request, jsonify, render_template, redirect, url_for, session, flash, make_response
from datetime import datetime, timedelta
import sqlite3
import requests
import json
from time import sleep
from take_bybit import *
from take_kucoin import *
from flask_cors import CORS, cross_origin



app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/login', methods=['POST'])
def login() -> json:

    result = {}
    data = request.get_json()
    login = str(data['params']['login']) 
    password = str(data['params']['password']) 
    print(login,password)

    if str(login) == 'admin@crypto' and str(password) == 'admin_crypto481':
        result['status'] = '200'
        result['message'] = 'Успешно'
        return jsonify(result)
    
    else:
        result['status'] = '400'
        result['message'] = 'Ошибка авторизации'
        return jsonify(result)

    
@app.route('/admin', methods=['POST'])
def admin()-> json:
    #настройки по умолчанию: покупка, usdt за  рубли, без заполнения количества, все методы оплаты
    data = request.get_json()
    #Выбор из какой монеты в какую валюту
    tokenId = str(data['params']['tokenId'])#None #должно предоваться 'USDT' если ничего не выбранно 
    currencyId = str(data['params']['currencyId']) #должно предоваться "RUB" если ничего не выбранно 

    #Получение доступных методов оплаты (банки):
    only_pays = take_payment_only(tokenId, currencyId) # это отсеивает те банки, которые подходят
    name_banks = take_metods(only_pays) # это записывает id которое потребуется при подборе price_list

    amount = str(data['params']['amount'])#'' #'20000'
    paymant = data['params']['paymant']#[] #тут ['7']
    side = str(data['params']['side'])#'0' #продажа 1-покупка


    price_list = take_byb(tokenId, amount, currencyId, paymant, side)

    print(price_list)
    result = {}
    result['price_byb'] = price_list
    result['only_code_bank_bybit'] = name_banks 

    coin = currencyId 
    symbol = tokenId
    type_c = side

    code_bank = ''#тут нужно будет поправить так как по другому у банков id 

    name_banks_kuc = take_code_bank(coin)
    price_list_kuc = parce_cucoin(symbol, coin, type_c, code_bank)

    result['price_kuc'] = price_list_kuc
    result['only_code_bank_kuc'] = name_banks_kuc

    return jsonify(result)

@app.route('/spot', methods=['POST'])
def spot()-> json:
    result = {}
    # data = request.get_json()
    spot_bybit_price = take_spot_bybit()
    spot_kukoin_price = kukoin_spot()
    result['bybit'] =  spot_bybit_price
    result['kucoin'] = spot_kukoin_price
    return jsonify(result)



if __name__ == '__main__':
   app.run(host="0.0.0.0", debug=True, port=3000)
