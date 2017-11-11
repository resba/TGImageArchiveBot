from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import File
import sys,os,traceback,logging,datetime

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.WARNING)

def start(bot, update):
	update.message.reply_text("Hello!")

def archive(bot, update):
	if update.message.photo != None:
		for x in update.message.photo:
			print "Download:  "+x.file_id
			f = bot.getFile(file_id=x.file_id)
			f.download()
			print "Completed: "+x.file_id
		print " ----------------- "

def error(bot, update, error):
	logging.warning('Update "%s" caused error "%s"' % (update, error))
	lasterr = 'Update "%s" caused error "%s"' % (update, error)

updater = Updater("TELEGRAM_KEY_GOES_HERE")
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))

dispatcher.add_handler(MessageHandler(Filters.all, archive))

dispatcher.add_error_handler(error)

updater.start_polling()
updater.idle()
