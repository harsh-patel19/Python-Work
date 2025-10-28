import os
import tkinter as tk
from tkinter import messagebox

# Folder to save posts
POST_FOLDER = "posts"

def save_post():
    name = entry_name.get().strip()
    title = entry_title.get().strip()
    content = text_content.get("1.0", tk.END).strip()

    if not name or not title or not content:
        messagebox.showwarning("Warning", "Please fill all fields!")
        return

    # Create folder if not exist
    if not os.path.exists(POST_FOLDER):
        os.makedirs(POST_FOLDER)

    # Create safe filename
    filename = f"{name.replace(' ', '_')}_{title.replace(' ', '_')}.txt"
    filepath = os.path.join(POST_FOLDER, filename)

    # Save post
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"Author: {name}\n")
            f.write(f"Title: {title}\n\n")
            f.write(content)
        messagebox.showinfo("Saved", f"Post saved successfully as {filename}")
        load_posts()
        entry_title.delete(0, tk.END)
        text_content.delete("1.0", tk.END)
    except Exception as e:
        messagebox.showerror("Error", f"Could not save file: {e}")

def load_posts():
    listbox_posts.delete(0, tk.END)
    if os.path.exists(POST_FOLDER):
        for file in os.listdir(POST_FOLDER):
            if file.endswith(".txt"):
                listbox_posts.insert(tk.END, file)

def view_post():
    selected = listbox_posts.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Select a post to view!")
        return

    filename = listbox_posts.get(selected[0])
    filepath = os.path.join(POST_FOLDER, filename)

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        text_preview.config(state="normal")
        text_preview.delete("1.0", tk.END)
        text_preview.insert(tk.END, content)
        text_preview.config(state="disabled")
    except Exception as e:
        messagebox.showerror("Error", f"Could not read file: {e}")

# ---------------- UI Setup ----------------
root = tk.Tk()
root.title("Mini Blog (Simple Version)")
root.geometry("600x500")

tk.Label(root, text="Your Name:").pack(anchor="w", padx=10, pady=2)
entry_name = tk.Entry(root, width=40)
entry_name.pack(padx=10, pady=2)

tk.Label(root, text="Post Title:").pack(anchor="w", padx=10, pady=2)
entry_title = tk.Entry(root, width=40)
entry_title.pack(padx=10, pady=2)

tk.Label(root, text="Content:").pack(anchor="w", padx=10, pady=2)
text_content = tk.Text(root, height=10, width=70)
text_content.pack(padx=10, pady=5)

tk.Button(root, text="Save Post", command=save_post).pack(pady=5)

tk.Label(root, text="Saved Posts:").pack(anchor="w", padx=10, pady=2)
listbox_posts = tk.Listbox(root, width=50)
listbox_posts.pack(padx=10, pady=2)
tk.Button(root, text="View Selected Post", command=view_post).pack(pady=5)

tk.Label(root, text="Post Preview:").pack(anchor="w", padx=10, pady=2)
text_preview = tk.Text(root, height=10, width=70, state="disabled")
text_preview.pack(padx=10, pady=5)

# Load existing posts on start
load_posts()

root.mainloop()
