from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view

from .models import Todo
from .serializers import TodoSerializer


# Create your views here
def list_todo(request: Request):
    queryset = Todo.objects.all()
    serializer = TodoSerializer(instance=queryset, many=True)
    return Response(serializer.data)


def get_todo(instance: Todo):
    serializer = TodoSerializer(instance=instance)
    return Response(serializer.data)


def create_post(request: Request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)


def update(instance: Todo, data: dict, partial: bool = False):
    serializer = TodoSerializer(instance=instance, data=data, partial=partial)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)


def delete(instance: Todo):
    instance.delete()
    return Response(f'Todo with uuid: {instance.uuid} successfully deleted')


@api_view(['GET', 'POST'])
def get_post(request: Request):
    if request.method == 'GET':
        return list_todo(request)

    if request.method == 'POST':
        return create_post(request)


@api_view(['GET', 'PATCH', 'PUT', 'DELETE'])
def put_patch_delete(request: Request, uuid: str):
    instance = get_object_or_404(Todo, uuid=uuid)

    if request.method in ['PATCH', 'PUT']:
        return update(instance=instance, data=request.data, partial=request.method=='PATCH')

    if request.method == 'DELETE':
        return delete(instance=instance)

    if request.method == 'GET':
        return get_todo(instance)

