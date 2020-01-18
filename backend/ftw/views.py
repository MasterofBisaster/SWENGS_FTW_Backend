from django.contrib.auth.decorators import permission_required
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.response import Response
from rest_framework import views
from django.contrib.auth.models import Group, User

from django.db.models import Q


from backend.ftw.serializers import EventListSerializer, EventFormSerializer, LocationFormSerializer, \
    CommentFormSerializer, CategoryFormSerializer, FTWWordFormSerializer, MediaSerializer, EventDetailSerializer, \
    RegisterFormSerializer, FTWUserDetailSerializer

from backend.ftw.models import Event, Comment, Category, Location, FTWWord, Media, FTWUser


######################################### Event ##################################################

@swagger_auto_schema(method='GET', responses={200: EventListSerializer(many=True)})
@api_view(['GET'])
#@permission_required('ftw.view_event', raise_exception=True)
def event_list(request):
    events = Event.objects.all()
    serializer = EventListSerializer(events, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='GET', responses={200: EventListSerializer(many=True)})
@api_view(['GET'])
def public_event_list(request):
    events = Event.objects.filter(private=False)
    serializer = EventListSerializer(events, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='GET', responses={200: EventListSerializer(many=True)})
@api_view(['GET'])
def search_event_list(request, searchString):
    events = Event.objects.filter(name__contains=searchString)
    serializer = EventListSerializer(events, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='GET', responses={200: EventListSerializer(many=True)})
@api_view(['GET'])
@permission_required('ftw.view_event', raise_exception=True)
def private_event_list(request, pk):
    events = Event.objects.filter(Q(private=False) | Q(creator__id=pk) | Q(creator__friends__id=pk))
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


@swagger_auto_schema(method='GET', responses={200: EventDetailSerializer()})
@api_view(['GET'])
def event_detail_get(request, pk):
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return Response({'error': 'Event does not exist.'}, status=404)

    serializer = EventDetailSerializer(event)
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


@swagger_auto_schema(method='GET', responses={200: LocationFormSerializer(many=True)})
@api_view(['GET'])
def location_list(request):
    locations = Location.objects.all()
    serializer = LocationFormSerializer(locations, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='GET', responses={200: LocationFormSerializer(many=True)})
@api_view(['GET'])
def search_location_list(request, searchString):
    locations = Location.objects.filter(name__contains=searchString)
    serializer = LocationFormSerializer(locations, many=True)
    return Response(serializer.data)


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

@swagger_auto_schema(method='GET', responses={200: CommentFormSerializer(many=True)})
@api_view(['GET'])
def comment_list(request):
    comments = Comment.objects.all()
    serializer = CommentFormSerializer(comments, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='GET', responses={200: CommentFormSerializer(many=True)})
@api_view(['GET'])
def comment_list_event(request, pk):
    comments = Comment.objects.filter(event__pk=pk)
    serializer = CommentFormSerializer(comments, many=True)
    return Response(serializer.data)


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

@swagger_auto_schema(method='GET', responses={200: CategoryFormSerializer(many=True)})
@api_view(['GET'])
def category_list(request):
    categorys = Category.objects.all()
    serializer = CategoryFormSerializer(categorys, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='GET', responses={200: CategoryFormSerializer(many=True)})
@api_view(['GET'])
def search_category_list(request, searchString):
    categories = Category.objects.filter(title__contains=searchString)
    serializer = CategoryFormSerializer(categories, many=True)
    return Response(serializer.data)


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

@swagger_auto_schema(method='GET', responses={200: FTWWordFormSerializer(many=True)})
@api_view(['GET'])
def ftwword_list(request):
    ftwwords = FTWWord.objects.all()
    serializer = FTWWordFormSerializer(ftwwords, many=True)
    return Response(serializer.data)


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


######################################### Media ##################################################

class FileUploadView(views.APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        file = request.FILES['file']
        file_input = {
            'original_file_name': file.name,
            'content_type': file.content_type,
            'size': file.size,
        }
        serializer = MediaSerializer(data=file_input)
        if serializer.is_valid():
            serializer.save()
            default_storage.save('media/' + str(serializer.data['id']), ContentFile(file.read()))
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


def media_download(request, pk):
    media = Media.objects.get(pk=pk)
    data = default_storage.open('media/' + str(pk)).read()
    content_type = media.content_type
    response = HttpResponse(data, content_type=content_type)
    original_file_name = media.original_file_name
    response['Content-Disposition'] = 'inline; filename=' + original_file_name
    return response


@swagger_auto_schema(method='GET', responses={200: MediaSerializer()})
@api_view(['GET'])
def media_get(request, pk):
    try:
        media = Media.objects.get(pk=pk)
    except Media.DoesNotExist:
        return Response({'error': 'Media does not exist.'}, status=404)

    serializer = MediaSerializer(media)
    return Response(serializer.data)


######################################### Register ##################################################

@swagger_auto_schema(method='POST', responses={200: RegisterFormSerializer()})
@api_view(['POST'])
def register_form_create(request):
    data = JSONParser().parse(request)
    serializer = RegisterFormSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        newUser = User.objects.get(username=serializer.data.get("username"))
        FTWUser.objects.create(user=newUser)
        return Response(serializer.data, status=201)
    return Response(status=400)


######################################### User ##################################################


@swagger_auto_schema(method='GET', responses={200: FTWUserDetailSerializer()})
@api_view(['GET'])
def user_detail_get(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except Event.DoesNotExist:
        return Response({'error': 'User does not exist.'}, status=404)

    serializer = FTWUserDetailSerializer(user)
    return Response(serializer.data)


######################################### add User to Event ##################################################

@swagger_auto_schema(method='POST', responses=200)
@api_view(['POST'])
def add_user_to_event(request, user_id, event_id):

    event = Event.objects.get(pk=event_id)
    users = event.confirmed_users.all()
    user = User.objects.get(pk=user_id)
    if user in users:
        users = users.filter(~Q(username=user.username))
        event.confirmed_users.set(users)
        #event.confirmed_users.exclude(username=user.username)
    else:
        event.confirmed_users.add(user)
    return Response(status=201)
