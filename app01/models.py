from django.db import models

# Create your models here.
class Depart(models.Model):

    """
    部门表
    """
    title = models.CharField(verbose_name="部门名称", max_length=32)

    def __str__(self):
        return self.title

class UserInfo(models.Model):
    """
    用户表
    """

    name = models.CharField(verbose_name="姓名",max_length=32)

    gender_choices = (
        (1,"男"),
        (2,"女")
    )
    gender = models.IntegerField(verbose_name='性别',choices=gender_choices,default=1)

    class_choices = (
        (11, "全栈一期"),
        (22, "全栈二期")
    )
    class_ch = models.IntegerField(verbose_name='班级', choices=class_choices, default=11)

    age = models.CharField(verbose_name="年龄",max_length=32)
    email = models.CharField(verbose_name="邮箱",max_length=32)
    depart = models.ForeignKey(verbose_name="部门", to="Depart",on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

class Deploy(models.Model):
    title = models.CharField(verbose_name="标题", max_length=32)
    status_choices = (
        (1,"在线"),
        (2,"离线")
    )

    status = models.IntegerField(verbose_name="状态",choices=status_choices)

    def __str__(self):
        return self.title