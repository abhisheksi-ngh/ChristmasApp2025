import tkinter as tk
from tkinter import Toplevel, messagebox
from PIL import Image, ImageTk
from src.init import clear_widgets, is_valid_email
from src.mail_process import send_email

def open_message_dialog():
    """
    Function to open a dialog for sending messages.
    """
    dialog = Toplevel(root)
    dialog.title("Send a Message")
    dialog.geometry("400x300")
    dialog.resizable(False, False)

    # Labels and input fields
    tk.Label(dialog, text="Recipient (Email):", font=("Arial", 14)).pack(pady=10)
    recipient_entry = tk.Entry(dialog, font=("Arial", 12))
    recipient_entry.pack(pady=5, fill="x", padx=10)

    tk.Label(dialog, text="Message:", font=("Arial", 14)).pack(pady=10)
    message_text = tk.Text(dialog, height=5, font=("Arial", 12))
    message_text.pack(pady=5, fill="x", padx=10)

    def send_dm():
        """
        Function to send a direct message to the recipient.
        """
        recipient = recipient_entry.get()
        message = message_text.get("1.0", tk.END).strip()

        if not recipient or not is_valid_email(recipient):
            messagebox.showwarning("Invalid Email", "Please enter a valid email address.")
            return
        if not message:
            messagebox.showwarning("Error", "Message field cannot be empty.")
            return

        if send_email(recipient, message):
            messagebox.showinfo("Success", f"Message sent to {recipient}!")
            clear_widgets(root, "static/background.jpg")
            dialog.destroy()
        else:
            messagebox.showerror("Error", "Failed to send the message. Try again.")

    # Send Button
    tk.Button(dialog, text="Send", command=send_dm, font=("Arial", 12), bg="green", fg="white").pack(pady=20)

def create_transparent_button(parent, text, command, x, y, width, height, bg_color="lightblue", fg_color="white", font=("Arial", 14)):
    """
    Function to create an attractive transparent rectangular button.
    """
    canvas = tk.Canvas(parent, width=width, height=height, bd=0, highlightthickness=0, relief="flat", bg=parent["bg"])
    canvas.place(x=x, y=y)

    # Create transparent background rectangle
    canvas.create_rectangle(0, 0, width, height, fill=bg_color, outline=bg_color, stipple="gray50")

    # Add button text
    button = tk.Button(parent, text=text, command=command, font=font, bg=bg_color, fg=fg_color, borderwidth=0, highlightthickness=0, activebackground=bg_color, activeforeground=fg_color)
    button.place(x=x, y=y, width=width, height=height)

    return button

# Main Application
root = tk.Tk()
root.title("Merry Christmas 2025")
root.geometry("800x600")
root.resizable(False, False)

# Load background image
try:
    background_image = Image.open("static/background.jpg")
    background_photo = ImageTk.PhotoImage(background_image.resize((800, 600)))
    bg_label = tk.Label(root, image=background_photo)
    bg_label.image = background_photo
    bg_label.place(relwidth=1, relheight=1)
except FileNotFoundError:
    messagebox.showerror("Error", "Background image not found!")
    root.destroy()
    exit()

# Add transparent rectangular button
create_transparent_button(
    root, "Send", open_message_dialog,
    x=350, y=500, width=120, height=50, bg_color="darkred", fg_color="white"
)

# Start the application
root.mainloop()
