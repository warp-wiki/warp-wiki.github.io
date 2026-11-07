+++
title = "Telegram и Youtube"
description = "Проверка DME и LED, поиск другой конечной точки WARP и обновление конфига."
weight = 7
toc = true
+++

## WARP подключён, но сервисы не работают

Если при подключении к **обычному WARP, без Relay**, Telegram или YouTube не работают, проверьте, через какой узел Cloudflare идёт соединение. Одна из возможных причин — маршрут через российский узел с фильтрацией трафика.

В [документации WARPSCOUT](https://github.com/vernette/warpscout/blob/master/README_RU.md#что-это) описана DPI-фильтрация трафика через московский узел **DME**: туннель подключается, но часть сайтов не открывается. Фильтрация ТСПУ — техническими средствами противодействия угрозам — может затрагивать трафик на сетевом маршруте. Это не означает, что оборудование ТСПУ принадлежит Cloudflare или установлено непосредственно в его дата-центре.

Сам по себе сбой Telegram или YouTube не доказывает подключение к DME: сначала проверьте код узла.

## Как проверить узел

1. Подключите WARP.
2. Откройте [cloudflare.com/cdn-cgi/trace](https://cloudflare.com/cdn-cgi/trace).
3. Найдите строку **`colo=`**.

| Значение | Узел |
| --- | --- |
| `colo=DME` | Москва; код связан с аэропортом Домодедово. |
| `colo=LED` | Санкт-Петербург. |

Если при проблемах с Telegram или YouTube видите **DME или LED**, попробуйте найти другую конечную точку через [WARPSCOUT](@/warpscout.md), исключив эти узлы.

`colo` показывает дата-центр Cloudflare, обслуживший именно этот запрос. Страница проверки должна открываться через WARP; при раздельной маршрутизации браузер может идти напрямую. Дополнительно сверяйте результат с колонкой **`NODE`** в WARPSCOUT.

## Найти точки без DME

Сначала установите WARPSCOUT и выполните регистрацию аккаунта, как описано в [быстром старте](@/warpscout.md). Запускайте сканирование из той сети, где будете пользоваться WARP.

**Windows:**

```powershell
.\warpscout.exe scan -p awg -P -exclude-node DME -best
```

**Linux, macOS и Termux:**

```sh
warpscout scan -p awg -P -exclude-node DME -best
```

`-exclude-node DME` убирает московский узел, `-P` проверяет туннель, а `-best` выводит один выбранный адрес в формате `IP:порт`.

## Исключить сразу DME и LED

Чтобы убрать оба узла, перечислите их через запятую.

**Windows:**

```powershell
.\warpscout.exe scan -p awg -P -exclude-node DME,LED -best
```

**Linux, macOS и Termux:**

```sh
warpscout scan -p awg -P -exclude-node DME,LED -best
```

## Вписать точку в конфиг

1. Скопируйте найденный WARPSCOUT адрес вместе с портом.
2. В конфиге WireGuard/AmneziaWG найдите параметр **`Endpoint`** в секции **`[Peer]`** и замените его значение найденной строкой `IP:порт`.
3. Сохраните конфиг, переподключите туннель и повторно проверьте Telegram, YouTube и строку `colo=`.

Если используете клиент с другим форматом профиля, измените адрес и порт конечной точки в его настройках.

Можно сразу создать новый конфиг AmneziaWG с лучшей найденной точкой без DME и LED.

**Windows:**

```powershell
.\warpscout.exe scan -p awg -P -exclude-node DME,LED -conf warp.conf
```

**Linux, macOS и Termux:**

```sh
warpscout scan -p awg -P -exclude-node DME,LED -conf warp.conf
```

Импортируйте полученный `warp.conf` в совместимый клиент. Если после смены точки проблема осталась, проверьте маршрутизацию приложения и доступность самого сервиса: другой узел не устраняет все возможные причины сбоя.

## Источники

- [WARPSCOUT: описание проблемы с DME](https://github.com/vernette/warpscout/blob/master/README_RU.md#что-это).
- [WARPSCOUT: фильтры узлов и конфиги](https://github.com/vernette/warpscout/blob/master/docs/ru/configs.md).
- [Cloudflare: проверка обслуживающего дата-центра через colo](https://developers.cloudflare.com/support/troubleshooting/general-troubleshooting/geographic-traffic-routing/).
