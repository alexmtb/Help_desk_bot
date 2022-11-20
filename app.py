import logging
from aiogram import Bot, Dispatcher, executor, types
from conf import config
from MenuButton import menuBtns
from data_Base import botDBase


token = config.BOT_API_TOKEN
logging.basicConfig(level=logging.DEBUG)
bot = Bot(token=token)
dp = Dispatcher(bot)


async def bot_startup(_):
    print('Бот WeBioMed на связи!')
    botDBase.sql_start()


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    global user_id
    user_id = message.from_user.id
    try:
        await bot.send_message(message.from_user.id, text = f'Привет, {message.from_user.first_name}! '
                        f'Это бот техподдержки компании WeBioMed. \nДля связи с техподдержкой напишите свой вопрос и нажмите кнопку "отправить"',
                               reply_markup=menuBtns)
        #await message.delete()
    except:
        await message.reply("Напишите боту техподдержки WeBioMed")

# время работы техподдержки
@dp.message_handler(commands=['work_hours'])
async def work_hours(message : types.Message):
    #await message.delete()
    await bot.send_message(message.from_user.id, text = 'Ну явно не круглосуточно!')

# commands=['question']
@dp.message_handler()
async def forward_msg(message: types.Message):
    user_id = message.from_user.id
    botDBase.sql_add_request(user_id, message.text)
    await message.forward(chat_id='-701935963')


@dp.message_handler()
async def reply_message_bot(message: types.Message):
    # chat_id = 202051874 message.forward_from.id
    await bot.send_message(chat_id=message.from_user.id, text=message.text)

    logging.info(user_id)


'''@dp.message_handler()
async def answer_bot(message: types.Message):
    chatid = await message.chat.id
    logging.INFO(chatid)
        #await message.send_copy(chat_id=chatid)
    #logging.info(chatid)

#    logging.info(userid)
'''

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=bot_startup)
