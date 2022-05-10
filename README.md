# Hosts

## 提示

由于最近steam被工信部拉黑了。直接改Hosts文件可能作用不大；需要配合一下措施！

1. 在steam启动快捷方式上右键打开属性；
2. 在属性 --> 快捷方式 --> 目标 尾部加上参数 ' -tcp' or '-websocket';(参数前必须预留一个空格) 一下图为例:

![image](https://user-images.githubusercontent.com/38210128/165656916-1866dd64-a836-48f1-a95a-80dd9f49cb25.png)


## 项目介绍

1. 目标：

   - 添加 epic无法登录和领取免费游戏 hosts。
   - 第一次写python，练手学习.....

## 脚本介绍

### python依赖

python引入rich库，使用脚本前需 pip install -r requirements；

### 命令介绍

cd 至 workingDir 文件夹后 执行以下操作；

1. python ph.py -a domain domain ...
   -a命令，在默认domain列表后加入需要解析的域名；
2. python ph.py -d domain domain ...
   -d命令，使用自定义域名替换默认解析列表；
3. python ph.py -f file
   -f 命令，接收文本文件。
   解析文本文件中的域名;

以上命令将在当前文件夹中生成hosts.txt文件。
使用 -o 命令自定义输出文件名；（-o outputFile）

## hosts

### 本仓库 hosts文件介绍

1. hosts.txt 文件包含 GitHub hosts，Epic hosts；
2. Github 和 Epic 分别有单独 hosts文件；

### hosts本仓库在线同步地址

1. Github   https://github.com/JohyC/Hosts/blob/main/hosts.txt

2. Gitee    https://gitee.com/yuchi-shentang/GithubHosts/blob/main/hosts.txt

3. Gitea    https://www.foul.trade:3000/Johy/Hosts/raw/branch/main/hosts.txt

4. ~~服务器~~  由于安全问题，不再提供服务链接，请使用gitea链接同步；
   
### 仓库同步地址
1. gitea https://www.foul.trade:3000/Johy/Hosts
2. gitee https://gitee.com/yuchi-shentang/GithubHosts

## 使用方式

### 通过 SwitchHosts! 自动更新 `推荐`

推荐使用  [SwitchHosts](https://swh.app/zh/) 配置`hosts`，操作简单，支持跨平台。

详细介绍 :   [SwitchHosts! 还能这样管理hosts，后悔没早点用](https://mp.weixin.qq.com/s/A37XnD3HdcGSWUflj6JujQ) 。

1. 打开  SwitchHosts ，点击左上角加号 添加hosts同步规则。
2. 规则配置：
   - 方案名：Johy/hosts (自行命名)
   - 类型：远程
   - URL 地址：https://www.foul.trade:3000/Johy/Hosts/raw/branch/main/hosts.txt (url: 推荐地址，国内同步更稳定)
   - 自动更新：24小时 （hosts地址变更不会特别频繁）

![image](https://user-images.githubusercontent.com/38210128/127502984-7ef25b7c-1901-4164-ab29-e5dbc487e63d.png)


### 手动配置hosts

#### macOS

`hosts`文件位置：`/etc/hosts`。

`macOS`系统下修改需要按照如下方式：

1. ##### 打开（访达）Finder。

2. ##### 组合键`Shift+Command+G`打开"前往文件夹"。

3. ##### 输入框中输入`/etc/hosts`;跳转到`hosts`文件位置。

> 注意：`VS Code`可以直接修改和保存，不需要以下步骤。

4. 复制`hosts`文件到桌面，右键点击文件，「打开方式」—「文本编辑」，复制本仓库提供的hosts文件内容至最下方。

5. 使用修改之后的`hosts`文件替换掉原本`/etc/hosts` 文件。

> 注意：如果弹出密码输入框，你需要输入你当前登录账号对应的密码。

6. 最后刷新缓存：

```
sudo killall -HUP mDNSResponder
```

#### Windows

`hosts`文件位置：`C:/windows/system32/drivers/etc/hosts`。

将前文`hosts`内容追加到`hosts`文件，然后刷新`DNS`缓存：

```powershell
# win键 + r键；输入cmd，回车；在cmd命令行窗口中输入以下！
ipconfig /flushdns
```

## TODO

- [x] GitHub Actions自动更新hosts内容；
- [x] GitHub Actions自动更新本仓库代码至[Gitee](https://gitee.com/yuchi-shentang/GithubHosts)；(可从Gitee获取最新hosts文件)
- [x] 自建git服务器，并同步仓库内容;(解决Gitee hosts.txt文件违规问题)

