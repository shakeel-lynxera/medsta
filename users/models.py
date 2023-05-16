from django.db import models
from baselayer.basemodel import LogsMixin
from django.contrib.auth.models import User


class FriendRelationsChoices(models.TextChoices):
    BLOCKED = 0, "Blocked"
    REQUESTED = 1, "Requested"
    FRIEND = 2, "Friend"
    FOLLOWER = 3, "Follower"


class Profile(LogsMixin):
    """
    User profile.
    """
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=50)
    title = models.TextField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def get_age(self):
        from datetime import date
        today = date.today()
        try:
            return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        except AttributeError:
            return None


class Experience(LogsMixin):
    """
    User experience.
    """
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    currently_working = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='experiences')


class Skill(LogsMixin):
    skill = models.CharField(max_length=99)
    rating = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skills')


class Interest(LogsMixin):
    interest = models.CharField(max_length=99)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='interests')


class Language(LogsMixin):
    language = models.CharField(max_length=99)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='languages')


class Accomplishment(LogsMixin):
    """
    User accomplishments.
    """
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    currently_working = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    visit_url = models.URLField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accomplishments')


class Education(LogsMixin):
    """
    User education.
    """
    degree = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    currently_studying = models.BooleanField(default=False)
    institution = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='educations')


class Friend(LogsMixin):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends')
    reciever = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend_of')
    status = models.CharField(max_length=50, choices=FriendRelationsChoices.choices, default=FriendRelationsChoices.REQUESTED)
    is_read = models.BooleanField(default=False)

    class Meta:
        unique_together = ('sender', 'reciever',)
