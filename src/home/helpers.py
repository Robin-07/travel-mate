from authentication.models import UserProfile

def get_profile_img_url(user):
    context = {}
    if user.is_authenticated:
        profile_img_url = UserProfile.objects.filter(user=user).first().image_url
        context.update({"profile_img_url": profile_img_url})
    return context