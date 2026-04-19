import qrcode
import random
from colorama import Fore , Back , Style
from PIL import ImageColor

while True:
    
    url = input(f"[To Exit 'exit']\n{Fore.LIGHTBLUE_EX}Enter URL or text: {Style.RESET_ALL}").strip()
    
    if url == "exit":
        exit()
        
    cf = input(f"{Fore.GREEN}foreground color: {Style.RESET_ALL}").strip()
    cb = input(f"{Fore.YELLOW}background color: {Style.RESET_ALL}").strip()
    try:
        ImageColor.getrgb(cf)
        ImageColor.getrgb(cb)
    except:
        print(f"{Fore.RED}Invalid color!{Style.RESET_ALL}")
        continue
    if cf == cb:
        print(f"{Fore.RED}Foreground color = Background color = Error{Style.RESET_ALL}")
        continue

    qr = qrcode.QRCode(version = 1 , box_size = 10 , border = 5)
    qr.add_data(url)
    qr.make(fit = True)

    fn = random.randint(1000,100000)
    img = qr.make_image(fill_color = cf , back_color = cb)
    img.save(f"qrcode_{fn}.png")

    print(f"{Fore.GREEN}qrcode{fn}.png saved.{Style.RESET_ALL}")
