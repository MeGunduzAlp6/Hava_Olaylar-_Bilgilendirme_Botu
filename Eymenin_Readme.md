# 🌍 Discord Hava Durumu Botu

Bu proje, Python kullanılarak geliştirilmiş, Discord sunucularınız için anlık hava durumu bilgilerini sunan kullanışlı ve şık bir Discord botudur. OpenWeatherMap API'sini kullanarak dünyanın herhangi bir şehrindeki güncel hava durumu verilerini çeker ve kullanıcıya şık bir mesaj (Embed) formatında sunar.

## ✨ Özellikler

*   **Gerçek Zamanlı Veri:** OpenWeatherMap API sayesinde anlık ve doğru hava durumu verileri.
*   **Detaylı Bilgilendirme:** Sıcaklık, hissedilen sıcaklık, nem oranı ve rüzgar hızı gibi detayları gösterir.
*   **Canlı Harita Entegrasyonu:** Sorgulanan şehrin koordinatlarına göre dinamik bir Ventusky radar linki oluşturur.
*   **Kullanıcı Dostu Arayüz:** Gelen verileri Discord Embed mesajları ile görsel açıdan zengin bir şekilde sunar.
*   **Türkçe Dil Desteği:** Hava durumu açıklamaları tamamen Türkçedir.

## 🛠️ Kullanılan Teknolojiler ve Kütüphaneler

*   **Python 3.8+**
*   `discord.py` (Discord API ile iletişim için)
*   `requests` (Web API'lerinden veri çekmek için)

## 🚀 Kurulum Adımları

Botu kendi bilgisayarınızda veya sunucunuzda çalıştırmak için aşağıdaki adımları izleyin:

### 1. Gerekli Kütüphaneleri Yükleyin
Öncelikle bilgisayarınızda Python'ın kurulu olduğundan emin olun. Daha sonra terminal veya komut satırını açarak gerekli kütüphaneleri indirin:

```bash
pip install discord requests
```

### 2. API Anahtarlarını Alın
Botun çalışması için iki farklı şifreye (Token/API Key) ihtiyacınız var:
*   **Discord Bot Token:** [Discord Developer Portal](https://discord.com/developers/applications)'a girerek yeni bir uygulama oluşturun ve bir Bot Token'ı alın. (Ayrıca "Message Content Intent" ayarını açmayı unutmayın).
*   **OpenWeatherMap API Key:** [OpenWeatherMap](https://openweathermap.org/) sitesine ücretsiz kayıt olarak bir API anahtarı edinin.

### 3. Ayarları Yapılandırın
Güvenlik nedeniyle Discord Bot Token'ınızı ana kodun içine yazmak yerine `config.py` adında yeni bir dosya oluşturun ve içine şu kodu ekleyin:
```python
TOKEN = "BURAYA_DISCORD_BOT_TOKENINIZI_YAZIN"
```

Ana kod dosyanızdaki (örn: `main.py`) şu kısmı bulun ve kendi OpenWeather API anahtarınızla değiştirin:
```python
OPENWEATHER_API_KEY = "BURAYA_KENDİ_OPENWEATHER_API_ANAHTARINIZI_YAZIN"
```

### 4. Botu Başlatın
Her şey hazır! Terminalden botunuzun bulunduğu klasöre gidin ve botu çalıştırın:
```bash
python main.py
```
*(Dosya adınız farklıysa `main.py` yerine kendi dosya adınızı yazın).*

## 📖 Komutlar ve Kullanım

Bot varsayılan olarak `!` ön ekini (prefix) kullanır.

| Komut | Açıklama | Örnek Kullanım |
| :--- | :--- | :--- |
| `!hava <şehir>` | Belirtilen şehrin güncel hava durumu detaylarını gösterir. | `!hava İstanbul` |
| `!yardim` | Botun kullanım rehberini ve yardım merkezini açar. | `!yardim` |
| `!info` | Botun sahip olduğu tüm komutların kısa bir listesini verir. | `!info` |
| `!start` | Botun kendini tanıttığı başlangıç mesajını gönderir. | `!start` |

## ⚠️ Önemli Uyarılar

*   **Güvenlik:** `config.py` dosyanızı ve API anahtarlarınızı asla GitHub gibi açık platformlarda paylaşmayın veya kimseye göndermeyin. Bu anahtarlar size özeldir.
*   **İsimlendirme:** Şehir isimlerini yazarken Türkçe karakterler kullanabilirsiniz (Örn: `İzmir`, `Çanakkale`). Eğer bot şehri bulamazsa yazım hatası olup olmadığını kontrol edin.

---
*Bu bot eğitim ve kişisel kullanım amacıyla geliştirilmiştir.*
