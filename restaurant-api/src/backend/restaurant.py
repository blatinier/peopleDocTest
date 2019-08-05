from flask_restful import Resource
from src.models.restaurant import Restaurant
from mongoengine import DoesNotExist


class RestaurantListApi(Resource):
    def get(self):
        query = Restaurant.objects()
        return [{"name": o.name} for o in query]


class RestaurantApi(Resource):

    def delete(self, restaurant_name):
        try:
            Restaurant.objects.get(name=restaurant_name).delete()
        except DoesNotExist:
            return {"error": "Restaurant not found"}, 404

    def get(self, restaurant_name):
        if restaurant_name == "random":
            restaurant = list(Restaurant.objects.aggregate({"$sample": {"size": 1}}))[0]
            return {"name": restaurant['name']}
        else:
            try:
                restaurant = Restaurant.objects.get(name=restaurant_name)
                return {"name": restaurant.name}
            except DoesNotExist:
                return {"error": "Restaurant not found"}, 404

    def post(self, restaurant_name=None):
        try:
            restaurant = Restaurant.objects.get(name=restaurant_name)
            return {"name": restaurant.name}
        except DoesNotExist:
            restaurant = Restaurant(name=restaurant_name)
            restaurant.save()
            return {"name": restaurant.name}
