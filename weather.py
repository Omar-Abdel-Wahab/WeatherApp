from tkinter import *
from PIL import ImageTk, Image
import requests

# Creating the root window, and adding some properties
root = Tk()
root.title("Weather App")
root.iconbitmap("weather.ico")
root.geometry("502x320")
root.configure(bg="#FFFFFF")
root.resizable(False, False)


def center(window):
    """Center a Tkinter window"""
    window.update_idletasks()

    # Find the screen resolution
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Find new (x, y) coordinates
    size = tuple(int(_) for _ in window.geometry().split('+')[0].split('x'))
    x = screen_width/2 - 5 * size[0] / 9
    y = screen_height/2 - 3 * size[1] / 5

    # Apply new coordinates
    window.geometry("+%d+%d" % (x, y))


center(root)

# Create a label, add an image to it and make the label in the center of the window
img = Image.open("weather_og.png")
img = img.resize((500, 200))
img = ImageTk.PhotoImage(img)
img_label = Label(root, image=img)
img_label.grid(row=0, column=0, columnspan=11)

# Create a label for the city name
city_label = Label(root, text="City: ", bg="#FFFFFF")
city_label.grid(row=1, column=4)

# Create an entry, adjust its properties and placement
city_var = StringVar()
city_var.set("Enter city name")
city_entry = Entry(root, textvariable=city_var, fg="#808080")
city_entry.grid(row=1, column=5)


def clear_entry(event):
    """Clear the entry upon mouse click"""
    city_var.set("")
    city_entry.configure(fg="#000000")


# Add mouse-click event
city_entry.bind("<Button-1>", clear_entry)

# API Request
# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}


def get_weather():
    """Get weather related data to show on the screen"""
    # URL parts
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    api_key = "c64618b984f6134b0d2f88e7b828cf8d"
    city_name = city_entry.get()
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key

    # Create a GET request and parse it as JSON
    response = requests.get(complete_url)
    json_data = response.json()

    # If the request was a success
    if["cod"] != '404':
        # Get the weather data, apply conversions or functions
        temperature = json_data["main"]["temp"]
        temperature = round(float(temperature) - 273.15, 2)
        pressure = json_data["main"]["pressure"]
        description = json_data["weather"][0]["description"].title()
        temperature_value_label.configure(text=str(temperature) + " C")
        pressure_value_label.configure(text=str(pressure) + " Pascal")
        description_value_label.configure(text=description)
    else:
        json_data = "Error"
        response = "Error"


# Create a button to search by city name
get_button = Button(root, text="Get Weather", command=get_weather)
get_button.grid(row=2, column=5)

# Create labels for temperature, pressure, and description
temperature_label = Label(root, text="Temperature: ", bg="#FFFFFF")
temperature_label.grid(row=3, column=4)

temperature_value_label = Label(root, text="Temperature here", bg="#FFFFFF")
temperature_value_label.grid(row=3, column=6)

pressure_label = Label(root, text="Pressure: ", bg="#FFFFFF")
pressure_label.grid(row=4, column=4)

pressure_value_label = Label(root, text="Pressure here", bg="#FFFFFF")
pressure_value_label.grid(row=4, column=6)

description_label = Label(root, text="Description: ", bg="#FFFFFF")
description_label.grid(row=5, column=4)

description_value_label = Label(root, text="Description here", bg="#FFFFFF")
description_value_label.grid(row=5, column=6)

# Keep the root window running
root.mainloop()
