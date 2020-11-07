import requests, wget, sys, platform, os
from bs4 import BeautifulSoup

class Automation:
    def __init__(self, anonfile_link, download=False):
        self.link = anonfile_link
        self.download_status = download
    def getLink(self):
        if not str(self.link).startswith("http"):
            link = str("http://" + self.link)
        else:
            link = str(self.link)
        req = requests.get(link)
        icerik = req.content
        soup = BeautifulSoup(icerik, "html.parser")
        for eleman in soup.find_all("a"):
            links = eleman.get("href")
            if str(links).startswith("https://cdn") or str(links).startswith("http://cdn"):
                real = str(links)
            else:
                pass
        return real
    def download(self):
        if self.download_status == True:
            link = self.getLink()
            if not str(link).startswith("http"):
                url = str("http://" + link)
            else:
                url = str(link)
            info = {
                "file_name": wget.detect_filename(url=url)
            }
            print(f"[*] {info['file_name']} isimli dosya indiriliyor...")
            wget.download(url=url)
            print(f"\n[+] {info['file_name']} isimli dosya indirildi !")

def par(sayi, msg):
    print(f"[ {sayi} ] {msg}")

def banner():
    ban = """
           █████▒▒█████   █    ██  ██▀███      ██░ ██  ▄▄▄       ▄████▄   ██ ▄█▀▓█████  ██▀███  ▒███████▒
         ▓██   ▒▒██▒  ██▒ ██  ▓██▒▓██ ▒ ██▒   ▓██░ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒▒ ▒ ▒ ▄▀░
         ▒████ ░▒██░  ██▒▓██  ▒██░▓██ ░▄█ ▒   ▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒░ ▒ ▄▀▒░ 
         ░▓█▒  ░▒██   ██░▓▓█  ░██░▒██▀▀█▄     ░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄    ▄▀▒   ░
         ░▒█░   ░ ████▓▒░▒▒█████▓ ░██▓ ▒██▒   ░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒▒███████▒
          ▒ ░   ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░    ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░░▒▒ ▓░▒░▒
          ░       ░ ▒ ▒░ ░░▒░ ░ ░   ░▒ ░ ▒░    ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░░░▒ ▒ ░ ▒
          ░ ░   ░ ░ ░ ▒   ░░░ ░ ░   ░░   ░     ░  ░░ ░  ░   ▒   ░        ░ ░░ ░    ░     ░░   ░ ░ ░ ░ ░ ░
                    ░ ░     ░        ░         ░  ░  ░      ░  ░░ ░      ░  ░      ░  ░   ░       ░ ░    
                                                                ░                               ░        
                                @@@   @@@       @@@@@@@   @@@@@@   @@@@@@@   
                               @@@@   @@@       @@@@@@@@  @@@@@@@  @@@@@@@@  
                              @@!@!   @@!       @@!  @@@      @@@  @@!  @@@  
                             !@!!@!   !@!       !@!  @!@      @!@  !@!  @!@  
                            @!! @!!   @!!       @!@@!@!   @!@!!@   @!@!!@!   
                           !!!  !@!   !!!       !!@!!!    !!@!@!   !!@!@!    
                           :!!:!:!!:  !!:       !!:           !!:  !!: :!!   
                           !:::!!:::   :!:      :!:           :!:  :!:  !:!  
                                :::    :: ::::   ::       :: ::::  ::   :::  
                                :::   : :: : :   :         : : :    :   : :  
    """
    return ban

if str(platform.system()).lower().startswith("win"):
    clear = lambda : os.system("cls")
else:
    clear = lambda : os.system("clear")

def main():
    print(banner())
    par(1, "İndirme Linkini Yakala.")
    par(2, "Dosyayı İndir.")
    print("\n")
    par(0, "Çıkış.")
    print("\n")
    try:
        choice = int(input("[?] Seçim: "))
    except:
        print("[!] Lütfen bir doğal sayı girin.")
        sys.exit()
    url = input("[?] URL: ")
    if choice == 1:
        clear()
        bot = Automation(url)
        print("\n")
        print(bot.getLink())
        print("\n")
    elif choice == 2:
        clear()
        print("\n")
        bot = Automation(url, download=True)
        bot.download()
        print("\n")
    elif choice == 0:
        print("[*] Görüşmek üzere...")
        sys.exit()
    else:
        print("[!] Lütfen geçerli bir işlem seçin.")
        sys.exit()

if __name__ == '__main__':
    main()