+++
title = "Клиенты AmneziaWG"
description = "Приложения для Android, Windows, iOS и macOS со ссылками на загрузку."
weight = 3
toc = true
+++

Для подключения нужен клиент с поддержкой **AmneziaWG** и подходящий профиль. Конфиг для WARP можно получить способами из статьи [«Подключение в России»](@/russia.md).

Поддержка отдельных параметров AmneziaWG зависит от версии приложения и его сетевого ядра. Для приложений семейства Clash выбирайте соответствующий профиль генератора; обычный `.conf` не является универсальным форматом для всех клиентов.

## Android

| Клиент | Где скачать | Примечание |
| --- | --- | --- |
| WG Tunnel | [GitHub](https://github.com/wgtunnel/android) | Клиент WireGuard и AmneziaWG. |
| AmneziaWG | [Google Play](https://play.google.com/store/apps/details?id=org.amnezia.awg) | Отдельное приложение для протокола AmneziaWG. |
| AmneziaVPN | [Google Play](https://play.google.com/store/apps/details?id=org.amnezia.vpn) | VPN-клиент с поддержкой AmneziaWG. |
| FlClash | [GitHub](https://github.com/chen08209/FlClash) | Используйте профиль формата Clash с параметрами AmneziaWG. |
| NekoBox+ | [4PDA](https://4pda.to/forum/index.php?showtopic=1121122) | Для открытия страницы при ограничении доступа из РФ нужен VPN с выходом в другой стране. |
| ThroneForAndroid | [GitHub](https://github.com/throneproj/ThroneForAndroid) | Android-клиент проекта Throne. |

## Windows

| Клиент | Где скачать | Примечание |
| --- | --- | --- |
| WireSock | [Сайт проекта](https://www.wiresock.net/) | В генераторе предусмотрен отдельный формат для WireSock. |
| AmneziaVPN | [GitHub](https://github.com/amnezia-vpn/amnezia-client) | VPN-клиент с поддержкой AmneziaWG. |
| AmneziaWG | [GitHub](https://github.com/amnezia-vpn/amneziawg-windows-client) | Клиент AmneziaWG для Windows. |
| AmneziaWG (RomikB) | [Релизы на GitHub](https://github.com/RomikB/amneziawg-windows-client/releases) | Неофициальная сборка с патчем для Windows 7. |
| Clash Verge | [GitHub](https://github.com/clash-verge-rev/clash-verge-rev) | Проект Clash Verge Rev; используйте совместимое ядро и профиль Clash. |
| FlClash | [GitHub](https://github.com/chen08209/FlClash) | Профиль формата Clash с параметрами AmneziaWG. |
| WG Tunnel | [GitHub](https://github.com/wgtunnel/desktop) | Настольный клиент WireGuard и AmneziaWG. |
| Throne | [GitHub](https://github.com/throneproj/Throne) | Настольный клиент с поддержкой AmneziaWG. |

## iOS

| Клиент | Где скачать | Примечание |
| --- | --- | --- |
| AmneziaWG | [App Store](https://apps.apple.com/ru/app/amneziawg/id6478942365) | Отдельное приложение для протокола AmneziaWG. |
| DefaultVPN | [App Store](https://apps.apple.com/us/app/defaultvpn/id6744725017) | Поддерживает AmneziaWG и импорт `.conf`. |
| AmneziaVPN | [App Store](https://apps.apple.com/us/app/amneziavpn/id1600529900) | Недоступен в регионе РФ. |
| Clash Mi | [App Store](https://apps.apple.com/us/app/clash-mi/id6744321968) | Используйте совместимую версию ядра и профиль формата Clash. |
| Shadowrocket | [App Store](https://apps.apple.com/us/app/shadowrocket/id932747118) | Поддержка параметров зависит от версии приложения. |

## macOS

| Клиент | Где скачать | Примечание |
| --- | --- | --- |
| AmneziaWG | [App Store](https://apps.apple.com/ru/app/amneziawg/id6478942365) | Приложение для iPhone, iPad и Mac. |
| Clash Mi | [Сайт проекта](https://clashmi.app/download) | Выберите сборку для macOS и совместимый профиль Clash. |
| Clash Verge | [GitHub](https://github.com/clash-verge-rev/clash-verge-rev) | Проект Clash Verge Rev. |
| FlClash | [GitHub](https://github.com/chen08209/FlClash) | Профиль формата Clash с параметрами AmneziaWG. |
| Throne | [GitHub](https://github.com/throneproj/Throne) | Настольный клиент с поддержкой AmneziaWG. |

## Совместимость профилей

Наличие AmneziaWG в клиенте не означает поддержку всех версий и всех параметров протокола. При выборе приложения учитывайте **формат конфига, версию AmneziaWG и версию сетевого ядра**. Источник загрузки и документация проекта указаны в каждой строке таблиц.

Дополнительно: [официальный список альтернативных клиентов Amnezia](https://docs.amnezia.org/documentation/alternative-clients/) и [параметры AmneziaWG в Mihomo](https://wiki.metacubex.one/en/config/proxies/wg/).

Иконки платформ — [Font Awesome Free](https://fontawesome.com/), лицензия [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
