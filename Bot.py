from __future__ import unicode_literals
import os
import random
import requests
import re
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import configparser
import ConnectPostgreSQL as sql

app = Flask(__name__)

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')
postgres_manager = sql.PostgresBaseManager()
postgres_manager.runServerPostgresDb()

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))

# 接收 LINE 的資訊


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


def MakeIntroduction():
    msg = "我是加碼券速速查小幫手，可以幫您查詢加碼券相關資訊：\n\n"
    msg += "您可以輸入以下關鍵字：\n"
    msg += "⭐開獎號碼：查看加碼券開獎號碼\n"
    msg += "⭐國旅券(1000元)\n⭐動滋券(500元)\n⭐i原券(1000元)\n⭐藝Fun券(600元)\n⭐農遊券(888元)\n⭐客庄券(500元)\n⭐地方創生券(500元\n"
    msg += "\t請在後方輸入縣市即可查看可使用店家資訊\n\tex：國旅券 台北市\n"
    msg += "⭐天氣：\n    查看當日氣溫🌦\n\n"
    msg += "⭐猜拳：\n    來和小幫手玩猜拳吧✌️👊✋\n"
    return msg


def Select_Number(choose):
    number = postgres_manager.SELECT_number(choose)
    print(number)
    msg = ""
    for i in range(len(number)):
        num = re.sub("\(|\,|\)", "", str(number[i]))
        print(num)
        msg += str(num) + "\t,"
    return msg

def Set_city(city_name):
    city_name = city_name.replace('台', '臺')
    if city_name == "基隆市":
        city = "keelung"
    elif city_name == "臺北市":
        city = "taipei"
    elif city_name == "新北市":
        city = "new_taipei"
    elif city_name == "桃園市":
        city = "taoyuang"
    elif city_name == "新竹市":
        city = "hsinchu"
    elif city_name == "新竹縣":
        city = "hsinchu_county"
    elif city_name == "苗栗縣":
        city = "miaoli"
    elif city_name == "臺中市":
        city = "taichung"
    elif city_name == "彰化縣":
         city = "changhua"
    elif city_name == "南投縣":
        city = "nantou"
    elif city_name == "雲林縣":
        city = "yunlin"
    elif city_name == "嘉義市":
        city = "chiayi"
    elif city_name == "嘉義縣":
        city = "chiayi_county"
    elif city_name == "臺南市":
        city = "tainan"
    elif city_name == "高雄市":
        city = "kaohsiung"
    elif city_name == "屏東縣":
        city = "pingtung"
    elif city_name == "臺東縣":
        city = "taitung"
    elif city_name == "花蓮縣":
        city = "hualien"
    elif city_name == "宜蘭縣":
        city = "yilan"
    elif city_name == "澎湖縣":
        city = "penghu"
    elif city_name == "金門縣":
        city = "kinmen"
    elif city_name == "連江縣":
        city = "lianjiang"
    else:
        city = "None"
    return city

def Select_data(choose, city):
    data = postgres_manager.SELECT_data(choose, city)
    print(data)
    msg = ""
    for i in range(len(data)):
        data = str(data[i])
        print(data)
        msg += str(data) + "\n,"
    return msg

# 天氣
def MakeRailFall(station):
    result = requests.get(
        "https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0002-001?Authorization=CWB-E5F5EFC0-30D2-43E6-B9C5-DDC64B24FA74")
    msg = "\n🌧 降雨報告 - " + station + "\n\n"

    if(result.status_code != 200):
        return "雨量資料讀取失敗"
    else:
        railFallData = result.json()
        for item in railFallData["records"]["location"]:
            if station in item["locationName"]:
                msg += "目前雨量：" + \
                    item["weatherElement"][7]["elementValue"] + "mm\n"
                if item["weatherElement"][3]["elementValue"] == "-998.00":
                    msg += "三小時雨量：0.00mm\n"
                else:
                    msg += "三小時雨量：" + \
                        item["weatherElement"][3]["elementValue"] + "mm\n"
                msg += "日雨量：" + \
                    item["weatherElement"][6]["elementValue"] + "mm\n"
                return msg
        return "沒有這個測站啦"


def GetWeather(station):
    token = 'CWB-E5F5EFC0-30D2-43E6-B9C5-DDC64B24FA74'
    end_point = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0001-001?Authorization=" + token

    data = requests.get(end_point).json()
    data = data["records"]["location"]

    target_station = "not found"
    for item in data:
        if item["locationName"] == str(station):
            target_station = item
    return target_station


def MakeWeather(station):
    WeatherData = GetWeather(station)
    if WeatherData == "not found":
        return False
    WeatherData = WeatherData["weatherElement"]
    msg = "⛅ 天氣報告 - " + station
    msg += "\n\n🌡🌡🌡 氣溫 = " + WeatherData[3]["elementValue"] + "℃\n"
    msg += "💧💧💧 濕度 = " + \
        str(float(WeatherData[4]["elementValue"]) * 100) + "% RH\n"

    msg += MakeRailFall(station)


def MakePaperScissorsStone(text):
    # 石頭：0, 布：1, 剪刀：2
    if text == "石頭👊！":
        player = 0
    elif text == "布✋！":
        player = 1
    else:
        player = 2

    opponent = random.randint(0, 2)

    # 電腦：石頭, 玩家：布
    if opponent == 0 and player == 1:
        msg = '我出👊，你出✋！\n你贏了.. ｡ﾟヽ(ﾟ´Д`)ﾉﾟ｡'
    # 電腦：石頭, 玩家：剪刀
    elif opponent == 0 and player == 2:
        msg = '我出👊，你出✌️！\n我贏啦(●ˊωˋ●)ゞ'
    # 電腦：布, 玩家：石頭
    elif opponent == 1 and player == 0:
        msg = '我出✋，你出👊！\n我贏啦(●ˊωˋ●)ゞ'
    # 電腦：布, 玩家：剪刀
    elif opponent == 1 and player == 2:
        msg = '我出✋，你出✌️！\n你贏了.. ｡ﾟヽ(ﾟ´Д`)ﾉﾟ｡'
    # 電腦：剪刀, 玩家：石頭
    elif opponent == 2 and player == 0:
        msg = '我出✌️，你出👊！\n你贏了.. ｡ﾟヽ(ﾟ´Д`)ﾉﾟ｡'
    # 電腦：剪刀, 玩家：布
    elif opponent == 2 and player == 1:
        msg = '我出✌️，你出✋！\n我贏啦(●ˊωˋ●)ゞ'
    else:
        if opponent == 0:
            msg = '我們都出👊！'
        elif opponent == 1:
            msg = '我們都出✋！'
        else:
            msg = '我們都出✌️！'
        msg += '\n這次平手啦～d(`･∀･)b'
    return msg


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    cmd = event.message.text.split(" ")
    if cmd[0] == "介紹":
        IntroductionMsg = MakeIntroduction()
        SendMsg = [TextSendMessage(text=IntroductionMsg),
                   StickerSendMessage(package_id=1, sticker_id=2)]
        line_bot_api.reply_message(event.reply_token, SendMsg)

    elif cmd[0] == "開獎號碼":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text="請選擇：\n國旅券中籤號碼\n動滋券中籤號碼\ni原券中籤號碼\n藝Fun券中籤號碼\n農遊券中籤號碼\n客庄券中籤號碼\n地方創生券中籤號碼",
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="國旅券", text="國旅券中籤號碼")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="動滋券", text="動滋券中籤號碼")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="i原券", text="i原券中籤號碼")
                        ),
                        QuickReplyButton(
                            action=MessageAction(
                                label="藝Fun券", text="藝Fun券中籤號碼")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="農遊券", text="農遊券中籤號碼")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="客庄券", text="客庄券中籤號碼")
                        ),
                        QuickReplyButton(
                            action=MessageAction(
                                label="地方創生券", text="地方創生券中籤號碼")
                        )
                    ])))

    elif cmd[0] == "國旅券中籤號碼":
        Travel_Number_Msg = Select_Number("travel")
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="國旅券中籤號碼:\n"+Travel_Number_Msg))

    elif cmd[0] == "動滋券中籤號碼":
        Sports_Number_Msg = Select_Number("sports")
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="動滋券中籤號碼:\n"+Sports_Number_Msg))

    elif cmd[0] == "i原券中籤號碼":
        I_original_Number_Msg = Select_Number("i_original")
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="i原券中籤號碼:\n"+I_original_Number_Msg))

    elif cmd[0] == "藝Fun券中籤號碼":
        Efun_digit_Number_Msg = Select_Number("efun_digit")
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="藝Fun券數位中籤號碼:\n"+Efun_digit_Number_Msg))
        Efun_entity_Number_Msg = Select_Number("efun_entity")
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="藝Fun券實體中籤號碼:\n"+Efun_entity_Number_Msg))

    elif cmd[0] == "農遊券中籤號碼":
        Farm_Number_Msg = Select_Number("farm")
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="農遊券中籤號碼:\n"+Farm_Number_Msg))

    elif cmd[0] == "客庄券中籤號碼":
        Hakka_Number_Msg = Select_Number("hakka")
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="客庄券中籤號碼:\n"+Hakka_Number_Msg))

    elif cmd[0] == "地方創生券中籤號碼":
        Creation_Number_Msg = Select_Number("creation")
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="地方創生券中籤號碼:\n"+Creation_Number_Msg))

    elif cmd[0] == "加碼券":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text="請選擇:\n國旅券\n動滋券\ni原券\n藝Fun券\n農遊券\n客庄券\n地方創生券",
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="國旅券", text="國旅券")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="動滋券", text="動滋券")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="i原券", text="i原券")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="藝Fun券", text="藝Fun券")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="農遊券", text="農遊券")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="客庄券", text="客庄券")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="地方創生券", text="地方創生券")
                        )
                    ])))
    elif cmd[0] == "國旅券":
        city_name = cmd[1]
        city = Set_city(city_name)
        if city =="None":
            Travel_Number_Msg = "輸入錯誤，請重新輸入!!!"
        else:
            Travel_Number_Msg = Select_data("travel", city)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=Travel_Number_Msg))

    elif cmd[0] == "動滋券":
        city_name = cmd[1]
        city = Set_city(city_name)
        if city =="None":
            Sports_Number_Msg = "輸入錯誤，請重新輸入!!!"
        elif city =="lianjiang":
            Sports_Number_Msg = "查無資料 -.-"
        else:
            Sports_Number_Msg = Select_data("sports", city)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=Sports_Number_Msg))

    elif cmd[0] == "i原券":
        city_name = cmd[1]
        city = Set_city(city_name)
        if city =="None":
            I_original_Number_Msg = "輸入錯誤，請重新輸入!!!"
        else:
            I_original_Number_Msg = Select_data("i_original", city)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=I_original_Number_Msg))

    elif cmd[0] == "藝Fun券":
        city_name = cmd[1]
        city = Set_city(city_name)
        if city =="None":
            Efun_Number_Msg = "輸入錯誤，請重新輸入!!!"
        else:
            Efun_Number_Msg = Select_data("efun", city)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=Efun_Number_Msg))

    elif cmd[0] == "農遊券":
        city_name = cmd[1]
        city = Set_city(city_name)
        if city =="None":
            Farm_Number_Msg = "輸入錯誤，請重新輸入!!!"
        else:
            Farm_Number_Msg = Select_data("farm", city)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=Farm_Number_Msg))

    elif cmd[0] == "客庄券":
        city_name = cmd[1]
        city = Set_city(city_name)
        if city =="None":
            Hakka_Number_Msg = "輸入錯誤，請重新輸入!!!"
        else:
            Hakka_Number_Msg = Select_data("hakka", city)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=Hakka_Number_Msg))

    elif cmd[0] == "地方創生券":
        city_name = cmd[1]
        city = Set_city(city_name)
        if city =="None":
            Creation_Number_Msg = "輸入錯誤，請重新輸入!!!"
        else:
            Creation_Number_Msg = Select_data("creation", city)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=Creation_Number_Msg))

    elif cmd[0] == "天氣":
        city = cmd[1]
        city = city.replace('台', '臺')
        WeatherMsg = MakeWeather(city)
        if not WeatherMsg:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(
                text="查詢格式為：天氣 氣象站\n查看氣象站：https://e-service.cwb.gov.tw/wdps/obs/state.htm"))
        else:
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text=WeatherMsg))

    elif cmd[0] == "猜拳":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text='剪刀石頭布！',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="石頭", text="石頭👊！"),
                            image_url='https://eswarupkumar.github.io/Stone-Paper-Scissor/rock.png'
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="布", text="布✋！"),
                            image_url='https://eswarupkumar.github.io/Stone-Paper-Scissor/paper.png'
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="剪刀", text="剪刀✌️！"),
                            image_url='https://eswarupkumar.github.io/Stone-Paper-Scissor/scissors.png'
                        )
                    ])))

    elif cmd[0] == "石頭👊！" or cmd[0] == "布✋！" or cmd[0] == "剪刀✌️！":
        SendMsg = MakePaperScissorsStone(cmd[0])+"\n\n再來一場嗎(*ˇωˇ*人)"
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text=SendMsg,
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="石頭", text="石頭👊！"),
                            image_url='https://eswarupkumar.github.io/Stone-Paper-Scissor/rock.png'
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="布", text="布✋！"),
                            image_url='https://eswarupkumar.github.io/Stone-Paper-Scissor/paper.png'
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="剪刀", text="剪刀✌️！"),
                            image_url='https://eswarupkumar.github.io/Stone-Paper-Scissor/scissors.png'
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="不玩了", text="不玩了"),
                            image_url='https://image.pngaaa.com/302/49302-middle.png'
                        )
                    ])))

    elif cmd[0] == "不玩了":
        ByeByeMsg = "好吧( ˘•ω•˘ ) 下次見！"
        SendMsg = [TextSendMessage(text=ByeByeMsg),
                   StickerSendMessage(package_id=11537, sticker_id=52002771)]
        line_bot_api.reply_message(event.reply_token, SendMsg)

    else:
        else_msg = '請正常輸入😀😀😀'
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=else_msg))


if __name__ == "__main__":
    app.run()
