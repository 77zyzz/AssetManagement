from django.shortcuts import get_object_or_404, render, redirect
from django_pandas.io import read_frame

import pandas as pd
#from sqlalchemy import create_engine
import os

from .models import host_assets, web_assets

# Create your views here.



# def listasset(request):
#     #df=pd.read_csv(os.path.abspath("AssetManagement/upload/goby-20210403142429.csv"))
#     #df=df.loc[df['Port']>80]
#     # engine = create_engine('mysql+pymysql://root:123456@192.168.137.134:3306/AssertManagement')

#     # # 查询语句，选出employee表中的所有数据
#     # sql = ''' select * from domain_domain; '''
#     # # read_sql_query的两个参数: sql语句， 数据库连接
#     # df = pd.read_sql_query(sql, engine)

#     qs = host_assets.objects.all()
#     print(qs)
#     df = read_frame(qs=qs)
#     df.drop('id',axis=1,inplace=True)
#     html=df.to_html(index=False)
#     return render(request,'asset/list.html', {'html_table': html})





