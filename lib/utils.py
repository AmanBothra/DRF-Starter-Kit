import os
from uuid import uuid4
from django.utils.deconstruct import deconstructible
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError


@deconstructible
class PathAndRename(object):

	def __init__(self, sub_path):
		self.path = sub_path

	def __call__(self, instance, filename):
		ext = os.path.splitext(filename)[1]
		# set filename as random string
		filename = '{}{}'.format(uuid4().hex, ext)
		# return the whole path to the file
		return os.path.join(self.path, filename)


def image_file_extension_validator(file):
	return [
		FileExtensionValidator(allowed_extensions=["svg", "png", "jpg", "jpeg", "webp"])(file)
	]


def file_size(value):
	"""
		Same as FileField, but you can specify:
			2.5MB - 2621440
			5MB - 5242880
			10MB - 10485760
			20MB - 20971520
			50MB - 5242880
			100MB - 104857600
			250MB - 214958080
			500MB - 429916160
	"""
	limit = 3 * 1024 * 1024
	if value.size > limit:
		raise ValidationError("File too large. Size should not exceed {} MB.".format(limit / 1024 / 1024))


def document_file_extension_validator(value):
	ext = os.path.splitext(value.name)[1]
	valid_extensions = [".pdf", ".doc", ".docx"]
	if ext not in valid_extensions:
		raise ValidationError("Unsupported file type. Only Pdf and MsWord files are allowed.")
