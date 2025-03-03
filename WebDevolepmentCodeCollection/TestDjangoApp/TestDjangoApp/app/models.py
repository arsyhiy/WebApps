from django.db import models

class TreeMenuCategory(models.Model):
    name = models.CharField('название меню', max_length=50, blank=False, unique=True)
    description = models.TextField('описание', max_length=300, blank=True, null=True)

    class Meta:
        db_table = "TreeMenuCategory"
        ordering = ['id']
        verbose_name = 'Menu category'
        verbose_name_plural = 'Menu categories'

    def __str__(self):
        return self.name
    

class TreeMenuItem(models.Model):
    name = models.CharField('название пункта меню', max_length=50, blank=False, unique=True)
    description = models.TextField('описание', max_length=300, blank=True, null=True)
    url = models.CharField(verbose_name='URL-адрес сторонего ресурса',
                           help_text=(
                           'Указывается для перехода на ресурс из конечного пункта меню, '
                           'если не указать, то алгоритм будет пытаться найти потомков '
                           'данного пункта меню и создать из них подменю'), 
    max_length=50, blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    menu = models.ForeignKey( TreeMenuCategory, on_delete=models.CASCADE, related_name='menu_items')

    class Meta:
        ordering = ['id']
        verbose_name = 'Tree menu item'
        verbose_name_plural = 'tree menu items'

    def __str__(self):
        return self.name
    