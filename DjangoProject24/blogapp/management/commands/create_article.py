import logging
from django.core.management.base import BaseCommand
from blogapp.models import Article
from faker import Faker

logger = logging.getLogger(__name__)
fake = Faker()


class Command(BaseCommand):
    help = 'Создать статью'

    def add_arguments(self, parser):
        parser.add_argument('author_id', type=int, help='ID автора статьи')
        parser.add_argument('--num', type=int, default=1, help='Количество статей для создания')

    def handle(self, *args, **options):
        author_id = options['author_id']
        num_articles = options['num']

        try:
            for _ in range(num_articles):
                title = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
                content = fake.text(max_nb_chars=200, ext_word_list=None)
                category = fake.word(ext_word_list=None)
                views = fake.random_int(min=0, max=1000)
                published = fake.boolean(chance_of_getting_true=50)

                article = Article.objects.create(
                    author_id=author_id,
                    title=title,
                    content=content,
                    category=category,
                    views=views,
                    published=published
                )

                self.stdout.write(self.style.SUCCESS(f'Статья "{article.title}" была успешно создана.'))
                logger.info(f'Статья "{article.title}" была успешно создана.')
        except Exception as e:
            error_message = f'Ошибка создания статьи: {str(e)}'
            self.stdout.write(self.style.ERROR(error_message))
            logger.error(error_message)

# Пример команды в терминале для создания одной статьи с идентификатором автора 1:
#
# python manage.py create_article 1
#
# Эта команда создаст три статьи с автором, имеющим идентификатор 1:
#
# python manage.py create_article 1 --num 3
