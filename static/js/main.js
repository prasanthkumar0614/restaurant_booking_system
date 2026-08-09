document.addEventListener('DOMContentLoaded', function () {

    // Remove initial load class (in case anything depends on it)
    document.body.classList.remove('page-loading');

    // ---- Scroll progress bar ----
    const progressBar = document.getElementById('scrollProgress');
    function updateProgress() {
        const scrollTop = window.scrollY;
        const docHeight = document.documentElement.scrollHeight - window.innerHeight;
        const pct = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
        if (progressBar) progressBar.style.width = pct + '%';
    }
    window.addEventListener('scroll', updateProgress);
    updateProgress();

    // ---- Header solidifies on scroll ----
    const header = document.querySelector('.site-header');
    if (header) {
        window.addEventListener('scroll', function () {
            header.classList.toggle('scrolled', window.scrollY > 30);
        });
    }

    // ---- Floating bubbles inside hero ----
    const hero = document.querySelector('.hero');
    if (hero) {
        for (let i = 0; i < 10; i++) {
            const bubble = document.createElement('span');
            bubble.className = 'bubble';
            const size = 10 + Math.random() * 30;
            bubble.style.width = size + 'px';
            bubble.style.height = size + 'px';
            bubble.style.left = Math.random() * 100 + '%';
            bubble.style.bottom = '-40px';
            bubble.style.animationDuration = (6 + Math.random() * 8) + 's';
            bubble.style.animationDelay = (Math.random() * 6) + 's';
            hero.appendChild(bubble);
        }
    }

    // ---- Scroll-reveal with stagger ----
    const targets = document.querySelectorAll(
        'main h2, main h3, .info-card, main > div[style*="border"], .site-main div[style*="border"], table, main > p, main > ul, main > li'
    );
    targets.forEach(function (el, i) {
        el.classList.add('reveal');
        el.style.transitionDelay = (Math.min(i, 8) * 0.08) + 's';
    });

    const observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.reveal').forEach(function (el) {
        observer.observe(el);
    });

    // ---- Ripple effect on every button click ----
    document.addEventListener('click', function (e) {
        const btn = e.target.closest('button, .btn-primary, .btn-outline');
        if (!btn) return;
        const rect = btn.getBoundingClientRect();
        const ripple = document.createElement('span');
        const size = Math.max(rect.width, rect.height);
        ripple.className = 'ripple';
        ripple.style.width = ripple.style.height = size + 'px';
        ripple.style.left = (e.clientX - rect.left - size / 2) + 'px';
        ripple.style.top = (e.clientY - rect.top - size / 2) + 'px';
        btn.style.position = btn.style.position || 'relative';
        btn.appendChild(ripple);
        setTimeout(function () { ripple.remove(); }, 650);
    });

    // ---- Auto-remove toast messages after animation ----
    document.querySelectorAll('.toast').forEach(function (toast) {
        setTimeout(function () { toast.remove(); }, 5000);
    });

    // ---- Scroll-to-top button ----
    const btn = document.createElement('button');
    btn.id = 'scrollTopBtn';
    btn.innerHTML = '&uarr;';
    btn.setAttribute('aria-label', 'Scroll to top');
    document.body.appendChild(btn);

    window.addEventListener('scroll', function () {
        btn.classList.toggle('show', window.scrollY > 300);
    });

    btn.addEventListener('click', function () {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

});