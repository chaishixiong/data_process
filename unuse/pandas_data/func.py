import pymysql
import pandas as pd
from sqlalchemy import create_engine

def engine(database='e_commerce',host='228'):
    result = create_engine('mysql+pymysql://{user}:{pw}@192.168.0.{host}/{db}?charset=utf8'.format(user='dev',pw='Data227or8Dev715#',host=host,db=database,),encoding='utf-8')
    return result

def engine_125(database='education_bi_online'):
    engine = create_engine('mysql+pymysql://{user}:{pw}@192.168.0.125/{db}?charset=utf8'.format(user='nriat_dev',pw='Dev530#',db=database,),encoding='utf-8')
    return engine
    


def readsql(database, table, fields=None,host=None):
    # print(database)
    if type(database) != str:
        raise ValueError
    conn = pymysql.connect(user='dev', password='Data227or8Dev715#', host=host, database=database, port=3306,charset='utf8')

    if fields == None:
        address = "select * from " + table
    elif type(fields) == str:
        address = "select" + table + ".fields from " + table
    elif type(fields) == list:
        if [i for i in fields if type(i) != str]:
            raise ValueError
        address = "select "
        for i in fields:
            address += table + '.'
            address += i
            address += ','
        address = address[:-1] + " from " + table
    return pd.read_sql(address, con=conn, coerce_float=False)
 


class pandas_sql:
    def __init__(self,database=None,library=None,host='227',user='dev',password='Data227or8Dev715#'):
        self.host='192.168.0.'+host
        self.database =database
        self.library = library
        self.user = user
        self.password = password
        self.port=3306
        self.charset = 'utf8'
        
    def reset(self,database=False,library=False,host=False):
        if database:
            self.database = database
        if library:
            self.library = library
        if host:
            self.host='192.168.0.'+host
            
    def shop_detail(self):
        print(self.host,'\n')
        print(self.database,'\n')
        print(self.library,'\n')
    
    def conn_sql(self):
        return pymysql.connect(user=self.user,
        password=self.password,
        host=self.host,
        database=self.database,
        port=self.port,
        charset=self.charset)
    
    def cursor_sql(self):
        return self.conn_sql().cursor()
    
    def number_sql(self):
        number = self.conn_sql().cursor()
        number.execute('select count(*) from '+self.library)
        return number.fetchone()[0]
        
    def columns_name(self):
        col_name = self.cursor_sql()
        col_name.execute("select COLUMN_NAME from information_schema.columns where TABLE_NAME='"+self.library+"'\
         and TABLE_SCHEMA="+"'"+self.database+"'")
        col_list = col_name.fetchall()
        return [i[0] for i in col_list]
    
    def distinct_sql(self,col=None):
        if col == None:
            print("need a column\'s name")
            return
        return pd.read_sql("select distinct "+ col +" from "+self.library,con=self.conn_sql())
    
    def read_sql(self,database=False,library=False,host=False,column=None,rule = None,rule_where=None):
        self.reset(database,library,host)
        if rule !=None:
            return pd.read_sql(rule,con=self.conn_sql(),coerce_float=False)
        if column == None:
            address = "select * from " + self.library
        elif type(column) == list:
            if [i for i in column if type(i) != str]:
                raise ValueError
            address = 'select '
            for i in column:
                address += i
                address += ','
            address = address[:-1]+' from '+self.library
        if rule_where!=None:
            address += ' where '+ rule_where
        return pd.read_sql(address,con= self.conn_sql(),coerce_float=False)   
    
 
def change_to_float(data,change,dropna=False):
    data.loc[:,(change)] = data[change].str.extract(r'(\d+\.{,1}\d*)',expand=False)
    if dropna:
        data = data.dropna(subset=[change])
    data.loc[:,(change)] = data[change].astype('float')
    data = data.fillna(value=0)
    return data

def change_to_int(data,change,dropna = False):
    data.loc[:,(change)] = data[change].str.extract(r'([\d]+)',expand=False)
    if dropna == True:
        data = data.dropna(subset=[change])
    data.loc[:,(change)] = data[change].astype('float')
    data = data.fillna(value=0)
    return data
   
def change_data_type(data,col,typec):
    def change_type(term,col_t,t_type):
        try:
            term[col_t]= term[col_t].astype(t_type)
        except:
            if t_type=='int':
                term = change_to_int(term,col_t)
            elif t_type=='float':
                term = change_to_float(term,col_t)
        return term
    if type(col) == str:
        data = change_type(data,col,typec)
    elif type(typec) == str:
        try:
            data.loc[:,(col)] = data[col].astype(typec)
        except:
            for i in col:
                data = change_type(data,i,typec)
    else:
        for i,j in zip(col,typec):
            data = change_type(data,i,j)
    return data
    
def district_data(data,group=None,by='sid',name='注册店铺数'):
    #计算店铺数量
    data = data.drop_duplicates(by)
    if name:
        data = data.rename(columns={by:name})
    else: name = by
    if group == 'all':
        a = data[['province',name]].groupby('province').count()
        b = data[['province','city',name]].groupby(['province','city']).count()
        c = data[['province','city','county',name]].groupby(['province','city','county']).count()
        return a,b,c
    elif group == 'province':
        return data[['province',name]].groupby('province').count()
    elif group == 'city':
        return data[['province','city',name]].groupby(['province','city']).count()
    elif group == 'county':
        return data[['province','city','county',name]].groupby(['province','city','county']).count()
    elif group==None:
        print('please enter a district')

def sales_data(data,group=None,by='sid',name=False):
    #计算销量
#    data = data.drop_duplicates(by)
    if name:
        data = data.rename(columns={by:name})
    else: name = by
    if group == 'all':
        a = data[['province',name]].groupby('province').sum()
        b = data[['province','city',name]].groupby(['province','city']).sum()
        c = data[['province','city','county',name]].groupby(['province','city','county']).sum()
        return a,b,c
    elif group == 'province':
        return data[['province',name]].groupby('province').sum()
    elif group == 'city':
        return data[['province','city',name]].groupby(['province','city']).sum()
    elif group == 'county':
        return data[['province','city','county',name]].groupby(['province','city','county']).sum()
    elif group==None:
        print('please enter a district')
