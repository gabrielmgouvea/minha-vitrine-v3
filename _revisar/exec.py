from django.contrib.auth.models import User
from core.models import Profile
user = User.objects.get(username='SEU_USERNAME')
user.profile.is_dev = True
user.profile.save()
exit()