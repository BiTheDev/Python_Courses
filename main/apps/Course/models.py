from django.db import models


class CourseManager(models.Manager):
	def basic_validator(self, postData):
		errors = {}
		if len(postData['name']) < 1:
			errors['first_name'] = "Course Name should not be blank"
		return errors
class DescManager(models.Manager):
	def basic_validator(self, postData):
		errors = {}
		if len(postData['DESC']) < 1:
			errors['DESC'] = "Description should not be blank"
		return errors


class Course(models.Model):
	name = models.CharField(max_length = 255)
	create_at = models.DateTimeField(auto_now_add= True)
	update_at = models.DateTimeField(auto_now= True)

	objects = CourseManager()
class Description(models.Model):
	Desc = models.TextField()
	course_desc = models.OneToOneField(Course, related_name = "DESC", on_delete = models.CASCADE, primary_key = True)
	create_at = models.DateTimeField(auto_now_add= True)
	update_at = models.DateTimeField(auto_now= True)
	objects = DescManager()