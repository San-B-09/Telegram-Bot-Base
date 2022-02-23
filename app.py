from flask import Flask, request, abort
import telegram
from decouple import config

API_KEY = config('API_KEY')
USER_NAME = config('BOT_USER_NAME')
HEROKU_URL = config('HEROKU_URL')
downloadedPDFs = []

bot = telegram.Bot(token=API_KEY)

app = Flask(__name__)


@app.route('/{}'.format(API_KEY), methods=['POST'])
def respond():
    # retrieve the message in JSON and then transform it to Telegram object
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    chat_id = update.message.chat.id
    msg_id = update.message.message_id

    if(update.message.text == None):
        return 'ok'

    # Telegram understands UTF-8, so encode text for unicode compatibility
    text = (update.message.text.encode('utf-8').decode()).lower()

    # the first time you chat with the bot AKA the welcoming message
    if "hi" in text:
        bot_welcome = """
        Welcome to Base Bot. 
        """
        bot.sendMessage(chat_id=chat_id, text=bot_welcome,
                        reply_to_message_id=msg_id)

    elif "bye" in text:
        bot_welcome = """
        Byee!\nHave a productive time! 
        """
        bot.sendMessage(chat_id=chat_id, text=bot_welcome,
                        reply_to_message_id=msg_id)

    return 'ok'


@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
   s = bot.setWebhook('{URL}{HOOK}'.format(URL=HEROKU_URL, HOOK=API_KEY))
   if s:
       return "webhook setup ok"
   else:
       return "webhook setup failed"


@app.route('/')
def index():
   return '.'


if __name__ == '__main__':
   app.run(threaded=True)
