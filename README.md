<h1>Notifier</h1>

<p>Use for sending mass messages by Telegram Bot without errors</p>

<h3>Example</h3>

<code>
#Let's create class object
notifier = Notifier(token,'html')

#Send text message to a chat
message = notifier.notify(chat_id = chat_id, message = 'Hello There')

#Now reply to your message
notifier.notify(chat_id = message, message = 'I am a notifier bot')

#Now send a document with caption
doc = open('docs/myDoc.doctype', 'rb')
notifier.notify(chat_id = message, message = doc, caption = 'Here is my first document')
</code>

