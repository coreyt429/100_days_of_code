"""
Kanye Quotes App
This app fetches a random quote from the Kanye West API and displays it on the screen.
"""
import tkinter as tk
import requests


def get_quote():
    """Get a random Kanye quote from the API and update the canvas text."""
    quote = ""
    # long quotes don't fit, so lets set a limit of 100 characters
    # and retry if we get a long one
    while not quote or len(quote) > 100:
        try:
            # Attempt to fetch a quote from the API
            response = requests.get("https://api.kanye.rest", timeout=5)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            quote = data["quote"]
        except requests.exceptions.RequestException as e:
            print(f"Error fetching quote: {e}")
            return   
    canvas.itemconfig(quote_text, text=quote)


window = tk.Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=300, height=414)
background_img = tk.PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(
    150,
    207,
    text="Kanye Quote Goes HERE",
    width=250,
    font=("Arial", 30, "bold"),
    fill="white",
)
canvas.grid(row=0, column=0)

kanye_img = tk.PhotoImage(file="kanye.png")
kanye_button = tk.Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)
get_quote()


window.mainloop()
