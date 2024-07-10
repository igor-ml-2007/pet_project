from rest_framework import serializers


class MediaURLSerializer(serializers.Serializer):
    def to_representation(self, media):
        if not media:
            return None
        # Постараемся получить абсолютный URL-адрес файла
        try:
            return self.context["request"].build_absolute_uri(media.file.url)
        except Exception:
            return "http://testserver" + str(media.file.url)


class CommonSettingsSerializer(serializers.Serializer):
    our_shop_text = serializers.CharField()
    service_page_back_image = MediaURLSerializer()
    discount_page_back_image = MediaURLSerializer()
