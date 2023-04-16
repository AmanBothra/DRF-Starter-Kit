from django.utils import timezone
from rest_framework import serializers

from apps.useraccount.models import (
	User,
	EmailOtpCode
)


class OTPSerializer(serializers.Serializer):
	email = serializers.EmailField()
	otp = serializers.CharField()

	def validate(self, data):
		email = data.get('email')
		otp = data.get('otp')
		try:
			user = User.objects.get(email=email)
			otp_obj = EmailOtpCode.objects.filter(user=user, otp=otp, expires_at__gt=timezone.now()).first()
			if not otp_obj:
				raise serializers.ValidationError('Invalid OTP')
		except User.DoesNotExist:
			raise serializers.ValidationError('User not found')
		data['user'] = user
		data['otp_obj'] = otp_obj
		return data
