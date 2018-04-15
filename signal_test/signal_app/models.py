from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.

# TODO 定义模型,与内置模型User为一对一关系
class Profile(models.Model):
	# TODO on_delete=models.CASCADE-->级联删除,一个表中删除数据,对应表数据也被删除
	user = models.OneToOneField(User,on_delete=models.CASCADE)


# TODO 定义一个方法,执行创建数据
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)


# TODO 信号监听-->当USer保存数据后,会调用create_user_profile,对其关联表也添加数据
post_save.connect(create_user_profile, sender=User)