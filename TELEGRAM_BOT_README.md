# 🤖 Telegram AGI Story Bot

بوت ذكاء اصطناعي متقدم يولد قصص إبداعية باستخدام نموذج TinyStories-1M

Advanced AI bot that generates creative stories using TinyStories-1M model

---

## 📋 المتطلبات / Requirements

### النظام / System Requirements:
- Python 3.8 أو أحدث / Python 3.8 or higher
- 4GB RAM (8GB موصى به / recommended)
- اتصال إنترنت / Internet connection
- (اختياري) GPU للأداء الأفضل / (Optional) GPU for better performance

### المكتبات / Python Libraries:
```bash
pip install -r requirements_telegram_bot.txt
```

أو / Or:
```bash
pip install python-telegram-bot transformers torch numpy requests
```

---

## 🚀 البدء السريع / Quick Start

### 1. تثبيت المكتبات / Install Dependencies:
```bash
pip install -r requirements_telegram_bot.txt
```

### 2. تشغيل البوت / Run the Bot:
```bash
python telegram_agi_bot.py
```

### 3. استخدام البوت / Use the Bot:
افتح التليجرام وابحث عن البوت أو استخدم الرابط:
Open Telegram and search for the bot or use the link:
```
https://t.me/WwAA3BOT444
```

---

## 📖 دليل الاستخدام / Usage Guide

### الأوامر / Commands:

#### `/start`
عرض رسالة الترحيب والمعلومات الأساسية
Show welcome message and basic information

#### `/help`
عرض دليل الاستخدام والنصائح
Show usage guide and tips

#### `/about`
معلومات عن البوت والمشروع
Information about the bot and project

#### `/status`
حالة النموذج والجهاز
Model and device status

### توليد القصص / Generate Stories:

ببساطة أرسل أي مطالبة والبوت سيولد قصة:
Simply send any prompt and the bot will generate a story:

**أمثلة / Examples:**
- "Once upon a time there was a brave knight"
- "في يوم من الأيام كان هناك ساحر قوي"
- "A mysterious forest with ancient trees"
- "قرية صغيرة بعيدة عن العالم"

---

## ⚙️ الإعدادات / Configuration

يمكنك تعديل الإعدادات في ملف `telegram_agi_bot.py`:

You can modify settings in `telegram_agi_bot.py`:

```python
# Model Configuration
MODEL_NAME = "roneneldan/TinyStories-1M"  # النموذج المستخدم
MAX_LENGTH = 150                          # الطول الأقصى للقصة
TEMPERATURE = 0.7                         # درجة الإبداعية (0-1)
TOP_P = 0.9                              # معامل التنويع
```

### شرح الإعدادات / Settings Explanation:

| الإعداد / Setting | الوصف / Description | النطاق / Range |
|---|---|---|
| `MAX_LENGTH` | الطول الأقصى للنص المولد / Max generated text length | 50-500 |
| `TEMPERATURE` | درجة الإبداعية (أعلى = أكثر إبداعاً) / Creativity level | 0.1-1.0 |
| `TOP_P` | معامل التنويع (أعلى = أكثر تنوعاً) / Diversity factor | 0.5-1.0 |

---

## 🔧 استكشاف الأخطاء / Troubleshooting

### المشكلة: "No module named 'telegram'"
**الحل / Solution:**
```bash
pip install python-telegram-bot
```

### المشكلة: "No module named 'transformers'"
**الحل / Solution:**
```bash
pip install transformers torch
```

### المشكلة: البوت لا يستجيب / Bot not responding
**الحل / Solution:**
1. تأكد من صحة Token البوت / Verify bot token is correct
2. تحقق من الاتصال بالإنترنت / Check internet connection
3. أعد تشغيل البوت / Restart the bot

### المشكلة: توليد القصص بطيء جداً / Story generation is very slow
**الحل / Solution:**
1. قلل `MAX_LENGTH` في الإعدادات / Reduce MAX_LENGTH in settings
2. استخدم GPU إذا توفر / Use GPU if available
3. تأكد من توفر الذاكرة / Ensure sufficient RAM

---

## 📊 معلومات النموذج / Model Information

### TinyStories-1M
- **الحجم / Size:** 1 مليون معامل / 1 Million parameters
- **اللغات / Languages:** متعدد اللغات / Multi-language
- **الاستخدام / Use:** توليد القصص / Story generation
- **الأداء / Performance:** سريع وفعال / Fast and efficient

---

## 🔗 الروابط المهمة / Important Links

- **GitHub Repository:** https://github.com/lwsh72462-design/500-AI-Agents-Projects
- **Telegram Channel:** https://t.me/+fOwCWbAJFME0ZGVk
- **Contact:** @WwAA3BOT444
- **AGI Blueprint Website:** https://agi-blueprint.manus.space

---

## 📝 أمثلة الاستخدام / Usage Examples

### مثال 1: قصة خيالية / Fantasy Story
```
المستخدم / User: "A wizard with magical powers"
البوت / Bot: يولد قصة عن ساحر بقوى سحرية
```

### مثال 2: قصة مغامرة / Adventure Story
```
المستخدم / User: "An explorer in a mysterious jungle"
البوت / Bot: يولد قصة عن مستكشف في غابة غامضة
```

### مثال 3: قصة خيال علمي / Sci-Fi Story
```
المستخدم / User: "A spaceship traveling through galaxies"
البوت / Bot: يولد قصة عن سفينة فضائية تسافر عبر المجرات
```

---

## 🎯 الميزات / Features

✅ توليد قصص إبداعية / Creative story generation
✅ دعم لغات متعددة / Multi-language support
✅ نموذج متقدم وفعال / Advanced and efficient model
✅ استجابة سريعة / Fast response
✅ واجهة سهلة الاستخدام / Easy-to-use interface
✅ معلومات تفصيلية / Detailed information
✅ معالجة الأخطاء / Error handling
✅ دعم GPU / GPU support

---

## 📈 الأداء / Performance

| المقياس / Metric | القيمة / Value |
|---|---|
| وقت التوليد / Generation Time | 5-15 ثانية / seconds |
| استهلاك الذاكرة / Memory Usage | 2-4 GB |
| استهلاك GPU / GPU Memory | 1-2 GB (if available) |
| عدد الطلبات المتزامنة / Concurrent Requests | 1 (sequential) |

---

## 🤝 المساهمة / Contributing

نرحب بالمساهمات والاقتراحات!
We welcome contributions and suggestions!

---

## 📄 الترخيص / License

هذا المشروع مفتوح المصدر
This project is open source

---

## 👨‍💻 الفريق / Team

**AGI Blueprint Team**
- **Contact:** @WwAA3BOT444
- **Project:** https://github.com/lwsh72462-design/500-AI-Agents-Projects

---

## 📞 الدعم / Support

للمساعدة والدعم، تواصل معنا على:
For help and support, contact us at:
- **Telegram:** @WwAA3BOT444
- **GitHub Issues:** https://github.com/lwsh72462-design/500-AI-Agents-Projects/issues

---

## ⚠️ ملاحظات مهمة / Important Notes

1. **الخصوصية / Privacy:** لا نحفظ بيانات المستخدمين / We don't store user data
2. **الاستخدام / Usage:** استخدم البوت بشكل مسؤول / Use the bot responsibly
3. **الأداء / Performance:** قد يكون التوليد بطيئاً على الأجهزة الضعيفة / Generation may be slow on weak devices
4. **الموارد / Resources:** يتطلب الاتصال بالإنترنت / Requires internet connection

---

**آخر تحديث / Last Updated:** 2026-03-13
**الإصدار / Version:** 1.0.0

✨ **استمتع باستخدام بوت AGI Story Bot!** / Enjoy using AGI Story Bot! ✨
