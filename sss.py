import tkinter

import tkinter as tk
r = tk.Tk()
r.title('Counting Seconds')
r.geometry("720x600")
button = tk.Button(r, text='Stop', width=25, command=r.destroy)
button.pack()
r.mainloop()
