from tkinter import *
from opencage.geocoder import OpenCageGeocode
import webbrowser


def get_coordinates(city, key):
    """Получаем координаты по названию города."""
    try:
        geocoder = OpenCageGeocode(key)
        query = city
        results = geocoder.geocode(query)
        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lng = round(results[0]['geometry']['lng'], 2)
            country = results[0]['components']['country']
            osm_url = f'https://www.openstreetmap.org/?mlat={lat}&mlon={lng}'
            if 'state' in results[0]['components']:
                region = results[0]['components']['state']
                # return (f'Широта: {lat}, Долгота: {lng}\n'
                #     f'Страна: {country}\nРегион: {region}')
                return {'coordinates': f'Широта: {lat}, Долгота: {lng}\n'
                                       f'Страна: {country}\nРегион: {region}',
                        'map_url': osm_url}
            else:
                # return (f'Широта: {lat}, Долгота: {lng}\n'
                #         f'Страна: {country}')
                return {'coordinates': f'Широта: {lat}, Долгота: {lng}\n'
                                       f'Страна: {country}',
                        'map_url': osm_url}
        else:
            # return 'Город не найден!'
            return {'coordinates': 'Город не найден!', 'map_url': None}
    except Exception as er:
        return {'coordinates': f'Ошибка {er}', 'map_url': None}


def show_coordinates(event=None):
    global map_url
    city = entry.get().strip()
    result = get_coordinates(city, key)
    label.config(text=result['coordinates'])
    map_url = result['map_url']


def show_map():
    if map_url:
        webbrowser.open(map_url)



key = '96112fb6d80d4059ae9dabea94898600'
map_url = None
root = Tk()
root.title('Поиск координат города')
root.geometry('300x150+200+300')

Label(text='Введите название города ').pack()

entry = Entry(width=40)
entry.pack(pady=10)
entry.bind('<Return>', show_coordinates)
label = Label()
label.pack()
btn = Button(text='Показать карту', command=show_map)
btn.pack()

root.mainloop()

# city = 'Санкт-Петербург'
# coordinates = get_coordinates(city, key)
# print(f'Координаты города {city}: {coordinates}')
