from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext, ConversationHandler

TOKEN = '6577280428:AAHqP3mYOgAkfAN_su2U7F_s0qztGbvZexM'

# Define states for the conversation
MAIN_MENU, PRODUCT_SELECTION, DELIVERY, CURRENCY_EXCHANGE, CONTACT_MANAGER, UNSURE_CHOICE = range(6)
PRODUCT_DETAILS, DELIVERY_DETAILS, EXCHANGE_DETAILS, CONTACT_DETAILS, UNSURE_OPTIONS = range(6, 11)

async def start(update: Update, context: CallbackContext) -> int:
    keyboard = [
        [KeyboardButton("Подбор и выкуп товара")],
        [KeyboardButton("Доставка")],
        [KeyboardButton("Обмен юаня / доллар")],
        [KeyboardButton("Связаться с менеджером")],
        [KeyboardButton("Я не знаю что выбрать")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    await update.message.reply_text(
        "Приветствуем! Мы - Local Dealers, помогаем предпринимателям и организациям успешно работать с Китаем.\n"
        "Выберите опцию:", reply_markup=reply_markup)
    return MAIN_MENU

async def main_menu(update: Update, context: CallbackContext) -> int:
    choice = update.message.text
    if choice == "Подбор и выкуп товара":
        return await product_selection(update, context)
    elif choice == "Доставка":
        return await delivery(update, context)
    elif choice == "Обмен юаня / доллар":
        return await currency_exchange(update, context)
    elif choice == "Связаться с менеджером":
        return await contact_manager(update, context)
    elif choice == "Я не знаю что выбрать":
        return await unsure_choice(update, context)
    else:
        await update.message.reply_text("Пожалуйста, выберите один из предложенных вариантов.")
        return MAIN_MENU

async def product_selection(update: Update, context: CallbackContext) -> int:
    keyboard = [
        [KeyboardButton("Тарифы на доставку")],
        [KeyboardButton("Заполнить таблицу")],
        [KeyboardButton("Главное меню")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    await update.message.reply_text(
        "Мы помогаем Вам в поиске нужных позиций, осуществляем безопасную сделку с поставщиками по выкупу оптовых и розничных партий товаров с Китайских маркетплейсов:\n"
        "- Poizon\n- 1688\n- TaoBao\n\n"
        "От вас потребуется только заполнение таблицы с указанием нужных характеристик товаров. Далее мы в режиме онлайн сможем сделать все расчеты по стоимости выкупа и согласовать дальнейшую доставку.\n\n"
        "Для мелких заказов вы можете обратиться напрямую к менеджеру, без заполнения таблицы.", reply_markup=reply_markup)
    return PRODUCT_DETAILS

async def delivery(update: Update, context: CallbackContext) -> int:
    keyboard = [
        [KeyboardButton("Тарифы на доставку")],
        [KeyboardButton("Как упаковать товары?")],
        [KeyboardButton("Главное меню")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    await update.message.reply_text("Для наших партнеров мы предлагаем услуги по перевозке и доставке из Китая. Тарифы на доставку зависят от веса и объема товара.", reply_markup=reply_markup)
    return DELIVERY_DETAILS

async def currency_exchange(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text(
        "Обмен юаня / доллар.\n"
        "Курсы обмена:\n"
        "Курс 1$ = более 6.3 юань\n"
        "Курс 5$ = более 6.3-6.5 юань\n"
        "Курс 10$ = более 6.5-6.8 юань\n"
        "Для получения дополнительной информации свяжитесь с менеджером.")
    return MAIN_MENU

async def contact_manager(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text("@localmanagr")
    await update.message.reply_text("Связаться с менеджером.\nНаши менеджеры помогут вам с любыми вопросами.")
    return MAIN_MENU

async def unsure_choice(update: Update, context: CallbackContext) -> int:
    keyboard = [
        [KeyboardButton("Производство")],
        [KeyboardButton("Мелкая партия")],
        [KeyboardButton("Много! Нужно многое!")],
        [KeyboardButton("Главное меню")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    await update.message.reply_text("Так, сейчас поможем, просто отвечайте на уточняющие вопросы и мы быстро поймем что требуется. Это не займет много времени.", reply_markup=reply_markup)
    return UNSURE_OPTIONS

async def product_details(update: Update, context: CallbackContext) -> int:
    choice = update.message.text
    if choice == "Тарифы на доставку":
        await update.message.reply_text("В стоимость услуг входит:\n- Подбор товара\n- Оценка продавцов\n- Коммуникация с продавцом\n- Совместная проверка и проверка на складе\n- Объединение посылок на складе\nЦены: до 50 шт - 10%, от 50 до 100 - 8%, от 100 шт - 5%")
        return PRODUCT_DETAILS
    elif choice == "Заполнить таблицу":
        await update.message.reply_text("Заполните таблицу, внесите данные о товаре, доставке и прочей информации и отправьте ее нам.")
        return PRODUCT_DETAILS
    elif choice == "Главное меню":
        return await start(update, context)
    else:
        await update.message.reply_text("Пожалуйста, выберите один из предложенных вариантов.")
        return PRODUCT_DETAILS

async def delivery_details(update: Update, context: CallbackContext) -> int:
    choice = update.message.text
    if choice == "Тарифы на доставку":
        await update.message.reply_text("Тарифы на доставку зависят от веса и объема товара.\nКурьез в более 6.3 юань за 1$.\nКурьез в более 6.3-6.5 юань за 5$.\нКурьез в более 6.5-6.8 юань за 10$.")
        return DELIVERY_DETAILS
    elif choice == "Как упаковать товары?":
        await update.message.reply_text("Упаковка зависит от типа и количества товаров. Свяжитесь с менеджером для получения более подробной информации.")
        return DELIVERY_DETAILS
    elif choice == "Главное меню":
        return await start(update, context)
    else:
        await update.message.reply_text("Пожалуйста, выберите один из предложенных вариантов.")
        return DELIVERY_DETAILS

async def unsure_options(update: Update, context: CallbackContext) -> int:
    choice = update.message.text
    if choice == "Производство":
        await update.message.reply_text("Найти производителя по проекту заказа и провести комплексный поиск, сообщить на что нужно указать при поиске производства паяльника с весом 2000 кг. Связаться с менеджером для получения более подробной информации.")
        return UNSURE_OPTIONS
    elif choice == "Мелкая партия":
        await update.message.reply_text("Вам нужна небольшая партия, например 1-4 вещи? Связаться с менеджером для получения более подробной информации.")
        return UNSURE_OPTIONS
    elif choice == "Много! Нужно многое!":
        await update.message.reply_text("Для больших заказов подготовьте список интересующих вас товаров и их количество. Связаться с менеджером для получения более подробной информации.")
        return UNSURE_OPTIONS
    elif choice == "Главное меню":
        return await start(update, context)
    else:
        await update.message.reply_text("Пожалуйста, выберите один из предложенных вариантов.")
        return UNSURE_OPTIONS

async def cancel(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text('Разговор завершен. До свидания!')
    return ConversationHandler.END

def main():
    application = ApplicationBuilder().token(TOKEN).build()
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            MAIN_MENU: [MessageHandler(filters.TEXT & ~filters.COMMAND, main_menu)],
            PRODUCT_SELECTION: [MessageHandler(filters.TEXT & ~filters.COMMAND, product_selection)],
            DELIVERY: [MessageHandler(filters.TEXT & ~filters.COMMAND, delivery)],
            CURRENCY_EXCHANGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, currency_exchange)],
            CONTACT_MANAGER: [MessageHandler(filters.TEXT & ~filters.COMMAND, contact_manager)],
            UNSURE_CHOICE: [MessageHandler(filters.TEXT & ~filters.COMMAND, unsure_choice)],
            PRODUCT_DETAILS: [MessageHandler(filters.TEXT & ~filters.COMMAND, product_details)],
            DELIVERY_DETAILS: [MessageHandler(filters.TEXT & ~filters.COMMAND, delivery_details)],
            UNSURE_OPTIONS: [MessageHandler(filters.TEXT & ~filters.COMMAND, unsure_options)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    application.add_handler(conv_handler)
    application.run_polling()

if __name__ == '__main__':
    main()
