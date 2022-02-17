import logging
import pathlib
import time
from multiprocessing.pool import ApplyResult, ThreadPool

import telebot


class Notifier(telebot.TeleBot):
    def __init__(self,
                token: str,
                parse_mode: str):

        self.pool = ThreadPool()
        super().__init__(token, parse_mode)

    def notify(self, chat_id, message, caption = None):
        """
        Returns a Notifier thread type object which you can as chat id, if you want to reply to this message

        Use this utilite for avoiding spamming errors
        If any Exception caused, you may find Error message in the file which located in folder logs

        chat_id: Id of the chat, where you want to send the message (or Notifier object, if you want to reply to the message)
        message: str or byte like object that you want to send
        caption: caption text for byte like objects
        """
        main_pool = self.pool.apply_async(self.send, (chat_id, message, caption))
        return main_pool


    def send(self, chat_id, message, caption, reply_to = None):
        """
        Use the nitify method to send messages, don't run this method customly
        """

        if type(chat_id) is ApplyResult:
            previous_pool = chat_id.get()
            reply_to = previous_pool.message_id
            chat_id = previous_pool.chat.id

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
