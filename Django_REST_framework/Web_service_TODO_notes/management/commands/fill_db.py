import random

from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from ToDoapp.models import Project, TODO
from users.models import User
from mimesis import Text, Person, Datetime, Internet

COUNT_USERS = 10
COUNT_PROJECTS = 10
COUNT_TODO = 10


class Command(BaseCommand):
    help = 'Create User'

    def handle(self, *args, **options):

        # CREATE USERS
        person = Person()

        for _ in range(COUNT_USERS):
            username_ = person.username(mask='C')
            password_ = person.password(length=8)
            print(f'Логин: {username_} / Пароль: {password_}')
            first_name_ = person.first_name()
            last_name_ = person.last_name()
            email_ = person.email()

            user = User(
                username=username_,
                email=email_,
                last_name=last_name_,
                first_name=first_name_,
            )

            user.set_password(password_)
            try:
                user.save()
            except Exception as err:
                print(f' ошибка: {err}, запись не создана')
                continue

        # Создаем суперпользователя при помощи менеджера модели
        try:
            super_user = User.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains')
        except Exception as err:
            print('Занято!', err)

        # Создаем таблицу Project
        print('Создаем таблицу Project')

        text = Text('ru')
        internet = Internet()

        for _ in range(COUNT_PROJECTS):
            name_ = text.word()
            link_ = internet.url(subdomains=['todo'])
            project = Project(
                name=name_,
                link=link_,
            )
            project.save()
            count_worker = random.randint(1, 6)
            workers = User.objects.order_by('?')[: count_worker]
            project.worker.set(workers)
            project.save()


            # Создаем таблицу to_do
            print('Создаем таблицу TODO')
            for _ in range(COUNT_TODO):
                author_ = User.objects.order_by('?').first()
                project_ = Project.objects.order_by('?').first()
                title_ = text.text(quantity=1)
                text_ = text.text(quantity=2)
                todo = TODO(
                    author=author_,
                    project=project_,
                    title=title_,
                    text=text_,
                )
                try:
                    todo.save()
                except Exception as err:
                    print(f' ошибка: {err}, запись не создана')

