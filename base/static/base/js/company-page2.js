
const hiddenElements = document.querySelectorAll('.hidden');
hiddenElements.forEach((el) => observer.observe(el))

document.addEventListener('DOMContentLoaded', () => {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add('show2');
            } else {
                entry.target.classList.remove('show2');
            }
        });
    });

    const hiddenElements = document.querySelectorAll('.hidden2');
    hiddenElements.forEach((el) => observer.observe(el));
});