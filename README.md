# Infrahub
The project is designed to help developers install essential software.

## How to use ansible
~~~bash
# 安装
bash ansible/install_ansible.sh

# 激活ansible环境
source ansible-env/bin/activate

# 退出ansible环境
deactivate

# 常用命令
ansible all --list-hosts
ansible all -m ping
ansible-playbook playbook.yml

# 使用文件寻找服务器安装
ansible-playbook playbooks/vim.yml --ask-become-pass

# 动态获取服务器安装
ansible-playbook -i inventory/dynamic.py dev playbooks/site.yml
~~~
