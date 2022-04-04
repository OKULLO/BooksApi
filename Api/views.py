from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.decorators import api_view

from rest_framework.views import APIView
from Api.models import Book
from Api.Serializer import BookSerializer



# # Create your views here.
# @api_view(['GET'])
# def books(request):
# 	books = Book.objects.all()

# 	serializer = BookSerializer(books,many=True)

# 	return Response(serializer.data)


# @api_view(['POST'])
# def createBook(request):

# 	serializer = BookSerializer(data=request.data)

# 	if serializer.is_valid():
# 		serializer.save()
# 		return Response(serializer.data)
# 	else:
# 		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def book(request,pk):

# 	try: book = Book.objects.get(id =int(pk))

# 	except: return Response({'error':'Book does not exist'},status.HTTP_404_NOT_FOUND)

		
# 	if request.method =="GET":
		
# 		serializer = BookSerializer(book)
# 		return Response(serializer.data)

# 	if request.method =='PUT':
# 		serializer = BookSerializer(book,data =request.data)
# 		if serializer.is_valid():

# 		   return Response(serializer.data)

# 		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# 	if request.method =='DELETE':
# 		book.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)



		
####---------------------class views


class BookList(APIView):

	def get(self, request):
		books = Book.objects.all()

		serializer = BookSerializer(books,many=True)

		return Response(serializer.data)

	def post(self,request):
		 return Response({'message':"I can make a post request"})


class BookCreate(APIView):

	def post(self,request):

		serializer = BookSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class BookDetail(APIView):

	def getBookByPk(self,pk):

		try: return  Book.objects.get(id =int(pk))

		except:return Response({'error':'Book does not exist'},status.HTTP_404_NOT_FOUND)

		
	def get(self,request,pk):
		
		book = self.getBookByPk(pk)
		serializer = BookSerializer(book)
		return Response(serializer.data)

	def put(self,request,pk):

		book = self.getBookByPk(pk)
		serializer = BookSerializer(book,data =request.data)
		if serializer.is_valid():

		   return Response(serializer.data)

		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

	def delete(self,request,pk):
		book = self.getBookByPk(pk)
		book.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


