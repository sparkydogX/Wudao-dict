#!/bin/bash

wd -k
# 删除系统命令wd
sudo rm -f /usr/local/bin/wd

# 删除自动补全
sudo rm -f /usr/local/etc/bash_completion.d/wd

echo 'Uninstall Finished! '

