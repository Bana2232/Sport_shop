document.addEventListener('DOMContentLoaded', function () {
const counters = document.querySelectorAll('.counter');

counters.forEach(function (counter) {
    const decrementButton = counter.querySelector('.decrement');
    const incrementButton = counter.querySelector('.increment');
    const counterValue = counter.querySelector('.counter-value');

    let count = counterValue.textContent;
    const maxCount = 20;

    decrementButton.addEventListener('click', function () {
    count = Math.max(0, count - 1);
    counterValue.textContent = count;
    });

    incrementButton.addEventListener('click', function () {
    if (count < maxCount) {
      count++;
      counterValue.textContent = count;
    }
    });
});
});
