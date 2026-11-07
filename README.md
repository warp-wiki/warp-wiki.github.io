# warp-wiki

Русскоязычная документация о Cloudflare WARP: что это такое, как работает туннель, чем WARP отличается от DNS 1.1.1.1 и почему он не предназначен для смены страны.

Сайт: https://eb-lan.github.io/warp-wiki.github.io/

## Устройство сайта

- `content/_index.md` — статья «Начало работы / Введение»; инструкций по установке WARP нет.
- `templates/` — шаблоны Hwaro.
- `static/css/site.css` — светлая и тёмная палитры с оранжевыми акцентами и адаптивная вёрстка.
- `static/css/typography.css` — Geist, Geist Mono и типографическая шкала по образцу документации Throne.
- `static/fonts/` — локальные файлы шрифтов; лицензия SIL OFL включена.
- `static/images/cloudflare.svg` — знак Cloudflare из Simple Icons (CC0).
- `.github/workflows/pages.yml` — сборка Hwaro v0.22.1, проверка и публикация на GitHub Pages при изменениях в `main`.

Типографический ориентир: https://throneproj.github.io/get_started/
Шрифты: https://github.com/throneproj/throneproj.github.io/tree/main/static/fonts
Знак: https://github.com/simple-icons/simple-icons/blob/develop/icons/cloudflare.svg

## Локальная проверка сайта

С установленным Hwaro v0.22.1 и Python 3.11+:

```bash
hwaro build
python3 scripts/check_site.py public
```

Для просмотра с автоматическим обновлением — `hwaro serve`. Результат сборки `public/` не коммитится.
