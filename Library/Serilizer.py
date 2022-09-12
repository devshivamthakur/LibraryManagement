from rest_framework import serializers

from Library.models import Book, Admin

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('email', 'password')    
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'            