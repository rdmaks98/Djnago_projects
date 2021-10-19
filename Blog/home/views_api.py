from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class LoginView(APIView):
    def post(self,request):
        response = {}
        response['status'] = 500
        response['message'] = "somthing went wrong here"
        try:
            data = request.data

            if data.get('username') is None:
                response['message'] = "your username is incorrect"
                raise Exception('Your username is incorrect')
            if data.get('password') is None:
                response['message'] = "your password is incorrect"
                raise Exception('Your password is incorrect')
            
            check_user = User.objects.filter(username = data.get('username')).first()

            if check_user is None:
                response['message'] = "invalid username"
                raise Exception('Invalid username')

            user_obj = authenticate(username = data.get('username'), password = data.get('password'))

            if user_obj:
                response['status'] = 200
                response['message'] = "Welcome to in Blog"
            else:
                response['message'] = "invalid password"
                raise Exception('Invalid password')


        except Exception as e :
            print(e)
        
        return Response(response)

LoginView = LoginView.as_view()


