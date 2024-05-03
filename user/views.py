from user.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from user.serializers import UserCreateSerializer, UserSerializer, UserUpdateSerializer

# Create your views here.


@api_view(["POST"])
def create_user(request, *args, **kwargs):
    seralizer = UserCreateSerializer(data=request.data)
    seralizer.is_valid(raise_exception=True)
    obj = User.objects.create(**seralizer.validated_data)
    return Response(
        {"success": "User created successfully.", "user_id": obj.user_id},
        status=status.HTTP_201_CREATED,
    )


@api_view(["GET"])
def get_users(request, *args, **kwargs):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response({"users": serializer.data}, status=status.HTTP_200_OK)


@api_view(["DELETE"])
def delete_user(request, *args, **kwargs):
    user_id = request.data.get("user_id")
    try:
        obj = User.objects.get(user_id=user_id)
        obj.delete()
        return Response(
            {"success": "User deleted successfully."}, status=status.HTTP_200_OK
        )
    except User.DoesNotExist:
        return Response(
            {"error": "User does not exist."}, status=status.HTTP_400_BAD_REQUEST
        )
    except User.MultipleObjectsReturned:
        return Response(
            {"error": "Multiple users found with the given ID."},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["PATCH"])
def update_user(request, *args, **kwargs):
    seralizer = UserUpdateSerializer(data=request.data)
    seralizer.is_valid(raise_exception=True)
    user_id = seralizer.validated_data.pop("user_id")
    try:
        obj = User.objects.get(user_id=user_id)
        for key, value in seralizer.validated_data.items():
            setattr(obj, key, value)
        obj.save()
        return Response(
            {"success": "User updated successfully.", "data": UserSerializer(obj).data},
            status=status.HTTP_200_OK,
        )
    except User.DoesNotExist:
        return Response(
            {"error": "User does not exist."}, status=status.HTTP_400_BAD_REQUEST
        )
    except User.MultipleObjectsReturned:
        return Response(
            {"error": "Multiple users found with the given ID."},
            status=status.HTTP_400_BAD_REQUEST,
        )
    except ValueError as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(
            {"error": "Something went wrong. Please try again."},
            status=status.HTTP_400_BAD_REQUEST,
        )
