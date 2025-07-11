from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Merhaba! Ben AF-Tech bilgilendirme botuyum.\nKomutlar:\n/misyon\n/vizyon\n/okul\n/altakimlar\n/basari\n/sosyalmedya")

async def misyon(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("AF-Tech, genç zihinlerin milli teknoloji hamlesine katkıda bulunduğu, yaratıcı fikirlere yön verdiği bir öğrenci topluluğudur. Topluluk, herhangi bir çıkar gözetmeksizin Milli Teknoloji Hamlesine hizmet eder.")

async def vizyon(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Türkiye’yi teknoloji sahnesinde temsil etmek.")

async def okul(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Takımımız, Baykar Fen Lisesi bünyesinde kurulmuştur. Okulumuz Türkiye'nin en iddialı fen liselerinin başında gelmektedir.")

async def altakimlar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🛩️ İHA-2: BAYSAL UAV Project (İHA)\n🛩️ İHA-3: SKYWIPE UAV Project (İHA)\n🛩️ AF-SAVAŞAN: TURCOFIGHTER (Savaşan İHA)\n🤖 AF-ASPAN: The Special One (Robolig)\n🌊 AF-TECH Su Altı: TALAY ROV")

async def basari(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏆 3 Robolig takımımız görev videosu aşamasında\n🏆 2 İHA takımımız görev videosu aşamasında")

async def sosyalmedya(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📷 Instagram: https://www.instagram.com/anatolian.falcons/\n🐦 Twitter: https://x.com/tech1AF")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("misyon", misyon))
app.add_handler(CommandHandler("vizyon", vizyon))
app.add_handler(CommandHandler("okul", okul))
app.add_handler(CommandHandler("altakimlar", altakimlar))
app.add_handler(CommandHandler("basari", basari))
app.add_handler(CommandHandler("sosyalmedya", sosyalmedya))

app.run_polling()
