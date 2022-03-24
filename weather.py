from tkinter import *
from configparser import ConfigParser
from tkinter import messagebox
import requests

url_api="http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
api_file='weather.keys'
file_a=ConfigParser()
file_a.read(api_file)
api_key=file_a['api_key']['key']


def weather_find(city):
    final=requests.get(url_api.format(city,api_key))
    if final:
        json_file=final.json()
        city=json_file['name']
        country_name=json_file['sys']['country']
        k_temp=json_file["main"]['temp']
        c_temperature=k_temp-273.15
        f_temp=(k_temp-273.15)*9/5+32
        weather_display=json_file['weather'][0]['main']
        result=(city,country_name,c_temperature,f_temp,weather_display)

        return result
    else:
        return None


def print_weather():
    city=search_city.get()
    weather=weather_find(city)
    if weather:
        location_entry['text']= '{},{}'.format(weather[0],weather[1])
        temp_entry['text']='{:.2f} C,{:.2f} F'.format(weather[2],weather[3])
        weather_entry['text']=weather[4]
    else:
        messagebox.showerror("Invalid City")

root=Tk()
root.geometry("500x400")
root.title("Search Weather")
root.config(background="black")
search_city=StringVar()
enter_city=Entry(root,textvariable=search_city,fg="blue",font=("Agency FB",20,"bold"))
enter_city.pack()

search_button=Button(root,text='search',width=10,bg="red",fg="white",font=("Agency FB",20,"bold"),command=print_weather)
search_button.pack()

location_entry=Label(root,text='',font=("Agency FB",20,"bold"),bg="lightblue")
location_entry.pack()

temp_entry=Label(root,text='',font=("Agency FB",20,"bold"),bg="lightpink")
temp_entry.pack()

weather_entry=Label(root,text='',font=("Agency FB",30,"bold"),bg="lightgreen")
weather_entry.pack()

root.mainloop()