import os
import requests
from tokens import OPENWEATHER_API_KEY

city_coordinates = {'Санкт-Петербург': ['59.9370', '30.3265'],
                    'Улан-Удэ': ['51.8347', '107.5839']}

def get_weather_now(OPENWEATHER_API_KEY, LAT, LON):
    final_url = requests.get('http://api.openweathermap.org/data/2.5/onecall',
                             params={'appid': OPENWEATHER_API_KEY,
                                     'lat': LAT,
                                     'lon': LON,
                                     'lang': 'ru',
                                     'units': 'metric',
                                     'exclude': ['minutely', 'hourly', 'alerts']})
    # this variable contain the JSON data which the API returns
    weather_data = final_url.json()

    uvi_now = weather_data['current']['uvi']
    uvi_today_max = weather_data['daily'][0]['uvi']
    temp_now = weather_data['current']['temp']
    temp_feels_like = weather_data['current']['feels_like']
    weather_status = [i['description'] for i in weather_data['current']['weather']]

    if uvi_now <1 or uvi_today_max <1:
        sunscreen_status = 'Санскрин не нужен'
    elif uvi_now <=3 or uvi_today_max <=3:
        sunscreen_status = 'Носите солнцезащитные очки в яркие дни' +'\n' + \
                           'Носите закрытую одежду и используйте санскрин, если ваша кожа легко сгорает даже при таком индексе'
    elif uvi_now <6 or uvi_today_max <6:
        sunscreen_status = 'Используйте солнцезащитный крем и носите закрытую одежду' +'\n' + \
                           'Оставайтесь в тени в обеденное время'
    elif uvi_now <8 or uvi_today_max <8:
        sunscreen_status = 'Сократите время на солнце с 10:00 до 16:00' + '\n' + \
                           'Носите закрытую одежду, панаму или шляпу и солнцезащитные очки' + \
                           '\n' +  'Используйте солнцезащитный крем'
    elif uvi_now >8 or uvi_today_max >8:
        sunscreen_status = 'Старайтесь избегайте солнца с 10:00 до 16:00' + '\n' \
                           + 'Если не получается, оставайтесь в тени, носите закрытую одежду, панаму или шляпу и солнцезащитные очки' + \
                           '\n' + 'Используйте солнцезащитный крем'






    clouds_state_now = str('Состояние погоды сейчас: ' + str(weather_status[0]) +'\n'+ \
                           'Температура сейчас: '+str(temp_now) + '°' +'\n' + \
                           'Ощущается как: '+str(temp_feels_like) + '°' + '\n' + \
'\n' + \
                           '☀UV индекс сейчас: ' + str(uvi_now) + '\n' + \
                           '☀Максимальный UV индекс сегодня: ' + str(uvi_today_max) + '\n' + '\n' +\
                           '😉Рекомендация на день:' + '\n' + sunscreen_status)
    return clouds_state_now
