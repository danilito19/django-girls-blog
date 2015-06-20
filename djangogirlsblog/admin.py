from django.contrib import admin
from .models import Post

# make the Post model (a table in the db, class Post) available on admin site
# we need to register it
admin.site.register(Post)

