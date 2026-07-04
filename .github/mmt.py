import tkinter as tk


def calculate():
    start = start_station.get()
    stop = stop_station.get()

    # Determine which line the stations are on
    if start in stn_sL:
        start_line = stn_sL
    else:
        start_line = stn_pL

    if stop in stn_sL:
        stop_line = stn_sL
    else:
        stop_line = stn_pL

    # Same line
    if start_line is stop_line:
        n_stops = abs(start_line.index(start) - start_line.index(stop))

    # Different lines
    else:
        route1 = abs(start_line.index(start) - start_line.index("Union"))
        route1 += abs(stop_line.index("Union") - stop_line.index(stop))

        route2 = abs(start_line.index(start) - start_line.index("BurJuman"))
        route2 += abs(stop_line.index("BurJuman") - stop_line.index(stop))

        n_stops = min(route1, route2)

    fare = n_stops * 20
    farelabel.configure(text="FARE = INR " + str(fare))


window = tk.Tk()
window.title("Dubai Metro Map")
window.configure(bg="white")
window.geometry("1600x900")

c = tk.Canvas(
    window,
    width=1550,
    height=850,
    bg="white"
)
c.pack()

# Station radius
r_stn = 5

# FIXED: reduced spacing so map fits
d_stn = 48

# ---------------- RED LINE ---------------- #

stn_sL = [
    "Centrepoint",
    "Emirates",
    "Airport Terminal 3",
    "Airport Terminal 1",
    "GGICO",
    "City Centre Deira",
    "Al Rigga",
    "Union",
    "BurJuman",
    "Max",
    "World Trade Centre",
    "Emirates Towers",
    "Financial Centre",
    "Burj Khalifa/Dubai Mall",
    "Business Bay",
    "ONPASSIVE",
    "Equiti",
    "Mall of the Emirates",
    "Mashreq",
    "Dubai Internet City",
    "Al Khail",
    "Sobha Realty",
    "DMCC",
    "Jabal Ali",
    "Ibn Battuta",
    "Energy",
    "Danube",
    "UAE Exchange"
]

# FIXED: shifted left slightly
x_s = 30
y_s = 420

red_coords = []

for stn in stn_sL:
    red_coords.append((x_s, y_s))
    x_s += d_stn
for i in range(len(red_coords) - 1):
    x1, y1 = red_coords[i]
    x2, y2 = red_coords[i + 1]

    c.create_line(x1, y1, x2, y2, fill="red", width=4)
    
# Draw red stations + labels
for i in range(len(stn_sL)):
    x, y = red_coords[i]

    c.create_oval(
        x - r_stn, y - r_stn,
        x + r_stn, y + r_stn,
        fill="red",
        outline="red"
    )

    # FIXED: smaller font for long names
    if len(stn_sL[i]) > 15:
        fs = 5
    else:
        fs = 6

    c.create_text(
        x,
        y + 22,
        text=stn_sL[i],
        angle=45,
        font=("Helvetica", fs)
    )

# ---------------- GREEN LINE ---------------- #

stn_pL = [
    "Etisalat",
    "Al Qusais",
    "Dubai Airport Free Zone",
    "Al Nahda",
    "Stadium",
    "Al Qiyadah",
    "Abu Hail",
    "Abu Baker Al Siddique",
    "Salah Al Din",
    "Union",
    "BurJuman",
    "Sharaf DG",
    "Al Fahidi",
    "Al Ghubaiba",
    "Al Ras",
    "Gold Souq",
    "Baniyas"
]

green_coords = []

# Vertical section (Etisalat → Union)
x_s = red_coords[7][0]
y_s = 70

for i in range(10):
    green_coords.append((x_s, y_s))
    y_s += d_stn

# Horizontal connection (Union → BurJuman)
x_s += d_stn
green_coords.append((x_s, green_coords[-1][1]))

# Vertical section (BurJuman → Baniyas)
y_s = green_coords[-1][1] + d_stn

for i in range(11, len(stn_pL)):
    green_coords.append((x_s, y_s))
    y_s += d_stn
# ---------------- DRAW GREEN LINE ---------------- #

for i in range(len(green_coords) - 1):
    x1, y1 = green_coords[i]
    x2, y2 = green_coords[i + 1]

    c.create_line(
        x1, y1, x2, y2,
        fill="green",
        width=4
    )

# Draw green stations + labels
for i in range(len(stn_pL)):
    x, y = green_coords[i]

    c.create_oval(
        x - r_stn, y - r_stn,
        x + r_stn, y + r_stn,
        fill="green",
        outline="green"
    )

    # smaller font if long name
    if len(stn_pL[i]) > 15:
        font_size = 5
    else:
        font_size = 6

    c.create_text(
        x + 8,
        y,
        text=stn_pL[i],
        anchor="w",
        font=("Helvetica", font_size)
    )

# Highlight interchange stations
for station in ["Union", "BurJuman"]:
    if station in stn_sL:
        x, y = red_coords[stn_sL.index(station)]
        c.create_oval(
            x - 8, y - 8,
            x + 8, y + 8,
            outline="black",
            width=2
        )

# ---------------- ALL STATIONS LIST ---------------- #

all_stations = []

for stn in stn_sL:
    if stn not in all_stations:
        all_stations.append(stn)

for stn in stn_pL:
    if stn not in all_stations:
        all_stations.append(stn)

# ---------------- TITLE ---------------- #

c.create_text(
    775,
    30,
    text="DUBAI METRO MAP",
    font=("Helvetica", 20, "bold"),
    fill="red"
)

c.create_text(
    775,
    55,
    text="Red Line & Green Line",
    font=("Helvetica", 12, "bold"),
    fill="green"
)
# ---------------- START STATION ---------------- #

c.create_text(
    250,
    770,
    text="Start Station",
    font=("Helvetica", 10, "bold")
)

start_station = tk.StringVar()
start_station.set(all_stations[0])

drop_start = tk.OptionMenu(
    window,
    start_station,
    *all_stations
)
drop_start.place(x=180, y=795)


# ---------------- DESTINATION ---------------- #

c.create_text(
    650,
    770,
    text="Destination",
    font=("Helvetica", 10, "bold")
)

stop_station = tk.StringVar()
stop_station.set(all_stations[1])

drop_stop = tk.OptionMenu(
    window,
    stop_station,
    *all_stations
)
drop_stop.place(x=580, y=795)

button = tk.Button(
    window,
    text="Calculate Fare",
    command=calculate,
    font=("Helvetica", 11, "bold")
)
button.place(x=980, y=795)


# ---------------- FARE ---------------- #

farelabel = tk.Label(
    window,
    text="FARE = ",
    bg="white",
    font=("Helvetica", 12, "bold")
)
farelabel.place(x=980, y=835)

window.mainloop()