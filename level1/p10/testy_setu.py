from level1.p10.zadanko import NetworkRouteMonitor

monitor = NetworkRouteMonitor()
monitor.use_target('1.1.1.1')
monitor.use_target('91.200.38.109')
monitor.use_target('google.pl')
print(monitor.net)
for (k,v) in monitor.net.items():
    print(f'{k} --> {v}')