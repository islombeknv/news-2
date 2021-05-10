from django.db import models


class CategoryModel(models.Model):
    title = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class NewsModel(models.Model):
    image = models.ImageField(upload_to='news', )
    title = models.CharField(max_length=100)
    comment = models.TextField()
    category = models.ForeignKey(CategoryModel, on_delete=models.PROTECT, related_name='news')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'
