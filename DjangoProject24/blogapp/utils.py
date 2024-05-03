# Функция для создания готового автора мужского пола
def create_fake_author_male():
    fake_fname = fake_ru.first_name_male()
    fake_lname = fake_ru.last_name_male()
    fake_email = f'{fake_fname}{fake_lname}@example.com'
    # fake_email = fake_ru.fake_email() # Создает случайную почту
    fake_bday = fake_ru.date_of_birth(minimum_age=18, maximum_age=65)
    fake_address = fake_ru.address()
    fake_job = fake_ru.job()
    fake_bio = f'{fake_fname} {fake_lname} родился {fake_bday.strftime("%d.%m.%Y")} ' \
               f'в городе {fake_address.split(",")[0]}. ' \
               f'Он работает {fake_job} и имеет почту {fake_email}.'

    author = Author(
        first_name=fake_fname,
        last_name=fake_lname,
        email=fake_email,
        birthday=fake_bday,
        biography=fake_bio
    )
    author.save()
    return author


# Функция для создания готового автора женского пола
def create_fake_author_female():
    fake_fname = fake_ru.first_name_female()
    fake_lname = fake_ru.last_name_female()
    fake_email = f'{fake_fname}{fake_lname}@example.com'
    #  fake_email = fake_ru.fake_email() # Создает случайную почту
    fake_bday = fake_ru.date_of_birth(minimum_age=18, maximum_age=65)
    fake_address = fake_ru.address()
    fake_job = fake_ru.job()
    fake_bio = f'{fake_fname} {fake_lname} родился {fake_bday.strftime("%d.%m.%Y")} ' \
               f'в городе {fake_address.split(",")[0]}. ' \
               f'Он работает {fake_job} и имеет почту {fake_email}.'

    author = Author(
        first_name=fake_fname,
        last_name=fake_lname,
        email=fake_email,
        birthday=fake_bday,
        biography=fake_bio
    )
    author.save()
    return author


# Создание новой статьи
def create_article(title, content, author_id, category):
    article = Article.objects.create(
        title=title,
        content=content,
        author_id=author_id,
        category=category
    )
    return article


# Получение списка всех статей
def get_all_articles():
    articles = Article.objects.all()
    return articles


# Получение информации о конкретной статье по идентификатору
def get_article_by_id(article_id):
    article = Article.objects.get(id=article_id)
    return article


# Обновление информации о статье
def update_article(article_id, title=None, content=None, category=None):
    article = Article.objects.get(id=article_id)
    if title:
        article.title = title
    if content:
        article.content = content
    if category:
        article.category = category
    article.save()
    return article


# Удаление статьи
def delete_article(article_id):
    article = Article.objects.get(id=article_id)
    article.delete()


# Представление для создания 10 авторов в базу
def write_authors(request):
    logger.info("Someone has visited the Blog / Write Authors page ")
    count = 10
    for i in range(count):
        create_fake_author_male()
        create_fake_author_female()
    logger.info("Created new authors")
    return HttpResponse("Created 20 new authors")