# SalaryCalculator

Данный скрипт позволяет узнать средние зарплаты по вакансиям, связанным с различными языками программирования на двух площадках:
1. Superjob
2. HeadHunter

### Установка
Для установки пакета склонируйте его из репозитория с помощью команды

```git clone https://github.com/D-spacer/SalaryCalculator.git```

Также необходимо установить пакеты, которые используются в скрипте, с помощью следующих команд:

```
pip install terminaltables
pip install requests
pip install python-dotenv
```

Проверить установленные пакеты можно с помощью команды `pydoc modules`.

### Зависимости

Для работы скрипта требуется один API-ключ от сервиса Superjob. Зарегистрироваться на сайте и ознакомиться с документацией можно по ссылке: https://api.superjob.ru/
Ключ должен храниться в файле .env в следующем виде:

```SJ_API_KEY=<токен>```

Документация к сервису HeadHunter находится здесь: https://dev.hh.ru/

### Запуск скрипта

Скрипт можно запустить через среду программирования или консоль с помощью команды

```python main.py```

Помимо API-ключа в файле .env вы можете изменить список поиска языков в переменной `languages`.

## Описание модулей

### hh_jobs

Данный модуль запрашивает через API сервиса HeadHunter вакансии в соответствии со списком ключевых слов из основного блока программы. Содержащаяся здесь функция находит все подходящие вакансии, находит среднюю зарплату и возвращает среднюю зарплату по всем вакансиям, а также количество найденных вакансий.

### salary_calculator

Этот вспомогательный модуль рассчитывает среднюю зарплату по вакансии и возвращает это значение.

### superjobs

Данный модуль аналогичен модулю hh_jobs, он находит вакансии на сервисе Superjob в соответствии с полученным на входе списком ключевых слов и возвращает общее количество найденных вакансий по каждому ключевому слову, а также средний уровень зарплаты.

### table_maker

Этот вспомогательный модуль принимает словарь, содержащий полученные от основных модулей, и создает на его основе таблицу со статистическими данными, а затем выводит ее в консоль.

### main

Это главный модуль, использующий другие модули для получения конечной статистики по зарплатам. В нем содержится список ключевых слов, по которым осуществляется поиск вакансий, который при желании можно изменить. Также здесь осуществляется проверка ссылок на наличие ошибок.
