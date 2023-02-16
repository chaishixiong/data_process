import os
from collections import defaultdict
from pathlib import Path

path = "/home/gmsz/data/mysql"
backup_path = "/home/gmsz/backup_hz/online_loads"


def reccover_file(db_name=None):
    db_dict = defaultdict(list)
    files = os.listdir(backup_path)
    files.sort(key=lambda x: int(x[-13:-3]))
    for file_name in files:
        if ".7z" in file_name and file_name.count("#spilit#") == 2:
            data = file_name.replace(".7z","").split("#spilit#")
            if db_name:
                db_dict[db_name].append((data[1],data[2]))
            else:
                db_dict[data[0]].append((file_name,(data[1],data[2])))
    return db_dict


def zip7(db_name,file_name):#压缩
    os.chdir(backup_path)
    try:
        print("正在解压", file_name)
        cmd = "7z x {} -aoa -o{}/{}".format(file_name,path,db_name)
        a = os.popen(cmd)
        console_str = a.read()
        if "Ok" in console_str:
            print("ok")
            return 1
        else:
            return 0
    except Exception as e:
        return 0


def run():
    for db_name,y in reccover_file().items():
        #files = os.listdir(Path(path)/db_name)
        #tables = {str(i).replace(".MYD","") for i in files if ".MYD" in i}
        for file,info in y:
            #if info[0] not in tables:
            result = zip7(db_name,file)
            print(result)
            if result == 1:
                backfile_name = Path(backup_path)/file
                os.remove(backfile_name)
            #else:
            #    print("{}更新".format(file))
        os.popen("chown mysql:mysql {}/{}/*".format(path,db_name))

if __name__=="__main__":
    run()