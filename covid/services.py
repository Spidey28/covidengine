from django.conf import settings
from django.core.exceptions import ValidationError


def file_extension_validator(value):
    valid_extensions_file = ('pdf', 'png', 'jpeg', 'jpg')
    if value:
        file_name = value.name
        file_extension = file_name.split('.')[-1].lower()
        if file_extension in valid_extensions_file:
            if value.size > int(settings.MAX_UPLOAD_SIZE):
                raise ValidationError("Please keep the file size under 10 MB")
        else:
            raise ValidationError("Please upload file in PDF/PNG/JPG/JPEG formats.")
    else:
        return True
