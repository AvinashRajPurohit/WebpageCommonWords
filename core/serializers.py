from rest_framework import serializers
from core.models import WebSiteEssentials


class WebsiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = WebSiteEssentials
        fields = ['website_name', 'html_content']


class WebHtmlRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = WebSiteEssentials
        fields = ['html_content']
