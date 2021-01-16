from dataclasses import dataclass
import unittest

#TODO RTTIME NAPRAWIC | HIDDEN DODAC

@dataclass
class TracerouteNode:
    ip: str
    hostname: str
    rt_time: int
    hidden: bool = False

line2 = '  1    <1 ms    <1 ms    <1 ms  192.168.3.1 '


def parse_traceroute_line_windows(line: str):
    ip = ''
    hostname = 'not specified'
    rt_time = 1
    print(line)
    if not line.__contains__('*'):
        x = line.split(' ')
        print(f'x to :{x}')
        if x[-2].__contains__('[') and x[-2].__contains__(']'):
            ip = x[-2][1:-1]
            hostname = x[-3]
            print(f'ip i hostname{ip}\n{hostname}')
        else:
            ip = x[-2]
            print(f'ip i hostname{ip}')
        if not x[6].__contains__('<'):
            try:
                avg = int(x[6]) + int(x[12]) + int(x[18])
                rt_time = avg
            except:
                rt_time = 666
        else:
            try:
                p = x[6].replace('<',"")
                print(f'zmiana p  {p}')
                avg = int(x[6].replace('<',''))
                rt_time = avg
            except:
                rt_time = 666
    else:
        print('HIDDEEEN')
        return TracerouteNode(ip,hostname,rt_time,True)
    print(ip,hostname,rt_time,)
    return TracerouteNode(ip,hostname,rt_time)
