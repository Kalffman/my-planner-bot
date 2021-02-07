from functools import wraps

from telegram import Update, ChatAction
from telegram.ext import Updater, CallbackContext, CommandHandler, ConversationHandler, MessageHandler, Filters

from api.client.user import *
from core.properties import properties

logger = LogFactory.getLogger(__name__)

HELLO_ACCEPTED, REMINDER = range(2)


def typing_action(func):
    """Sends typing action while processing func command."""

    @wraps(func)
    def command_func(update: Update, context: CallbackContext, *args, **kwargs):
        context.bot.send_chat_action(
            chat_id=update.effective_message.chat_id,
            action=ChatAction.TYPING,
            timeout=5
        )
        return func(update, context, *args, **kwargs)

    return command_func


@typing_action
def hello(update: Update, context: CallbackContext) -> int:
    logger.info(f"{update.effective_user.name} iniciou o chat.")
    user = update.effective_user
    chat = update.effective_chat
    bot = context.bot

    bot.send_message(
        chat_id=chat.id,
        text=f"Oi {user.first_name}, Tudo bem?"
    )

    bot.send_message(
        chat_id=chat.id,
        text=f"Sou a {bot.first_name}. Uma excelente assistente para ajudar na sua rotina."
    )

    bot.send_message(
        chat_id=chat.id,
        text="Para que a gente se conheça mais, como eu posso te chamar? 😁"
    )

    bot.send_message(
        chat_id=chat.id,
        text="Detalhe: No máximo 15 letras, tá?\nIsso facilita pra mim nas minhas anotações. 😉"
    )

    return HELLO_ACCEPTED


@typing_action
def hello_accepted(update: Update, context: CallbackContext) -> int:
    logger.info(f"{update.effective_user.name} aceitou a conversa.")
    user = update.effective_user
    chat = update.effective_chat
    bot = context.bot
    apelido = update.effective_message.text

    bot.send_message(
        chat_id=chat.id,
        text=f"{apelido}!!"
    )
    bot.send_message(
        chat_id=chat.id,
        text="Nunca esquecerei 😆😆"
    )

    bot.send_message(
        chat_id=chat.id,
        text=f"Pode contar comigo, {apelido}!"
    )

    bot.send_message(
        chat_id=chat.id,
        text="Sempre estarei a disposição para te ajudar nos seus compromissos."
    )

    bot.send_message(
        chat_id=chat.id,
        text="Isso eu garanto! 😌"
    )

    created = new_user({
        "chatId": str(chat.id),
        "usuarioTelegram": user.name,
        "primeiroNome": user.first_name,
        "sobrenome": user.last_name,
        "nomeCompleto": user.full_name,
        "apelido": apelido,
    })

    if created:
        bot.send_message(
            chat_id=chat.id,
            text="Brevemente mandarei as ações pra te responder."
        )
    else:
        bot.send_message(
            chat_id=chat.id,
            text=f"Agora nesse momento estou ocupada {apelido}! Quando eu puder eu respondoo... 😮 🏃‍♀️"
        )

    return ConversationHandler.END


def cancel(update: Update, context: CallbackContext) -> int:
    logger.info(f"")

    return ConversationHandler.END


def main():
    updater = Updater(properties["BOT_TOKEN"])

    logger.info(f"Acordando {updater.bot.first_name}")

    dispatcher = updater.dispatcher

    main_handler = ConversationHandler(
        entry_points=[
            CommandHandler("start", hello)
        ],
        states={
            HELLO_ACCEPTED: [
                MessageHandler(Filters.regex("^(\w{3,15})$"), hello_accepted)
            ]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    dispatcher.add_handler(main_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
