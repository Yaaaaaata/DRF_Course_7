## Курсовая 7. DRF 

### Контекст

В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек. Заказчик прочитал книгу, впечатлился и обратился к вам с запросом реализовать трекер полезных привычек.

В рамках учебного курсового проекта реализуйте бэкенд-часть SPA веб-приложения.


## Описание задач

- Добавьте необходимые модели привычек.
- Реализуйте эндпоинты для работы с фронтендом.
- Создайте приложение для работы с Telegram и рассылками напоминаний.


### Модели
В книге хороший пример привычки описывается как конкретное действие, которое можно уложить в одно предложение:

я буду [ДЕЙСТВИЕ] в [ВРЕМЯ] в [МЕСТО]

За каждую полезную привычку необходимо себя вознаграждать или сразу после делать приятную привычку. Но при этом привычка не должна расходовать на выполнение больше 2 минут. Исходя из этого получаем первую модель — Привычка.

### Привычка:
- Пользователь — создатель привычки.
- Место — место, в котором необходимо выполнять привычку.
- Время — время, когда необходимо выполнять привычку.
- Действие — действие, которое представляет из себя привычка.
- Признак приятной привычки — привычка, которую можно привязать к выполнению полезной привычки.
- Связанная привычка — привычка, которая связана с другой привычкой, важно указывать для полезных привычек, но не для приятных.
- Периодичность (по умолчанию ежедневная) — периодичность выполнения привычки для напоминания в днях.
- Вознаграждение — чем пользователь должен себя вознаградить после выполнения.
- Время на выполнение — время, которое предположительно потратит пользователь на выполнение привычки.
- Признак публичности — привычки можно публиковать в общий доступ, чтобы другие пользователи могли брать в пример чужие привычки.
- Обратите внимание, что в проекте у вас может быть больше, чем одна описанная здесь модель.

### Валидаторы

- Исключить одновременный выбор связанной привычки и указания вознаграждения.
- Время выполнения должно быть не больше 120 секунд.
- В связанные привычки могут попадать только привычки с признаком приятной привычки.
- У приятной привычки не может быть вознаграждения или связанной привычки.
- Нельзя выполнять привычку реже, чем 1 раз в 7 дней.

### Пагинация

Для вывода списка привычек реализовать пагинацию с выводом по 5 привычек на страницу.

### Права доступа

Каждый пользователь имеет доступ только к своим привычкам по механизму CRUD.
Пользователь может видеть список публичных привычек без возможности их как-то редактировать или удалять.

### Эндпоинты

- Регистрация
- Авторизация
- Список привычек текущего пользователя с пагинацией
- Список публичных привычек
- Создание привычки
- Редактирование привычки
- Удаление привычки

### Интеграция

Для полноценной работы сервиса необходим реализовать работу с отложенными задачами для напоминания о том, в какое время какие привычки необходимо выполнять.

Для этого потребуется интегрировать сервис с мессенджером Telegram, который будет заниматься рассылкой уведомлений.

### Безопасность

Для проекта необходимо настроить CORS, чтобы фронтенд мог подключаться к проекту на развернутом сервере.

### Документация

Для реализации экранов силами фронтенд-разработчиков необходимо настроить вывод документации. При необходимости эндпоинты, на которые документация не будет сгенерирована автоматически, описать вручную.

***Старт***

Win -> `python manage.py`

Linux -> `python3 manage.py`

***Запуск тестов***

Win -> `python manage.py test`

Linux -> `python3 manage.py test`

***ENV***

> Необходимо прописать переменные окружения 
> для подключения к базе данных Postgres:

`POSTGRES_DB`
`POSTGRES_USER`
`POSTGRES_PASSWORD`
`POSTGRES_HOST`
`POSTGRES_PORT`

`SECRET_KEY`

`CHAT_ID_ADMIN`
`ADMIN_PASSWORD`
`TELEGRAM_BOT_TOKEN`

`CELERY_BROKER_URL`
`CELERY_RESULT_BACKEND`

 Файл `.env` должен находиться в корне проекта.

### В проекте используется Docker Compose

* Установите Docker, следуя инструкциям для вашей операционной
  системы: [Docker Install](https://docs.docker.com/get-docker/).
* Установите Docker Compose: [Docker Compose Install](https://docs.docker.com/compose/install/).

Для запуска приложения необходимо выполнить следующие команды: 
* ***docker-compose build*** - сборка образа
* ***docker-compose up*** - запуск контейнера

Вот пошаговая инструкция:

1. Откройте командную строку или терминал и перейдите в директорию, где находится файл docker-compose.yml.

2. Запустите команду docker-compose up. Docker Compose будет читать файл docker-compose.yml и создавать и запускать контейнеры, описанные в этом файле.

3. По умолчанию, команда docker-compose up будет выводить логи контейнеров в текущем терминале. Чтобы запустить контейнеры в фоновом режиме, используйте флаг -d, например: docker-compose up -d.

4. Docker Compose создаст и запустит все контейнеры, описанные в файле docker-compose.yml. Вы сможете видеть логи работы контейнеров и контролировать их состояние.

5. Чтобы остановить контейнеры, используйте команду docker-compose down. Эта команда остановит и удалит все контейнеры, созданные с помощью docker-compose.yml.