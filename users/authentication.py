from users.models import User


class PhoneAuthentication:

    def authenticate(self, request, phone=None, ot_pass=None):
        try:
            user = User.objects.get(phone=phone)
            if ot_pass == '1234':
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            user = User.objects.get(pk=user_id)
            return user
        except User.DoesNotExist:
            return None