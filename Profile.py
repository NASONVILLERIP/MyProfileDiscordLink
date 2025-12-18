import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class NetlifyDropboxUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Netlify Dropbox UI")
        self.geometry("500x600")
        self.configure(bg="#2c3e50")

        self.username = "Swiper"
        self.friends = ["Screamingcat", "Popcat", "Zen", "Foot_Licker", "W1NGZ"]
        self.languages = ["C++"]

        self.pfp_image = None
        self.pfp_path = None

        self.create_widgets()

    def create_widgets(self):
        # Username label
        user_label = tk.Label(self, text=f"User: {self.username}", font=("Helvetica", 18, "bold"), fg="white", bg="#2c3e50")
        user_label.pack(pady=15)

        # Profile picture frame
        pfp_frame = tk.Frame(self, bg="#34495e", bd=2, relief="ridge")
        pfp_frame.pack(pady=10)

        self.pfp_canvas = tk.Canvas(pfp_frame, width=150, height=150, bg="#ecf0f1", bd=0, highlightthickness=0)
        self.pfp_canvas.pack()

        # Default pfp placeholder
        self.load_default_pfp()

        # Button to choose pfp
        choose_pfp_btn = tk.Button(self, text="Choose Profile Picture", command=self.choose_pfp, bg="#2980b9", fg="white", font=("Helvetica", 12, "bold"), relief="flat", padx=10, pady=5)
        choose_pfp_btn.pack(pady=10)

        # Friends list
        friends_label = tk.Label(self, text="Friends:", font=("Helvetica", 16, "bold"), fg="white", bg="#2c3e50")
        friends_label.pack(pady=(20, 5))

        friends_frame = tk.Frame(self, bg="#34495e", bd=2, relief="ridge")
        friends_frame.pack(pady=5, fill="x", padx=50)

        for friend in self.friends:
            f_label = tk.Label(friends_frame, text=friend, font=("Helvetica", 14), fg="#ecf0f1", bg="#34495e")
            f_label.pack(anchor="w", padx=10, pady=2)

        # Languages scripted on
        lang_label = tk.Label(self, text="Languages I script on:", font=("Helvetica", 16, "bold"), fg="white", bg="#2c3e50")
        lang_label.pack(pady=(20, 5))

        lang_frame = tk.Frame(self, bg="#34495e", bd=2, relief="ridge")
        lang_frame.pack(pady=5, fill="x", padx=50)

        for lang in self.languages:
            l_label = tk.Label(lang_frame, text=lang, font=("Helvetica", 14), fg="#ecf0f1", bg="#34495e")
            l_label.pack(anchor="w", padx=10, pady=2)

        # Dropbox upload simulation button
        upload_btn = tk.Button(self, text="Upload to Dropbox (Simulated)", command=self.simulate_upload, bg="#27ae60", fg="white", font=("Helvetica", 14, "bold"), relief="flat", padx=10, pady=8)
        upload_btn.pack(pady=30)

    def load_default_pfp(self):
        # Create a simple placeholder image (gray circle)
        size = (150, 150)
        img = Image.new("RGBA", size, (200, 200, 200, 255))
        mask = Image.new("L", size, 0)
        mask_draw = Image.new("L", size, 0)
        from PIL import ImageDraw
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, size[0], size[1]), fill=255)
        img.putalpha(mask)
        self.pfp_image = ImageTk.PhotoImage(img)
        self.pfp_canvas.create_image(75, 75, image=self.pfp_image)

    def choose_pfp(self):
        filetypes = [("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")]
        path = filedialog.askopenfilename(title="Choose Profile Picture", filetypes=filetypes)
        if path:
            try:
                img = Image.open(path)
                img = img.convert("RGBA")
                img = img.resize((150, 150), Image.ANTIALIAS)
                # Make circle mask
                mask = Image.new("L", (150, 150), 0)
                draw = ImageDraw.Draw(mask)
                draw.ellipse((0, 0, 150, 150), fill=255)
                img.putalpha(mask)
                self.pfp_image = ImageTk.PhotoImage(img)
                self.pfp_canvas.delete("all")
                self.pfp_canvas.create_image(75, 75, image=self.pfp_image)
                self.pfp_path = path
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load image:\n{e}")

    def simulate_upload(self):
        msg = f"Uploading profile for {self.username} to Dropbox...\n"
        if self.pfp_path:
            msg += f"Profile picture: {self.pfp_path}\n"
        else:
            msg += "Profile picture: Default\n"
        msg += f"Friends: {', '.join(self.friends)}\n"
        msg += f"Languages: {', '.join(self.languages)}\n"
        msg += "\nUpload simulated successfully!"
        messagebox.showinfo("Dropbox Upload", msg)

if __name__ == "__main__":
    app = NetlifyDropboxUI()
    app.mainloop()
