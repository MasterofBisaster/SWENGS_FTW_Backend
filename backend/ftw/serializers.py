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

    class Meta:
        model = Event
        fields = ['__all__', 'user_name', 'category_name']

    def get_user_name(self, obj):
        return obj.creator.username if obj.creator else ''

    def get_category_name(self, obj):
        return obj.category.title if obj.category else ''


class CommentFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


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
