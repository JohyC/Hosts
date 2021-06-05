# GithubHosts

## 介绍
1. Python脚本默认解析GitHub domain获取ip，生成hosts。
2. 接收参数解析自定义域名。

## 脚本使用
1. python引入rich库，使用脚本前需 pip install rich；
2. python parsing_hosts.py -a domain domain ...
   -a命令，在默认domain列表后加入需要解析的域名；
3. python parsing_hosts.py -d domain domain ...
   -d命令，使用自定义域名替换默认解析列表；
4. 脚本将在当前文件夹生成hosts.txt文件；

## hosts

- 推荐 [SwitchHosts](https://github.com/oldj/SwitchHosts) 工具；

- 修改hosts文件完成后 win10 请使用 ipconfig /flushdns 刷新dns缓存；
