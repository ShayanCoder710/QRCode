import qrcode
import random
from PIL import ImageColor
import customtkinter as ctk
from tkinter import messagebox



app = ctk.CTk()
app.geometry("460x320")
app.title("QRCode Creator")
app.resizable(False , False)
ctk.set_appearance_mode("Light")


frame = ctk.CTkFrame(app , corner_radius = 6 , border_color = 'white' , border_width = 4)
frame.pack(pady = 10)
frame.configure(fg_color = "#dadada")


l = ctk.CTkLabel(frame , text = "QRCode Creator" , width = 410 ,  text_color = "#161616" , font = ("ubuntu" , 24))
l.pack(pady = 12)

url_e = ctk.CTkEntry(frame , placeholder_text = "Enter URL or text" , font = ("ubuntu" , 21) , justify = "center" , width = 360 , height = 42)
url_e.pack(pady = 10)

cf_e = ctk.CTkEntry(frame , placeholder_text = "foreground color" , font = ("ubuntu" , 21) , justify = "center" , width = 360 , height = 42)
cf_e.pack(pady = 10)

cb_e = ctk.CTkEntry(frame , placeholder_text = "background color" , font = ("ubuntu" , 21) , justify = "center" , width = 360 , height = 42)
cb_e.pack(pady = 10)

def check_make():
    url = url_e.get().strip()
    cf = cf_e.get().strip()
    cb = cb_e.get().strip()

    try:
        ImageColor.getrgb(cf)
        ImageColor.getrgb(cb)
    except:
        messagebox.showerror("Error" , "Invalid color!")

    if cf == cb:
        messagebox.showerror("Error" , "Foreground color = Background color = Error")
    else:
        qr = qrcode.QRCode(version = 1 , box_size = 10 , border = 5)
        qr.add_data(url)
        qr.make(fit = True)
        fn = random.randint(1000,100000)
        img = qr.make_image(fill_color = cf , back_color = cb)
        img.save(f"qrcode_{fn}.png")
        messagebox.showinfo("QRCode Saved" , f"QRCode was made successfully by name 'qrcode{fn}.png'")
        url_e.delete(0 , "end")
        cf_e.delete(0 , "end")
        cb_e.delete(0 , "end")
        

btn = ctk.CTkButton(frame , width = 370 , height = 45 , text = "Make QRCode" , font = ("ubuntu" , 24) , text_color = "#1D1D1D" , fg_color = "#bdbdbd", hover_color = "#d1d1d1" , command = check_make) 
btn.pack(pady = 10)
    


app.mainloop()
