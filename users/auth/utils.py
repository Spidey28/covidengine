from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

from base import exceptions as exc

User = get_user_model()


def get_and_authenticate_user(email: str, password: str) -> User:
    """Authenticate the user corresponding to the given args.

    Args:
        email (str): The email of the user to be authenticated
        password (str): The password of the user

    Returns:
        User: The authenticated user instance

    Raises:
        exc.BadRequest: When user is not authenticated
    """
    if User.objects.filter(email=email).exists():
        user = User.objects.get(email=email)
        if not user.check_password(password):
            raise exc.BadRequest("Invalid email/password!")
        if not user.is_active:
            raise exc.BadRequest("User account has been disabled! Contact admin")
        return user
    else:
        raise exc.BadRequest("User account doesn't exists")


def delete_token(user: User) -> None:
    """Deletes token of the user.

    Args:
        user (User): The user whose token is to be deleted
    """
    token = Token.objects.get(user=user)
    token.delete()
