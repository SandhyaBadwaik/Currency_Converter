from currency_converter import CurrencyConverter
import tkinter as tk

c = CurrencyConverter()

window = tk.Tk()
window.geometry("500x360")
window.title("Currency Converter")

def clicked():
    try:
        amount = float(entry1.get())
        cur1 = entry2.get().upper()  # Convert to uppercase
        cur2 = entry3.get().upper()
        
        # Check if currencies exist in the dataset
        if cur1 not in c.currencies or cur2 not in c.currencies:
            result_label.config(text="Invalid currency code!", fg="red")
            return
        
        data = c.convert(amount, cur1, cur2)
        result_label.config(text=f"{amount} {cur1} = {data:.2f} {cur2}", fg="blue")

    except ValueError:
        result_label.config(text="Enter a valid number!", fg="red")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}", fg="red")

# GUI Components
label = tk.Label(window, text="Currency Converter", font="Times 20 bold")
label.place(x=120, y=40)

label1 = tk.Label(window, text="Enter amount", font="Times 16 bold")
label1.place(x=50, y=100)
entry1 = tk.Entry(window)
entry1.place(x=270, y=105)

label2 = tk.Label(window, text="From Currency", font="Times 16 bold")
label2.place(x=50, y=150)
entry2 = tk.Entry(window)
entry2.place(x=270, y=155)

label3 = tk.Label(window, text="To Currency", font="Times 16 bold")
label3.place(x=50, y=200)
entry3 = tk.Entry(window)
entry3.place(x=270, y=205)

button = tk.Button(window, text="Convert", font="Times 20 bold", command=clicked)
button.place(x=200, y=250)

result_label = tk.Label(window, text="", font="Times 20 bold", fg="blue")
result_label.place(x=120, y=300)

window.mainloop()
