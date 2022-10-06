from django import forms
from .models import BarangWishlist
class WishlistForm(forms.ModelForm):
    class Meta:
        model = BarangWishlist
        field = ['nama_barang', 'harga_barang', 'deskripsi']