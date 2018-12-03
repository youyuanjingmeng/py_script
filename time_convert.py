# -*- coding: UTF-8 -*-
import time
import sys

# 时间戳转换为时间
def timestamp_to_time(timestamp):
    # 从命令行传入的参数为 str 类型
    try:
        if(len(timestamp) == 13):
            timestamp = float(timestamp) / 1000
        time_local = time.localtime(float(timestamp))
        str_time = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
        return str_time
    except ValueError as e:
        return e.message

# 时间转换为时间戳
def time_to_timestamp(str_time, str_time_ex):
    str_time += " " + str_time_ex
    try:
        time_struct = time.strptime(str_time, "%Y-%m-%d %H:%M:%S")
        timestamp = int(time.mktime(time_struct))
        return timestamp
    except ValueError as e:
        return e.message

def show_usage():
    print "***************************************************************"
    print "***usage:python file_name oper timestamp(or str_time)**********"
    print "***oper:0 means timestamp_to_time;1 means time_to_timestamp****"
    print "***Example:python time_convert.py 0 1543851536*****************"
    print "***Example:python time_convert.py 1 2018-12-03 11:10:21********"
    print "***************************************************************"
def main():
    if (sys.argv[1] == "0"):
        if (len(sys.argv) != 3):
            print "Error Input"
            show_usage()
            return
        print (timestamp_to_time(sys.argv[2]))
    elif (sys.argv[1] == "1"):
        if (len(sys.argv) != 4):
            show_usage()
            return
        print time_to_timestamp(sys.argv[2], sys.argv[3])
    else:
        print "Error Param"
        show_usage()

if __name__ == '__main__':
    main()
