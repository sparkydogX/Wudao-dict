# 无道词典(查询+朗读+默写+云同步)

![py](https://img.shields.io/badge/python-3.4.5-green.svg?style=plastic)![plat](https://img.shields.io/badge/platform-Ubuntu/CentOS/Debian/macOS-green.svg?style=plastic)

---
Forked from https://github.com/ChestnutHeng/Wudao-dict  
无道词典，是一个简洁优雅的有道词典命令行版本。支持英汉互查的功能，包含释义、词组、例句等有助于学习的内容。

无道词典致力于做最好的命令行词典，随着我们优化排版、显示，增加生词本和补全功能，提供了良好的用户体验，并在不断改进中。  
本Repo添加了一些新的功能。  
英汉：

![En_Zh Demo](http://obbgthtoc.bkt.clouddn.com/gitScreenshot%20from%202016-09-22%2010-55-23.png)

汉英:

![Zh_En Demo](http://obbgthtoc.bkt.clouddn.com/Screenshot%20from%202016-09-22%2011-04-50.png)

## 功能特性

1. 基础词典(20w英汉查询 + 10w汉英查询 + 网络词库)
2. 词组查询功能(例如直接输入`wd in order to`)
3. 自动补全功能(按Tab自动补全单词，包含1w个最热的词)
4. 生词本(自动把历史记录存为生词本，`wd -h`查看生词本文件位置)
5. 默写单词的功能
6. 朗读单词的功能
7. 通过百度网盘在云端同步生词本

## 安装说明

遇到任何问题，或者有任何改善建议请联系作者。
注意，你现在看到的代码是从 https://github.com/ChestnutHeng/Wudao-dict fork过来的。  
如果对于原始的代码有任何疑问，请联系原作者或者到原始的repo<a href="https://github.com/ChestnutHeng/Wudao-dict/issues/new">创建新的 issue</a>进行提问

### 关于这个repo新增功能的问题
邮箱: csyguo@njust.edu.cn  
issue:[在本repo创建新的issue](https://github.com/sparkydogX/Wudao-dict/issues)
### 其他问题
邮箱: chestnutheng@hotmail.com

issue: <a href="https://github.com/ChestnutHeng/Wudao-dict/issues/new">创建新的 issue</a>

### Linux/macOS 环境 

1. 安装环境: 需要python3和bs4, lxml(在线搜索用)
    #### Debian/Ubuntu
    ```
    sudo apt-get install python3
    sudo apt-get install python3-pip
    sudo pip3 install bs4
    sudo pip3 install lxml
    ```
 
    #### OpenSUSE
    ```
    sudo zypper install python3-pip
    sudo pip3 install bs4
    sudo pip3 install lxml
    ```
    #### CentOS
    ```
    sudo yum install python34
    sudo yum install python34-pip
    sudo pip3 install bs4
    sudo pip3 install lxml
    ```
    #### macOS
    需要安装有`brew`和`python3`
    ```
    sudo pip3 install bs4
    sudo pip3 install lxml
    ```

2.  运行
    ```sh
    git clone https://github.com/sparkydogX/Wudao-dict.git
    cd ./wudao-dict/wudao-dict
    sudo bash setup.sh #或者sudo ./setup.sh
    ```

    看到出现`Setup Finished!`表明安装成功。如果发生由于移动安装文件不能使用的情况，只需再次运行该脚本即可。

无法clone的，可以在[项目页面](https://github.com/sparkydogX/Wudao-dict/tree/master)下载zip文件 ,然后解压安装使用。

**Note: 注意python的版本，只支持python3**

3.  添加发音功能(可选)

    安装ffplay
    #### Linux
    需要使用到wget和ffmpeg中的ffplay
    `sudo apt-get install wget ffmpeg`
    #### macOS
    通过brew安装ffplay。这里有个trick。
    ```
    brew install wget
    brew install sdl --use-gcc
    brew uninstall ffmpeg
    brew install ffmpeg --use-gcc
    ```
    
4. 云端同步生词本
    
    需要在python3下安装[bypy](https://github.com/houtianze/bypy)
    第一次运行时需要授权，只需跑任何一个命令（比如 bypy info）然后跟着说明（登陆等）来授权即可。授权只需一次，一旦成功，以后不会再出现授权提示.
    但是由于百度方面的限制,授权有时候会失效,需要使用`bypy refresh`来重新授权.


 
## 使用说明

运行`wd -h`查看使用说明。


```
$ wd -h
Usage: wd [OPTION]... [WORD]
Youdao is wudao, a powerful dict.
-k, --kill             kill the server process    (退出服务进程)
-h, --help             display this help and exit (查看帮助)
-s, --short-desc       do not show sentence       (只看释义)
-n, --not-save         query and save to notebook (不存入生词本)
-d, --dictation        spell words in notebook (默写生词本中的单词)
-su, --sync-up         Sync up to baidu pan(同步上传到百度网盘)
-sd, --sync-down       Sync down to baidu pan(从百度网盘下载同步)
生词本文件: ... some path .../notebook.txt
查询次数: ... some path .../usr_word.json
```

查词时可以直接使用`wd 词语`查汉英词典，或`wd word`查英汉词典(可以自动检测)。


## 小贴士

0. ./wd_monofile 是本词典的在线查询的单文件版本, 可以复制到`/usr/bin`下直接使用.(需要安装bs4)
1. 如果您不想看到例句, 请在`/usr/bin/wd`中的`./wdd`后面加上-s参数.
2. 有的用户反馈字体颜色看不清的问题, 你可以找到./wudao-dict/wudao-dict/src/CommandDraw.py, 可以看到释义,读音等采用的颜色, 直接修改即可.
3. 查询词组直接键入类似`wd take off`即可.

## Release Notes

#### Ver 1.0 (Oct 10, 2016)

* 提供了基础的英汉互查的功能
* 提供了在线查询的功能，并且查过后会缓存

#### Ver 1.1 (Dec 1, 2016)

* 提供了可以单独运行的单文件版本

#### Ver 1.2 (Nov 22, 2017)

* 在线查询修复了不显示被查词的bug

#### Ver 2.0 

* 修复了文件夹过大的问题，由263M缩小到80M左右。<a href="https://github.com/ChestnutHeng/Wudao-dict/issues/1"> issue #1: 文件夹大小</a>
* 添加了更多的常用词和单复数形式
* 取消了网络搜索功能，没有在本地找到时会自动进行网络搜索
* 添加了tab补全的支持，对常用的1w词进行tab补全 <a href="https://github.com/ChestnutHeng/Wudao-dict/issues/15">issue #15: 模糊查询的支持</a>
* 添加了生词本功能，自动把查过的词和释义添加到生词本文件中
* 优化了排版，同一单词不再截断换行了 #该功能因为转移字符的问题搁置 <a href="https://github.com/ChestnutHeng/Wudao-dict/issues/16">issue #16:避免在单词内换行</a>

#### Ver 2.1

* 增加了默写的功能，并且能够显示错误次数。  
* 更新了ReadMe文件

#### Ver 2.1.1

* 修改命令行用以在Mac上运行  
* 按照 https://github.com/ChestnutHeng/Wudao-dict/issues/23#issuecomment-368378350 提供的方法增加发音的功能
* 存在的问题：存储的音频文件不会被自动删除，大量使用时需要定期手动清理  

#### Ver2.2 

* BugFix:修正了无法正确朗读词组的问题
* 流畅性改进:更换词典的音频来源,提高了获取音频文件的速度. 

#### Ver2.3

* New Feature:增加云端同步生词本的功能.
