from django.db import models



class host_assets(models.Model):
    company = models.CharField(max_length=50,verbose_name=u'厂商')
    ip = models.CharField(max_length=50,verbose_name=u'IP',null=True,blank=True)
    port = models.CharField(max_length=50,verbose_name=u'端口',null=True,blank=True)
    service = models.CharField(max_length=50,verbose_name=u'服务',null=True,blank=True)
    banner = models.CharField(max_length=50,verbose_name=u'banner',null=True,blank=True)
    describe = models.CharField(max_length=50,verbose_name=u'描述',null=True,blank=True)

class web_assets(models.Model):
    company = models.CharField(max_length=50,verbose_name=u'厂商')
    URL = models.CharField(max_length=50,verbose_name=u'URL',null=True,blank=True)
    webtitle = models.CharField(max_length=50,verbose_name=u'系统名称',null=True,blank=True)
    finger = models.CharField(max_length=50,verbose_name=u'指纹',null=True,blank=True)
    describe = models.CharField(max_length=50,verbose_name=u'描述',null=True,blank=True)
