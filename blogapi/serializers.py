from rest_framework import serializers
from django.contrib.auth.models import User
from .models import BlogModel
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(read_only=True)
    password2=serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['username','email','password','password2']

        def valide(self , data):

            if data['password'] != data ['password2']:
                raise serializers.ValidationError({'password not match'})
            return data
        
        def create(self , validated_data):
            validated_data.pop('password2')
            password = validated_data.pop('password')
            user = User(**validated_data)
            user.set_password(password)
            user.save()
            return user

            
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    
    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            raise serializers.ValidationError({"error": "Must include 'username' and 'password'."})

        # Authenticate user
        user = authenticate(request=self.context.get('request') ,username=username, password=password)
        if not user:
            raise serializers.ValidationError({"error": "Unable to log in with provided credentials."})

        if not user.is_active:
            raise serializers.ValidationError({"error": "User account is inactive."})

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)

        return {
            'user': user,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
            

class TokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()
        


class BlogModelSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta :
        model = BlogModel
        fields = ['id','name','title','author','created_at']
        read_only_fields = ['author' ,'created_at']