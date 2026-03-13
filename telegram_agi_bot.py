#!/usr/bin/env python3
"""
Telegram AGI Bot - يربط نموذج TinyStories-1M ببوت التليجرام
Connects TinyStories-1M model to Telegram Bot

This bot uses the TinyStories-1M model to generate creative stories
based on user prompts through Telegram.

المتطلبات / Requirements:
- python-telegram-bot
- transformers
- torch
"""

import logging
import os
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# ============================================================================
# Configuration / الإعدادات
# ============================================================================

# Telegram Bot Token
BOT_TOKEN: Final = "7974128410:AAFNO_sVaIW8_VaWQKz4jXbhJ3uXgH2xabI"

# Model Configuration
MODEL_NAME = "roneneldan/TinyStories-1M"
MAX_LENGTH = 150
TEMPERATURE = 0.7
TOP_P = 0.9

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ============================================================================
# Model Initialization / تهيئة النموذج
# ============================================================================

print("🤖 جاري تحميل النموذج... Loading model...")
print(f"📦 Model: {MODEL_NAME}")

try:
    # Load tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
    
    # Use GPU if available / استخدم GPU إن توفر
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = model.to(device)
    model.eval()
    
    print(f"✅ تم تحميل النموذج بنجاح! Model loaded successfully!")
    print(f"📍 Device: {device}")
except Exception as e:
    print(f"❌ خطأ في تحميل النموذج / Error loading model: {e}")
    exit(1)

# ============================================================================
# Helper Functions / دوال مساعدة
# ============================================================================

def generate_story(prompt: str, max_length: int = MAX_LENGTH) -> str:
    """
    Generate a story based on the given prompt.
    توليد قصة بناءً على المطالبة المعطاة.
    
    Args:
        prompt: The initial prompt for story generation
        max_length: Maximum length of generated text
    
    Returns:
        Generated story text
    """
    try:
        # Encode the prompt
        inputs = tokenizer.encode(prompt, return_tensors="pt").to(device)
        
        # Generate story
        with torch.no_grad():
            outputs = model.generate(
                inputs,
                max_length=max_length,
                temperature=TEMPERATURE,
                top_p=TOP_P,
                do_sample=True,
                pad_token_id=tokenizer.eos_token_id,
                num_return_sequences=1
            )
        
        # Decode the output
        story = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return story
    
    except Exception as e:
        logger.error(f"Error generating story: {e}")
        return f"❌ حدث خطأ في توليد القصة / Error generating story: {str(e)}"

# ============================================================================
# Telegram Bot Handlers / معالجات بوت التليجرام
# ============================================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle /start command.
    معالجة أمر /start
    """
    welcome_message = """
🤖 **مرحباً بك في AGI Story Bot!** / Welcome to AGI Story Bot!

📖 **ماذا يفعل هذا البوت؟** / What does this bot do?
- يولد قصص إبداعية باستخدام نموذج TinyStories-1M
- Generates creative stories using TinyStories-1M model

🎯 **كيفية الاستخدام** / How to use:
1. أرسل أي مطالبة / Send any prompt
2. البوت سيولد قصة بناءً على مطالبتك / Bot will generate a story based on your prompt

📝 **أمثلة** / Examples:
- "Once upon a time..."
- "في يوم من الأيام..."
- "A brave knight..."
- "ساحر قوي..."

⚙️ **الأوامر** / Commands:
/start - عرض هذه الرسالة / Show this message
/help - مساعدة / Help
/about - معلومات عن البوت / About the bot
/status - حالة النموذج / Model status

✨ **تم تطويره بواسطة** / Developed by: AGI Blueprint Team
"""
    await update.message.reply_text(welcome_message, parse_mode='Markdown')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle /help command.
    معالجة أمر /help
    """
    help_message = """
📚 **دليل الاستخدام** / Usage Guide

🎨 **توليد القصص** / Generate Stories:
- اكتب أي مطالبة وسيقوم البوت بتوليد قصة
- Write any prompt and the bot will generate a story

⚡ **الخصائص** / Features:
- 🧠 نموذج TinyStories-1M متقدم / Advanced TinyStories-1M model
- 🚀 توليد سريع / Fast generation
- 🎯 قصص إبداعية / Creative stories
- 🌍 دعم اللغات المتعددة / Multi-language support

💡 **نصائح** / Tips:
- استخدم مطالبات واضحة / Use clear prompts
- جرب مطالبات مختلفة / Try different prompts
- كن صبوراً مع النموذج / Be patient with the model

❓ **أسئلة شائعة** / FAQ:
Q: كم الوقت المستغرق؟ / How long does it take?
A: عادة 5-15 ثانية / Usually 5-15 seconds

Q: هل يمكن استخدام أي لغة؟ / Can I use any language?
A: نعم، النموذج يدعم لغات متعددة / Yes, the model supports multiple languages
"""
    await update.message.reply_text(help_message, parse_mode='Markdown')

async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle /about command.
    معالجة أمر /about
    """
    about_message = """
ℹ️ **معلومات عن البوت** / About This Bot

🤖 **AGI Story Bot** - بوت ذكاء اصطناعي متقدم

📊 **تقنيات مستخدمة** / Technologies Used:
- **النموذج**: TinyStories-1M
- **المكتبات**: Transformers, PyTorch, python-telegram-bot
- **المعمارية**: Causal Language Model

🎯 **الهدف** / Purpose:
هذا البوت جزء من مشروع AGI Blueprint الذي يهدف إلى تطوير
نظام ذكاء اصطناعي عام (AGI) متقدم.

This bot is part of the AGI Blueprint project, which aims to develop
an advanced Artificial General Intelligence (AGI) system.

🔗 **روابط مهمة** / Important Links:
- GitHub: https://github.com/lwsh72462-design/500-AI-Agents-Projects
- Telegram: https://t.me/+fOwCWbAJFME0ZGVk
- Contact: @WwAA3BOT444

✨ **الميزات** / Features:
✅ توليد قصص إبداعية / Creative story generation
✅ دعم لغات متعددة / Multi-language support
✅ استجابة سريعة / Fast response
✅ نموذج متقدم / Advanced model

📝 **الإصدار** / Version: 1.0.0
📅 **التاريخ** / Date: 2026-03-13
"""
    await update.message.reply_text(about_message, parse_mode='Markdown')

async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle /status command.
    معالجة أمر /status
    """
    device_info = "GPU (CUDA)" if torch.cuda.is_available() else "CPU"
    status_message = f"""
✅ **حالة النموذج** / Model Status

🟢 **الحالة** / Status: **جاهز** / **Ready**

📊 **معلومات النموذج** / Model Info:
- **النموذج** / Model: {MODEL_NAME}
- **الجهاز** / Device: {device_info}
- **الحالة** / State: تقييم / Evaluation

⚙️ **الإعدادات** / Settings:
- **الطول الأقصى** / Max Length: {MAX_LENGTH}
- **درجة الحرارة** / Temperature: {TEMPERATURE}
- **Top P**: {TOP_P}

🚀 **جاهز للعمل!** / Ready to work!
"""
    await update.message.reply_text(status_message, parse_mode='Markdown')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle user messages and generate stories.
    معالجة رسائل المستخدم وتوليد القصص.
    """
    user_message = update.message.text
    user_name = update.message.from_user.first_name or "Friend"
    
    # Show typing indicator
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
    
    # Log the request
    logger.info(f"User {user_name} requested story with prompt: {user_message}")
    
    # Send processing message
    processing_msg = await update.message.reply_text(
        "⏳ جاري توليد القصة... / Generating story...\n\n"
        f"📝 المطالبة / Prompt: {user_message}"
    )
    
    try:
        # Generate story
        story = generate_story(user_message)
        
        # Create response message
        response = f"""
✨ **القصة المولدة** / Generated Story:

{story}

---
📝 **المطالبة الأصلية** / Original Prompt: {user_message}
👤 **المستخدم** / User: {user_name}
"""
        
        # Edit the processing message with the result
        await processing_msg.edit_text(response, parse_mode='Markdown')
        
        logger.info(f"Story generated successfully for {user_name}")
        
    except Exception as e:
        error_msg = f"❌ حدث خطأ / Error: {str(e)}"
        await processing_msg.edit_text(error_msg)
        logger.error(f"Error generating story: {e}")

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Log the error and send a message to notify the user.
    تسجيل الخطأ وإرسال رسالة لإخطار المستخدم.
    """
    logger.error(msg="Exception while handling an update:", exc_info=context.error)
    
    if isinstance(update, Update) and update.effective_message:
        await update.effective_message.reply_text(
            "❌ حدث خطأ غير متوقع / An unexpected error occurred. "
            "يرجى المحاولة مرة أخرى / Please try again later."
        )

# ============================================================================
# Main Function / الدالة الرئيسية
# ============================================================================

def main() -> None:
    """
    Start the bot.
    تشغيل البوت.
    """
    print("\n" + "="*60)
    print("🚀 بدء تشغيل بوت AGI Story Bot / Starting AGI Story Bot")
    print("="*60 + "\n")
    
    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about_command))
    application.add_handler(CommandHandler("status", status_command))
    
    # Add message handler for text messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Add error handler
    application.add_error_handler(error_handler)
    
    print("✅ تم إعداد البوت / Bot configured successfully")
    print("📡 جاري الاتصال بخادم التليجرام / Connecting to Telegram servers...")
    print("💬 البوت جاهز لاستقبال الرسائل / Bot ready to receive messages\n")
    
    # Start the Bot
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
