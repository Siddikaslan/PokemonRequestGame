import tkinter as tk
import requests
from tkinter import messagebox, PhotoImage

def pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None


def compare_pokemons():
    pokemon1_name = pokemon1_entry.get()
    pokemon2_name = pokemon2_entry.get()

    pokemon1_info = pokemon_data(pokemon1_name)
    pokemon2_info = pokemon_data(pokemon2_name)

    if not pokemon1_name or not pokemon2_name:
        messagebox.showwarning("Alert","Please enter both pokemons.")
        return

    if pokemon1_info and pokemon2_info:
        result = f"( {pokemon1_info['name']} )   vs   ( {pokemon2_info['name']} )\n"
        result += f"id: {pokemon1_info["id"]}   <--->   id: {pokemon2_info["id"]}\n"
        result += f"Weight:  {pokemon1_info["weight"]}   <--->   {pokemon2_info["weight"]}\n"
        result += f"Height:  {pokemon1_info["height"]}   <--->   {pokemon2_info["height"]}\n"
        result += "Type: \n"
        for type1, type2 in zip(pokemon1_info["types"], pokemon2_info["types"]):
            result += f"{type1["type"]["name"]}   <--->   {type2["type"]["name"]}\n"

        result += "Stats: \n"
        pokemon1_total_stats = 0
        pokemon2_total_stats = 0
        for stat1, stat2 in zip(pokemon1_info["stats"], pokemon2_info["stats"]):
            result += f"{stat1["stat"]["name"]}: {stat1["base_stat"]}   <--->   {stat2["stat"]["name"]}: {stat2["base_stat"]}\n"
            pokemon1_total_stats += stat1["base_stat"]
            pokemon2_total_stats += stat2["base_stat"]

        result += "Abilities: \n"
        for ability1, ability2 in zip(pokemon1_info["abilities"], pokemon2_info["abilities"]):
            result += f"{ability1["ability"]["name"]}   <--->   {ability2["ability"]["name"]}\n"

        result += "Total Stats:\n"
        result += f"{pokemon1_info['name']}: {pokemon1_total_stats}\n"
        result += f"{pokemon2_info['name']}: {pokemon2_total_stats}\n"

        if pokemon1_total_stats > pokemon2_total_stats:
            result += f"\nWinner -->  {pokemon1_info['name']}  c(:"
        elif pokemon2_total_stats > pokemon1_total_stats:
            result += f"\nWinner -->  {pokemon2_info['name']}  c(:"
        else:
            result += "\nTie"

        result_label.config(text=result)
    else:
        messagebox.showinfo("Info","Failed to retrieve Pokemon information.")


window = tk.Tk()
window.title("Pokemon Comparator")
window.minsize = (400,700)
window.config(padx=15, pady=15)
FONT = ("Ariel" , 14)

img = PhotoImage(file="Poke_Ball.png")
img_label = tk.Label(image=img)
img_label.pack(pady=8)


pokemon1_label = tk.Label(text="Enter your first pokemon", font=FONT)
pokemon1_label.pack(pady=3)
pokemon1_entry = tk.Entry(width=25)
pokemon1_entry.pack(pady=3)

pokemon2_label = tk.Label(text="Enter your second pokemon", font=FONT)
pokemon2_label.pack(pady=3)
pokemon2_entry = tk.Entry(width=25)
pokemon2_entry.pack(pady=3)

compare_button = tk.Button(text="Compare", font=FONT, command=compare_pokemons)
compare_button.pack(pady=3)

result_label = tk.Label(text="", font=FONT)
result_label.pack(pady=6)

window.mainloop()