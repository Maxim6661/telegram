import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup
global city_is_showing

class Weather():
    def __init__(self,link,city):
        self.link = link
        self.city = city
        self.res = requests.get(self.link).text
        self.soup = BeautifulSoup(self.res, 'html.parser')
        self.soup.encode('utf-8')
        self.temp = self.soup.find("div", {"class": "today_nowcard-temp"}).text
        self.feeling_temp = self.soup.find("span", {"class": "deg-feels"}).text
        self.wind = self.soup.select("tr")[0].find("span").text
        self.damp = self.soup.select("tr")[1].find("span").text
        self.pressure = self.soup.select("tr")[3].find("span").text
        self.visibitily_range = self.soup.select("tr")[4].find("span").text
        self.weather_feeling = self.soup.find("div", {"class": "today_nowcard-phrase"}).text
        self.lastupdate = self.soup.select("p", {"class": "today_nowcard-timestamp"})[0].select("span")[1].text
        self.info = f"<b>Погода в {city_is_showing}</b>\n<em>Температура сейчас:</em> {self.temp}\n<em>Ощущается:</em> {self.feeling_temp}\n{self.weather_feeling}\n<b>Дополнительная информация</b>\n<em>Ветер:</em> {self.wind}\n<em>Влажность:</em> {self.damp}\n<em>Давление:</em> {self.pressure}\n<em>Видимость:</em> {self.visibitily_range}\n\n<i>Последнее обновление данных в </i> {self.lastupdate}"


#page = Weather("https://weather.com/ru-BY/weather/today/l/c855859306f030f8d49f5384679a8178ea208b09006cad98a5994feab8b43666",city_is_showing)
TOKEN = '1251767336:AAEvb6BfPhzCgXeWZGftavYf0_U92YLkUHg'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itemMinsk = types.KeyboardButton("Минск")
    itemBrest = types.KeyboardButton("Брест")
    itemGomel = types.KeyboardButton("Гомель")
    itemVitebsk = types.KeyboardButton("Витебск")
    itemMogilev = types.KeyboardButton("Могилев")
    itemGrodno = types.KeyboardButton("Гродно")
    itemMoscow = types.KeyboardButton("Москва")
    itemKiev = types.KeyboardButton("Киев")
    itemPiter = types.KeyboardButton("Санкт-Петербург")
    itemRim = types.KeyboardButton("Рим")
    itemNew_York = types.KeyboardButton("Нью-Йорк")
    itemLondon = types.KeyboardButton("Лондон")
    itemParis = types.KeyboardButton("Париж")
    itemLondon = types.KeyboardButton("Варшава")
    itemParis = types.KeyboardButton("Берлин")
    markup.add(itemMinsk, itemBrest, itemGomel,itemVitebsk,itemMogilev,itemGrodno,itemMoscow,itemKiev,itemPiter,itemRim,itemNew_York,itemLondon,itemParis)
    bot.send_message(message.chat.id, "Чтобы узнать погоду, выберите или напишите  свой город", reply_markup=markup)
@bot.message_handler(content_types=['text'])
def msg(message):
    global city_is_showing
    if message.text == "Минск":
        city_is_showing = "Минске"
        minsk = Weather("https://weather.com/ru-BY/weather/today/l/c855859306f030f8d49f5384679a8178ea208b09006cad98a5994feab8b43666",city_is_showing)
        bot.send_message(message.chat.id, minsk.info,parse_mode='html')
    elif message.text == "Брест":
        city_is_showing = "Бресте"
        brest = Weather("https://weather.com/ru-BY/weather/today/l/d5f6c50e45908fd280db2ec352b585db6358bd07a175917379e0b38495d5f586",city_is_showing)
        bot.send_message(message.chat.id, brest.info, parse_mode='html')
    elif message.text == "Гомель":
        city_is_showing = "Гомеле"
        gomel = Weather("https://weather.com/ru-BY/weather/today/l/8493ac1c3a23de4a15e24bd8fee7a078ae89435c6079fb9b81c1d004f5a9263a",city_is_showing)
        bot.send_message(message.chat.id, gomel.info, parse_mode='html')
    elif message.text == "Витебск":
        city_is_showing = "Витебске"
        vitebsk = Weather("https://weather.com/ru-BY/weather/today/l/ea75133c0b3a5de4343e0fde70c4860a06f029a6a21c7b7cfe676d651b9a3263",city_is_showing)
        bot.send_message(message.chat.id, vitebsk.info, parse_mode='html')
    elif message.text == "Могилев":
        city_is_showing = "Могилеве"
        mogilev = Weather("https://weather.com/ru-BY/weather/today/l/d7cf2d820b01c4be1e750f5c2cb025db49dfed295939bf6d39222959d9dce7e4",city_is_showing)
        bot.send_message(message.chat.id, mogilev.info, parse_mode='html')
    elif message.text == "Гродно":
        city_is_showing = "Гродно"
        grodno = Weather("https://weather.com/ru-BY/weather/today/l/e97f643dd1508ae32c9d801c0db8382f2e32f10d93b6d2f02af487c647d1aa1a",city_is_showing)
        bot.send_message(message.chat.id, grodno.info, parse_mode='html')
    elif message.text == "Москва":
        city_is_showing = "Москве"
        moscow = Weather("https://weather.com/ru-BY/weather/today/l/34f2aafc84cff75ae0b014754856ea5e7f8ddf618cf9735549dfb5e016c28e10",city_is_showing)
        bot.send_message(message.chat.id, moscow.info, parse_mode='html')
    elif message.text == "Киев":
        city_is_showing = "Киеве"
        kiev = Weather("https://weather.com/ru-BY/weather/today/l/d198c31dca17aa9ac8e4ff2e4dbdb48e4ca8c01f0fd1369998f0a09f53ef0b1d",city_is_showing)
        bot.send_message(message.chat.id, kiev.info, parse_mode='html')
    elif message.text == "Санкт-Петербург":
        city_is_showing = "Санкт-Петербурге"
        piter = Weather("https://weather.com/ru-BY/weather/today/l/4edb4827c7f66b1542f84ce1d8d644970e9b935d45d21d4d143e87d94925a4bf",city_is_showing)
        bot.send_message(message.chat.id, piter.info, parse_mode='html')
    elif message.text == "Рим":
        city_is_showing = "Риме"
        rim = Weather("https://weather.com/ru-BY/weather/today/l/1d1a251383dc0d1bdbfb8efbc155374b376eff6f5232f36110b823e47362866e",city_is_showing)
        bot.send_message(message.chat.id, rim.info, parse_mode='html')
    elif message.text == "Нью-Йорк":
        city_is_showing = "Нью-Йорке"
        new_york = Weather("https://weather.com/ru-BY/weather/today/l/f892433d7660da170347398eb8e3d722d8d362fe7dd15af16ce88324e1b96e70",city_is_showing)
        bot.send_message(message.chat.id, new_york.info, parse_mode='html')
    elif message.text == "Лондон":
        city_is_showing = "Лондоне"
        london = Weather("https://weather.com/ru-BY/weather/today/l/7517a52d4d1815e639ae1001edb8c5fda2264ea579095b0f28f55c059599e074",city_is_showing)
        bot.send_message(message.chat.id, london.info, parse_mode='html')
    elif message.text == "Париж":
        city_is_showing = "Париже"
        paris = Weather("https://weather.com/ru-BY/weather/today/l/1a8af5b9d8971c46dd5a52547f9221e22cd895d8d8639267a87df614d0912830",city_is_showing)
        bot.send_message(message.chat.id, paris.info, parse_mode='html')
    elif message.text == "Варшава":
        city_is_showing = "Варшаве"
        varshava = Weather("https://weather.com/ru-BY/weather/today/l/a8b0daa43d13b260354967e7b6792eae37e9924dee035d82922e416e63de4051",city_is_showing)
        bot.send_message(message.chat.id, varshava.info, parse_mode='html')
    elif message.text == "Берлин":
        city_is_showing = "Берлине"
        paris = Weather("https://weather.com/ru-BY/weather/today/l/5ca23443513a0fdc1d37ae2ffaf5586162c6fe592a66acc9320a0d0536be1bb9",city_is_showing)
        bot.send_message(message.chat.id, paris.info, parse_mode='html')
    else:
        bot.send_message(message.chat.id, f"<b>Город не найден, либо ещё не добавлен!</b>\nДоступные города:\n <em>Минск</em> \n <em>Брест</em> \n <em>Гомель</em> \n <em>Могилёв</em> \n <em>Гродно</em>"
                                          f" \n <em>Витебск</em> \n <em>Москва</em> \n <em>Санкт-Петербург</em> \n <em>Киев</em> \n <em>Париж</em> \n <em>Лондон</em> \n <em>Нью-Йорк</em> \n <em>Рим</em> \n <em>Варшава</em> \n <em>Берлин</em>", parse_mode='html')
bot.polling(none_stop=True)

