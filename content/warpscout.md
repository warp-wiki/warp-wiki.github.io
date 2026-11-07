+++
title = "WARPSCOUT"
description = "Поиск рабочих конечных точек Cloudflare WARP, проверка туннеля и создание конфига."
weight = 6
toc = true
+++

## Что такое WARPSCOUT

**[WARPSCOUT](https://github.com/vernette/warpscout)** — программа для поиска конечных точек Cloudflare WARP, доступных из вашей сети. Она перебирает адреса, проверяет соединение, показывает узел Cloudflare и определяемый регион выхода. Для найденной точки можно сразу сохранить готовый конфиг.

Программа работает без TUN-интерфейса и прав администратора. Сканировать лучше из той сети, в которой вы будете подключаться: результаты для домашнего Wi-Fi и мобильного интернета могут отличаться.

У каждого блока команд на этой странице есть кнопка **«Копировать»**. Команды выполняются в терминале на вашем устройстве.

## Установка и запуск

### Windows

На [странице релизов WARPSCOUT](https://github.com/vernette/warpscout/releases) скачайте архив `warpscout_..._windows_amd64.zip`, распакуйте и откройте терминал в папке с `warpscout.exe`.

Проверьте запуск:

```powershell
.\warpscout.exe version
```

### Linux, macOS, OpenWrt и Termux

Официальный установщик сам выбирает сборку для системы:

```sh
curl -fsSL https://raw.githubusercontent.com/vernette/warpscout/master/install.sh | sh
```

Если в системе нет `curl`, можно использовать `wget`:

```sh
wget -qO- https://raw.githubusercontent.com/vernette/warpscout/master/install.sh | sh
```

Проверка установленной версии:

```sh
warpscout version
```

Для обновления повторно запустите установщик.

### Android

Для Android есть отдельное приложение **[WARPSCOUT for Android](https://github.com/openwarpkit/warpscout-android)** от OpenWarpKit. Оно позволяет регистрировать WARP-аккаунт, сканировать конечные точки и экспортировать конфиги через графический интерфейс.

APK можно скачать на [странице Android-релизов](https://github.com/openwarpkit/warpscout-android/releases). Выберите сборку для архитектуры устройства или универсальный APK. Это самостоятельный проект OpenWarpKit на основе WARPSCOUT CLI.

### Устройства Apple

- **iPhone и iPad:** отдельная версия WARPSCOUT для **iOS и iPadOS** в указанных проектах не представлена. Запустить описанные здесь команды прямо в iOS-приложении WARPSCOUT нельзя.
- **Mac:** консольный WARPSCOUT поддерживает **macOS**. В [релизах оригинального проекта](https://github.com/vernette/warpscout/releases) есть сборки `darwin_arm64` для Apple Silicon и `darwin_amd64` для Intel. Для них подходят инструкции по macOS на этой странице.

## Быстрый старт на Windows

### 1. Зарегистрировать аккаунт WARP

```powershell
.\warpscout.exe register
```

Появится файл `warpscout-account.json`. Он нужен для сканирования и последующего создания конфигов. Содержит приватные ключи и токены — храните его у себя и не публикуйте.

Остальные команды запускайте из той же папки, чтобы программа нашла файл аккаунта.

### 2. Найти доступные конечные точки

```powershell
.\warpscout.exe scan -p awg -P
```

`-p awg` выбирает AmneziaWG. Флаг `-P` дополнительно проверяет пинг и потери **внутри туннеля**: одного успешного подключения недостаточно, чтобы считать точку рабочей.

### 3. Вывести один лучший адрес

```powershell
.\warpscout.exe scan -p awg -P -best
```

Вместо таблицы программа напечатает выбранный адрес в формате `IP:порт`.

Если нужно исключить московский узел `DME`, используйте:

```powershell
.\warpscout.exe scan -p awg -P -exclude-node DME -best
```

### 4. Сохранить конфиг AmneziaWG

```powershell
.\warpscout.exe scan -p awg -P -exclude-node DME -conf warp.conf
```

Программа выберет подходящую точку и запишет конфиг в `warp.conf`. Импортируйте его в [совместимый клиент AmneziaWG](@/clients.md). Исключение `DME` в этом примере необязательно: уберите `-exclude-node DME`, если фильтр вам не нужен.

## Быстрый старт на Linux, macOS и Termux

Последовательно выполните команды из одного каталога.

Регистрация:

```sh
warpscout register
```

Сканирование с проверкой туннеля:

```sh
warpscout scan -p awg -P
```

Сохранение конфига с исключением `DME`:

```sh
warpscout scan -p awg -P -exclude-node DME -conf warp.conf
```

В остальных примерах для Windows заменяйте `.\warpscout.exe` на `warpscout`.

## Как читать результаты

| Поле | Значение |
| --- | --- |
| `NODE` | Код узла Cloudflare, например `FRA`, `ARN` или `DME`. |
| `NODE LOCATION` | Местоположение этого узла. |
| `SEEN AS` | Какой регион определяется при проверке выхода через туннель. |
| `ENDPOINT PING` | Задержка до самой конечной точки. |
| `TUN PING` | Пинг внутри туннеля, измеряемый с `-P`. |
| `LOSS` | Потери пакетов внутри туннеля; ориентируйтесь на `0%`. |
| `SPEED` | Результат замера скорости, если добавлен `-speed`. |

**Страна узла и регион выхода — разные параметры.** Узел за границей не гарантирует, что сайты определят вас как пользователя этой страны. Фильтр `-country` отбирает точки по стране узла; он не является гарантированной сменой страны для сайтов.

Отметка `torn down` означает, что туннель оборвался во время проверки. Такие точки исключаются из результатов `-best` и `-conf`.

## Полезные команды

### Проверить скорость внутри туннеля

```powershell
.\warpscout.exe scan -p awg -P -speed
```

Замеры увеличивают время сканирования. Сам флаг `-speed` добавляет измерение, но не переключает сортировку на скорость.

### Сохранить профиль для Mihomo / Clash

```powershell
.\warpscout.exe scan -p awg -P -conf warp.yaml -conf-type mihomo
```

### Отобрать узлы в Германии и Нидерландах

```powershell
.\warpscout.exe scan -p awg -P -country DE,NL -best
```

### Посмотреть справку по сканированию

```powershell
.\warpscout.exe scan -h
```

## Если точки не находятся

Если обычный WireGuard не проходит через фильтрацию, используйте `-p awg`. Если и с ним нет результата, попробуйте другой начальный маскировочный пакет:

```powershell
.\warpscout.exe scan -p awg -P -gen-i1 quic
```

Другие варианты `-gen-i1`: `dns`, `sip`, `stun`, `random`.

Автоматический поиск подходящих параметров AmneziaWG:

```powershell
.\warpscout.exe find-junk -gen-i1 random
```

После подбора программа покажет команду с найденными параметрами. Этот поиск сам по себе не заменяет проверку найденных точек с `-P`.

## Документация проекта

- [Исходный проект WARPSCOUT](https://github.com/vernette/warpscout).
- [Оригинальный быстрый старт на русском](https://github.com/vernette/warpscout/blob/master/README_RU.md#быстрый-старт).
- [Регистрация и файл аккаунта](https://github.com/vernette/warpscout/blob/master/docs/ru/account.md).
- [Форматы конфигов и фильтры](https://github.com/vernette/warpscout/blob/master/docs/ru/configs.md).
- [Подбор маскировки и решение проблем](https://github.com/vernette/warpscout/blob/master/docs/ru/blocking.md).

Примеры команд подготовлены по документации WARPSCOUT. Проект распространяется по [лицензии MIT](https://github.com/vernette/warpscout/blob/master/LICENSE), © 2026 Nikita S.
