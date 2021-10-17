from authentication.models import UserProfile
from django.utils import timezone


def get_profile_img_url(user):
    context = {}
    if user.is_authenticated:
        profile_img_url = UserProfile.objects.filter(user=user).first().image_url
        context.update({"profile_img_url": profile_img_url})
    return context


def past_years(ago):
    this_year = timezone.now().year
    return list(range(this_year - ago - 1, this_year))