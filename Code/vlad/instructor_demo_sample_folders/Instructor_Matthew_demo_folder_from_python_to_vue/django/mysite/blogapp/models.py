from django.db import models



# tag = BlogPostTag.objects.get(name='#delicious')
# default if related name is not specified
# "here is what you call the set of all of me"
# tag.blogpost_set.all()
# tag.posts.all()




class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    body = models.TextField()
    type = models.ForeignKey('BlogPostType', on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField('BlogPostTag', related_name='posts')
    created_date = models.DateTimeField()
    approved = models.BooleanField()

    def __str__(self):
        return self.title



class BlogPostTag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class BlogPostType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


