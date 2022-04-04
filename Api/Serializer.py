from rest_framework import serializers
from Api.models import Book


# class BookSerializer(serializers.Serializer):
# 	id = serializers.IntegerField(read_only=True)
# 	title = serializers.CharField()
# 	pages = serializers.IntegerField()
# 	quantity = serializers.IntegerField()


# 	def create(self,data):

# 		return Book.objects.create(**data)

# 	def update(self,instance,data):
# 		pass


class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book

		fields = "__all__"


