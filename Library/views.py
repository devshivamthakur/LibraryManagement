from Library.Serilizer import AdminSerializer, BookSerializer, LoginSerializer
from Library.models import Admin, Book
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

#admin api
# Create your views here.
class LoginAdmin(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        try:

            serializer = LoginSerializer(data=request.data)
            if serializer.is_valid():
                print(serializer.data['password'],serializer.data['password'])
                admin_=Admin.objects.filter(email=serializer.data['email'],password=serializer.data['password'])
                print(admin_)
                if admin_.exists():
                    user = authenticate(username=serializer.data['email'], password=serializer.data['password'])

                    token = Token.objects.get_or_create(user=user)[0].key
                    return Response({'token':token,'message':'Login Successfull',
                    "id":admin_[0].id,
                    },status=200)
                else:
                    return Response({'message':'Invalid Credentials'},status=400)
            else:
                return Response({'message':'Invalid Credentials'},status=400)            
        except Exception as e:
            return Response({'message':str(e)},status=400)
class AdminView(APIView):
    permission_classes = (AllowAny,)
     #allow any user to create admin
    def post(self, request):
        try:
            admin_=Admin.objects.filter(email=request.data['email'])
            if admin_!=None and admin_.count()>0:
                return Response({"message": "Email already exists"})
            admin_serializer=AdminSerializer(data=request.data) 
            if admin_serializer.is_valid():
                admin_serializer.save()
                User.objects.create_user(username=request.data['email'],password=request.data['password'])
                return Response({"message": "Admin created successfully"}) 
            else:
                return Response({"message": admin_serializer.errors})
            
        except Exception as e:
            return Response({"message": str(e)})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_admin(request):
    try:
        print(request.user)
        admin_=Admin.objects.get(email=request.user)
        admin_serializer=AdminSerializer(admin_)
        return Response(admin_serializer.data)
    except Exception as e:
        return Response({"message": str(e)})
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_admin(request):
    try:
                admin_=Admin.objects.filter(id=request.data['id'])
                if admin_!=None and admin_.exists():    
                    admin_serializer=AdminSerializer(admin_[0],partial=True ,data=request.data) 
                    if admin_serializer.is_valid():
                        admin_serializer.save()
                        return Response({"message": "Admin updated successfully"}) 
                    else:
                        return Response({"message": admin_serializer.errors})
                else:
                    return Response({"message": "Admin not found"})
    except Exception as e:
                return Response({"message": str(e)})    

#book api

#return all books
@api_view(['GET'])
@permission_classes([AllowAny])
def get_books(request):
    try:
        books=Book.objects.all()
        books_serializer=BookSerializer(books,many=True)
        return Response(books_serializer.data)
    except Exception as e:
        return Response({"message": str(e)})

#create book
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_book(request):
    try:
        book_serializer=BookSerializer(data=request.data) 
        if book_serializer.is_valid():
            book_serializer.save()
            return Response({"message": "Book created successfully"}) 
        else:
            return Response({"message": book_serializer.errors})
    except Exception as e:
        return Response({"message": str(e)})


#update book
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_book(request):
    try:
        book_=Book.objects.filter(id=request.data['id'])
        if book_!=None and book_.exists():    
            book_serializer=BookSerializer(book_[0],partial=True ,data=request.data) 
            if book_serializer.is_valid():
                book_serializer.save()
                return Response({"message": "Book updated successfully"}) 
            else:
                return Response({"message": book_serializer.errors})
        else:
            return Response({"message": "Book not found"})
    except Exception as e:
        return Response({"message": str(e)})

#delete book
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_book(request,id):
    try:
        book_=Book.objects.filter(id=id)
        if book_!=None and book_.exists():    
            book_[0].delete()
            return Response({"message": "Book deleted successfully"}) 
        else:
            return Response({"message": "Book not found"})
    except Exception as e:
        return Response({"message": str(e)})
