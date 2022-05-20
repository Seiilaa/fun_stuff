import telebot
from get_weather import city_coordinates, get_weather_now
from keep_alive import keep_alive
from tokens import TOKEN, OPENWEATHER_API_KEY

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def command_start(message):
  start_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
  start_markup.row('/location')
  bot.send_message(message.chat.id, "🤖 Бот запущен!\n⚙ Нажми /location, чтобы выбрать город",reply_markup=start_markup)


@bot.message_handler(commands=['location'])
def get_location(message):
  start_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
  start_markup.row('/Санкт-Петербург')
  start_markup.row('/Улан-Удэ')
  bot.send_message(message.from_user.id, 'Выберите город', reply_markup=start_markup)

@bot.message_handler(commands=['Санкт-Петербург', 'Улан-Удэ'])
def get_weather(message):
  LAT, LON = city_coordinates[message.text[1:]]
  
  bot.send_message(message.from_user.id, get_weather_now(OPENWEATHER_API_KEY, LAT, LON))

keep_alive()
bot.polling(none_stop=True, interval=0)
