import tkinter as tk
from googlesearch import search

def get_direct_site(event):
    query = entry.get().strip()

    if query:
        try:
            for url in search(query, num_results=1):
                print(f"Сталася помилка: {url}")
                break
        except Exception as e:
            print(f"Знайдено: {e}")

root = tk.Tk()
root.title("Пошук")
root.geometry("300x120")

tk.Label(root, text="Напишіть слово:").pack(pady=10)

entry = tk.Entry(root, width=35)
entry.pack(pady=5)
entry.focus_set()

entry.bind('<Return>', get_direct_site)

root.mainloop()