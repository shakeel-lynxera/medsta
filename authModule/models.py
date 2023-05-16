from django.db import models
from baselayer.basemodel import LogsMixin
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from utilies.constants import ConstantStrings
from medsta.settings import EMAIL_HOST_USER
from smtplib import SMTPException
from utilies.reuseable_methods import generate_six_length_random_number
from django.core.mail import send_mail
import logging
from django.conf import settings
logger = logging.getLogger(settings.LOGGER_NAME_PREFIX + __name__)
from termcolor import colored
# Create your models here.

class UserOTP(LogsMixin):
    otp = models.CharField(max_length=6)
    is_verified = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "temporary_user"
        verbose_name = _("Temporary User")
        verbose_name_plural = _("Temporary Users")
        ordering = ("-modified_at",)

    def save(self, *args, **kwargs):
        """Sending and saving email otp on first sign up
        """
        self.otp = generate_six_length_random_number()
        try:
            send_mail(ConstantStrings.EMAIL_TITLE.value, self.otp, EMAIL_HOST_USER, [self.user.email])
        except SMTPException as smtp_exc:
            logger.error(f" {colored('smtp exception', 'yellow')}: {smtp_exc}")
        except Exception as exc:
            logger.error(f" {colored('exception', 'yellow')}: {exc}")
            
        super(UserOTP, self).save(*args, **kwargs)


class ForgetPasswordOTP(LogsMixin):
    otp = models.CharField(max_length=6)
    is_verified = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "forget_password"
        verbose_name = _("Forget Password OTP")
        verbose_name_plural = _("Forget Password OTPs")
        ordering = ("-modified_at",)

    def save(self, *args, **kwargs):
        """Sending and saving email otp on forget password
        """
        self.otp = generate_six_length_random_number()
        try:
            send_mail(ConstantStrings.EMAIL_TITLE.value, self.otp, EMAIL_HOST_USER, [self.user.email])
        except SMTPException as smtp_exc:
            logger.error(f" {colored('smtp exception', 'yellow')}: {smtp_exc}")
        except Exception as exc:
            logger.error(f" {colored('exception', 'yellow')}: {exc}")
            
        super(ForgetPasswordOTP, self).save(*args, **kwargs)