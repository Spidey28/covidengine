from django.db import models
from .services import file_extension_validator

class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


# class User(TimeStampedModel):
#     name = models.CharField(
#         blank=True,
#         null=True,
#         max_length=30,
#     )
#     mobile_no = models.CharField(
#         max_length=16,
#         blank=True,
#         null=True,
#     )
#     email = models.EmailField(
#         blank=True,
#         null=True,
#     )

#     def __str__(self):
#         return self.name


class Category(TimeStampedModel):
    name = models.CharField(
        max_length=50, 
        blank=True,
        null=False,
        unique=True,
    )

    def __str__(self):
        return self.name


class Address(TimeStampedModel):
    line_1 = models.CharField(max_length=128, blank=True, null=True)
    line_2 = models.CharField(max_length=128, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    landmark = models.CharField(max_length=64, blank=True, null=True)
    pincode = models.CharField(
        max_length=10,
        blank=True,
        null=True,
    )

    def __str__(self):
        return ("Line 1: %s, Line 2: %s, Landmark: %s,"
                "Pincode: %s, City: %s, State: %s" %
                (
                    self.line_1 or '-', self.line_2 or '-',
                    self.landmark or '-', self.pincode or '-', self.city or '-',
                    self.state or '-'
                ))


class Feedback(TimeStampedModel):
    user = models.OneToOneField(
        "users.Account",
        related_name="user_feedback",
        on_delete=models.CASCADE,
    )
    message = models.TextField(
        blank=True,
        null=True,
    )
    report = models.BooleanField(
        default=False
    )
    post = models.ForeignKey(
        "Post",
        related_name="post",
        on_delete=models.CASCADE
    )


class Post(TimeStampedModel):
    user = models.OneToOneField(
        "users.Account",
        related_name="user",
        on_delete=models.CASCADE,
    )
    category = models.ManyToManyField(
        "Category",
        related_name="categories"
    )
    address = models.OneToOneField(
        "Address",
        related_name="address",
        on_delete=models.CASCADE,
    )
    message = models.TextField(
        blank=True,
        null=True,
    )
    document = models.FileField(
        upload_to="covid-documents/%Y/%m/%d",
        validators=[file_extension_validator],
        blank=True,
        null=True
    )
    like = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    dislike = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
