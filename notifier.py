import logging
import pathlib
import time
from multiprocessing.pool import ThreadPool, ApplyResult

import telebot

pathlib.Path('logs').mkdir(parents=True, exist_ok=True)
logging.basicConfig(
    filename='logs/Notifier_errors.txt',
    level=logging.WARNING,
    format=
    '[%(asctime)s:%(levelname)s] %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    encoding='UTF-8')

class Notifier(telebot.TeleBot, ThreadPool):
    def __init__(self,
                token: str,
                parse_mode: str):

        super().__init__(token, parse_mode)

    def notify(self, chat_id, message, caption = None, reply_to = None):
        """
        Use this utilite for avoiding spamming errors
        If any Exception caused, you may find Error message in the file which located in folder logs
        """
        main_pool = self.apply_async(self.send, (message, chat_id, caption, reply_to))
        return main_pool


    def send(self, chat_id, message, caption, reply_to):

        if type(reply_to) is ApplyResult:
            reply_to = reply_to.get()

        elif reply_to is not None:
            reply_to=reply_to.message_id
            
        while True:
            try:
                if type(message) is str:
                    result = self.send_message(chat_id, message, reply_to_message_id=reply_to)

                else:
                    result = self.send_document(chat_id, message, reply_to, caption)

                return result
            except Exception as e:
                retry=str(e).split('Too Many Requests: retry after')
                if len(retry)>1:
                    time.sleep(float(retry[-1]))
                else:
                    logging.warning('Bot undefinded error')
                    logging.exception(e)


def ask():
    time.sleep(10)
    return 90