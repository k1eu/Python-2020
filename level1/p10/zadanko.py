import subprocess

from typing import List, Dict, Set

from level1.p10.line_spliter import TracerouteNode, parse_traceroute_line_windows
from igraph import Graph, plot

"""
Zadanie: zrobić strukturę (klasę) która będzie trzymała informację o grafie sieci internet, 
i miała metody update'owania tej informacji wg. wyników działania komendy traceroute. 

Powinna istnieć też metoda exportowania grafu w postacji png'ka. 
"""


class NetworkRouteMonitor:
    net: Dict[str, Set] = {}

    def insert_edge(self, ip_from: str, ip_to: str):
        if ip_from not in self.net:
            self.net[ip_from] = set()
        self.net[ip_from].add(ip_to)

    def insert_route(self, nodes: List[TracerouteNode]):
        # przejść przez listę i pododawać linki
        n = len(nodes)
        for i in range(1, n):
            if nodes[i].hidden != True and nodes[i-1].hidden != True:
                self.insert_edge(nodes[i - 1].ip, nodes[i].ip)
            elif nodes[i].hidden == True or nodes[i-1].hidden == True:
                continue

    def use_target(self, ip):
        output = subprocess.check_output(f'tracert {ip}', shell=True).decode('UTF-8')
        lines = output.splitlines()[4:-2]
        print(lines)
        nodes = []
        for line in lines:
            nodes.append(parse_traceroute_line_windows(line))
        self.insert_route(nodes)
        print(nodes)



monitor = NetworkRouteMonitor()
monitor.use_target('1.1.1.1')
monitor.use_target('91.200.38.109')
monitor.use_target('google.pl')
print(monitor.net)
for (k,v) in monitor.net.items():
    print(f'{k} --> {v}')

