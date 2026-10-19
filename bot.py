import discord  # Discord API'si ile iletişim kurmak için ana kütüphane
from discord.ext import commands  # Bot komutlarını (commands.Bot) kolayca yönetmek için uzantı kütüphanesi
import requests  # Hava durumu API'sine HTTP istekleri (Get) atıp veri çekmek için kütüphane
from config import TOKEN  # Bot tokenini güvenlik amacıyla 'config.py' dosyasından içe aktarıyoruz

# Botun Discord sunucularındaki verilere (mesajlar vb.) erişebilmesi için gerekli izin ayarları (Intents)
intents = discord.Intents.default()
intents.message_content = True  # Kullanıcıların yazdığı mesaj içeriklerini okuma izni (Zorunludur)

# Belirlenen prefix (!) ve izinler (intents) ile bot nesnesini oluşturuyoruz
bot = commands.Bot(command_prefix="!", intents=intents)

# 🔑 OpenWeatherMap platformundan alınan benzersiz API anahtarı
OPENWEATHER_API_KEY = "YOUR_OPENWEATHER_API_KEY"

@bot.event
async def on_ready():
    """Bot başarıyla giriş yapıp Discord sunucularına bağlandığında tetiklenen fonksiyon."""
    print(f"{bot.user} olarak giris yapildi ✅")

@bot.command()
async def hava(ctx, *, sehir: str = None):
    """
    Belirtilen şehrin anlık hava durumunu OpenWeatherMap API'sinden çeken komut.
    Usage: !hava <şehir_adı>
    """
    # Kullanıcı şehir adı girmemişse nasıl kullanacağını hatırlatıyoruz
    if sehir is None:
        await ctx.send("⚠️ Örnek kullanım: `!hava İstanbul`")
        return

    # API istek URL'si (metric: Santigrat derece için, lang=tr: Türkçe sonuçlar için)
    url = f"https://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={OPENWEATHER_API_KEY}&units=metric&lang=tr"
    veri = requests.get(url).json()  # API'ye istek atıp gelen yanıtı Python sözlük (dict) yapısına çeviriyoruz

    # Eğer API "200" (Başarılı) kodu döndürmediyse şehir bulunamamış demektir
    if str(veri.get("cod")) != "200":
        await ctx.send(f"❌ '{sehir}' bulunamadı.")
        return

    # JSON verisinin içinden ihtiyacımız olan bilgileri değişkenlere atıyoruz
    sicaklik = veri["main"]["temp"]
    nem = veri["main"]["humidity"]
    durum = veri["weather"][0]["description"]  # Hava olayının metinsel açıklaması (örn: parçalı bulutlu)

    # Elde ettiğimiz bilgileri formatlayarak Discord kanalına gönderiyoruz
    await ctx.send(f"🌍 {veri['name']}\n🌡️ {sicaklik}°C\n💧 Nem: %{nem}\n☁️ {durum}")

@bot.command()
async def info(ctx):
    """Bot içindeki tüm komutların ne işe yaradığını listeleyen komut."""
    await ctx.send(
        "!hava: Bir Yerin Hava Durumunu Öğrenmenizi Sağlar\n"
        "!info: Bütün Komutları Gösterir\n"
        "!start: Botu Başlatır\n"
        "!yardim: Yardım gerekiyorsa bunu kullanın"
    )

@bot.command()
async def yardim(ctx): 
    """
    Botun kullanımı ve olası hataların çözümü hakkında rehberlik sunan yardım komutu.
    Not: Varsayılan 'help' komutuyla çakışmaması için ismi 'yardim' olarak belirlenmiştir.
    """
    mesaj = (
        "❓ **Hava Durumu Botu Yardım Merkezi** ❓\n\n"
        "Botu kullanırken sorun mu yaşıyorsunuz? İşte bilmeniz gerekenler:\n\n"
        "1️⃣ **Nasıl Sorgulama Yapılır?**\n"
        "Hava durumunu öğrenmek için `!hava` komutunun yanına bir şehir ismi yazmalısınız.\n"
        "Örn: `!hava Antalya` veya `!hava Londra`.\n\n"
        "2️⃣ **Bot Komutlara Cevap Vermiyor mu?**\n"
        "• Komutların başına ünlem (**!**) işareti koyduğunuzdan emin olun.\n"
        "• Şehir isimlerini doğru yazdığınızı kontrol edin.\n\n"
        "3️⃣ **Tüm Komutları Görmek İçin:**\n"
        "`!info` komutunu kullanarak botun sahip olduğu tüm yetenekleri anında listeleyebilirsiniz."
    )
    await ctx.send(mesaj)

@bot.command()
async def start(ctx):
    """Bot sunucuya ilk eklendiğinde veya başlatıldığında kullanılan selamlama komutu."""
    await ctx.send("Merhaba. Ben bir Dünya hava durumu botuyum. Denemek İçin `!hava` yazın. Tüm Komutlar İçin De `!info` diyin. Yardım istiyorsanız ise `!yardim` komutunu kullanabilirsiniz.")

# config.py içinden çekilen gizli token ile botu resmi olarak ayağa kaldırıyoruz
bot.run(TOKEN)
