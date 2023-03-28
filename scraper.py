from pyrogram import Client
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

chat_title=input('Введите название чата:  ')
username=input('Введите имя пользователя:   ')

app = Client(
    name = config['Telegram']['username'],
    api_id = config['Telegram']['api_id'],
    api_hash = config['Telegram']['api_hash']
)

async def main():
    async with app:
        async for dialog in app.get_dialogs():
            
            if dialog.chat.title==chat_title:
                chat_id=dialog.chat.id
                async for message in app.get_chat_history(chat_id):
                    data=message.from_user.username
                    
                    
                    if data==username:
                        try:
                            mess=str(message.text)
                            if mess!="None":
                                with open("messages.txt", "a", encoding="utf-8") as f: 
                                    f.write(mess + "\n")
                        except:
                            pass
    
app.run(main())
print('Парсинг закончен')