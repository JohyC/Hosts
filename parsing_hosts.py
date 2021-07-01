#!/usr/bin/env python
# coding:utf-8
#   
#   Author  :   Johy
#   E-mail  :   c13340908272@outlook.com
#   Date    :   2021-06-05
#   Desc    :   从域名列解析出对应ip地址；

import socket
import argparse
import sys

from datetime import datetime, timedelta, timezone
from rich.console import Console

console = Console()

parser = argparse.ArgumentParser(description='Parse the github domain to get ip, or parse given domain.')
parser.add_argument('-d','--domains',nargs='*',help = 'input one domain to be parse')
parser.add_argument('-a','--add',nargs='*',help = 'add domain to be parse list')
parser.add_argument('-f','--file',nargs='?',type=argparse.FileType('r'),help='give me a file here!')
parser.add_argument('-o','--output',nargs=1,type=str,help='output name')
args = parser.parse_args()

domains = [
    'github.com',
    'github.blog',
    'githubapp.com',
    'api.github.com',
    'raw.github.com',
    'gist.github.com',
    'octocaptcha.com',
    'help.github.com',
    'live.github.com',
    'github.community',
    'githubstatus.com',
    'pages.github.com',
    'status.github.com',
    'uploads.github.com',
    'nodeload.github.com',
    'training.github.com',
    'codeload.github.com',
    'assets-cdn.github.com',
    'github.githubassets.com',
    'documentcloud.github.com',
    'raw.githubusercontent.com',
    'gist.githubusercontent.com',
    'camo.githubusercontent.com',
    'cloud.githubusercontent.com',
    'media.githubusercontent.com',
    'github-com.s3.amazonaws.com',
    'github.global.ssl.fastly.net',
    'desktop.githubusercontent.com',
    'github-cloud.s3.amazonaws.com',
    'avatars.githubusercontent.com',
    'favicons.githubusercontent.com',
    'avatars0.githubusercontent.com',
    'avatars1.githubusercontent.com',
    'avatars2.githubusercontent.com',
    'avatars3.githubusercontent.com',
    'avatars4.githubusercontent.com',
    'avatars5.githubusercontent.com',
    'avatars6.githubusercontent.com',
    'avatars7.githubusercontent.com',
    'avatars8.githubusercontent.com',
    'customer-stories-feed.github.com',
    'user-images.githubusercontent.com',
    'repository-images.githubusercontent.com',
    'marketplace-screenshots.githubusercontent.com',
    'github-production-user-asset-6210df.s3.amazonaws.com',
    'github-production-release-asset-2e65be.s3.amazonaws.com',
    'github-production-repository-file-5c1aeb.s3.amazonaws.com',
    'hcaptcha.com',
    'newassets.hcaptcha.com',
    'imgs.hcaptcha.com',
]
name = "hosts.txt"

if args.output:
  name = args.output[0]

if args.domains:
  domains = args.domains
elif args.add:
  for list in args.add:
    console.print(list)
    domains.append(list)
elif args.file:
  domains = args.file
        
def get_ip_list(domain): # 获取域名解析出的IP列表
  ip_list = []
  try:
    addrs = socket.getaddrinfo(domain, None)
    for item in addrs:
      if item[4][0] not in ip_list:
        ip_list.append(item[4][0])
  except Exception:
    ip_list.append('No resolution for '+domain)
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
            f.write('%s %s\n'%(ip, domain.strip()))
        f.write('\n# Last update at %s (Beijing Time)'%(get_time()))
        f.write('\n# Star me GitHub url: https://github.com/JohyC/GithubHosts')
        f.write('\n# Hosts End \n\n')
if __name__ == '__main__':
    output_hosts()
