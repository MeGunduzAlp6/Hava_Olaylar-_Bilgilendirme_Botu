#🌍 Discord Hava Durumu Bilgilendirme Botu

Bu proje, **discord.py** kütüphanesi ve **OpenWeatherMap API** altyapısı kullanılarak geliştirilmiş, sunucunuzdaki kullanıcıların dünya genelindeki anlık hava durumu verilerine kolayca erişmesini sağlayan modern bir Discord botudur.

## ✨ Özellikler

* 🗺️ **Dünya Genelinde Sorgulama:** Sadece Türkiye değil, globaldeki tüm şehirlerin verilerini saniyeler içinde getirir.
* 🇹🇷 **Türkçe Dil Desteği:** Hava olaylarının açıklamalarını tamamen Türkçe ve anlaşılır şekilde sunar.
* 🛠️ **Gelişmiş Hata Kontrolü:** Geçersiz veya hatalı yazılan şehir isimlerinde botun çökmesini engeller ve kullanıcıyı bilgilendirir.
* 🔒 **Güvenli Altyapı:** Bot tokeni gibi hassas verileri ana kod dosyasından bağımsız bir şekilde saklar.

## 🚀 Komutlar

Botun varsayılan komut ön eki (prefix) `!` olarak ayarlanmıştır.

| Komut | Açıklama | Örnek Kullanım |
| :--- | :--- | :--- |
| `!start` | Botu başlatır ve bir selamlama mesajı gönderir. | `!start` |
| `!hava <şehir>` | Girilen şehrin anlık sıcaklık, nem ve hava durumunu listeler. | `!hava Antalya` |
| `!info` | Botta aktif olarak çalışan tüm komutları listeler. | `!info` |
| `!yardim` | Botun kullanımı ve sorun giderme adımları hakkında rehber açar. | `!yardim` |

## 🛠️ Kurulum ve Çalıştırma

Projeyi yerel bilgisayarınızda veya bir sunucuda (VDS) çalıştırmak için aşağıdaki adımları sırasıyla takip edin:

### 1. Gereksinimlerin Yüklenmesi
Sisteminizde Python 3.8 veya üzeri bir sürümün yüklü olduğundan emin olun. Ardından gerekli kütüphaneleri terminal üzerinden yükleyin:

```bash
pip install discord.py requests
```

### 2. Yapılandırma Dosyası (`config.py`)
Güvenliğiniz için bot dosyanızla aynı dizinde `config.py` adında bir dosya oluşturun ve içerisine [Discord Developer Portal](https://discord.com)'dan aldığınız bot tokenini ekleyin:

```python
# config.py içeriği
TOKEN = "YOUR_DISCORD_BOT_TOKEN_HERE"
```

### 3. Botun Başlatılması
Gereksinimler yüklendikten ve yapılandırma tamamlandıktan sonra ana kod dosyanızı çalıştırabilirsiniz:

```bash
python main.py
```
Terminalde `[Bot_Adı] olarak giris yapildi ✅` yazısını gördüğünüzde botunuz sunucularda aktif hale gelmiş olacaktır.

## 📦 Teknolojiler
* [Python](https://python.org) - Programlama Dili
* [Discord.py](https://readthedocs.io) - Discord API Wrapper
* [OpenWeatherMap API](https://openweathermap.org) - Hava Durumu Sağlayıcısı
