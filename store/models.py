from django.db import models
from PIL import Image
import os

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم القسم")

    class Meta:
        verbose_name = "قسم"
        verbose_name_plural = "الأقسام"

    def __str__(self):
        return self.name

class Banner(models.Model):
    title = models.CharField(max_length=150, verbose_name="عنوان العرض / البنر")
    subtitle = models.CharField(max_length=250, blank=True, verbose_name="وصف قصير")
    image = models.ImageField(upload_to='banners/', verbose_name="صورة البنر")
    link = models.CharField(max_length=300, blank=True, verbose_name="رابط التوجيه (اختياري)")
    is_active = models.BooleanField(default=True, verbose_name="مفعل")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "بنر إعلاني"
        verbose_name_plural = "البنرات الإعلانية"

    def __str__(self):
        return self.title

class Product(models.Model):
    STOCK_CHOICES = [
        ('in_stock', 'تسليم فوري (متاح)'),
        ('on_demand', 'متاح بالطلب / تصنيع'),
        ('out_of_stock', 'غير متاح حالياً'),
    ]

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='products', verbose_name="القسم")
    name = models.CharField(max_length=200, verbose_name="اسم المنتج")
    description = models.TextField(blank=True, verbose_name="وصف المنتج")
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="السعر (اختياري)")
    status = models.CharField(max_length=20, choices=STOCK_CHOICES, default='in_stock', verbose_name="حالة التوفر")
    main_image = models.ImageField(upload_to='products/', verbose_name="الصورة الرئيسية")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='gallery', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/gallery/', verbose_name="صورة إضافية")
    order = models.PositiveIntegerField(default=0, verbose_name="ترتيب العرض")

    class Meta:
        verbose_name = "صورة للمعرض"
        verbose_name_plural = "صور معرض المنتج"
        ordering = ['order']