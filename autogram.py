from pyrogram import Client # pip3 install -U pyrogram
from datetime import datetime
import asyncio
import time

async def mining_nrb():
    async with Client("my_account", api_id, api_hash) as app:
        await app.send_message(chat_id, "\U0001f579Игры")
        time.sleep(10)
        # эмодзи мини-игры: баскетбольный мяч, футбольный мяч, боулинг, дартс
        dice_emojis = ["\U0001F3C0", "\u26BD", "\U0001F3B3", "\U0001F3AF"]
        for emoji in dice_emojis:
            await app.send_dice(chat_id, emoji)
            time.sleep(10)
            # получаем последнее сообщение из чата с ботом
            async for message in app.get_chat_history(chat_id, limit=1):
                last_message = message.text
            # условие выполнится, когда угадаем нужный сегодня эмодзи
            if last_message != "Команда не опознана":
                break

if __name__ == "__main__":
    api_id = 12345
    api_hash = "0123456789abcdef0123456789abcdef"
    chat_id = "@tn_mp_bot" # ТН - Маркетплейс Бот
    # chat_id = "me" # для тестов
    start_time = datetime.strptime("10:00", "%H:%M")

    while(True):
        # раз в минуту проверяю наступило ли заданное время
        if(datetime.now().strftime("%H:%M") == start_time.strftime("%H:%M")):
            asyncio.run(mining_nrb())
            time.sleep(60) # чтобы после майнинга точно была другая минута
        else:
            time.sleep(60)
