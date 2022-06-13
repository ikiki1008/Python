from tkinter import *
import requests
import json
from datetime import datetime

root = Tk()
root.geometry("400x400")  # size of tk window!
root.resizable(0, 0)  # to make the window size fixed
root.title("날씨앱 - 파이썬 과제")
city_value = StringVar()


def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()


city_value = StringVar()


def showWeather():
    api_key = "ecdae3eee02b1b7f2eaa7b43745be9df"  # enter my api key
    city_name = city_value.get()
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid=' + api_key
    response = requests.get(weather_url)
    weather_info = response.json()
    tfield.delete("1.0", "end")  # to clear the text field for every new output

    # if the cod is 200, it means that weather data was successfully fetched!
    if weather_info['cod'] == 200:
        kelvin = 273  # value of kelvin

        # Storing the fetched values of weather of a city

        temp = int(weather_info['main']['temp'] - kelvin)  # converting default kelvin value to Celcius
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed'] * 3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']

        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)


        weather = f"\n도시이름: {city_name}\n온도(섭씨): {temp}°\n체감상 온도(섭씨): {feels_like_temp}°\n기압: {pressure} hPa\n\습도: {humidity}%\n동 트는 시간은 {sunrise_time} 해가 지는 시간은 {sunset_time} 입니다. \n구름: {cloudy}%\n 그 외: {description}"
    else:
        weather = f"\n\t'{city_name}' 도시를 찾을 수 없습니다.\n\t알고싶은 도시를 다시 입력해주세용!"

    tfield.insert(INSERT, weather)


# Interface part, frontend!


city_head = Label(root, text='날씨를 알고싶은 도시를 입력해주세요', font='Arial 12 bold').pack(pady=10)
inp_city = Entry(root, textvariable=city_value, width=24, font='Arial 14 bold').pack()
Button(root, command=showWeather, text="날씨 확인하기", font="Arial 10", bg='lightblue', fg='black',
       activebackground="teal", padx=5, pady=5).pack(pady=20)

#output part

weather_now = Label(root, text="현재의 날씨는 :", font='arial 12 bold').pack(pady=10)
tfield = Text(root, width=46, height=10)
tfield.pack()

root.mainloop()