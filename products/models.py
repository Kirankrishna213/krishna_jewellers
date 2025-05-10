 
from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('products:product_list_by_category', args=[self.slug])

class Product(models.Model):
    GOLD = 'GD'
    DIAMOND = 'DM'
    PLATINUM = 'PT'
    SILVER = 'SL'
    
    METAL_CHOICES = [
        (GOLD, 'Gold'),
        (DIAMOND, 'Diamond'),
        (PLATINUM, 'Platinum'),
        (SILVER, 'Silver'),
    ]
    
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    metal_type = models.CharField(max_length=2, choices=METAL_CHOICES, default=GOLD)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=6, decimal_places=2, help_text='Weight in grams')
    karat = models.PositiveSmallIntegerField(null=True, blank=True, help_text='Karat purity (e.g., 22, 18, 14)')
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('products:product_detail', args=[self.id, self.slug])
