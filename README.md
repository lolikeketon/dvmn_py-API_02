# Сокращение URL (vk.cc)

Скрипт для сокращения ссылок через VK (`vk.cc`) и просмотра количества переходов по уже сокращённой ссылке.

- Если передать обычный URL — получишь короткую ссылку `vk.cc/...`.
- Если передать уже сокращённую ссылку `vk.cc/...` — увидишь суммарное число кликов по ней.

## Требования

- Python 3.10+
- Установленные зависимости: `requests`, `python-dotenv`

## Установка

```bash
cd your-project

python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .\.venv\Scripts\Activate.ps1  # Windows PowerShell

python -m pip install -U pip
pip install requests python-dotenv
```

> Или с файлом зависимостей:
> ```bash
> echo "requests
python-dotenv" > requirements.txt
> pip install -r requirements.txt
> ```

## Настройка переменных окружения

Создай файл `.env` в корне проекта и добавь в него токен VK:

```env
VK_TOKEN=your_vk_token_here
```

## Запуск

Теперь скрипт запускается сразу с аргументом — ссылкой:

```bash
python main.py https://example.com
```

или

```bash
python main.py https://vk.cc/abcd12
```

### Примеры

**1) Сократить обычную ссылку**

```
$ python main.py https://example.com/some/long/path
Сокращённая ссылка: https://vk.cc/abcd12
```

**2) Посмотреть клики по короткой ссылке**

```
$ python main.py https://vk.cc/abcd12
Количество переходов по ссылке: 42
```

## Как это работает (внутри)

- `shorten_link(token, url)` — делает запрос в `utils.getShortLink`
- `count_clicks(token, url)` — запрашивает статистику `utils.getLinkStats`
- `is_shorten_link(token, url)` — проверяет, является ли ссылка сокращённой VK
- `main()` — загружает токен, парсит аргументы, определяет режим работы
