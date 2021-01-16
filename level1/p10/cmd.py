import subprocess

output = subprocess.check_output('tracert 1.1.1.1', shell=True).decode('UTF-8')

for i in output.splitlines():
    print(i)