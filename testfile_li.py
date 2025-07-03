import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple GUI")
root.geometry("200x100") # Set the window size

# Create a button that closes the window
close_button = tk.Button(root, text="Close", command=root.destroy)
close_button.pack(pady=20)

# Run the application
root.mainloop()

print('Dette funker')
