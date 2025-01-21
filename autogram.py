from pyrogram import Client # pip3 install -U pyrogram
from datetime import datetime
import asyncio
import random
import time

async def mining_nrb():
    async with Client("my_account", api_id, api_hash) as app:
        #await app.send_message(chat_id, "\U0001f579Игры") # старый эмодзи джойстика
        await app.send_message(chat_id, "\U0001F91D Игры") # теперь изменили на эмодзи рукопожатия
        time.sleep(30)
        # получаем последнее сообщение из чата с ботом
        async for message in app.get_chat_history(chat_id, limit=1):
            last_message = message.text
        if last_message == "Проверь свою интуицию: угадай, какое значение выпадет":
            # отправляем случайное число от 1 до 6
            await app.send_message(chat_id, random.randint(1,6))
            time.sleep(30)
            # затем кидаем кубик
            await app.send_dice(chat_id, "\U0001f3b2")
        elif last_message == "Okay, let's go!":
            # эмодзи мини-игры: баскетбольный мяч, футбольный мяч, боулинг, дартс
            dice_emojis = ["\U0001F3C0", "\u26BD", "\U0001F3B3", "\U0001F3AF"]
            for emoji in dice_emojis:
                await app.send_dice(chat_id, emoji)
                time.sleep(30)
                # получаем последнее сообщение из чата с ботом
                async for message in app.get_chat_history(chat_id, limit=1):
                    last_message = message.text
                # условие выполнится, когда угадаем нужный сегодня эмодзи
                if last_message != "Команда не опознана":
                    break

        # НИЖЕ ПОПЫТКИ НАЖАТИЙ НА КНОПКИ - НЕ РАБОТАЕТ
        # # Получаем последнее сообщение из чата с ботом
        # async for last_message in app.get_chat_history("@tn_mp_bot", limit=1):
        #     #await app.send_message("@tn_mp_bot", text=last_message.reply_markup[0][0].text)
        #     #last_message.click(0)

if __name__ == "__main__":
    api_id = 12345
    api_hash = "0123456789abcdef0123456789abcdef"
    chat_id = "@tn_mp_bot" # ТН - Маркетплейс Бот
    #chat_id = "me" # для тестов
    start_time = datetime.strptime("10:00", "%H:%M")

    # with Client("my_account", api_id, api_hash) as app:
        # bot_username = "tn_mp_bot"  # замените на юзернейм вашего бота
        # query = ''  # ваш запрос для получения результатов

        # results = app.get_inline_bot_results(bot_username, "\U0001f579Игры")

        # for result in results.results:
        #     print(result.title)  # Вывод текста кнопки

        
        # chat = app.get_chat(chat_id)  # замените chat_id на ID чата с ботом
        # print(chat.ChatPreview)

        # if chat.reply_markup:
        #     keyboard = chat.reply_markup.keyboard  # для ReplyKeyboardMarkup использовать .keyboard
        #     for row in keyboard:
        #         for button in row:
        #             print(button.text)  # Вывод текста на кнопках


    while(True):
        # раз в минуту проверяю наступило ли заданное время
        if(datetime.now().strftime("%H:%M") == start_time.strftime("%H:%M")):
            asyncio.run(mining_nrb())
            time.sleep(60) # чтобы после майнинга точно была другая минута
        else:
            time.sleep(60)
