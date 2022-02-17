# Notifier

>Use this utilite for sending mass messages by Telegram Bot and avoiding spam errors

## Example

```
#Let's create a class object
notifier = Notifier(token,'html')

#Send text message to a chat
message = notifier.notify(chat_id = chat_id, message = 'Hello There')

#Now reply to your message
notifier.notify(chat_id = message, message = 'I am a notifier bot')

#Now send a document with caption
doc = open('docs/myDoc.doctype', 'rb')
notifier.notify(chat_id = message, message = doc, caption = 'Here is my first document')
```

