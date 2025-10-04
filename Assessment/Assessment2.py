import os
import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk


# --------- Data Classes ----------
class User:
    def __init__(self, name):
        self.name = name.strip()


class Post:
    def __init__(self, user: User, title: str, content: str):
        self.user = user
        self.title = title.strip()
        self.content = content.strip()

    def filename(self):
        safe_name = self.user.name.replace(" ", "_")
        safe_title = self.title.replace(" ", "_")
        return f"{safe_name}_{safe_title}.txt"

    def save(self, folder="posts"):
        if not os.path.exists(folder):
            os.makedirs(folder)
        filepath = os.path.join(folder, self.filename())
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"Author: {self.user.name}\n")
                f.write(f"Title: {self.title}\n\n")
                f.write(self.content)
            return filepath
        except Exception as e:
            messagebox.showerror("Error", f"Could not save post: {e}")


# --------- Main App ----------
class MiniBlogApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MiniBlog App")
        self.root.geometry("600x500")

        # Input Section
        tk.Label(root, text="Your Name:").pack(anchor="w", padx=10, pady=2)
        self.entry_name = tk.Entry(root, width=40)
        self.entry_name.pack(padx=10, pady=2)

        tk.Label(root, text="Post Title:").pack(anchor="w", padx=10, pady=2)
        self.entry_title = tk.Entry(root, width=40)
        self.entry_title.pack(padx=10, pady=2)

        tk.Label(root, text="Content:").pack(anchor="w", padx=10, pady=2)
        self.text_content = tk.Text(root, height=10, width=70)
        self.text_content.pack(padx=10, pady=5)

        # Buttons
        tk.Button(root, text="Save Post", command=self.save_post).pack(pady=5)

        # Listbox for saved posts
        tk.Label(root, text="Saved Posts:").pack(anchor="w", padx=10, pady=2)
        self.listbox = tk.Listbox(root, width=50)
        self.listbox.pack(padx=10, pady=2)
        tk.Button(root, text="View Selected Post", command=self.view_post).pack(pady=5)

        # Output display
        tk.Label(root, text="Post Preview:").pack(anchor="w", padx=10, pady=2)
        self.text_preview = tk.Text(root, height=10, width=70, state="disabled")
        self.text_preview.pack(padx=10, pady=5)

        # Load saved posts
        self.load_posts()

    def save_post(self):
        name = self.entry_name.get().strip()
        title = self.entry_title.get().strip()
        content = self.text_content.get("1.0", tk.END).strip()

        if not name or not title or not content:
            messagebox.showwarning("Warning", "All fields are required!")
            return

        user = User(name)
        post = Post(user, title, content)
        filepath = post.save()

        if filepath:
            messagebox.showinfo("Success", f"Post saved as {filepath}")
            self.load_posts()
            self.entry_title.delete(0, tk.END)
            self.text_content.delete("1.0", tk.END)

    def load_posts(self):
        self.listbox.delete(0, tk.END)
        folder = "posts"
        if os.path.exists(folder):
            for file in os.listdir(folder):
                if file.endswith(".txt"):
                    self.listbox.insert(tk.END, file)

    def view_post(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a post to view.")
            return

        filename = self.listbox.get(selection[0])
        filepath = os.path.join("posts", filename)
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            self.text_preview.config(state="normal")
            self.text_preview.delete("1.0", tk.END)
            self.text_preview.insert(tk.END, content)
            self.text_preview.config(state="disabled")
        except FileNotFoundError:
            messagebox.showerror("Error", f"File {filename} not found.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not read file: {e}")


# --------- Run App ----------
if __name__ == "__main__":
    root = tk.Tk()
    app = MiniBlogApp(root)
    root.mainloop()
