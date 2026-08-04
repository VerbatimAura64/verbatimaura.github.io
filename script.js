document.addEventListener('DOMContentLoaded', function () {
    var toggle = document.querySelector('.nav-toggle');
    var links = document.querySelector('.nav-links');

    if (toggle && links) {
        toggle.addEventListener('click', function () {
            var isOpen = links.classList.toggle('is-open');
            toggle.setAttribute('aria-expanded', isOpen);
        });

        links.querySelectorAll('a').forEach(function (a) {
            a.addEventListener('click', function () {
                links.classList.remove('is-open');
                toggle.setAttribute('aria-expanded', 'false');
            });
        });
    }

    document.querySelectorAll('.nav-more-btn').forEach(function (btn) {
        btn.addEventListener('click', function (e) {
            e.stopPropagation();
            btn.parentElement.classList.toggle('open');
        });
    });

    window.addEventListener('click', function () {
        document.querySelectorAll('.nav-more.open').forEach(function (el) {
            el.classList.remove('open');
        });
    });
});
