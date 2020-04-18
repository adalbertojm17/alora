from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.serializers import (
    CharField,
    EmailField,
    ModelSerializer,
    ValidationError, Serializer
)

User = get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserCreateSerializer(ModelSerializer):
    password = CharField(max_length=32, label='Password', write_only=True)
    password2 = CharField(max_length=32, label='Confirm Password', write_only=True)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'phone',
            'email',
            'username',
            'password',
            'password2'
        ]

    def validate_password(self, value):
        data = self.get_initial()
        password1 = data.get('password2')
        password2 = value
        if password1 != password2:
            raise ValidationError('Passwords must match')
        return value

    def validate_password2(self, value):
        data = self.get_initial()
        password1 = data.get('password')
        password2 = value
        if password1 != password2:
            raise ValidationError('Passwords must match')
        return value

    def create(self, validated_data):
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        username = validated_data['username']
        password = validated_data['password']
        user_obj = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField(required=False, allow_blank=True)
    email = EmailField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'password',
            'token',
        ]
        extra_kwargs = {'password':
                            {'write_only': True}
                        }

    def validate(self, data):
        email = data.get('email')
        username = data.get('username')
        password = data["password"]
        if not email and not username:
            raise ValidationError("A username or email is required to login.")
        user = User.objects.filter(
            Q(email=email) |
            Q(username=username)
        ).distinct()
        user = user.exclude(email__isnull=True).exclude(email__iexact='')
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("This username/email is not valid.")
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect credentials, please try again.")

        return data


class ChangePasswordSerializer(Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = CharField(
        required=True
    )
    new_password = CharField(
        required=True
    )
    new_password2 = CharField(
        label='Confirm Password',
        required=True
    )

    def validate_new_password(self, value):
        data = self.get_initial()
        password1 = data.get('new_password2')
        password2 = value
        if password1 != password2:
            raise ValidationError('Passwords must match')
        return value

    def validate_new_password2(self, value):
        data = self.get_initial()
        password1 = data.get('new_password')
        password2 = value
        if password1 != password2:
            raise ValidationError('Passwords must match')
        return value
