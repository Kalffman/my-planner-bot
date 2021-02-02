from config.properties import config
from telegram.ext import Updater, CallbackContext, CommandHandler
from telegram import Update
import logging

logging.basicConfig(
    filename="./my_planner_bot.log",
    format="{\"time\": \"%(asctime)s\","
           " \"name\": \"%(name)s\","
           " \"level\": \"%(levelname)s\","
           " \"message\": \"%(message)s\"}",
    level=logging.INFO
)

logger = logging.getLogger(__name__)


def hello(update: Update, context: CallbackContext) -> None:
    logger.info(fr"hello -> {update.effective_user.name} sent hello")
    update.message.reply_text("Olá! Sou a MyPlanner Bot. Será um prazer ajudá-lo a organizar seu dia :D")


def main():
    updater = Updater(config["TELEGRAM_BOT_TOKEN"])

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("oi", hello))

    updater.start_polling()

    logger.info("Iniciando Planner BOT")
    updater.idle()


if __name__ == '__main__':
    main()
