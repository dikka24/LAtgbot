import os

from app.models import AddPublication, Admin, Group, Settings


def get_active_settings(id=None):
    if id: id = str(id)
    settings = Settings.objects.filter(group__tgid=id)
    if settings.exists():
        return settings.first()
    return Settings.objects.filter(base=True).first()


API_TOKEN = os.environ.get("API_TOKEN")


ALLOWED_GROUPS = Group.objects.all()

ADMINS = Admin.objects.all()

async def check_publications():
    return AddPublication.objects.all()
