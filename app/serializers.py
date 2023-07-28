from rest_framework import serializers
from app.models.test import Test

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['id', 'panel_id', 'name', 'description', 'info_url', 'normal_reference', 'unit_of_measure']






        