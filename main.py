import tkinter as tk
from tkinter import messagebox
import ButtonEvent 
import Parameters as Params
#準備の騎士(ここからループ)
root = tk.Tk()
#windowの名前を設定
root.title("OMTシステム")
#ウィンドウのサイズ設定
root.geometry(str(Params.WindowWidth)+"x"+str(Params.WindowHeight))
#ボタンが押された場合の処理

BackButton = tk.Button(root, text="先月",command=ButtonEvent.show_messagebox)
BackButton.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
#ここまでループ
root.mainloop()
