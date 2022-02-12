import datetime
import logging
import pathlib
import time
import telebot
from threading import Thread

pathlib.Path('logs').mkdir(parents=True, exist_ok=True)
logging.basicConfig(
    filename='logs/Notifier_errors.txt',
    level=logging.WARNING,
    format=
    '[%(asctime)s:%(levelname)s] %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    encoding='UTF-8')

class Notifier(telebot.TeleBot):
    def __init__(self,
                token: str,
                parse_mode: str):

        super().__init__(token, parse_mode)

    def notify(self, chat_id, message, caption = None, reply_to = None):
        """
        Use this utilite for avoiding spamming errors
        If any Exception caused, you may find Error message in the file which located in folder logs
        """

        main_thread = Thread(target = self.send, args = (message, chat_id, caption, reply_to))
        main_thread.start()


    def send(self, chat_id, message, caption, reply_to):
        if reply_to:
            reply_to=reply_to.message_id
        while True:
            try:
                if type(message) is str:
                    self.send_message(chat_id, message, reply_to_message_id=reply_to)

                else:
                    self.send_document(chat_id, message, reply_to, caption)

                return None
            except Exception as e:
                retry=str(e).split('Too Many Requests: retry after')
                if len(retry)>1:
                    time.sleep(float(retry[-1]))
                else:
                    logging.warning('Bot undefinded error')
                    logging.exception(e)


