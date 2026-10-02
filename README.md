# Finmarket Lab

Лаборатория для экспериментов с рыночными данными: получение стакана Bybit, запись сообщений и визуализация в Jupyter. Окружение запускается в Docker с поддержкой GPU.

## Сборка и запуск

Нужны Docker с Compose и доступом к NVIDIA GPU. На Windows используется Docker Desktop с WSL 2 и установленным драйвером NVIDIA.

Команды необходимо выполнять на компьютере из корня проекта:

```bash
# Создать локальные настройки (при первом запуске).
cp .env.example .env

# Собрать образ и установить зависимости из requirements.txt.
docker compose build

# Проверить доступ к GPU во временном контейнере.
docker compose run --rm pytorch-gpu nvidia-smi

# Запустить контейнер с JupyterLab.
docker compose up
```

JupyterLab доступен по адресу http://localhost:8888. Порт можно изменить через `JUPYTER_PORT` в `.env`. Ссылка с токеном входа выводится при запуске и доступна в логах:

```bash
docker compose logs pytorch-gpu
```

## Установка пакета проекта

В другом терминале на компьютере открыть оболочку работающего контейнера:

```bash
docker compose exec pytorch-gpu bash
```

Внутри контейнера выполнить:

```bash
cd /workspace
pip install -e . --break-system-packages
```

`-e .` устанавливает проект в editable-режиме: изменения Python-кода доступны без повторной установки. Флаг `--break-system-packages` разрешает установку в системное Python-окружение контейнера. После пересоздания контейнера установку проекта необходимо повторить.

## Работа

- В VS Code открыть корень проекта и выполнить **Dev Containers: Reopen in Container**, затем выбрать **Python / GPU** или **Frontend**. При изменении образа использовать **Dev Containers: Rebuild and Reopen in Container**.
- **Python / GPU** (`.devcontainer/python/devcontainer.json`) открывает весь проект в `/workspace` и запускает сервис `pytorch-gpu`. Установку Python-пакета можно выполнить в терминале этого окна.
- **Frontend** (`.devcontainer/frontend/devcontainer.json`) открывает весь проект в `/workspace` и запускает сервисы `frontend` и `api`. Vite работает из `/workspace/frontend`; для команд npm в терминале перейти в эту папку: `cd /workspace/frontend`. Страница доступна по адресу http://localhost:5173.
- Для одновременной работы открыть корень проекта в двух окнах VS Code и выбрать разные конфигурации. При закрытии окон контейнеры продолжают работать (`shutdownAction: none`). Остановить их из терминала Windows в корне проекта командой `docker compose stop`.
- Для Python-файлов выбрать интерпретатор `/usr/bin/python`, для ноутбуков — ядро этого окружения.
- `notebooks/` — исследовательские ноутбуки; `examples/` — небольшие запускаемые примеры; `src/finmarket_lab/` — код проекта; `data/` — данные.
- Корень проекта подключён к `/workspace`: изменения файлов в контейнере сохраняются на компьютере.

Для запуска примера стакана в ноутбуке:

```python
%cd /workspace
from examples.demo_orderbook_realtime import main

main()
```

Рабочая папка `/workspace` нужна, чтобы относительные пути записи вели в общую папку `data/`, а не в `notebooks/data/`. Пример работает непрерывно; для полной остановки его фоновых потоков необходимо перезапустить ядро ноутбука.

## Остановка и обновление окружения

Остановить запуск в терминале можно через `Ctrl+C`. Остановить сервисы и удалить контейнеры проекта:

```bash
docker compose down
```

Файлы проекта и данные в подключённой папке сохранятся. После изменения `requirements.txt` или `Dockerfile` пересобрать и запустить окружение:

```bash
docker compose up --build
```
