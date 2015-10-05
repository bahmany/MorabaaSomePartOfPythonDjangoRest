from rest_framework import serializers
from rest_framework_mongoengine.serializers import DocumentSerializer
from amspApp.MyProfile.models import Posts, Profile


class PostsSerializer(DocumentSerializer):
    class Meta:
        model = Posts
        fields = (
            'id',
            'dateOfPost',
            'likes',
            'text',
            'extra',
        )

    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    def _get_default_field_names(self, *args, **kwargs):
        return self.get_field_names(*args, **kwargs)


    def create(self, validated_data, **kwargs):
        if not 'text' in validated_data:
            raise serializers.ValidationError(
                {"status": "Bad request", "message": [{"name": "Name", "message": "This field is required"}]})
        validated_data['authorUserID'] = kwargs['request'].user.pk
        validated_data['profile'] = Profile.objects.get(userID=kwargs['request'].user.pk)
        instance = Posts.objects.create(**validated_data)
        return instance
