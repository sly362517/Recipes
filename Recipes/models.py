from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Recipe(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    steps = models.TextField(verbose_name='Шаги приготовления')
    cooking_time = models.PositiveIntegerField(verbose_name='Время приготовления')
    image = models.ImageField(upload_to='media/', verbose_name='Изображение')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    categories = models.ManyToManyField(Category, through='RecipeCategory', related_name='recipes',
                                        verbose_name='Категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name='Рецепт')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return f'{self.recipe.title} - {self.category.name}'

    class Meta:
        verbose_name = 'Связь Рецепт-Категория'
        verbose_name_plural = 'Связи Рецепт-Категория'
