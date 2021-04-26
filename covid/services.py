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


def update_object(obj, data, force_save=True):
    '''
    Helper function to update(mainly for Partial updates) an ORM object with
    given dictionary (i.e. keys are fields, and respective values are updated
    values).

    Args:
        obj (object): Django ORM object.
        data (dict): Dict object with key-value pairs of field-value.
        force_save (bool): Boolean value to toggle execution of .save()

    Returns:
        object: Returns, updated Django ORM object.
    '''
    for key, value in data.items():
        setattr(obj, key, value)

    if force_save:
        obj.save(update_fields=data.keys())

    return obj