# Generated by Django 5.0.3 on 2024-03-16 16:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
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
                ("name", models.CharField(max_length=255, unique=True)),
                ("address", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name="Device",
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
                    "name",
                    models.CharField(
                        choices=[
                            ("mobile", "Mobile"),
                            ("tab", "Tablet"),
                            ("laptop", "Laptop"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "condition",
                    models.CharField(
                        choices=[
                            ("new", "New"),
                            ("used", "Used"),
                            ("damaged", "Damaged"),
                            ("faulty", "Faulty"),
                            ("repaired", "Repaired"),
                        ],
                        max_length=100,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Employee",
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
                ("name", models.CharField(max_length=100)),
                (
                    "designation",
                    models.CharField(
                        choices=[
                            ("TL", "Team Lead"),
                            ("PO", "Product Owner"),
                            ("PM", "Project Manager"),
                            ("OA", "Office Assistant"),
                            ("SWE", "Software Engineer"),
                            ("HRM", "Human Resource Manager"),
                            ("SQAE", "Software Quality Assurance Engineer"),
                            ("others", "Others"),
                        ],
                        max_length=100,
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.company"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Checkout",
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
                ("checkout_date", models.DateTimeField(auto_now_add=True)),
                (
                    "checkout_condition",
                    models.CharField(
                        choices=[
                            ("new", "New"),
                            ("used", "Used"),
                            ("damaged", "Damaged"),
                            ("faulty", "Faulty"),
                            ("repaired", "Repaired"),
                        ],
                        max_length=100,
                    ),
                ),
                ("return_date", models.DateTimeField(blank=True, null=True)),
                (
                    "return_condition",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("new", "New"),
                            ("used", "Used"),
                            ("damaged", "Damaged"),
                            ("faulty", "Faulty"),
                            ("repaired", "Repaired"),
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.company"
                    ),
                ),
                (
                    "device",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.device"
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.employee"
                    ),
                ),
            ],
        ),
    ]
