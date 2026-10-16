// Переключение страниц
function navigateTo(pageId) {
    // Скрываем все вкладки
    const tabs = document.querySelectorAll('.tab-content');
    tabs.forEach(tab => tab.classList.remove('active'));

    // Показываем нужную страницу
    const selectedTab = document.getElementById(`page-${pageId}`);
    if (selectedTab) {
        selectedTab.classList.add('active');
    }

    // Подсвечиваем активную кнопку навигации
    const buttons = document.querySelectorAll('.nav-btn');
    buttons.forEach(btn => {
        if (btn.getAttribute('data-page') === pageId) {
            btn.classList.add('active');
        } else {
            btn.classList.remove('active');
        }
    });

    // Прокрутка наверх при переходе
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Калькулятор КБЖУ
function calculateCalories() {
    const age = parseFloat(document.getElementById('calcAge').value) || 0;
    const weight = parseFloat(document.getElementById('calcWeight').value) || 0;
    const height = parseFloat(document.getElementById('calcHeight').value) || 0;

    if (!age || !weight || !height) {
        alert('Пожалуйста, заполните все поля!');
        return;
    }

    // Формула Миффлина-Сан Жеора
    const bmr = Math.round(10 * weight + 6.25 * height - 5 * age + 5);
    const maintenance = Math.round(bmr * 1.375);

    const resultBox = document.getElementById('calcResult');
    const kcalVal = document.getElementById('kcalVal');

    kcalVal.textContent = `${maintenance} ккал`;
    resultBox.classList.remove('hidden');
}

// Добавление товара в корзину
function addToCart() {
    alert('Товар успешно добавлен в корзину!');
}

// Проверка ответа в квизе
function checkAnswer(isCorrect, element) {
    const res = document.getElementById('quizRes');
    res.classList.remove('hidden', 'correct', 'wrong');

    if (isCorrect) {
        res.textContent = 'Правильно! 👍 В футболе на поле выходит 11 игроков.';
        res.classList.add('correct');
    } else {
        res.textContent = 'Неверно, попробуйте еще раз! ❌';
        res.classList.add('wrong');
    }
}

// Отправка формы контактов
function sendMessage() {
    alert('Спасибо за ваше сообщение! Мы ответим вам в ближайшее время.');
}