from subprocess import PIPE, Popen
def pip_(module):
    onemli(f"installing {module} for cerceynlab")
    pip_cmd = ["pip", "install", f"{module}"]
    process = Popen(pip_cmd, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    return stdout
from time import sleep as antripp
from .clabtoken import CLabToken
try: 
    from rich.console import Console
    from rich.panel import Panel
except:
    pip_("rich")
finally:
    from rich.console import Console
    from rich.panel import Panel
import sys,random,string

console = Console()
def hata (text):
    console.print(Panel(f'[bold red]{text}[/]',width=70),justify="center")    
    sys.exit()
def myscript ():
    return "ZnJvbSByaWNoLmNvbnNvbGUgaW1wb3J0IENvbnNvbGUNCmZyb20gcmljaC5wYW5lbCBpbXBvcnQgUGFuZWwNCg0KaW1wb3J0IHN5cw0KY29uc29sZSA9IENvbnNvbGUoKQ0KZGVmIGJpbGdpICh0ZXh0KToNCiAgICBjb25zb2xlLnByaW50KFBhbmVsKGYnW2JsdWVde3RleHR9Wy9dJyx3aWR0aD03MCksanVzdGlmeT0iY2VudGVyIikgIA0KZGVmIHNvcnUgKHNvcnUpOg0KICAgIGNvbnNvbGUucHJpbnQoUGFuZWwoZidbYm9sZCB5ZWxsb3dde3NvcnV9Wy9dJyx3aWR0aD03MCksanVzdGlmeT0iY2VudGVyIikgICAgICAgICAgICAgICAgICAgICAgICAgDQogICAgcmV0dXJuIGNvbnNvbGUuaW5wdXQoZiJbYm9sZCB5ZWxsb3ddPj4gWy9dIikNCmRlZiBoYXRhICh0ZXh0KToNCiAgICBjb25zb2xlLnByaW50KFBhbmVsKGYnW2JvbGQgcmVkXXt0ZXh0fVsvXScsd2lkdGg9NzApLGp1c3RpZnk9ImNlbnRlciIpICAgIA0KICAgIHN5cy5leGl0KCkNCg0KYmlsZ2koIlBhc3N3b3JkIGRlY29kaW5nLi4uIikNCmRvZ3J1cGFzcz0gNjg5Nw0KICAgIA0Kc2lmcmUgPSBzb3J1KCJNZXJoYWJhISDFnmlmcmU6IikNCnRyeToNCiAgICBkb2dydXBhc3M9IGludChkb2dydXBhc3MpDQogICAgaWYgaW50KHNpZnJlKSAhPSBkb2dydXBhc3M6DQogICAgICAgIGhhdGEoIllhbmzEscWfIMWfaWZyZSIpDQpleGNlcHQgVHlwZUVycm9yOg0KICAgIGhhdGEoIllhbmzEscWfIMWfaWZyZSIpDQpleGNlcHQgRXhjZXB0aW9uIGFzIGU6DQogICAgaGF0YSgiSGF0YTogIitzdHIoZSkp"                 
def bilgi (text):
    console.print(Panel(f'[blue]{text}[/]',width=70),justify="center")  
def clabtoken(text,coz=True):
    data = [1, 2, 3, 4, 5]
    ktext=None
    key=None
    with console.status("[bold blue] Clabtoken İşlemi Sürüyor...") as status:
        while data:
            num = data.pop(0)
            antripp(2)
            if num==1:
                console.log(f"[green] Şifrelenmiş keyler ayrıştırılıyor...[/green]")
                try:
                    ktext=text.split('&&')[1]
                    key=text.split('&&')[2]
                except IndexError:
                    hata("Bu bir CLab-AccountToken değil!")
            elif num==2:
                test_crpt = CLabToken()
                console.log(f"[green]Token nesnesi oluşturuldu![/green]")
            elif num==3 and coz==False:
                test_enctext = test_crpt.yap(ktext, key)
                console.log(f"[green]Token Şifreleniyor.[/green]")
                antripp(2)
                test_enc_text = f"CLab&&{test_enctext}&&{key}"
                console.log(f"[green]Token Formatı Ayarlandı![/green]")
            elif num==4 and coz:
                console.log(f"[green]Token çözülüyor..[/green]")
                test_dec_text = test_crpt.coz(ktext, key)
                console.log(f"[green]Bilgiler ayrıştırılıyor...[/green]")
                antripp(2)
                api_id = test_dec_text.split("|")[0]
                api_hash = test_dec_text.split("|")[1]
                string = test_dec_text.split("|")[2]
            elif num==5:
                if not coz:
                    console.log(f"[green]Token oluşturma işlemi başarılı![/green]")
                    return test_enc_text
                else:
                    console.log(f"[green]Token çözme işlemi başarılı![/green]")
                    return api_id, api_hash, string 

    try:
        ss = text.split('|')
        if len(ss[1]) <29:
            hata("Bu bir CLab-AccountToken değil!")
        return ss[2], ss[1], ss[3]
    except IndexError:
        hata("Bu bir CLab-AccountToken değil!")
    return None, None, None
def login():
    bilgi("Password decoding...")
    dogrupass= [6897,999]
    
    sifre = soru("Merhaba! Şifre:")
    try:
        sifre = int(sifre)
        if sifre not in dogrupass:
            hata("Yanlış şifre")
        if sifre == dogrupass[1]:
            return True
        else:return False
    except TypeError:
        hata("Yanlış şifre")
    except Exception as e:
        hata("Hata: "+str(e))
def passed (text):
    console.print(Panel(f'[yellow]{text}[/]',width=70),justify="center") 
def noadded (text):
    console.print(Panel(f'[red]{text}[/]',width=70),justify="center")  
def basarili (text):
    console.print(Panel(f'[bold green] {text}[/]',width=70),justify="center")                         
def onemli (text):
    console.print(Panel(f'[bold cyan]{text}[/]',width=70),justify="center")      
def ads (text,time=5):
   console.print(Panel(f'[green]{text}[/]',width=70),justify="center")     
   antripp(time)        
def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    bilgi(f"Rastgele üretilen {length} uzunluğundaki mesaj: {result_str}")
    return result_str   
def soru (soru):
    console.print(Panel(f'[bold yellow]{soru}[/]',width=70),justify="center")                         
    return console.input(f"[bold yellow]>> [/]")
def logo (satirbırak=False):
    text = "█▀▀ █▀▀ █▀█ █▀▀ █▀▀ █▄█ █▄░█\n█▄▄ ██▄ █▀▄ █▄▄ ██▄ ░█░ █░▀█\n\n█░░ ▄▀█ █▄▄\n█▄▄ █▀█ █▄█"
    if satirbırak:
        for i in range(25):
            console.print("\n")
    console.print(Panel(f'[bold cyan]{text}[/]',width=90),justify="center")
