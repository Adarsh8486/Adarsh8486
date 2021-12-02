
from rest_framework import serializers
from .models import registerUser, Ingredients
from django.contrib.auth import get_user_model




class registerUserSerializers(serializers.ModelSerializer):
    registerUser = get_user_model()
    
    Password = serializers.CharField(required=True)
    Re_password = serializers.CharField(required=True)


    class Meta:
        model = registerUser
        fields= [
            'Name',
            'Username',
            'Password',
            'Re_password',
        ]
        

    def Create(self, validated_data):

        Name = validated_data.get('Name')
        Username = validated_data.get('Username')
        Password = validated_data.get('Password')
        Re_password = validated_data.get('Re_password')

        
        if Password==Re_password:
            user = registerUser(Username= Username)
            user.set_password(Re_password)
            user.save()
            return user
        else:
            raise serializers.ValidationError({'error': 'both password do not match'})

        
       
class IngredientsSerializers(serializers.ModelSerializer):
    class Meta:
        model= Ingredients
        fields = '__all__'
    


    


    def Create(self, validated_data):
        return Ingredients.objects.create(**validated_data)


    def Update(self, instance, validated_data):
        instance.product= validated_data.get('product', instance.product)
        instance.Quantity_of_product= validated_data.get('Quantity_of_product', instance.Quantity_of_product)
        instance.cost= validated_data.get('cost', instance.cost)
        instance.selling_price= validated_data.get('selling_price', instance.selling_price)
        instance.save()
        return instance

class registeruserSerializers(serializers.ModelSerializer):
    class Meta:
        model= registerUser
        fields = '__all__'

        def Create(self, validated_data):
            return registerUser.objects.create(**validated_data)
