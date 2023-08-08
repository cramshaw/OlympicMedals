from olympic_data.models import Country
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class CountryMedalSerializer(ModelSerializer):
    gold_medal_count = SerializerMethodField(read_only=True)
    silver_medal_count = SerializerMethodField()
    bronze_medal_count = SerializerMethodField()
    population_per_gold_medal = SerializerMethodField(read_only=True)
    population_per_silver_medal = SerializerMethodField()
    population_per_bronze_medal = SerializerMethodField()

    class Meta:
        model = Country
        fields = [
            "country_name",
            "country_code",
            "gold_medal_count",
            "silver_medal_count",
            "bronze_medal_count",
            "population_per_gold_medal",
            "population_per_silver_medal",
            "population_per_bronze_medal",
        ]

    def get_gold_medal_count(self, inst):
        return inst.gold_medals

    def get_silver_medal_count(self, inst):
        return inst.silver_medals

    def get_bronze_medal_count(self, inst):
        return inst.bronze_medals

    def get_population_per_gold_medal(self, inst):
        return inst.population_per_gold_medal

    def get_population_per_silver_medal(self, inst):
        return inst.population_per_silver_medal

    def get_population_per_bronze_medal(self, inst):
        return inst.population_per_bronze_medal
