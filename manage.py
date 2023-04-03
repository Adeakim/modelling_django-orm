#!/usr/bin/env python
from decouple import config

def init_django():
    import django
    from django.conf import settings

    if settings.configured:
        return

    settings.configure(
        INSTALLED_APPS=[
            'db',
        ],
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': config("DB_NAME"),
                'USER': config("DB_USER"),
                'PASSWORD': config("DB_PASSWORD"),
                'HOST': config("DB_HOST"),
                'PORT': config("DB_PORT")
            }
        },
        MIDDLEWARE_CLASSES=[],
        ROOT_URLCONF='',
        DEBUG=False,
    )

    django.setup()

if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    
    init_django()
    from db.models import Post
    # Post.objects.create(post="Post1", author="Hakeem1")
    # Post.objects.create(post="Post2", author="Hakeem2")

    for i in Post.objects.all():
        print(i)
    # print(post)
    # execute_from_command_line()


