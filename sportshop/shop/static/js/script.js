let currentIndex = 0;
const slides = document.querySelectorAll('.images .slide');

function showSlide(index) {
    if (index < 0) {
        currentIndex = slides.length - 1;
    } else if (index >= slides.length) {
        currentIndex = 0;
    }

    slides.forEach((slide, i) => {
        if (i === currentIndex) {
            slide.style.display = 'block';
        } else {
            slide.style.display = 'none';
        }
    });
}

function changeSlide(direction) {
    currentIndex += direction;
    showSlide(currentIndex);
}

showSlide(currentIndex);
