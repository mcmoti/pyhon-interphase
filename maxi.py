import tkinter as tk
from pymongo import MongoClient

def retrieve_order_info():
    order_number = entry_search.get()
    order_info = collection.find_one({"order_number": order_number})
    if order_info:
        entry_name.delete(0, tk.END)
        entry_items.delete(0, tk.END)
        entry_quantity.delete(0, tk.END)
        entry_waiter.delete(0, tk.END)
        entry_name.insert(0, order_info["name"])
        entry_items.insert(0, order_info["items"]) 
        entry_quantity.insert(0, order_info["quantity"])
        entry_waiter.insert(0, order_info["waiter"])
    else:
        clear_entries()
        print("Order not found")

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_items.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    entry_waiter.delete(0, tk.END)

def save_order_info():
    order_number = entry_order_number.get()
    name = entry_name.get()
    items = entry_items.get()
    quantity = entry_quantity.get()
    waiter = entry_waiter.get()

    order_info = {
        "order_number": order_number,
        "name": name,
        "items": items,
        "quantity": quantity,
        "waiter": waiter
    }

    collection.insert_one(order_info)
    print("Order information saved successfully")

def delete_order_info():
    order_number = entry_search.get()
    result = collection.delete_one({"order_number": order_number})
    if result.deleted_count > 0:
        clear_entries()
        print("Order information deleted successfully")
    else:
        print("Order not found")

# Create the main application window
root = tk.Tk()
root.title("Order Information")

# Create text entry widgets
entry_search = tk.Entry(root)
entry_order_number = tk.Entry(root)
entry_name = tk.Entry(root)
entry_items = tk.Entry(root)
entry_quantity = tk.Entry(root)
entry_waiter = tk.Entry(root)

# Create labels for text entry widgets
label_search = tk.Label(root, text="Order Number:")
label_admission_number = tk.Label(root, text="Order Number:")
label_name = tk.Label(root, text="Name:")
label_items = tk.Label(root, text="Items:")
label_quantity = tk.Label(root, text="Quantity:")
label_waiter = tk.Label(root, text="Waiter:")

# Pack labels and text entry widgets
label_search.pack()
entry_search.pack()

label_name.pack()
entry_name.pack()

label_items.pack()
entry_items.pack()

label_quantity.pack()
entry_quantity.pack()

label_waiter.pack()
entry_waiter.pack()

# Create buttons
button_retrieve = tk.Button(root, text="Retrieve", command=retrieve_order_info)
button_retrieve.pack(pady=5)

button_save = tk.Button(root, text="Save", command=save_order_info)
button_save.pack(pady=5)

button_delete = tk.Button(root, text="Delete", command=delete_order_info)
button_delete.pack(pady=5)

# Connect to the MongoDB database
client = MongoClient("mongodb://localhost:27017/")
db = client["restaurant_database"]
collection = db["restaurant"]

# Run the application
root.mainloop()