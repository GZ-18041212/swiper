import datetime
from django.db import models
from django.utils.functional import cached_property

# Create your models here.
from lib.orm import ModelMixin


class User(models.Model):
    # 用户数据模型
    SEX=(
        ('M','男'),('F','女'),
    )
    nickname=models.CharField(max_length=32,unique=True)       #这是模板里面对数据变量和类型的一些定义
    phonenum=models.CharField(max_length=16,unique=True)
    sex=models.CharField(max_length=8,choices=SEX)
    birth_year=models.IntegerField(default=2000)
    birth_month=models.IntegerField(default=1)
    birth_day=models.IntegerField(default=1)
    avatar=models.CharField(max_length=256)
    location=models.CharField(max_length=64)
    # profile=models.ForeignKey()
    @cached_property     #把age当做是class一个属性
    def age(self):
        today=datetime.date.today()
        birth_date=datetime.date(
            self.birth_year,
            self.birth_month,
            self.birth_day
        )
        times=today-birth_date
        return times.days//365
    @property
    def profile(self):
        #用户的配置项目
        # self.id
        # user,created=User.objects.get_or_create(id=123)
        # if '_profile' not in self.__dict__:
        if not hasattr(self,'_profile'):
            _proflie,_=Profile.objects.get_or_create(id=self.id)
            self._proflie=_proflie
        return self._proflie

# User.profile.location='guanugzhou'
# User.profile.location='guanugzhou'
# new__user_profile

    def to_dict(self):
        return {
            'id':self.id,
            'nickname':self.nickname,
            'phonenum':self.phonenum,
            'sex':self.sex,
            'avatar':self.avatar,
            'location':self.location,
            'age':self.age,

        }






class Profile(models.Model,ModelMixin):
    # 用户配置项
    SEX = (
        ('M', '男'), ('F', '女'),
    )
    dating_sex = models.CharField(default='女',max_length=8, choices=SEX, verbose_name='匹配的性别')
    location=models.CharField(max_length=32,verbose_name='目标城市')

    min_distance=models.IntegerField(default=1,verbose_name='最小查找范围')
    max_distance=models.IntegerField(default=10,verbose_name='最大查找范围')

    min_dating_age=models.IntegerField(default=18,verbose_name='最小交友年龄')
    max_dating_age=models.IntegerField(default=45,verbose_name='最大交友年龄')

    vibration=models.BooleanField(default=True,verbose_name='是否开启震动')
    only_matche=models.BooleanField(default=True,verbose_name='不让为匹配的人看到我的相册')
    # auto_play=models.Field(default=True,verbose_name='自动播放视频')































