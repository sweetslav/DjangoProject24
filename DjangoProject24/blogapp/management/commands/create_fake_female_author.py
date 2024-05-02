import logging
from django.core.management.base import BaseCommand
from blogapp.models import Author
from faker import Faker

logger = logging.getLogger(__name__)
fake = Faker('ru_RU')  # Указываем локаль 'ru_RU' для русских фальшивых данных


class Command(BaseCommand):
    help = 'Создать авторов'

    def add_arguments(self, parser):
        parser.add_argument('--num', type=int, default=1, help='Количество создаваемых авторов')

    def handle(self, *args, **options):
        num_authors = options['num']

        try:
            for _ in range(num_authors):
                fake_fname = fake.first_name_female()
                fake_lname = fake.last_name_female()
                fake_email = f'{fake_fname.lower()}.{fake_lname.lower()}@example.com'
                fake_bday = fake.date_of_birth(minimum_age=18, maximum_age=65)
                fake_address = fake.address()
                fake_job = fake.job()
                fake_bio = f'{fake_fname} {fake_lname} родился {fake_bday.strftime("%d.%m.%Y")} ' \
                           f'в городе {fake_address.split(",")[0]}. ' \
                           f'Он работает {fake_job} и имеет почту {fake_email}.'

                author = Author.objects.create(
                    first_name=fake_fname,
                    last_name=fake_lname,
                    email=fake_email,
                    birthday=fake_bday,
                    biography=fake_bio
                )

                self.stdout.write(self.style.SUCCESS(f'Автор {author.full_name} был успешно создан.'))
                logger.info(f'Автор {author.full_name} был успешно создан.')
        except Exception as e:
            error_message = f'Ошибка создания автора: {str(e)}'
            self.stdout.write(self.style.ERROR(error_message))
            logger.error(error_message)

# Эта команда создаст 3 авторов женского пола с русскими именами.
# python manage.py create_fake_female_author --num 3
