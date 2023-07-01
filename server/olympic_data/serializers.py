from rest_framework.serializers import ModelSerializer, SerializerMethodField

from olympic_data.models import Country


class CountryMedalSerializer(ModelSerializer):
    gold_medal_count = SerializerMethodField(read_only=True)
    silver_medal_count = SerializerMethodField()
    bronze_medal_count = SerializerMethodField()

    class Meta:
        model = Country
        fields = [
            "country_name",
            "country_code",
            "gold_medal_count",
            "silver_medal_count",
            "bronze_medal_count",
        ]

    def get_gold_medal_count(self, inst):
        return inst.gold_medals

    def get_silver_medal_count(self, inst):
        return inst.silver_medals

    def get_bronze_medal_count(self, inst):
        return inst.bronze_medals
