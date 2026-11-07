+++
title = "MASQUE"
description = "Ещё один транспорт для подключения к Cloudflare WARP: принцип работы и варианты использования."
weight = 9
toc = true
+++

## Что такое MASQUE

**MASQUE** — технологии передачи сетевого трафика через HTTP-соединение. Cloudflare использует MASQUE для создания защищённого туннеля между устройством и своей сетью.

**К Cloudflare WARP можно подключаться через MASQUE.** Это ещё один транспорт WARP наряду с WireGuard; в актуальных официальных приложениях Cloudflare MASQUE уже используется для передачи трафика.

## Как он работает

Клиент упаковывает трафик в туннель до Cloudflare. После этого Cloudflare передаёт его к нужному сервису, а ответы возвращаются через туннель. В основном варианте используются HTTP/3 и QUIC, работающий поверх UDP.

В [WARPSCOUT](@/warpscout.md) доступны два варианта подключения:

| Режим | Транспорт |
| --- | --- |
| `masque` | HTTP/3 / QUIC поверх UDP. |
| `masque-h2` | HTTP/2 поверх TCP с TLS. |

Вариант HTTP/2 можно попробовать, если в вашей сети ограничивается UDP или не устанавливается соединение по другим транспортам. Работоспособность зависит от сети: MASQUE не гарантирует обход любой блокировки.

## Чем отличается от AmneziaWG

AmneziaWG основан на WireGuard и использует свои параметры маскировки. MASQUE использует другой способ туннелирования и отдельные конечные точки Cloudflare.

Для MASQUE нужен **клиент с поддержкой MASQUE**. Форматы конфигов также отличаются: например, WARPSCOUT создаёт JSON для [usque](https://github.com/Diniboy1123/usque) или профиль для [Mihomo](https://github.com/MetaCubeX/mihomo).

Смена транспорта не добавляет WARP выбор страны и сама по себе не обеспечивает обход [белых списков](@/whitelists.md) мобильного интернета.

## Клиенты с поддержкой MASQUE

Для подключения к Cloudflare WARP через MASQUE можно использовать:

- [NekoBox+](https://4pda.to/forum/index.php?showtopic=1121122).
- [Throne](https://github.com/throneproj/Throne).
- Любой клиент на базе [Mihomo](https://github.com/MetaCubeX/mihomo), если в нём используется актуальная версия ядра с поддержкой MASQUE.

Используйте актуальную версию приложения и конфиг MASQUE, подходящий для выбранного клиента. Поддержка протокола в Mihomo описана в [документации ядра](https://wiki.metacubex.one/ru/config/proxies/masque/).

## Генерация конфигов и Relay

В [Telegram-боте @warp_generator_bot](https://t.me/warp_generator_bot) и на [сайте генератора](https://warp-generation.github.io/) также доступна **генерация конфигов MASQUE для клиентов с ядром Mihomo**. Полученный конфиг можно импортировать в совместимый клиент.

**К [Relay-серверам](@/relay.md) также можно подключаться через MASQUE.** Для этого используйте конфиг Relay с протоколом MASQUE, полученный в боте или на сайте.

## Проверка через WARPSCOUT

Установка программы описана в [статье WARPSCOUT](@/warpscout.md). Команды ниже — для Linux, macOS и Termux. В Windows вместо `warpscout` используйте `.\warpscout.exe`.

Если аккаунт ещё не подготовлен, выполните регистрацию: она также пытается создать данные для MASQUE.

```sh
warpscout register
```

Сканирование конечных точек через QUIC:

```sh
warpscout scan -p masque
```

Сканирование через HTTP/2:

```sh
warpscout scan -p masque-h2
```

Если соединение не устанавливается, можно подобрать **SNI** — имя хоста, используемое при установке защищённого соединения:

```sh
warpscout find-sni -p masque-h2
```

Программа выведет команду сканирования с найденным SNI. Используйте её; подходящий SNI для QUIC и HTTP/2 может различаться.

## Сохранение конфига

Профиль для usque:

```sh
warpscout scan -p masque-h2 -conf usque.json
```

Профиль для Mihomo:

```sh
warpscout scan -p masque-h2 -conf warp.yaml -conf-type mihomo
```

Если ранее был подобран SNI, добавьте к команде параметр `-masque-sni` с найденным именем. При создании конфига usque WARPSCOUT также показывает команду его запуска.

По документации WARPSCOUT, все точки одного MASQUE-сканирования проходят через одну ноду, определяемую вашей сетью. Поэтому подбор ноды перебором адресов здесь работает иначе, чем в примерах для AmneziaWG; фильтры `-node` и `-country` для MASQUE не поддерживаются.

## Источники

- [Cloudflare: режимы клиента WARP](https://developers.cloudflare.com/warp-client/warp-modes/).
- [Cloudflare: переход приложений WARP на MASQUE](https://blog.cloudflare.com/masque-now-powers-1-1-1-1-and-warp-apps-dex-available-with-remote-captures/).
- [WARPSCOUT: MASQUE, SNI и форматы конфигов](https://github.com/vernette/warpscout/blob/master/docs/ru/masque.md).
