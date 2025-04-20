#coding:utf-8
from django.db import models

from .model import BaseModel

from datetime import datetime



class yonghu(BaseModel):
    __doc__ = u'''yonghu'''
    __tablename__ = 'yonghu'

    __loginUser__='zhanghao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='zhanghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    zhanghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='账号' )
    xingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='姓名' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    lianxidianhua=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系电话' )
    touxiang=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    '''
    zhanghao=VARCHAR
    xingming=VARCHAR
    mima=VARCHAR
    xingbie=VARCHAR
    lianxidianhua=VARCHAR
    touxiang=Text
    '''
    class Meta:
        db_table = 'yonghu'
        verbose_name = verbose_name_plural = '用户'
class traveldemand(BaseModel):
    __doc__ = u'''traveldemand'''
    __tablename__ = 'traveldemand'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    starttime=models.DateTimeField  (  null=True, unique=False, verbose_name='开始时间' )
    jieshushijian=models.DateTimeField  (  null=True, unique=False, verbose_name='结束时间' )
    kaishizhandian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='开始站点' )
    jieshuzhandian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='结束站点' )
    shiyongzhebianhao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='使用者编号' )
    shiyongzhexingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='使用者性别' )
    shiyongzhenianling=models.CharField ( max_length=255, null=True, unique=False, verbose_name='使用者年龄' )
    qixingshizhang=models.FloatField   (  null=True, unique=False, verbose_name='骑行时长(分钟)' )
    qixingjuli=models.FloatField   (  null=True, unique=False, verbose_name='骑行距离(公里)' )
    dangritianqi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='当日天气' )
    dangriwendu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='当日温度(摄氏度)' )
    dangrishidu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='当日湿度(%)' )
    dangrifengsu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='当日风速(米/秒)' )
    shifougongzuori=models.CharField ( max_length=255, null=True, unique=False, verbose_name='是否工作日' )
    shifoujiejiari=models.CharField ( max_length=255, null=True, unique=False, verbose_name='是否节假日' )
    hourlyrentalquantity=models.IntegerField  (  null=True, unique=False, verbose_name='小时级租赁数量' )
    traveldemand=models.IntegerField  (  null=True, unique=False, verbose_name='出行需求量' )
    travelfrequency=models.IntegerField  (  null=True, unique=False, verbose_name='出行频率' )
    '''
    starttime=DateTime
    jieshushijian=DateTime
    kaishizhandian=VARCHAR
    jieshuzhandian=VARCHAR
    shiyongzhebianhao=VARCHAR
    shiyongzhexingbie=VARCHAR
    shiyongzhenianling=VARCHAR
    qixingshizhang=Float
    qixingjuli=Float
    dangritianqi=VARCHAR
    dangriwendu=VARCHAR
    dangrishidu=VARCHAR
    dangrifengsu=VARCHAR
    shifougongzuori=VARCHAR
    shifoujiejiari=VARCHAR
    hourlyrentalquantity=Integer
    traveldemand=Integer
    travelfrequency=Integer
    '''
    class Meta:
        db_table = 'traveldemand'
        verbose_name = verbose_name_plural = '出行需求'
class traveldemandforecast(BaseModel):
    __doc__ = u'''traveldemandforecast'''
    __tablename__ = 'traveldemandforecast'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    starttime=models.DateTimeField  (  null=True, unique=False, verbose_name='日期' )
    hourlyrentalquantity=models.IntegerField  (  null=True, unique=False, verbose_name='小时级租赁数量' )
    traveldemand=models.IntegerField  (  null=True, unique=False, verbose_name='出行需求量' )
    travelfrequency=models.IntegerField  (  null=True, unique=False, verbose_name='出行频率' )
    '''
    starttime=DateTime
    hourlyrentalquantity=Integer
    traveldemand=Integer
    travelfrequency=Integer
    '''
    class Meta:
        db_table = 'traveldemandforecast'
        verbose_name = verbose_name_plural = '出行需求预测'
