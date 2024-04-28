function changeSlide(direction, cardIndex) {
    let currentIndex = 0; // Установка текущего индекса на 0

    // Получение списка слайдов для текущей карточки
    const cardSlides = document.querySelectorAll('.cards .card')[cardIndex].querySelectorAll('.images .slide');

    // Определение текущего индекса слайда для текущей карточки
    let currentSlideIndex = Array.from(cardSlides).findIndex(slide => slide.style.display === 'block');

    // Если текущий слайд не обнаружен, начать с первого слайда
    if (currentSlideIndex === -1) {
        currentSlideIndex = 0;
    }

    // Переключение индекса слайда в зависимости от направления
    currentSlideIndex += direction;

    // Проверка на выход за границы массива слайдов
    if (currentSlideIndex < 0) {
        currentSlideIndex = cardSlides.length - 1;
    } else if (currentSlideIndex >= cardSlides.length) {
        currentSlideIndex = 0;
    }

    // Отображение текущего слайда и скрытие остальных
    cardSlides.forEach((slide, i) => {
        if (i === currentSlideIndex) {
            slide.style.display = 'block';
        } else {
            slide.style.display = 'none';
        }
    });
}