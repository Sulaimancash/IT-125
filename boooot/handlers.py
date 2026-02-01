from aiogram import types, Router
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile
from quiz import Quiz
from question import Question

router = Router()


questions = [
    Question("images/железный человек.jfif", "Кто Железный человек?", ["Стив Роджерс", "Тони Старк", "Брюс Беннер", "Тор"], 1),
    Question("images/капитан америка.jfif", "Имя Капитана Америки?", ["Стив Роджерс", "Баки Барнс", "Тони Старк", "Пегги Картер"], 0),
    Question("images/торр.jfif", "Тор — бог чего?", ["Ветра", "Грома", "Огня", "Воды"], 1),
    Question("images/халк.jfif", "Кто превращается в Халка?", ["Тони Старк", "Брюс Беннер", "Скотт Лэнг", "Локи"], 1),
    Question("images/черная вдова.jfif", "Настоящее имя Чёрной вдовы?", ["Наташа Романофф", "Ванда Максимофф", "Кэрол Дэнверс", "Пегги Картер"], 0),
    Question("images/соколиные глаза.png", "Какое оружие у Соколиного глаза?", ["Лук", "Меч", "Пистолет", "Копьё"], 0),
    Question("images/танос.jfif", "Главный враг в Войне бесконечности?", ["Локи", "Танос", "Ультрон", "Красный череп"], 1),
    Question("images/Ник фьюри.jfif", "Как называется организация Ника Фьюри?", ["ГИДРА", "Щ.И.Т.", "Мстители", "Стражи"], 1),
    Question("images/мстители.jfif", "Кто собрал команду Мстителей?", ["Тони Старк", "Ник Фьюри", "Тор", "Халк"], 1),
    Question("images/мир.jfif", "В какой вселенной Мстители?", ["DC", "Marvel", "Star Wars", "Matrix"], 1),
    Question("images/тони старк.jfif", "Как называется ИИ Тони Старка?", ["Джарвис", "Фридэй", "Ультрон", "Вижен"], 0),
    Question("images/тор.jfif", "Родной мир Тора?", ["Земля", "Асгард", "Криптон", "Сакаар"], 1),
    Question("images/халк становится сильней.jfif", "Как Халк становится сильнее?", ["Когда злится", "Когда думает", "Когда спит", "Когда бегает"], 0),
    Question("images/что использует капитан америка.jfif", "Что использует Капитан Америка как оружие?", ["Щит", "Меч", "Лук", "Молот"], 0),
    Question("images/камни бесконечности.jfif", "Сколько камней бесконечности?", ["5", "6", "7", "8"], 1),
]

quiz = Quiz(questions)



def get_options_keyboard(options):
    
    buttons = [
        [InlineKeyboardButton(text=o, callback_data=str(i)) for i, o in enumerate(options)][i:i+2]
        for i in range(0, len(options), 2)
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


@router.message(CommandStart())
async def start(message: types.Message):
    q = quiz.get_current_question()
    if q:
        photo = FSInputFile(q.image_path)
        await message.answer_photo(photo=photo, caption=q.text, reply_markup=get_options_keyboard(q.options))



@router.callback_query()
async def handle_answer(callback: types.CallbackQuery):
    answer_index = int(callback.data)
    
    quiz.answer(answer_index)

    next_q = quiz.get_current_question()
    if next_q:
        photo = FSInputFile(next_q.image_path)
        await callback.message.answer_photo(photo=photo, caption=next_q.text, reply_markup=get_options_keyboard(next_q.options))
    else:
        await callback.message.answer(
            f"Викторина окончена!\nПравильных: {quiz.correct}\nНеправильных: {quiz.wrong}"
        )
    await callback.answer()
