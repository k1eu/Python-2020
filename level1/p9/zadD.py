from dataclasses import dataclass
import subprocess
@dataclass
class TracerouteNode:
    ip: str
    hostname: str
    rt_time: int
    hidden: bool = False

    def __repr__(self):
        return f'{self.hostname}\n{self.ip}\nRT Time: {self.rt_time} ms'



ip_adress = '1.1.1.1'
output = subprocess.check_output(f'tracert {ip_adress}', shell=True).decode('UTF-8')
print(output)
lines = output.splitlines()
print(lines)
otp = []
for i in range(4,30):
    temp = lines[i]

    if temp[-2] != ']' and temp[8] != '*':
        print(f'---ip bez nazw i gwizdki---\n{temp}')
        print(temp[17])
        rt_time = 0
        if temp[16] != '<':
            rt_time = temp[16:19]
        else:
            rt_time = temp[17:19]
        node = TracerouteNode(temp[32:-1], 'not specified', int(rt_time))
        otp.append(node)

    elif temp[-2] == ']' and temp[8] != '*':
        print(f'---same nazwy---\n{temp}')
        rt_time = 0
        if temp[16] != '<':
            rt_time = temp[16:19]
        else:
            rt_time = temp[17:19]
        indx = temp.find('[', 32)
        hostname = temp[32:indx]
        node = TracerouteNode(temp[indx + 1:-2], hostname, int(rt_time))
        otp.append(node)

    if temp.__contains__(ip_adress):
        break

for i in otp:
    print(i)
"""8 znak
[0'',
 1'Tracing route to one.one.one.one [1.1.1.1]',
 2 'over a maximum of 30 hops:',
 3  '',
 4   '  1    <1 ms    <1 ms    <1 ms  192.168.3.1 ',
 5    '  2    <1 ms     1 ms    <1 ms  192.168.233.1 ',
 6     '  3     4 ms     2 ms     5 ms  10.30.32.1 ',
 7      '  4     2 ms     1 ms     2 ms  10.8.2.1 ',
 8      '  5     2 ms     2 ms     1 ms  ip-194-33-77-221.static.speed-net.com.pl [194.33.77.221] ',
 9        '  6     5 ms     4 ms     5 ms  91.198.97.146 ',
 10         '  7    29 ms    25 ms    24 ms  et-0-0-59-701.edge1.Budapest1.Level3.net [212.187.202.117] ',
 11          '  8     *        *        *     Request timed out.',
 12           '  9    28 ms    28 ms    27 ms  195.122.183.210 ',
 13            ' 10    27 ms    27 ms    27 ms  one.one.one.one [1.1.1.1] ',
 14             '',
 15              'Trace complete.']

"""