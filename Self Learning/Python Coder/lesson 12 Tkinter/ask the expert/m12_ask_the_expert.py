from tkinter import Button, Entry, Label, Tk, font, messagebox

print('Ask the Expert - Capital Cities of the World')

root = Tk()
root.withdraw()

the_world = {}


# Fungsi untuk menyimpan data baru ke dalam file m12_capital_data.txt
def write_to_file(country_name, city_name):
    with open('m12_capital_data.txt', 'a') as file:
        file.write('\n' + country_name + '/' + city_name)


def custom_askstring(
    title,
    prompt,
    dialog_size="450x150",
    bg_color="lightblue",
    font_size=12,
    font_weight="bold",
):
    dialog = Tk()
    dialog.title(title)
    dialog.geometry(dialog_size)
    dialog.configure(bg=bg_color)

    custom_font = font.Font(size=font_size, weight=font_weight)

    label = Label(dialog, text=prompt, bg=bg_color, font=custom_font)
    label.pack(pady=10)

    entry = Entry(dialog, font=custom_font)
    entry.pack(pady=5)
    entry.focus_set()

    def on_ok():
        dialog.result = entry.get()
        dialog.destroy()

    button = Button(dialog, text="OK", command=on_ok, font=custom_font)
    button.pack(pady=5)

    dialog.wait_window()

    try:
        return dialog.result
    except AttributeError:
        return ""


# Loop utama program
while True:
    query_country_input = custom_askstring(
        "Country",
        "Type the name of a country",
        dialog_size="450x150",
        bg_color="lightgreen",
        font_size=14,
        font_weight="bold",
    )

    if query_country_input:
        query_country = query_country_input.capitalize()

        if query_country in the_world:
            result = the_world[query_country]
            messagebox.showinfo(
                "Answer",
                "The capital city of "
                + query_country
                + " is "
                + result
                + "!",
            )
        else:
            new_city = custom_askstring(
                "Teach me",
                "I don't know. What is the capital city of "
                + query_country
                + "?",
                dialog_size="450x150",
                bg_color="lightblue",
                font_size=12,
                font_weight="bold",
            )

            if new_city:
                new_city = new_city.capitalize()
                the_world[query_country] = new_city
                write_to_file(query_country, new_city)
    else:
        break