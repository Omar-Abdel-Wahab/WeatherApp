from tkinter import *
from PIL import ImageTk, Image
import requests, json

# Creating the root window, and adding some properties
root = Tk()
root.title("Weather App")
root.iconbitmap("weather.ico")
root.geometry("600x400")
root.configure(bg="#FFFFFF")
root.resizable(False, False)

# Create a label, add an image to it and make the label in the center of the window
img = Image.open("weather_og.png")
img = img.resize((500, 200))
img = ImageTk.PhotoImage(img)
img_label = Label(root, image=img)
#img_label.grid(row=0, column=1, columnspan=3)
img_label.pack()

# Create an entry, adjust its properties and placement
city_var = StringVar()
city_var.set("Enter city name")
city_entry = Entry(root, textvariable=city_var, fg="#808080")
#city_entry.grid(row=1, column=1, columnspan=3)
city_entry.pack()


def clear_entry(event):
    """Clear the entry upon mouse click"""
    city_var.set("")


# Add mouse-click event
city_entry.bind("<Button-1>", clear_entry)

# API Request
# api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}


def get_weather():

    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    api_key = "c64618b984f6134b0d2f88e7b828cf8d"
    city_name = city_entry.get()
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key
    try:
        response = requests.get(complete_url)
        json_data = response.json()
        weather_label.configure(text=json_data["main"]["temp"])
    except requests.exceptions.RequestException as e:
        response = "Error"
    except ValueError as e:
        json_data = "Error"


get_button = Button(root, text="Get Weather", command=get_weather)
get_button.pack()

weather_label = Label(root, text="Temperature here")
weather_label.pack()

# Keep the root window running
root.mainloop()
