(() => {
  'use strict';
  const root = document.documentElement;
  const themeButton = document.getElementById('theme-toggle');
  const updateThemeButton = () => {
    const label = root.dataset.theme === 'dark' ? 'Включить светлую тему' : 'Включить тёмную тему';
    themeButton.setAttribute('aria-label', label);
    themeButton.title = label;
  };
  updateThemeButton();
  themeButton.addEventListener('click', () => {
    root.dataset.theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
    try { localStorage.setItem('warp-theme', root.dataset.theme); } catch (_) {}
    updateThemeButton();
  });
  window.addEventListener('storage', event => {
    if (event.key === 'warp-theme' && ['light', 'dark'].includes(event.newValue)) {
      root.dataset.theme = event.newValue;
      updateThemeButton();
    }
  });

  const menu = document.getElementById('mobile-menu');
  const menuButton = document.getElementById('menu-toggle');
  menuButton.addEventListener('click', () => {
    menu.showModal();
    root.classList.add('menu-open');
    menuButton.setAttribute('aria-expanded', 'true');
  });
  document.getElementById('menu-close').addEventListener('click', () => menu.close());
  menu.addEventListener('close', () => {
    root.classList.remove('menu-open');
    menuButton.setAttribute('aria-expanded', 'false');
  });
  menu.addEventListener('click', event => {
    if (event.target !== menu) return;
    const box = menu.getBoundingClientRect();
    if (event.clientX > box.right || event.clientY > box.bottom) menu.close();
  });
  window.matchMedia('(min-width: 801px)').addEventListener('change', event => {
    if (event.matches && menu.open) menu.close();
  });

  if (/Mac|iPhone|iPad/.test(navigator.platform)) {
    document.querySelectorAll('.search-button kbd').forEach(kbd => { kbd.textContent = '⌘ K'; });
  }

  if (navigator.clipboard && window.isSecureContext) {
    document.querySelectorAll('.prose pre').forEach(pre => {
      const code = pre.querySelector('code');
      if (!code) return;
      const button = document.createElement('button');
      button.type = 'button';
      button.className = 'copy-button';
      button.textContent = 'Копировать';
      button.setAttribute('aria-label', 'Скопировать пример кода');
      button.addEventListener('click', async () => {
        try {
          await navigator.clipboard.writeText(code.textContent);
          button.textContent = 'Скопировано ✓';
        } catch (_) {
          button.textContent = 'Выделите и скопируйте';
        }
        setTimeout(() => { button.textContent = 'Копировать'; }, 2000);
      });
      pre.prepend(button);
    });
  }

  const headings = Array.from(document.querySelectorAll('.prose h2[id], .prose h3[id]'));
  const tocLinks = Array.from(document.querySelectorAll('.toc a[href^="#"]'));
  if ('IntersectionObserver' in window && headings.length) {
    const observer = new IntersectionObserver(entries => {
      const visible = entries.filter(entry => entry.isIntersecting);
      if (!visible.length) return;
      const id = visible[0].target.id;
      tocLinks.forEach(link => {
        const active = decodeURIComponent(link.hash.slice(1)) === id;
        link.classList.toggle('active', active);
        if (active) link.setAttribute('aria-current', 'location');
        else link.removeAttribute('aria-current');
      });
    }, { rootMargin: '-90px 0px -55% 0px' });
    headings.forEach(heading => observer.observe(heading));
  }
})();
