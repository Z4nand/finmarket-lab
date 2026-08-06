# PyTorch GPU

Шаблон основан на корневых `Dockerfile.pytorch` и `docker-compose.yml`, но запускает
JupyterLab сразу и использует современное поле Compose `gpus: all`.

```bash
cp .env.example .env
docker compose build
docker compose run --rm pytorch-gpu nvidia-smi
docker compose up
```

JupyterLab будет доступен на `http://localhost:8888`. При запуске Jupyter создаст
токен и напечатает полный URL в логах. Получить его можно командой
`docker compose logs pytorch-gpu`. Не публикуйте порт во внешнюю сеть без
дополнительной защиты.

## VS Code Dev Container

Установите расширение **Dev Containers**, откройте палитру команд (`Ctrl+Shift+P`)
и выберите **Dev Containers: Reopen in Container**. VS Code откроет `/workspace`
в том же контейнере, установит Python, Pylance, Jupyter и Docker extensions и
будет анализировать импорты через контейнерный Python.

После открытия ноутбука выберите локальное для контейнера ядро
**Python Environments → Python 3**. Подключать `Existing Jupyter Server` вручную
в этом режиме не требуется. Обычный `docker compose up` независимо от VS Code
продолжает сразу запускать JupyterLab.

Для shell вместо Jupyter:

```bash
docker compose run --rm pytorch-gpu bash
```
