from bakery.viewsets import IngredientsViewset , registerUserViewset
from rest_framework import routers

router = routers.DefaultRouter()

router.register('ingredients', IngredientsViewset)

router.register('registerUser', registerUserViewset)



