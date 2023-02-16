from tools.tools_s.sql_base import get_data
from collections import defaultdict

sql_prame = {
    "host": "192.168.0.227",
    "db": "ec_cross_border",
    "user": "read",
    "password": "nriat227read@x#",
    "port":9227
}
sql = "select id,pid,NodeId from sorftime_sort_202007"
data = get_data(sql_prame,sql)

pid_dict = {i[0]:i[1] for i in data}

def get_root(id):
    pid = pid_dict.get(id)
    if pid == "0":
        return id
    elif int(pid) < 26:
        return pid
    else:
        pid = get_root(pid)
    return pid

root_dict = defaultdict(list)
# with open("sorftime_nodeid_root.txt","w",encoding="utf-8") as f:
for i in data:
    root_id = get_root(i[0])
    root_dict[root_id].append(i[2])
for i,y in root_dict.items():
    sql = '''select sum(CommentCount),sum(SaleCount) from sorftime_goodsinfo_202007
where NodeId in ("{}")'''.format('","'.join(y))
    data = get_data(sql_prame, sql)
    print(i,data[0][0],data[0][1])
#     print(i,len(y))

    # f.write("{},{}\n".format(i[2],root_id))