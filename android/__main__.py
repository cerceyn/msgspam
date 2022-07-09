from time import sleep
from android import *
try:
    from telethon.tl.functions.messages import AddChatUserRequest
except:
    pip_("telethon")
finally:
    from telethon.tl.functions.messages import AddChatUserRequest


from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
from .events import register as clabtetikleyici 
from telethon.sessions import StringSession
from telethon import TelegramClient
from traceback import format_exc
from random import choice
import asyncio, string


userbot=None
uyecalmaaraligi=8
async def hesabagir ():
    bilgi("Şimdi hesabını tanımam lazım.")
    api_hash=0
    stringsession=None
    api_id = soru("Hesabınızın API ID'i veya CLab-AccountToken:")
    if api_id.startswith("CLab"):
        api_id, api_hash, stringsession = clabtoken(api_id)
        onemli("CLab-AccountToken algılandı!")
    else:
        try:
            int(api_id)
        except Exception:
            hata("🛑 API ID Hatalı ! 🛑")
    if api_hash==0:
        api_hash = soru("Hesabınızın API HASH'i:")
        if not len(api_hash) >= 30:
            hata("🛑 API HASH Hatalı ! 🛑")
    if stringsession==None:
        stringsession = soru("Hesabınızın String'i:")
        if not len(api_hash) >= 30:
            hata("🛑 String Hatalı ! 🛑")

    try:
        userbot = TelegramClient(
        StringSession(stringsession),
        api_id=api_id,
        api_hash=api_hash,
        lang_code="tr")
        onemli(api_hash + " için client oluşturuldu !")
    except Exception as e:
        hata(api_hash + f" için client oluşturulamadı ! 🛑 Hata: {str(e)}")

    return userbot
reklamtext="Dikkat! Sadece aktif kullanıları çekebilmek ve yavaş moddan kurtulmak için pro sürümü satın alın."
passs = "4387"
pro=False
islem=0

async def islemler():
    grupc = 1540252536
    try:await userbot(JoinChannelRequest(grupc))
    except:pass
    global islem
    grup = soru("Hangi grupla işlem yapılacak? ")
    try:
        grup = (await userbot.get_entity(grup)).id
        count = (await userbot.get_participants(grup, limit=1)).total
        bilgi(f"{grup} ögesinde {count} kişi bulundu! ")
    except Exception as e:
        if "deleted/deactivated" in str(e):
            hata("Telegram adminleri hesabınızı yasaklamış olduğundan işlem yapılamıyor")
        hata(e)
    islem=0;adet=0;sure=0
    msg=None
    while True:
        try:
            if islem==0:
                bilgi("1-Belirlediğim mesajı gönder\n2-Rastgele mesajlar gönder")
                islem = int(soru("Yapacağınız işlemin numarasını girin:"))
                if islem==1:
                    msg = str(soru("Göndereceğiniz mesajı yazın:"))
                if islem<0 or islem>2:raise Exception("Hatalı işlem")
                elif islem==2: msg="rand"
            if adet==0:
                adet = int(soru("Toplam kaç adet göndereyim:"))
                if adet<0 or adet>9999:raise Exception("Hatalı işlem")
            if sure==0:
                sure = int(soru("Mesajları kaç saniyede bir göndereyim:"))
                if sure<0 or sure>999:raise Exception("Hatalı işlem")
            break
        except:
            noadded("Hatalı işlem!")
            continue
    await spamla(grup,islem,adet,sure,msg)
    onemli("Tüm işlemler bitti. Teşekkürler...")

async def spamla(grup,islem,adet,sure,msg="None"):
    #print(grup," ",islem," ",adet," ",sure," ",msg)
    for i in range(adet):
        try:
            if islem==1:
                msg=msg
            elif islem==2 or msg=="rand":
                msg=str(get_random_string(choice(range(1,20))))
            await userbot.send_message(grup, msg)

        except Exception as e:
            noadded(f"Mesaj gönderilemedi... Hata: {str(e)}")
        sleep(sure)



async def main():
    global userbot, pro
    logo(True)
    #hata("Bot şuan bakımda!")
    #basarili("Yeniden tasarlanmış v3 karşınızda, elveda pyrogram!")
    onemli("Gruba mesaj spamlama")
    pro=login()
    if not pro:
        ads("Free sürüm! Yavaş Mod ve Reklamlar aktif!")
        ads("Free mod için bekleme odası! Kısa bir süre sonra başlayacak!",15)
    else: ads("Premium için teşekkürler !")
    #eval(compile(base64.b64decode(myscript()),'<string>','exec'))
    userbot = await hesabagir()
    a = True
    while a:
        try: userbot = await conn(userbot);await islemler()
        except Exception as e:
            if "deleted/deactivated" in str(e):
                hata("Telegram adminleri hesabınızı yasaklamış olduğundan işlem yapılamıyor")
            noadded("Bot bir hata ile karşılaştı: \n" + format_exc())
        finally:
            userbot= await disconn(userbot)
            cevap= soru("Kod tekrar yürütülsün mü? (y/n)")
            if cevap == "n":
                a = False
                hata("Güle Güle !")
            else:
                continue


async def conn(userbot):
    try: await userbot.connect()
    except Exception as e:
        try: await userbot.disconnect();await userbot.connect()
        except:
            if "deleted/deactivated" in str(e):
                hata("Telegram adminleri hesabınızı yasaklamış olduğundan işlem yapılamıyor")
            hata("Bu hesaba giremiyorum! Hata: "+ str(e))
    return userbot 
async def disconn(userbot):
    try: await userbot.disconnect()
    except: pass
    return userbot 

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try: loop.run_until_complete(main())
    except KeyboardInterrupt: loop.run_until_complete(disconn(userbot))