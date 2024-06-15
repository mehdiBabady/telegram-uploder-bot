
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes,MessageHandler,filters

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context.args:
        chat_id , msg_id = context.args[0].split("_")
        await context.bot.copy_message(chat_id=update.message.chat.id,from_chat_id=chat_id,message_id=msg_id)
    else:
        await update.message.reply_text("any file you send me i give you a link for it")
        print(update.message.id)
    
async def upload(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(text=f"{URL}?start={update.message.chat.id}_{update.message.id}")
    
# example : https://t.me/mychannelLink
URL = ""

TOKEN = ""

app = ApplicationBuilder().token(TOKEN).build()

docFilter = (filters.Document.ALL|filters.ATTACHMENT)


app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters=docFilter,callback=upload))

app.run_polling()