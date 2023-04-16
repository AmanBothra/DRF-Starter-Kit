from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.useraccount.serializers import (
	OTPSerializer
)


class OTPVerificationView(APIView):
	def post(self, request):
		serializer = OTPSerializer(data=request.data)
		if serializer.is_valid():
			user = serializer.validated_data['user']
			otp_obj = serializer.validated_data['otp_obj']
			if otp_obj.expires_at < timezone.now():
				return Response({'message': 'OTP expired'}, status=status.HTTP_400_BAD_REQUEST)
			user.is_verified = True
			user.save()
			otp_obj.delete()
			return Response({'message': 'OTP verified successfully'}, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
