from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import get_user_model

class TokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_token = request.query_params.get('api_token')
        User = get_user_model()

        if api_token:
            try:
                user = User.objects.get(api_token=api_token)
                return (user, None)
            except User.DoesNotExist:
                pass
        raise AuthenticationFailed('Invalid API token.')
   
    
class NoAuthentication(BaseAuthentication):
    def authenticate(self, request):
        return None
