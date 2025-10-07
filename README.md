# Сокращение URL (vk.cc)

Скрипт для сокращения ссылок через VK (`vk.cc`) и просмотра количества переходов по уже сокращённой ссылке.

- Если ввести обычный URL — получишь короткую ссылку `vk.cc/...`.
- Если ввести уже сокращённую ссылку `vk.cc/...` — увидишь суммарное число кликов по ней.

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
> echo "requests\npython-dotenv" > requirements.txt
> pip install -r requirements.txt
> ```

## Настройка переменных окружения

Создай файл `.env` в корне проекта и добавь в него токен VK:

```env
VK_API=vk1.a.your_long_access_token_here
```

## Запуск

```bash
python main.py
```

Скрипт спросит ссылку во вводе.

### Примеры

**1) Сократить обычную ссылку**

```
$ python main.py
Введите ссылку: https://example.com/some/long/path
Сокращённая ссылка: https://vk.cc/abcd12
```

**2) Посмотреть клики по короткой ссылке**

```
$ python main.py
Введите ссылку: https://vk.cc/abcd12
Количество переходов по ссылке: 42
```

## Как это работает (внутри)

- `shorten_link(token, url)` — делает запрос в `utils.getShortLink`
- `count_clicks(token, url)` — запрашивает статистику `utils.getLinkStats`
- `is_shorten_link(url)` — проверяет домен `vk.cc`
- `main()` — управляет вводом/выводом и логикой
- 