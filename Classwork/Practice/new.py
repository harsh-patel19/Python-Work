import os
import tkinter as tk
from tkinter import messagebox, filedialog


class MiniBlogApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MiniBlog - Desktop Blog App")
        self.root.geometry("600x500")

        # Create a folder to save posts
        self.posts_dir = "posts"
        os.makedirs(self.posts_dir, exist_ok=True)

        # Widgets
        self.create_widgets()
        self.load_posts()

    def create_widgets(self):
        # --- Input Fields ---
        tk.Label(self.root, text="Your Name:").pack(anchor="w", padx=10, pady=2)
        self.name_entry = tk.Entry(self.root, width=40)
        self.name_entry.pack(padx=10, pady=2)

        tk.Label(self.root, text="Post Title:").pack(anchor="w", padx=10, pady=2)
        self.title_entry = tk.Entry(self.root, width=40)
        self.title_entry.pack(padx=10, pady=2)

        tk.Label(self.root, text="Post Content:").pack(anchor="w", padx=10, pady=2)
        self.content_text = tk.Text(self.root, height=10, width=60)
        self.content_text.pack(padx=10, pady=5)

        # Buttons
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Save Post", command=self.save_post).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Clear Fields", command=self.clear_fields).grid(row=0, column=1, padx=5)

        # --- View Posts Section ---
        tk.Label(self.root, text="Saved Posts:").pack(anchor="w", padx=10, pady=5)
        self.post_listbox = tk.Listbox(self.root, width=50)
        self.post_listbox.pack(padx=10, pady=5)
        self.post_listbox.bind("<<ListboxSelect>>", self.view_post)

        self.view_text = tk.Text(self.root, height=10, width=60, state="disabled")
        self.view_text.pack(padx=10, pady=5)

    def save_post(self):
        name = self.name_entry.get().strip()
        title = self.title_entry.get().strip()
        content = self.content_text.get("1.0", tk.END).strip()

        if not name or not title or not content:
            messagebox.showerror("Error", "All fields must be filled!")
            return

        # Create safe filename
        safe_name = "".join(c for c in name if c.isalnum() or c in ("_", "-"))
        safe_title = "".join(c for c in title if c.isalnum() or c in ("_", "-"))
        filename = f"{safe_name}_{safe_title}.txt"
        filepath = os.path.join(self.posts_dir, filename)

        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"Author: {name}\n")
                f.write(f"Title: {title}\n\n")
                f.write(content)
            messagebox.showinfo("Success", "Post saved successfully!")
            self.clear_fields()
            self.load_posts()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save post: {e}")

    def load_posts(self):
        """Load all saved posts into listbox"""
        self.post_listbox.delete(0, tk.END)
        try:
            for file in os.listdir(self.posts_dir):
                if file.endswith(".txt"):
                    self.post_listbox.insert(tk.END, file)
        except FileNotFoundError:
            pass

    def view_post(self, event):
        """View selected post in the text widget"""
        selection = self.post_listbox.curselection()
        if not selection:
            return
        filename = self.post_listbox.get(selection[0])
        filepath = os.path.join(self.posts_dir, filename)

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            self.view_text.config(state="normal")
            self.view_text.delete("1.0", tk.END)
            self.view_text.insert(tk.END, content)
            self.view_text.config(state="disabled")
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found!")

    def clear_fields(self):
        """Clear input fields"""
        self.name_entry.delete(0, tk.END)
        self.title_entry.delete(0, tk.END)
        self.content_text.delete("1.0", tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = MiniBlogApp(root)
    root.mainloop()
