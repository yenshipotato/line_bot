#from _future_ import print_function
#from apiclient.discovery import build
#from httplib2 import Http
#from oauth2client import file, client, tools

#import time
#import re
#import datetime
import os
import random
import plurk
import plurkNM
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
    InvalidSignatureError, LineBotApiError
)
from linebot.models import *
import dev
import slut


#################################################################################
app = Flask(__name__)
# Channel Access Token
line_bot_api = LineBotApi(
    "N/v0C7lGHaN90PeH9kzLvByRWliKRtaP2OxddqAYA0znrm+C5urMequ/c3HxCYyroLzMEqUNmBA+xg0gE6pFN7wUjqRa66FYYqW/sLjrQGZVjSaawnYbTrXDnNHm+GlWrlTikHIENzl97e+dEvfecAdB04t89/1O/w1cDnyilFU=")
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
    # 15754506059298
    print(event.source.user_id)
    text = event.message.text

    if (text == "奕丞" or text == '冠毅'):
        reply_text = "愛愛愛愛愛愛愛愛愛愛愛愛愛愛~~~~~<3"

    elif(text == "藍猴猴" or text == "鼓鼓掌"):
        reply_text = "-1"
    elif(text == "紫薇" or text == "子緯"):
        reply_text = "-3"
    elif(text == "御倫" or text == "鞋子"):
        reply_text = "-4"
    elif(text == "紅豆" or text == "手拋紅豆"):
        reply_text = "-5"
    elif(text == "崇發" or text == "重發"):
        reply_text = "-6"
    elif(text == "爛台大" or text == "爛臺大"):
        reply_text = "-7"
    elif(text == "什麼意思"):
        reply_text = "-69"
    elif(text == "yhboys"):
        reply_text = "同性戀姦淫"

    elif(text == "塵抑"):
        reply_text = "叫三小 老娘忙著做愛你知道嗎"
    elif(text == "晨瑋"):
        reply_text = "臭婊子"
    elif(text == "奶妹"):
        reply_text = "臭大奶婊子"
    elif(text == "文賓"):
        reply_text = "只剩顏值的智障馬鈴薯"
    elif(text == "御倫"):
        reply_text = "誰?"
    elif(text == "抽"):
        reply_text = "抽你媽B啦幹 當老娘情色機器人膩"
    elif("slut_ " in text):

        reply_text = slut.strtslut(text)
    elif("發噗 " == text[0:3]):
        if(event.source.user_id == 'Uf98201bfc7c87d4641666f0565a6094f'):
            print(plurk.plurkAdd(text[3::]))
            reply_text = "發囉 懶蟲"
        elif(event.source.user_id == "Uc0deeee84c1c50ea2c87db028215e87b"):
            print(plurkNM.plurkAdd(text[3::]))
            reply_text = "發囉 懶奶"
        else:
            reply_text = "沒有你的噗浪權限喔 哈哈 笑死"
    else:
        if len(text) > 30:
            reply_text = dev.pros(text)  # 如果非以上的選項，就call respond()
        else:
            pass
#################################################################################################################################################
    if(reply_text == "-1"):
        message = StickerSendMessage(package_id="11539", sticker_id="52114139")
    elif(reply_text == "-3"):
        message = ImageSendMessage(original_content_url="https://cdn.discordapp.com/attachments/758157661740073031/925615766076805130/78268391_826250951130198_8204874367138529280_n.jpg",
                                   preview_image_url="https://cdn.discordapp.com/attachments/758157661740073031/925615637550739476/78268391_826250951130198_8204874367138529280_n_2.jpg")
    elif(reply_text == "-4"):
        message = ImageSendMessage(original_content_url="https://ppt.cc/fDtsNx@.jpg",
                                   preview_image_url="https://ppt.cc/fDtsNx@.jpg")
    elif(reply_text == "-5"):
        message = AudioSendMessage(original_content_url="https://doc-0o-ao-docs.googleusercontent.com/docs/securesc/oli48j0aff87qgemnh96jj8kf94r6pv1/7q03sfo7hvoil76ehl407gerhbockn5j/1647434700000/08900282080025306965/00208019747079213226/1UQBnJYkezBaEAgSmzYJsIkeSYgdPQ0Xo?e=download&ax=ACxEAsayBMd__0miST-P8hL10zVG8Ul1JRBGUMDOu3sr-RRUy2z_vZTTRUfslhTdOgAyy2IzMpku4adhDKOHUq18EML1rOU2zHrJCHecVuwddiGzuU7YaMi_YKn5CqGNUkWomnS84G2YVgMraTi8Gx3AFFWEDPAkWP7J5OHKj4QTGymb_adAI4RRYDj_TXVAlzhvo5uG2dipuyi_rCf75pCFpceh6m5h71e1VZD3UhFDuJWfIi618RYg1gtuhR2IUTs1_FWBjkwwKJbgRJnniPUOX_5ncAaBkbVoqbirHR31o2_oLgM6O3mgFQknPJJ-BkDtmT3PUMtHIy1dw0QS-QhcBJAODRQoX3CVTEHHqyHb5dUGp37eov3K-Ch8V7gJ6BZrqpx09rfC53_wHEqc72i7xIvgWAQt65vA4hP3JRJZhxrkVKZ9iuKMCZ3ozWkTLZjNSBhnTQfAr0QB63WUMnSeTC9h7iIYujbJKtt08YV9r9iG_qnS5b-27Tl37rNhv9Utep0_wLOWs3ujBt2Of5G7oe9DAO8M5Ym7lzH3Wm176pBLXsNCfrzNjWfK46RgVawGcJqdJe3N1LL8MRakbYbC6VUNo2gNiRyezFhu0F3kbs2tH-WjGgtAs9tNkwErYRMMYVSzX8JgyDEYrl32cDxBEiF4RGMw9vurZ078ZhA&authuser=0", duration=220000)
    elif(reply_text == "-6"):
        message = VideoSendMessage(original_content_url="https://storage.risu.io/EZWiLG6a4kTPjg1KBr7pHj5r?GoogleAccessId=storage%40risu-248412.iam.gserviceaccount.com&Expires=1647445592&Signature=Py9wDh9ZRPVzF1iiyUpQt0gdNK2%2BDgxRDq%2BaMV8wzXvyYW6YPOO179AVd6%2Fl0xjmTsH9JhtodBQZQH%2BQKSHCQrg8EJYLLKSXz5luouHH4xE%2BVQgCneVzfwgp80ZjzNw%2FJevY8PSalr4EslEjHPdFCz4uTGJv5mVtdmaUr1k4SFWNCy13eTz%2BDa4qthYqdMdYwilBAQOHqvZrJ5GRw3iKL2zsZep0xPoTXIMC5OutDgdpE9p4Rsoc7u5f9URaMf6mhxSeJ%2FEBD5DMLjTsHzCU2FArQ9KNZF%2BXOfczQh4m9NFJ6NCp%2BCL8b43wO17x04rjIkiORH%2FrhZVv6uTN02nIdA%3D%3D&response-content-disposition=attachment%3B+filename%3D%22Screen_Recording_20220315-223944_YouTube.mp4%22%3B+filename%2A%3DUTF-8%27%27Screen_Recording_20220315-223944_YouTube.mp4",
                                   preview_image_url="https://ppt.cc/fFzacx@.jpg")
    elif(reply_text == "-7"):
        message = VideoSendMessage(original_content_url="https://cdn.discordapp.com/attachments/676035431103594519/1028323514228420629/Screen_Recording_20221008_013422_Gallery.mp4",
                                   preview_image_url="https://cdn.discordapp.com/attachments/676035431103594519/1028326233731248148/uIXX4Ok.jpg")
    elif(reply_text == "-69"):
        message = ImageSendMessage(original_content_url="https://ppt.cc/fRybxx@.jpg",
                                   preview_image_url="https://ppt.cc/fRybxx@.jpg")
    elif(reply_text != "-2"):
        message = TextSendMessage(reply_text)
##################################################################################################################################################

    line_bot_api.reply_message(event.reply_token, message)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
