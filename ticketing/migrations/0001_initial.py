# Generated by Django 2.2.5 on 2019-09-24 13:08

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [("auth", "0011_update_proxy_permissions")]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Category")),
            ],
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "c_name",
                    models.CharField(max_length=150, verbose_name="Customer Name"),
                ),
                ("c_id", models.CharField(max_length=100, verbose_name="Customer ID")),
                (
                    "c_phone",
                    models.CharField(
                        max_length=14, verbose_name="Customer Phone Number"
                    ),
                ),
                (
                    "c_email",
                    models.CharField(max_length=111, verbose_name="Customer Email"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Status",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Status")),
            ],
        ),
        migrations.CreateModel(
            name="Technician",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "te_name",
                    models.CharField(max_length=150, verbose_name="Technician Name"),
                ),
                (
                    "te_id",
                    models.CharField(
                        max_length=100, verbose_name="Assigned Technician"
                    ),
                ),
                (
                    "te_phone",
                    models.CharField(
                        max_length=14, verbose_name="Technician Phone Number"
                    ),
                ),
                (
                    "te_email",
                    models.CharField(max_length=111, verbose_name="Technician Email"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Ticket",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "timestamp",
                    models.DateTimeField(auto_now_add=True, verbose_name="Timestamp"),
                ),
                (
                    "t_opened",
                    models.DateTimeField(auto_now_add=True, verbose_name="Date Opened"),
                ),
                ("t_subject", models.CharField(max_length=100, verbose_name="Subject")),
                ("t_body", models.TextField(verbose_name="Ticket Summary")),
                (
                    "t_closed",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Date Closed"
                    ),
                ),
                (
                    "c_info",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ticketing.Customer",
                    ),
                ),
                (
                    "t_category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ticketing.Category",
                    ),
                ),
                (
                    "t_status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ticketing.Status",
                    ),
                ),
                (
                    "tech_info",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ticketing.Technician",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=30, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "u_name",
                    models.CharField(max_length=150, verbose_name="Customer Name"),
                ),
                ("u_id", models.CharField(max_length=100, verbose_name="Customer ID")),
                (
                    "u_phone",
                    models.CharField(
                        max_length=14, verbose_name="Customer Phone Number"
                    ),
                ),
                (
                    "u_email",
                    models.CharField(max_length=111, verbose_name="Customer Email"),
                ),
                (
                    "u_permission_level",
                    models.CharField(
                        choices=[("1", "User"), ("2", "Technician")], max_length=11
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[("objects", django.contrib.auth.models.UserManager())],
        ),
    ]
