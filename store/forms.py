from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'status', 'description', 'main_image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-gray-300 focus:ring-2 focus:ring-amber-800 focus:border-amber-800 outline-none text-sm transition',
                'placeholder': 'مثال: طقم انتريه مودرن'
            }),
            'category': forms.Select(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-gray-300 focus:ring-2 focus:ring-amber-800 focus:border-amber-800 outline-none text-sm bg-white transition'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-gray-300 focus:ring-2 focus:ring-amber-800 focus:border-amber-800 outline-none text-sm transition',
                'placeholder': 'أدخل السعر بالجنيه'
            }),
            'status': forms.Select(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-gray-300 focus:ring-2 focus:ring-amber-800 focus:border-amber-800 outline-none text-sm bg-white transition'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-gray-300 focus:ring-2 focus:ring-amber-800 focus:border-amber-800 outline-none text-sm transition h-28 resize-none',
                'placeholder': 'اكتب تفاصيل المنتج وخامات التصنيع...'
            }),
            'main_image': forms.FileInput(attrs={
                'class': 'hidden',
                'id': 'image-upload-input',
                'accept': 'image/*'
            }),
        }