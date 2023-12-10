// JavaScript
document.addEventListener('DOMContentLoaded', function () {
    const ellipsisButtons = document.querySelectorAll('.ellipsis');
    const modal = document.getElementById('myModal');
    const modalContent = document.querySelector('.modal-content');

    ellipsisButtons.forEach(function (button) {
        button.addEventListener('click', function (event) {
            event.preventDefault();
            toggleModal(); // Відкриває або закриває модальне вікно
        });
    });

    // Закриття модального вікна при натисканні на "..."
    function toggleModal() {
        if (modal.style.display === 'block') {
            closeModal();
        } else {
            openModal();
        }
    }

    // Відображення модального вікна
    function openModal() {
        const button = document.querySelector('.ellipsis');
        const buttonRect = button.getBoundingClientRect();
        const modalWidth = modalContent.offsetWidth;

        const topPosition = buttonRect.bottom + window.scrollY + 10;
        const leftPosition = buttonRect.left + window.scrollX + buttonRect.width / 2 - modalWidth / 2;

        modal.style.top = `${topPosition}px`;
        modal.style.left = `${leftPosition}px`;
        modal.style.display = 'block';
    }

    // Закриття модального вікна
    function closeModal() {
        modal.style.display = 'none';
    }

    // Обробка зміни розмірів вікна для перерахування позиції під час прокрутки
    window.addEventListener('resize', function () {
        if (modal.style.display === 'block') {
            const button = document.querySelector('.ellipsis');
            const buttonRect = button.getBoundingClientRect();
            const modalWidth = modalContent.offsetWidth;

            const topPosition = buttonRect.bottom + window.scrollY + 10;
            const leftPosition = buttonRect.left + window.scrollX + buttonRect.width / 2 - modalWidth / 2;

            modal.style.top = `${topPosition}px`;
            modal.style.left = `${leftPosition}px`;
        }
    });
});
