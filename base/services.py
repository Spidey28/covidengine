import os


def _set_django_settings_module():
    build_mode = os.environ.get("BUILD_MODE", "LOCAL")
    if build_mode == "STAGE":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.stage")
    elif build_mode == "PROD":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.prod")
    elif build_mode == "LOCAL":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.local")
