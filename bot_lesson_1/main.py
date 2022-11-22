from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import Filters  # помогает фильтровать все приходящие от юзеров сообщения (выбор: текст, стикеры и тд)
from telegram.ext import MessageHandler  # обработчик, который определяет к какому сообщению подходит данная функция
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove  # скрывает клавиатуру после сообщения юзера

with open("token_bot_anubis.txt", "r") as file:
    TOKEN = file.read().strip()
file.close()
#  кнопки
button_help = "кнопка сверху 1"
button_help_2 = "кнопка сверху 2"
button_down = "кнопка снизу"


def button_handler(update: Update, context: CallbackContext):
    update.message.reply_text(  # reply_text это ответное сообщение от бота
        text="Это реакция на нажатие кнопки",
        reply_markup=ReplyKeyboardRemove(),  # метод убирает кнопки после выбора одной из кнопок
    )


def message_handler(update: Update, context: CallbackContext):
    text = update.message.text
    if text == button_help: #  если текст совпадет с кнопко, то сработает функция которая отвечает и скрывает кнопки
        return button_handler(update=update, context=context)
    #  в ином случае кнопки не будут скрыты
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_help), KeyboardButton(text=button_help_2)
            ], [KeyboardButton(text=button_down)]
        ],
        resize_keyboard=True,
    )
    update.message.reply_text(
        text="Ответное сообщение от бота на сообщение юзера",
        reply_markup=reply_markup,
    )


def main():
    print("Start")
    # вся логика построена на классе Updater. Именно он будет связывать все новые приходящие сообщения от юзеров
    # и обрабатывать под них все функции
    # здесь же учитываем token
    updater = Updater(
        token=TOKEN,
        use_context=True,
    )
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))
    updater.start_polling()  # запускает бота после сообщения юзера
    updater.idle()  # поддерживает код постоянно активным для обработки приходящих сообщений


if __name__ == "__main__":
    main()
