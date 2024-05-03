from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import User, Manager
from datetime import datetime
from .serializers import UserSerializer
from .utils import validate_manager_id

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.


@api_view(["POST"])
def create_user(request):
    data = request.data
    seralizer = UserSerializer(data=data)
    seralizer.is_valid(raise_exception=True)
    seralizer.save()
    return Response(
        {"success": "User created successfully.", "user_id": seralizer.data["user_id"]},
        status=status.HTTP_201_CREATED,
    )

    # manager_id = data.get('manager_id')
    # if manager_id:
    #     if not validate_manager_id(manager_id):
    #         return JsonResponse({'error': 'Invalid manager ID.'}, status=400)

    # user = User.objects.create(
    #     full_name=data['full_name'],
    #     mob_num=data['mob_num'],
    #     pan_num=data['pan_num'].upper(),
    #     manager_id=manager_id
    # )
    # return JsonResponse({'success': f'User {user.user_id} created successfully.'})


@api_view(["GET"])
def get_users(request, *args, **kwargs):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response({"users": serializer.data}, status=status.HTTP_200_OK)

    # # user_id = request.data.get('user_id')
    # # mob_num = request.data.get('mob_num')
    # # manager_id = request.data.get('manager_id')

    # users = User.objects.all()
    # # if user_id:
    # #     users = users.filter(user_id=user_id)
    # # elif mob_num:
    # #     users = users.filter(mob_num=mob_num)
    # # elif manager_id:
    # #     users = users.filter(manager_id=manager_id)

    # serializer = UserSerializer(users, many=True)
    # return JsonResponse({"users": serializer.data})


@require_http_methods(["POST"])
def delete_user(request):
    user_id = request.data.get("user_id")
    mob_num = request.data.get("mob_num")

    if user_id:
        user = User.objects.filter(user_id=user_id).first()
    elif mob_num:
        user = User.objects.filter(mob_num=mob_num).first()
    else:
        return JsonResponse(
            {"error": "Either user_id or mob_num is required."}, status=400
        )

    if not user:
        return JsonResponse({"error": "User not found."}, status=404)

    user.delete()
    return JsonResponse({"success": "User deleted successfully."})


@require_http_methods(["POST"])
def update_user(request):
    data = request.data
    if "error" in data:
        return JsonResponse(data, status=400)

    user_ids = data.get("user_ids", [])
    update_data = data.get("update_data", {})

    if not user_ids:
        return JsonResponse({"error": "user_ids is required."}, status=400)

    if "manager_id" in update_data:
        manager_id = update_data["manager_id"]
        if not validate_manager_id(manager_id):
            return JsonResponse({"error": "Invalid manager ID."}, status=400)

    users = User.objects.filter(user_id__in=user_ids)
    if users.count() != len(user_ids):
        return JsonResponse({"error": "One or more user IDs are invalid."}, status=400)

    for user in users:
        for field, value in update_data.items():
            if field == "full_name":
                user.full_name = value
            elif field == "mob_num":
                user.mob_num = value
            elif field == "pan_num":
                user.pan_num = value.upper()
            elif field == "manager_id":
                if user.manager_id != value:
                    user.is_active = False
                    user.save()
                    user.pk = None
                    user.manager_id = value
                    user.is_active = True
                    user.save()
            user.updated_at = datetime.now()
        user.save()

    return JsonResponse({"success": "Users updated successfully."})
