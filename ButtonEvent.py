import tkinter as tk
from tkinter import messagebox
def show_messagebox():
    result = messagebox.askokcancel("確認", "このパソコンはウイルスに感染しています")
    if result:
        print("OK が選択されました")
    else:
        print("キャンセルが選択されました")