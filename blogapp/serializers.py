from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Blog


User = get_user_model()

class UpdateUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "username", "first_name", "last_name", "password","job_title", "bio", "profile_picture","facebook", "youtube","instagram", "twitter"]


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "username", "first_name", "last_name", "password"]

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
            username = validated_data['username']
            first_name = validated_data['first_name']
            last_name = validated_data['last_name']
            password = validated_data['password']


            
            new_user = User.objects.create(username=username, 
                                           first_name=first_name, last_name=last_name)
            
            new_user.set_password(password)
            new_user.save()
            return new_user
    
class SimpleAutherSerializer(serializers.ModelSerializer):
     
     class Meta:
          model = get_user_model()
          fields = ['id', 'username', 'first_name', 'last_name', 'profile_picture']
    
class BlogSerializer(serializers.ModelSerializer):
     author = SimpleAutherSerializer(read_only=True)
     class Meta:
        model = Blog
        fields = ["id","title","slug", "content", "author", "created_at", "updated_at", "publish_date", "is_draft", "category", "featured_image"]


class UserInfoSerializer(serializers.ModelSerializer):
     
     author_posts = serializers.SerializerMethodField()
     class Meta:
          model = get_user_model()
          fields = ['id', 'username', 'first_name', 'last_name', 'job_title','bio', 'profile_picture', 'author_posts']
    

     def get_author_posts(self, user):
            blogs = Blog.objects.filter(author=user)[:9]
            serializer = BlogSerializer(blogs, many=True)
            return serializer.data
           
            
            
              

    

     
