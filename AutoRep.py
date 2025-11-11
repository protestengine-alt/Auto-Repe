from telethon.sync import TelegramClient, events
import time
api_id = 24124328 
api_hash = '24ba5fad9e7e59d2b64d43172fb1d491'
phone_number = '+919429693221'
AUTO_REPLY_MESSAGE = "Hy I Am Assistant, Protest Abhi Offline He. Me Unko Message Kardungi Over And Out! 📡"
client = TelegramClient('my_assistant_session', api_id, api_hash)
@client.on(events.NewMessage(incoming=True, from_users='me', forwards=False))
async def handle_my_messages(event):
    pass
@client.on(events.NewMessage(incoming=True))
async def auto_responder(event):
    if event.is_private:
        sender = await event.get_sender()
        sender_id = sender.id
        my_info = await client.get_me()
        if sender_id == my_info.id:
            return
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] New Message {sender.first_name} se: '{event.text}'")     
        time.sleep(2) 
        await event.reply(AUTO_REPLY_MESSAGE)
        print(f"Auto-reply Done {sender.first_name} ko.")
async def main():
    await client.start(phone_number)
    print("Ok Boss Iam Waiting for New Message For Replay Auto")
    await client.run_until_disconnected()
if __name__ == '__main__':
    import asyncio
    asyncio.run(main())