# GithubHosts

## 项目介绍
1. 目标：

   - 解决vpn失效时，无法访问GitHub的问题。
   - 第一次写python，练手学习.....

2. 原理：

   - python从域名解析出对应ip地址列；

   - 编辑hosts直接映射GitHub域名到ip，从中间环节杜绝dns污染；

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

## TODO

- [x] GitHub Actions自动更新hosts内容；
