# Обзор Команд Управления Django
#### Создает одну фальшивую статью для указанного ID автора.
```sh
python manage.py create_fake_article <id_автора>
````

#### Создает указанное количество фальшивых статей для указанного ID автора.
```sh
python manage.py create_fake_article <id_автора> --num <кол_во_статей>
````

#### Создает указанное количество фальшивых авторов женского пола.
```sh
python manage.py create_fake_female_author --num <кол_во_авторов>
```

#### Создает указанное количество фальшивых авторов мужского пола.
```sh
python manage.py create_fake_male_author --num <кол_во_авторов>
```

#### Создает нового клиента с указанным именем, email, телефоном и адресом.
```sh
python manage.py create_client --name "<имя>" --email "<email>" --phone "<телефон>" --address "<адрес>"
````

#### Создает фальшивый заказ с указанным количеством продуктов.
```sh
python manage.py create_fake_order --num_products <кол_во_продуктов>
````

#### Создает фальшивого клиента.
```sh
python manage.py create_fake_client
````

#### Создает фальшивый продукт.
```sh
python manage.py create_fake_product
````

#### Обновляет информацию о клиенте с указанным ID.
```sh
python manage.py update_client <id_клиента> --name "<имя>" --email "<email>" --phone "<телефон>" --address "<адрес>"
````

#### Обновляет информацию о заказе с указанным ID.
```sh
python manage.py update_order --order_id <id_заказа> --client_id <id_клиента> --product_ids <id_продуктов> --total <сумма>
````

#### Обновляет информацию о продукте с указанным ID.
```sh
python manage.py update_product <id_продукта> --name "<название>" --description "<описание>" --price <цена> --quantity <количество>
````

#### Удаляет клиента с указанным ID.
```sh
python manage.py delete_client --client_id <id_клиента>
````

#### Удаляет заказ с указанным ID.
```sh
python manage.py delete_order --order_id <id_заказа>
````

##### Удаляет продукт с указанным ID.
```sh
python manage.py delete_product --product_id <id_продукта>
```
## Установка

Для установки зависимостей проекта выполните:

```bash
pip install -r requirements.txt
