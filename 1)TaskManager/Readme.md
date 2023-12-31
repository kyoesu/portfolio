## ТЗ:

## Название проекта: ***Task Manager***

### Описание проекта:

Task Manager - это веб-приложение, которое позволяет пользователям создавать, редактировать и отслеживать свои задачи. Пользователи могут создавать учетные записи, входить в систему и управлять своими задачами. Приложение должно предоставлять удобный и интуитивно понятный интерфейс для работы с задачами.

### Функциональные требования:

#### Регистрация и аутентификация:
* Пользователи могут создавать учетные записи с помощью электронной почты и пароля.
* Пользователи должны иметь возможность войти в систему с помощью своих учетных данных.

#### Создание задач:
* Пользователи могут создавать новые задачи, указывая заголовок, описание и срок выполнения.
* Задачи должны иметь статус (например, "в ожидании", "в работе", "завершено").

#### Управление задачами:
* Пользователи могут просматривать список всех своих задач.
* Пользователи могут фильтровать задачи по статусу и сортировать их по дате создания или сроку выполнения.
* Пользователи могут редактировать или удалять свои задачи.

### Технические требования:
#### Backend:
* Используйте Python с фреймворком Django или Flask для создания backend-части приложения.
* Реализуйте API для обработки запросов от фронтенда, включая функции регистрации, аутентификации и управления задачами.
* Используйте базу данных (например, PostgreSQL или SQLite) для хранения информации о пользователях и задачах.
#### Frontend:
* Разработайте интуитивно понятный и отзывчивый интерфейс для работы с задачами.
* Используйте HTML, CSS и JavaScript для создания пользовательского интерфейса.
* Используйте фронтенд-фреймворк (например, React или Angular) для упрощения разработки интерфейса.

### Аутентификация и безопасность:
* Реализуйте механизм аутентификации и авторизации пользователей.
* Обеспечьте безопасность передачи данных между клиентом и сервером с помощью шифрования (например, HTTPS).

### Дополнительные требования:
* Добавьте возможность установки приоритета задач.
* Реализуйте функцию напоминаний или уведомлений о приближающихся сроках выполнения задач.

## На данный момент сделано:
* реализован Flask (localhost на порте 9091)
* созданы html, css, js файлы (index.html, login.html, menu...)
* ведется работы над авторизацией/аунтификацией с помощью flask-login


###### P.S. заранее извините за дизайн, я всё-таки программист, а не дизайнер