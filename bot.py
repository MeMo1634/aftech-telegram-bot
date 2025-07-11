from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Merhaba! Ben AF-Tech bilgilendirme botuyum.\nKomutlar:\n/misyon\n/vizyon\n/okul\n/altakimlar\n/basari\n/sosyalmedya")

async def misyon(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("AF-Tech, genç zihinlerin teknolojiye yön verdiği bir öğrenci topluluğudur.")

async def vizyon(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Türkiye’yi teknoloji sahnesinde temsil etmek.")

async def okul(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Baykar Fen Lisesi (Baykar MTAL) öğrencilerinden oluşmaktadır.")

async def altakimlar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🛩️ Besnek (İHA)\n🤖 Robolig (Otonom Robot)\n🌊 Mucilage ROV")

async def basari(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏆 Teknofest Ön Değerlendirme Geçildi\n🏆 ROV Projesi Finalisti")

async def sosyalmedya(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📷 Instagram: https://instagram.com/aftech.team\n🐦 Twitter: https://twitter.com/aftech_team")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("misyon", misyon))
app.add_handler(CommandHandler("vizyon", vizyon))
app.add_handler(CommandHandler("okul", okul))
app.add_handler(CommandHandler("altakimlar", altakimlar))
app.add_handler(CommandHandler("basari", basari))
app.add_handler(CommandHandler("sosyalmedya", sosyalmedya))

app.run_polling()
