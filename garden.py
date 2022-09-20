from tkinter import *
import json
from utils import *

GREEN = "#778A35"
LIGHT_GREEN = "#D1E2C4"
DARK_GREY = "#31352E"
RED = "#EE5007"
YELLOW = "#F8CB2E"

with open("plant_data.json") as plant_data:
    data = json.load(plant_data)

plant_name = [""] * 48


def has_been_planted(plant):
    if plant != "" and data[plant]["Day planted"] != 0:
        return True
    else:
        return False


def get_plot_info(plant):
    pass


def show_data(plant):
    if has_been_planted(plant):
        countdown = data[plant]['Ready'] - today_int()
        if countdown > 0:
            return countdown
        else:
            return "\nREADY"
    else:
        return ""


for plant in data:
    for location in data[plant]["Location"]:
        plant_name[location - 1] = plant

window = Tk()

s = []
for i in range(48):
    if show_data(plant_name[i]) == "":
        s.append(Frame(width=120, height=120, bg=GREEN, highlightthickness=5, highlightbackground="white"))
        s[i].grid(row=int(i / 12), column=i % 12)
    elif show_data(plant_name[i]) == "\nREADY":
        s.append(Frame(width=120, height=120, bg=RED, highlightthickness=5, highlightbackground="white"))
        s[i].grid(row=int(i / 12), column=i % 12)
    elif show_data(plant_name[i]) <= 7:
        s.append(Frame(width=120, height=120, bg=YELLOW, highlightthickness=5, highlightbackground="white"))
        s[i].grid(row=int(i / 12), column=i % 12)
    else:
        s.append(Frame(width=120, height=120, bg=GREEN, highlightthickness=5, highlightbackground="white"))
        s[i].grid(row=int(i / 12), column=i % 12)

labels = []
for i in range(48):
    if show_data(plant_name[i]) == "":
        labels.append(Label(text=f"{plant_name[i]}\n{show_data(plant_name[i])}", bg=GREEN))
        labels[i].grid(row=int(i / 12), column=i % 12, sticky="n", pady=10)
    elif show_data(plant_name[i]) == "\nREADY":
        labels.append(Label(text=f"{plant_name[i]}\n{show_data(plant_name[i])}", bg=RED))
        labels[i].grid(row=int(i / 12), column=i % 12, sticky="n", pady=10)
    elif show_data(plant_name[i]) <= 7:
        labels.append(Label(text=f"{plant_name[i]}\n{show_data(plant_name[i])}", bg=YELLOW))
        labels[i].grid(row=int(i / 12), column=i % 12, sticky="n", pady=10)
    else:
        labels.append(Label(text=f"{plant_name[i]}\n{show_data(plant_name[i])}", bg=GREEN))
        labels[i].grid(row=int(i / 12), column=i % 12, sticky="n", pady=10)

buttons = []
for i in range(48):
    if show_data(plant_name[i]) == "":
        buttons.append(Button(state="disabled", bd=-2, highlightthickness=0, highlightbackground=GREEN))
        buttons[i].grid(row=int(i / 12), column=i % 12, sticky="s", pady=10)
        buttons[i].grid_forget()
    elif show_data(plant_name[i]) == "\nREADY":
        buttons.append(Button(text="More Info", bd=-2, highlightthickness=0, highlightbackground=RED))
        buttons[i].grid(row=int(i / 12), column=i % 12, sticky="s", pady=10)
    elif show_data(plant_name[i]) <= 7:
        buttons.append(Button(text="More Info", bd=-2, highlightthickness=0, highlightbackground=YELLOW))
        buttons[i].grid(row=int(i / 12), column=i % 12, sticky="s", pady=10)
    else:
        buttons.append(Button(text="More Info", bd=-2, highlightthickness=0, highlightbackground=GREEN))
        buttons[i].grid(row=int(i / 12), column=i % 12, sticky="s", pady=10)


info_box = LabelFrame(text="Here is some info", height=200, width=400)
info_box.grid(row=4, column=0, columnspan=4)


# buttons = []
# for i in range(48):
#     buttons.append(Button(text="Get Info", bg=GREEN, highlightthickness=0))
#     buttons[i].grid(row=int(i / 12), column=i % 12, sticky="s", pady=(0, 6))

# info_frame = LabelFrame(text=get_plot_info)

window.mainloop()



