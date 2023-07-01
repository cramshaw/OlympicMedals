# Generated by Django 4.2.2 on 2023-07-01 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Athlete",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("athlete_name", models.CharField(max_length=200)),
                (
                    "gender",
                    models.CharField(choices=[("MEN", "Men"), ("WOMEN", "Women")]),
                ),
            ],
        ),
        migrations.CreateModel(
            name="City",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("city_name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("country_name", models.CharField(max_length=50)),
                ("country_code", models.SlugField(max_length=3)),
                ("population", models.IntegerField(blank=True, null=True)),
                (
                    "gdp_per_capita",
                    models.DecimalField(
                        blank=True, decimal_places=30, max_digits=50, null=True
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Discipline",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("discipline_name", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("event_name", models.CharField(max_length=200)),
                (
                    "gender",
                    models.CharField(choices=[("MEN", "Men"), ("WOMEN", "Women")]),
                ),
                (
                    "discipline",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="olympic_data.discipline",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Games",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("year", models.PositiveSmallIntegerField()),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="olympic_data.city",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Sport",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sport_name", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="MedalWin",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "medal_type",
                    models.CharField(
                        choices=[
                            ("GOLD", "Gold"),
                            ("SILVER", "Silver"),
                            ("BRONZE", "Bronze"),
                        ]
                    ),
                ),
                ("athletes", models.ManyToManyField(to="olympic_data.athlete")),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="olympic_data.country",
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="olympic_data.event",
                    ),
                ),
                (
                    "games",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="olympic_data.games",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="discipline",
            name="sport",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="olympic_data.sport"
            ),
        ),
        migrations.AddField(
            model_name="athlete",
            name="country",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="olympic_data.country"
            ),
        ),
    ]
