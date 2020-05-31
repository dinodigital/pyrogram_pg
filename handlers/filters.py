from pyrogram import Message, Filters, CallbackQuery


def m_template(_, m: Message):
    """
    Приме фильтра сообщений
    """
    text = m.text
    return True if text else False


def q_template(_, q: CallbackQuery):
    """
    Пример фильтра callback_data
    """
    data = q.data
    return True if data else False


m_filter = Filters.create(m_template)
q_filter = Filters.create(q_template)
