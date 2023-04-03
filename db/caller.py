# from modelling_django_orm.db.models import Post
from db.models import Post

for i in Post.objects.all():
    print(i)