import subprocess

output = subprocess.check_output('ping -n 10 1.1.1.1', shell=True).decode('UTF-8')
print(output)
lines = output.splitlines()
print(lines)
#easy way
average_easy_way = (lines[16])[36:]
print(average_easy_way)
#prefered way
otp = []
for i in range(2,12):
    otp.append(lines[i][34:-9])
print(otp)
avg = 0
iteration = 0
for i in otp:
    try:
        temp = int(i)
        avg += temp
        iteration += 1
    except:
        continue
print(f'{avg/iteration} ms')


"""
[1'',
 2'Pinging 1.1.1.1 with 32 bytes of data:',
 3'Request timed out.',
 4'Reply from 1.1.1.1: bytes=32 time=29ms TTL=57',
 5'Reply from 1.1.1.1: bytes=32 time=28ms TTL=57',
 6'Reply from 1.1.1.1: bytes=32 time=29ms TTL=57',
 7'Reply from 1.1.1.1: bytes=32 time=27ms TTL=57',
 8'Reply from 1.1.1.1: bytes=32 time=30ms TTL=57', 
 9'Reply from 1.1.1.1: bytes=32 time=29ms TTL=57',
 10'Reply from 1.1.1.1: bytes=32 time=28ms TTL=57',
 11'Reply from 1.1.1.1: bytes=32 time=30ms TTL=57', 
 12'Reply from 1.1.1.1: bytes=32 time=29ms TTL=57',
 13'',
 14'Ping statistics for 1.1.1.1:',
 15'    Packets: Sent = 10, Received = 9, Lost = 1 (10% loss),',
 16'Approximate round trip times in milli-seconds:',
 17'    Minimum = 27ms, Maximum = 30ms, Average = 28ms']
"""

