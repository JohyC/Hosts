# Hosts

## 项目介绍
1. 目标：

   - 解决vpn失效时，无法访问GitHub的问题。
   - 添加 epic无法登录和领取免费游戏 hosts。
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

### 本仓库 hosts文件介绍

1. hosts.txt 文件包含 GitHub hosts，Epic hosts；
2. Github 和 Epic 分别有单独 hosts文件；

### hosts本仓库在线同步地址

1. Github https://github.com/JohyC/Hosts/blob/main/hosts.txt
2. Gitee https://gitee.com/yuchi-shentang/GithubHosts/blob/main/hosts.txt
3. 私人服务器 https://www.suni.cf:8880/hosts.txt

### 修改方法

- 使用 [SwitchHosts](https://github.com/oldj/SwitchHosts) 工具（推荐）
- 手动修改 hosts 文件；
  - Windows 打开 C:\Windows\System32\drivers\etc 文件夹；
    - 右键 hosts 文件，打开方式中选择记事本或其他文本工具，复制仓库中的hosts文件内容至最后；
  - Linux 请自行谷歌.......

修改hosts文件完成后 win10 请使用 ipconfig /flushdns 刷新dns缓存；

## TODO

- [x] GitHub Actions自动更新hosts内容；
- [x] GitHub Actions自动更新本仓库代码至[Gitee](https://gitee.com/yuchi-shentang/GithubHosts)；(可从Gitee获取最新hosts文件)
- [x] Github actions自动同步hosts文件至私人服务器地址；[hosts](https://www.suni.cf:8880/hosts.txt)；(解决Gitee hosts.txt文件违规问题)
