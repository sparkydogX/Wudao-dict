#!/bin/bash

# 用户词
if [ ! -d usr ]
then
    mkdir usr
fi

chmod -R 777 usr

# 添加系统命令wd
echo '#!/bin/bash'>./wd
echo 'save_path=$PWD'>>./wd
echo 'cd '$PWD >>./wd
echo './wdd $*'>>./wd
echo 'cd $save_path'>>./wd
sudo cp ./wd /usr/local/bin/wd
sudo chmod +x /usr/local/bin/wd

# 添加自动补全
sudo rm -f /usr/local/etc/bash_completion.d/wd
sudo cp wd_com /usr/local/etc/bash_completion.d/wd
. /usr/local/etc/bash_completion.d/wd

echo 'Setup Finished! '
echo 'use wd [OPTION]... [WORD] to query the word.'
echo '自动补全会在下次打开命令行时启用'
echo '或者手动运行 source ~/.bashrc'

