# app/admin.py
from fastapi_admin.app import app as admin_app
from fastapi_admin.resources import Field, Model
from fastapi_admin.widgets import displays, filters, inputs

from app.db.models import User, YourModel


class UserResource(Model):
    label = "User"
    model = User
    filters = [
        filters.Search(
            name="username",
            label="Username",
            search_mode="contains",
        )
    ]
    fields = [
        "id",
        "username",
        "email",
        Field(
            name="password",
            label="Password",
            display=displays.Password(),
            input_=inputs.Password(),
        ),
    ]


class YourModelResource(Model):
    label = "YourModel"
    model = YourModel
    filters = [
        filters.Search(
            name="name",
            label="Name",
            search_mode="contains",
        )
    ]
    fields = [
        "id",
        "name",
        "description",
    ]


admin_app.register(UserResource)
admin_app.register(YourModelResource)
