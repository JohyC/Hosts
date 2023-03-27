#!/usr/bin/env python
# coding:utf-8
#   
#   Author  :   Johy
#   E-mail  :   c13340908272@outlook.com
#   Date    :   2021-06-05
#   Desc    :   parsing_hosts.py;从域名列解析出对应ip地址；

import socket
import argparse
import sys

from datetime import datetime, timedelta, timezone
from rich.console import Console

console = Console()

parser = argparse.ArgumentParser(description='Parse the github domain to get ip, or parse given domain.')
parser.add_argument('-d','--domains',nargs='*',help = 'input domain to be parse')
parser.add_argument('-f','--file',nargs='*',type=argparse.FileType('r'),help='give me a file here!')
parser.add_argument('-o','--output',nargs=1,type=str,help='output name')
args = parser.parse_args()

domains = []
name = "hosts.txt"

if args.output:
  name = args.output[0]

if args.domains:
  for domain in args.domains:
    domains.append(domain)
elif args.file:
  for f in args.file:
    domains.extend(f.readlines())
        
def get_ip_list(domain): # 获取域名解析出的IP列表
  ip_list = []
  try:
    addrs = socket.getaddrinfo(domain, None)
    for item in addrs:
      if item[4][0] not in ip_list:
        ip_list.append(item[4][0])
  except Exception:
    ip_list.append('# No resolution for '+domain)
    pass
  return ip_list

def gen_host():
    for domain in domains:
        console.print('Querying ip for domain ',style="#66CCFF",end="")
        console.print(domain,style="#ff6800")
        list = get_ip_list(domain.strip())
        for ip in list:
            yield (ip, domain)
        

def get_time(format_string="%Y-%m-%d %H:%M:%S"):#"%Y-%m-%d %H:%M:%S"
    utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
    bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
    str_date = bj_dt.strftime(format_string)
    return str_date

def output_hosts():
    with open(name, 'w') as f:
        f.write('# Hosts Start \n')
        for ip, domain in gen_host():
            console.print('ip %s'%ip)
            f.write('%s %s\n'%(ip.ljust(30), domain.strip()))
        f.write('\n# Last update at %s (Beijing Time)'%(get_time()))
        f.write('\n# Star me GitHub url: https://github.com/JohyC/Hosts')
        f.write('\n# Hosts End \n\n')
if __name__ == '__main__':
    output_hosts()
