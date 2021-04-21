from django.contrib import admin
from .models import host_assets,web_assets

from import_export import resources
from import_export.admin import ExportActionModelAdmin

admin.site.site_header = '资产管理'
admin.site.site_title = '资产管理系统'


class host_assets_resource(resources.ModelResource):
    class Meta:
        model = host_assets
        #导出时不包含id
        exclude = ('id',)

    #自定义导出头，以verbose_name为列名
    def get_export_headers(self):
        headers=[]
        for field in self.get_export_fields():
            headers.append(self.Meta.model._meta.get_field(field.column_name).verbose_name)
        return headers

class show_host_assets(ExportActionModelAdmin):
    resource_class = host_assets_resource
    # 设置页面可以展示的字段
    list_display = ('company','ip','port','service','banner','describe')

    # 增加搜索
    search_fields = ('company','ip','port','service','banner','describe')
    # 每页显示条目数 缺省值8 分页有bug
    
    list_max_show_all  = 200
    list_per_page = 8

    
class web_assets_resource(resources.ModelResource):
    class Meta:
        model = web_assets
        #导出时不包含id
        exclude = ('id',)

    #自定义导出头，以verbose_name为列名
    def get_export_headers(self):
        headers=[]
        for field in self.get_export_fields():
            headers.append(self.Meta.model._meta.get_field(field.column_name).verbose_name)
        return headers

class show_web_assets(ExportActionModelAdmin):
    resource_class = web_assets_resource
    # 设置页面可以展示的字段
    list_display = ('company','URL','webtitle','finger','describe')
    # 增加搜索
    search_fields = ('company','URL','webtitle','finger','describe')
    # 每页显示条目数 缺省值8 分页有bug
    list_max_show_all  = 200
    list_per_page = 8
    


admin.site.register(host_assets, show_host_assets)
admin.site.register(web_assets, show_web_assets)