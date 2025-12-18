import tkinter as tk
from tkinter import filedialog, messagebox

# List of friends
friends = ["Screamingcat", "Popcat", "Zen", "Foot_Licker", "W1NGZ"]

class ProfileApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Netlify Dropbox Profile")
        self.root.geometry("400x600")
        self.pfp_path = ""

        # User Info Frame
        user_frame = tk.Frame(root)
        user_frame.pack(pady=10)

        # Username Label
        self.username = "Swiper"
        tk.Label(user_frame, text=f"Username: {self.username}", font=("Arial", 14)).pack()

        # Profile picture chooser
        self.pfp_label = tk.Label(user_frame, text="Profile Picture: None", font=("Arial", 12))
        self.pfp_label.pack(pady=5)
        tk.Button(user_frame, text="Choose Profile Picture", command=self.choose_pfp).pack()

        # Friends List
        friends_frame = tk.LabelFrame(root, text="Friends", padx=10, pady=10)
        friends_frame.pack(pady=10, fill="both", expand=True)
        self.friends_listbox = tk.Listbox(friends_frame)
        for friend in friends:
            self.friends_listbox.insert(tk.END, friend)
        self.friends_listbox.pack(fill="both", expand=True)

        # Scripts section
        scripts_frame = tk.LabelFrame(root, text="Scripts", padx=10, pady=10)
        scripts_frame.pack(pady=10, fill="both", expand=True)

        # List of scripts
        self.scripts = ["C++"]
        self.scripts_listbox = tk.Listbox(scripts_frame)
        for script in self.scripts:
            self.scripts_listbox.insert(tk.END, script)
        self.scripts_listbox.pack(fill="both", expand=True)

        # Add Script Button
        tk.Button(scripts_frame, text="Add Script", command=self.add_script).pack(pady=5)

    def choose_pfp(self):
        path = filedialog.askopenfilename(title="Select Profile Picture",
                                          filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
        if path:
            self.pfp_path = path
            self.pfp_label.config(text=f"Profile Picture: {path.split('/')[-1]}")

    def add_script(self):
        # For simplicity, adding a fixed script type
        new_script = "Python"
        self.scripts.append(new_script)
        self.scripts_listbox.insert(tk.END, new_script)
        messagebox.showinfo("Script Added", f"Added {new_script} script!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ProfileApp(root)
    root.mainloop()
