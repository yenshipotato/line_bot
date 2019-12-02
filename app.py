#from _future_ import print_function
#from apiclient.discovery import build
#from httplib2 import Http
#from oauth2client import file, client, tools

#import time
#import re
#import datetime
import random
#import codecs
#import sys
#import json

from flask import Flask, request, abort
from urllib.request import urlopen
#from oauth2client.service_account import ServiceAccountCredentials

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError,LineBotApiError
)
from linebot.models import *


#################################################################################
app = Flask(__name__)
# Channel Access Token
line_bot_api = LineBotApi("N/v0C7lGHaN90PeH9kzLvByRWliKRtaP2OxddqAYA0znrm+C5urMequ/c3HxCYyroLzMEqUNmBA+xg0gE6pFN7wUjqRa66FYYqW/sLjrQGZVjSaawnYbTrXDnNHm+GlWrlTikHIENzl97e+dEvfecAdB04t89/1O/w1cDnyilFU=")
# Channel Secret
handler = WebhookHandler('9dd29e43016d88723bb8bcffc6ae60e4')
#################################################################################


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():

    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print(event)
    text=event.message.text

    if (text=="奕丞" or text=='冠毅'):
        reply_text = "愛愛愛愛愛愛愛愛愛愛愛愛愛愛~~~~~<3"
        #Your user ID

    elif(text=="藍猴猴"):
        reply_text = "-1"
    elif(text=="紫薇" or text=="子緯"):
        reply_text = "-3"
    elif(text=="yhboys"):
        reply_text = "同性戀姦淫"


    elif(text=="塵抑"):
        reply_text = "叫三小 老娘忙著做愛你知道嗎"
    elif(text=="晨瑋"):
        reply_text = "臭婊子"
    elif(text=="奶妹"):
        reply_text = "臭大奶婊子"
    elif(text=="文賓"):
        reply_text = "只剩顏值的智障馬鈴薯"
    elif(text=="御倫"):
        reply_text = "誰?"

    
    else:
       reply_text = respond()       #如果非以上的選項，就respond


    if(reply_text=="-1"):
        message = StickerSendMessage(package_id="11539",sticker_id="52114139")
    elif(reply_text=="-3"):
        message = ImageSendMessage(original_content_url="https://i.imgur.com/5UOsUm7.jpg",preview_image_url="https://i.imgur.com/FjYPGXu.jpg")
    elif(reply_text!="-2"):
        message = TextSendMessage(reply_text)

    line_bot_api.reply_message(event.reply_token, message)

def respond():
    randnum=random.randint(0,65535)
    if(randnum%30==0):
        return "閉嘴 婊子"
    elif(randnum%30==1):
        return "一齊做愛 生活無礙"
    elif(randnum%30==2 or (randnum%8>=4 and randnum<=7)):
        return "你們都是tucking birch"
    elif(randnum%30==3):
        return "不會餓肚子  愛愛共產"
    else:
        return "-2"
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)