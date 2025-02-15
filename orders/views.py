import json

from django.http  import JsonResponse
from django.views import View
from json.decoder import JSONDecodeError

from orders.models         import Order_Product
from products.models       import Cart, Product
from users.models          import User
from utils.login_decorator import login_decorator

class CartView(View):
    @login_decorator
    def post(self, request):
        try:
            data = json.loads(request.body)
            
            user       = request.user
            product_id = data['product_id']
            quantity   = data['quantity']

            cart, created  = Cart.objects.get_or_create(
                user_id    = user.id,
                product_id = product_id
            )
            cart.quantity += quantity
            cart.save()
            return JsonResponse({'message': 'CREATE_CART_SUSSESS'}, status = 201)
        
        except KeyError:
            JsonResponse({'message': 'KEY_ERROR'}, status = 400)
            
        except JSONDecodeError:
            return JsonResponse({'message': 'JsonDecodeError'}, status = 400)

        except Cart.DoesNotExist:
            return JsonResponse({'message': 'CART_NOT_EXIST'}, status = 404)    

    @login_decorator
    def get(self, request):

        user   = request.user
        carts  = Cart.objects.select_related('product').filter(user = user)
       
        result = [{
            'cart_id'            : cart.id,
            'product_id'         : cart.product.id,
            'product_name'       : cart.product.name,
            'thumbnail_image_url': cart.product.thumbnail_image.url,
            'price'              : int(cart.product.price),
            'quantity'           : cart.quantity
        } for cart in carts]

        return JsonResponse({'result': result}, status = 200)
       
    @login_decorator
    def delete(self, request):
        try:
            data = json.loads(request.body)

            user = request.user
            cart_id = data['cart_id']

            cart = Cart.objects.get(id = cart_id, user = user)
            
            if not Cart.objects.filter(id = cart_id, user = user).exists():
                return JsonResponse({'message': 'NOT_EXIST'}, status = 400)
            
            cart.delete()

            return JsonResponse({'message': 'DELETE_CART_SUCCESS'}, status = 204)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status = 400)

class OrderView(View):
    @login_decorator
    def post(self, request):
        try:
            data = json.loads(request.body)

            product_id = data['product_id']
            quantity   = data['quantity']

            users        = request.user
            points       = int(users.point)
            products     = Product.objects.get(id=product_id)
            total_price  = int(products.price) * int(quantity)
            remain_point = points - total_price

            if remain_point < 0:
                print('잔액 부족')
                return JsonResponse({"message" : "NOT_ENOUGH_POINT"}, status=400)

            Order_Product.objects.create(
                product_id  = product_id,
                quantity    = quantity,
                total_price = total_price
            )

            updated_user       = User.objects.get(id = users.id)
            updated_user.point = remain_point
            updated_user.save()

            user_data = {
                "user_name"  : users.name,
                "user_point" : remain_point
            }

            return JsonResponse({"result" : user_data}, status=200)

        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)
        except JSONDecodeError:
            return JsonResponse({"message" : "JSONDecodeError"}, status=400)
        except Product.DoesNotExist:
            return JsonResponse({"message" : "INVALID_PRODUCT"}, status=400)
