# **INFORCE DATA ENGINEERING TASK: Python ETL Pipeline with Docker and PostgreSQL**
## **Table of Contents**
- [Overview]()
- [Requirements]()
- [Setup and Run]()
    - [1. Build and Run Containers]()
    - [2. Verify the PostgreSQL Database]()

- [Database Schema]()
- [SQL Queries]()
- [Assumptions]()
- [Results Verification]()
- [Included Files]()

## **Overview**
Цей проект реалізує ETL-процес, який:
1. **E**xtract (витягує) дані з джерела (в моєму випадку це CSV файл).[^1] 
2. **T**ransform (перетворює) дані — виконує необхідні зміни.
3. **L**oad (завантажує) результати в базу даних PostgreSQL.

[^1]: Також в процесі "витягування" я реалізував генерацію синтетичних даних завдяки пакету Faker. за замовчуванням виставлена генерація 10000 записів.

Проект також виконує кілька SQL-запитів із метою аналізу даних після основного ETL-процесу. Усі сервіси працюють у Docker-контейнерах.
## **Requirements**
Перед запуском проекту переконайтеся, що у вас встановлено:
- **Docker** (23.0.0 або новіший)
- **Docker Compose** (v2.20.2 або новіший)
- **Python 3.10** (або новіший).

## **Setup and Run**
### **1. Build and Run Containers**
1. Клонувати проект:
``` bash
   cd <folder-name>
   git clone https://github.com/Oleksef/ETL-pipeline-task.git
```
2. Перевірити та налаштувати змінні у `.env`:
``` env
   POSTGRES_HOST=postgres
   POSTGRES_PORT=5432
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=your_password
   POSTGRES_DB=postgres
```
3. Запустити всі сервіси через Docker Compose:
``` bash
   docker-compose up --build
```
Docker створить два контейнери:
- `postgres` — база даних PostgreSQL.
- `python` — контейнер із ETL-кодом.

4. Контейнер Python автоматично виконає ETL та SQL-запити після побудови.

### **2. Verify the PostgreSQL Database**
Після виконання всіх контейнерів можна підключитися до бази даних PostgreSQL для перевірки результатів.
1. Увійти в контейнер PostgreSQL:
``` bash
   docker exec -it postgres_container psql -U postgres -d postgres
```
2. Переглянути таблицю `users`:
``` sql
   SELECT * FROM users;
```
## **Database Schema**
У базі даних використовується одна таблиця `users`, з наступною схемою:

| **Column Name** | **Type** | **Description** |
| --- | --- | --- |
| `user_id` | INTEGER | Унікальний ідентифікатор користувача |
| `name` | VARCHAR(255) | Повне ім'я користувача |
| `email` | VARCHAR(255) | Електронна пошта користувача |
| `signup_date` | DATE | Дата реєстрації користувача |
| `domain` | VARCHAR(100) | Домен пошти |

Таблиця автоматично створюється через Python-скрипт.
## **SQL Queries**
### 1. **Отримати кількість зареєстрованих користувачів за кожен день:**
Можна прибрати коментар "--", щоб дані виводились від найбільшого числа.
``` sql
SELECT signup_date, count(1)
FROM users
GROUP BY signup_date
--ORDER BY count DESC;
```
### 2. **Отримання унікальних доменів:**
``` sql
SELECT DISTINCT domain
FROM users;
```
### 3. **Отримання користувачів, які були зареєстровані за останні 7 діб:**
Тут є дві варіації виконання цього запиту.
``` sql
SELECT *
FROM users
WHERE signup_date BETWEEN current_date - 7 AND current_date;


-- SELECT *
-- FROM users
-- WHERE signup_date > current_date - INTERVAL '7 day';
```
### 4. **Вивід користувачів, чий домен електронної пошти найпоширеніший:**
``` sql
WITH common_domain AS (SELECT
    domain, COUNT(domain)
FROM users
GROUP BY domain
ORDER BY count DESC
LIMIT 1)

SELECT users.*
FROM users
JOIN common_domain USING(domain);
```
### 5. **Видалення усіх записів з невідповідним доменом:**
``` sql
DELETE FROM users
WHERE domain NOT IN ('google.com', 'yahoo.com', 'hotmail.com');

--SELECT *
--FROM users;
```
## **Assumptions**


## **Results Verification**
Для перевірки змісту CSV-файлу data.csv:
``` bash
cat src/data/data.csv
```

Для перевірки процесу Transformation цього пайплайну в файлі __*main.py*__ можна передати функції __*transformer()*__ аргумент **"save_to_csv=True"**, завдяки якому можна буде перевірити процес очищення даних в CSV файлі __*transformed_data.csv*__.
``` bash
cat src/data/transformed_data.csv
```
## **Included Files**
1. **Python scripts:**
    - `etl/extract.py`, `etl/transform.py`, `etl/load.py` — виконують ETL-процес.
    - `database/execute_queries.py` — виконує SQL-запити після ETL.
    - `database/db.py` — налаштування підключення до бази даних PostgreSQL.

2. **SQL Scripts:**
    - `sql/query_(*номер файлу*)` — SQL запити.

3. **Docker Configuration:**
    - `Dockerfile` — Створення образу для ETL-коду.
    - `docker-compose.yml` — Запускає PostgreSQL і Python-контейнери.

4. **Data:**
    - Зберігаються у папці `data/`.

## **Conclusion**
Цей проект представляє ефективний ETL-процес з подальшим виконанням SQL-запитів. Його легко запускати, і він добре структурується завдяки використанню Docker-контейнерів.
А задача була досить цікавою, працював над її реалізацією із задоволенням.
