from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from backend.ftw.serializers import EventListSerializer, EventFormSerializer, LocationFormSerializer, \
    CommentFormSerializer, CategoryFormSerializer, FTWWordFormSerializer
from backend.ftw.models import Event, Comment, Category, Location, FTWWord

######################################### Event ##################################################

@swagger_auto_schema(method='GET', responses={200: EventListSerializer(many=True)})
@api_view(['GET'])
@permission_required('ftw.view_event', raise_exception=True)
def event_list(request):
    events = Event.objects.all()
    serializer = EventListSerializer(events, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='POST', request_body=EventFormSerializer, responses={200: EventFormSerializer()})
@api_view(['POST'])
@permission_required('ftw.add_event', raise_exception=True)
def event_form_create(request):
    data = JSONParser().parse(request)
    serializer = EventFormSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@swagger_auto_schema(method='PUT', request_body=EventFormSerializer, responses={200: EventFormSerializer()})
@api_view(['PUT'])
@permission_required('ftw.change_event', raise_exception=True)
def event_form_update(request, pk):
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return Response({'error': 'Event does not exist.'}, status=404)

    data = JSONParser().parse(request)
    serializer = EventFormSerializer(event, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@swagger_auto_schema(method='GET', responses={200: EventFormSerializer()})
@api_view(['GET'])
@permission_required('ftw.view_event', raise_exception=True)
def event_form_get(request, pk):
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return Response({'error': 'Event does not exist.'}, status=404)

    serializer = EventFormSerializer(event)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_required('ftw.delete_event', raise_exception=True)
def event_delete(request, pk):
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return Response({'error': 'Event does not exist.'}, status=404)
    event.delete()
    return Response(status=204)

######################################### Location ##################################################


#@swagger_auto_schema(method='GET', responses={200: LocationListSerializer(many=True)})
#@api_view(['GET'])
#@permission_required('ftw.view_location', raise_exception=True)
#def location_list(request):
#    locations = Location.objects.all()
#    serializer = LocationListSerializer(locations, many=True)
#    return Response(serializer.data)


@swagger_auto_schema(method='POST', request_body=LocationFormSerializer, responses={200: LocationFormSerializer()})
@api_view(['POST'])
@permission_required('ftw.add_location', raise_exception=True)
def location_form_create(request):
    data = JSONParser().parse(request)
    serializer = LocationFormSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@swagger_auto_schema(method='PUT', request_body=LocationFormSerializer, responses={200: LocationFormSerializer()})
@api_view(['PUT'])
@permission_required('ftw.change_location', raise_exception=True)
def location_form_update(request, pk):
    try:
        location = Location.objects.get(pk=pk)
    except Location.DoesNotExist:
        return Response({'error': 'Location does not exist.'}, status=404)

    data = JSONParser().parse(request)
    serializer = LocationFormSerializer(location, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@swagger_auto_schema(method='GET', responses={200: LocationFormSerializer()})
@api_view(['GET'])
@permission_required('ftw.view_location', raise_exception=True)
def location_form_get(request, pk):
    try:
        location = Location.objects.get(pk=pk)
    except Location.DoesNotExist:
        return Response({'error': 'Location does not exist.'}, status=404)

    serializer = LocationFormSerializer(location)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_required('ftw.delete_location', raise_exception=True)
def location_delete(request, pk):
    try:
        location = Location.objects.get(pk=pk)
    except Location.DoesNotExist:
        return Response({'error': 'Location does not exist.'}, status=404)
    location.delete()
    return Response(status=204)

######################################### Comment ##################################################

#@swagger_auto_schema(method='GET', responses={200: CommentListSerializer(many=True)})
#@api_view(['GET'])
#@permission_required('ftw.view_comment', raise_exception=True)
#def comment_list(request):
#    comments = Comment.objects.all()
#    serializer = CommentListSerializer(comments, many=True)
#    return Response(serializer.data)


@swagger_auto_schema(method='POST', request_body=CommentFormSerializer, responses={200: CommentFormSerializer()})
@api_view(['POST'])
@permission_required('ftw.add_comment', raise_exception=True)
def comment_form_create(request):
    data = JSONParser().parse(request)
    serializer = CommentFormSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@swagger_auto_schema(method='PUT', request_body=CommentFormSerializer, responses={200: CommentFormSerializer()})
@api_view(['PUT'])
@permission_required('ftw.change_comment', raise_exception=True)
def comment_form_update(request, pk):
    try:
        comment = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return Response({'error': 'Comment does not exist.'}, status=404)

    data = JSONParser().parse(request)
    serializer = CommentFormSerializer(comment, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@swagger_auto_schema(method='GET', responses={200: CommentFormSerializer()})
@api_view(['GET'])
@permission_required('ftw.view_comment', raise_exception=True)
def comment_form_get(request, pk):
    try:
        comment = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return Response({'error': 'Comment does not exist.'}, status=404)

    serializer = CommentFormSerializer(comment)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_required('ftw.delete_comment', raise_exception=True)
def comment_delete(request, pk):
    try:
        comment = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return Response({'error': 'Comment does not exist.'}, status=404)
    comment.delete()
    return Response(status=204)

######################################### Category ##################################################

#@swagger_auto_schema(method='GET', responses={200: CategoryListSerializer(many=True)})
#@api_view(['GET'])
#@permission_required('ftw.view_category', raise_exception=True)
#def category_list(request):
#    categorys = Category.objects.all()
#    serializer = CategoryListSerializer(categorys, many=True)
#    return Response(serializer.data)


@swagger_auto_schema(method='POST', request_body=CategoryFormSerializer, responses={200: CategoryFormSerializer()})
@api_view(['POST'])
@permission_required('ftw.add_category', raise_exception=True)
def category_form_create(request):
    data = JSONParser().parse(request)
    serializer = CategoryFormSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@swagger_auto_schema(method='PUT', request_body=CategoryFormSerializer, responses={200: CategoryFormSerializer()})
@api_view(['PUT'])
@permission_required('ftw.change_category', raise_exception=True)
def category_form_update(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({'error': 'Category does not exist.'}, status=404)

    data = JSONParser().parse(request)
    serializer = CategoryFormSerializer(category, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@swagger_auto_schema(method='GET', responses={200: CategoryFormSerializer()})
@api_view(['GET'])
@permission_required('ftw.view_category', raise_exception=True)
def category_form_get(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({'error': 'Category does not exist.'}, status=404)

    serializer = CategoryFormSerializer(category)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_required('ftw.delete_category', raise_exception=True)
def category_delete(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({'error': 'Category does not exist.'}, status=404)
    category.delete()
    return Response(status=204)

######################################### FTWWort ##################################################

#@swagger_auto_schema(method='GET', responses={200: FTWWordListSerializer(many=True)})
#@api_view(['GET'])
#@permission_required('ftw.view_ftwword', raise_exception=True)
#def ftwword_list(request):
#    ftwwords = FTWWord.objects.all()
#    serializer = FTWWordListSerializer(ftwwords, many=True)
#    return Response(serializer.data)


@swagger_auto_schema(method='POST', request_body=FTWWordFormSerializer, responses={200: FTWWordFormSerializer()})
@api_view(['POST'])
@permission_required('ftw.add_ftwword', raise_exception=True)
def ftwword_form_create(request):
    data = JSONParser().parse(request)
    serializer = FTWWordFormSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@swagger_auto_schema(method='PUT', request_body=FTWWordFormSerializer, responses={200: FTWWordFormSerializer()})
@api_view(['PUT'])
@permission_required('ftw.change_ftwword', raise_exception=True)
def ftwword_form_update(request, pk):
    try:
        ftwword = FTWWord.objects.get(pk=pk)
    except FTWWord.DoesNotExist:
        return Response({'error': 'FTWWord does not exist.'}, status=404)

    data = JSONParser().parse(request)
    serializer = FTWWordFormSerializer(ftwword, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@swagger_auto_schema(method='GET', responses={200: FTWWordFormSerializer()})
@api_view(['GET'])
@permission_required('ftw.view_ftwword', raise_exception=True)
def ftwword_form_get(request, pk):
    try:
        ftwword = FTWWord.objects.get(pk=pk)
    except FTWWord.DoesNotExist:
        return Response({'error': 'FTWWord does not exist.'}, status=404)

    serializer = FTWWordFormSerializer(ftwword)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_required('ftw.delete_ftwword', raise_exception=True)
def ftwword_delete(request, pk):
    try:
        ftwword = FTWWord.objects.get(pk=pk)
    except FTWWord.DoesNotExist:
        return Response({'error': 'FTWWord does not exist.'}, status=404)
    ftwword.delete()
    return Response(status=204)
