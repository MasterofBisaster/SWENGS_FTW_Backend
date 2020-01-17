from rest_framework import serializers

from backend.ftw.models import Event, Comment, Category, Location, FTWWord, Media


class EventListSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ['id', 'name', 'start_date', 'end_date', 'user_name', 'category_name', 'short_description']

    def get_user_name(self, obj):
        return obj.creator.username if obj.creator else ''

    def get_category_name(self, obj):
        return obj.category.title if obj.category else ''


class EventFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class EventDetailSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    category_name = serializers.SerializerMethodField()
    location_name = serializers.SerializerMethodField()
    location_city = serializers.SerializerMethodField()
    location_street = serializers.SerializerMethodField()
    location_zip_code = serializers.SerializerMethodField()
    location_country = serializers.SerializerMethodField()
    location_max_user = serializers.SerializerMethodField()

    # location_picture = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ['id', 'name', 'start_date', 'end_date', 'user_name', 'creator',
                  'private', 'short_description', 'location_name', 'location_street', 'location_city',
                  'location_zip_code', 'location_country', 'location_max_user', 'max_users', 'costs', 'user_name',
                  'category_name']

    def get_user_name(self, obj):
        return obj.creator.username if obj.creator else ''

    def get_category_name(self, obj):
        return obj.category.title if obj.category else ''

    def get_location_name(self, obj):
        return obj.location.name if obj.location else ''

    def get_location_street(self, obj):
        return obj.location.street if obj.location else ''

    def get_location_city(self, obj):
        return obj.location.city if obj.location else ''

    def get_location_zip_code(self, obj):
        return obj.location.zip_code if obj.location else ''

    def get_location_country(self, obj):
        return obj.location.country if obj.location else ''

    def get_location_max_user(self, obj):
        return obj.location.max_user if obj.location else ''

    # def get_location_picture(self, obj):
    #   return obj.location.picture if obj.location else ''


class CommentFormSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'event', 'creator', 'content', 'create_date', 'user_name']

    def get_user_name(self, obj):
        return obj.creator.username if obj.creator else ''


class CategoryFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class LocationFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class FTWWordFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = FTWWord
        fields = '__all__'


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'
