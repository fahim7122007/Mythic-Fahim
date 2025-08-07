import os
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, ContextTypes, filters

# Use your actual token or set it via Render environment variables
BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📖 About Me", callback_data='about')],
        [InlineKeyboardButton("📞 Contact", callback_data='contact')],
        [InlineKeyboardButton("🛠️ Skills", callback_data='skills')],
        [InlineKeyboardButton("🌐 Socials", callback_data='socials')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Hi! I’m Mythic Fahim. Choose an option below to know more:", reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'about':
        await query.edit_message_text("I’m Mythic Fahim — a Binary, Forex, and Crypto trader, AI specialist, Cyber Security expert, and a passionate learner. I’m also a top student with golden A+ in PEC, JSC, and SSC.")
    elif query.data == 'contact':
        await query.edit_message_text("📨 Contact Info\n\n🔹 Business Telegram: @safahim_2010\n🔹 Personal Telegram: @mythic_fahim\n🔹 Facebook: facebook.com/safahim2010\n🔹 Pinterest: blueprint_fahim")
    elif query.data == 'skills':
        await query.edit_message_text("🛠️ My Skills:\n• Forex & Binary Trading\n• Cyber Security Expert\n• Gamer (ex-Free Fire Esports Player)\n• Professional Chess Player\n• Email Marketing\n• Social Media Marketing")
    elif query.data == 'socials':
        await query.edit_message_text("🌐 My Social Media Links\n\n🔵 Facebook: https://facebook.com/safahim2010\n📩 Telegram (Business): https://t.me/safahim_2010\n📩 Telegram (Personal): https://t.me/mythic_fahim\n📌 Pinterest: https://pinterest.com/blueprint_fahim")

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text.lower()
    if "who are you" in msg:
        await update.message.reply_text("I’m Mythic Fahim — trader, AI expert, and cybersecurity enthusiast.")
    elif "where do you live" in msg:
        await update.message.reply_text("I live in Masterbari, Mymensingh, Bangladesh.")
    elif "birthday" in msg:
        await update.message.reply_text("My birthday is December 7, 2007.")
    elif "student" in msg:
        await update.message.reply_text("Yes, I'm a class topper with golden A+ in PEC, JSC, and SSC.")
    elif "favorite actor" in msg:
        await update.message.reply_text("Cillian Murphy is my favorite actor.")
    else:
        await update.message.reply_text("Ask me anything about Mythic Fahim or use /start to explore!")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

    app.run_polling()
