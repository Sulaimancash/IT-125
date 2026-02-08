from aiogram import Router, types
from aiogram.filters import Command
from core.roulette import RussianRouletteGame

class BotHandlers:
    def __init__(self, bot):
        self.router = Router()
        self.bot = bot
        self.roulette_games = {}

        self.register_handlers()

    def register_handlers(self):
        self.router.message.register(self.start_command, Command("start"))
        self.router.message.register(self.start_roulette, Command("roulette"))
        self.router.message.register(self.shoot_roulette, Command("shoot"))
        self.router.message.register(self.stop_roulette, Command("stop"))

    async def start_command(self, message: types.Message):
        await message.answer(
            "Привет 👋\n\n"
            "/roulette — начать русскую рулетку\n"
            "/shoot — выстрел\n"
            "/stop — остановить игру"
        )

    async def start_roulette(self, message: types.Message):
        user_id = message.from_user.id

        if user_id in self.roulette_games:
            await message.answer("Игра уже идёт!")
            return

        game = RussianRouletteGame("Игрок 1", "Игрок 2")
        self.roulette_games[user_id] = game

        await message.answer(
            "🎲 Русская рулетка началась!\n\n"
            "🔴 Игрок 1\n"
            "🔵 Игрок 2\n\n"
            "Первый ход: Игрок 1\n"
            "⏱ У тебя 5 секунд\n\n"
            "Нажми /shoot"
        )

    async def shoot_roulette(self, message: types.Message):
        user_id = message.from_user.id
        game = self.roulette_games.get(user_id)

        if not game:
            await message.answer("Сначала запусти игру: /roulette")
            return

        current_player = game.get_current_player()
        result = game.shoot()

        if result == "click":
            await message.answer(
                f"😮‍💨 Щёлк...\n"
                f"Ход переходит к: {game.get_current_player()}\n"
                f"⏱ 5 секунд"
            )

        elif result == "boom":
            await message.answer(f"💥 Бах!\n{current_player} проиграл!")
            del self.roulette_games[user_id]

        elif result == "time_over":
            await message.answer(f"⏰ Время вышло!\n{current_player} проиграл!")
            del self.roulette_games[user_id]

        elif result == "no_bullets":
            await message.answer("🤝 Патроны закончились. Ничья!")
            del self.roulette_games[user_id]

    async def stop_roulette(self, message: types.Message):
        user_id = message.from_user.id

        if user_id not in self.roulette_games:
            await message.answer("Игра не запущена")
            return

        del self.roulette_games[user_id]
        await message.answer("🛑 Игра остановлена")
