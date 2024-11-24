import tkinter as tk
from tkinter import filedialog, messagebox
import signature_match as sm

def browse_file(entry):
    filename = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, filename)

def compare_signatures():
    # Get the values from the entry widgets
    signature1 = entry1.get()
    signature2 = entry2.get()
    
    # Call the signature matching function and get the result
    result = sm.main(signature1, signature2)
    print(result)
    
    # Display the result in a message box
    messagebox.showinfo("Comparison Result", result)

# Create the main window
root = tk.Tk()
root.title("Signature Matching")

# Create and place the labels, entries, and buttons
tk.Label(root, text="Compare Two Signatures:").grid(row=0, column=0, columnspan=3, pady=10)

tk.Label(root, text="Signature 1").grid(row=1, column=0, padx=10, pady=5, sticky='e')
entry1 = tk.Entry(root, width=50)
entry1.grid(row=1, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=lambda: browse_file(entry1)).grid(row=1, column=2, padx=10, pady=5)

tk.Label(root, text="Signature 2").grid(row=2, column=0, padx=10, pady=5, sticky='e')
entry2 = tk.Entry(root, width=50)
entry2.grid(row=2, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=lambda: browse_file(entry2)).grid(row=2, column=2, padx=10, pady=5)

tk.Button(root, text="Compare", command=compare_signatures).grid(row=3, column=0, columnspan=3, pady=10)

# Run the application
root.mainloop()
