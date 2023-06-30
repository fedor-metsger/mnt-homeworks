
# Ответы к домашнему заданию 1 «Введение в Ansible»

## Основная часть

### Задача 1:

---

Попробуйте запустить playbook на окружении из test.yml, зафиксируйте значение, которое имеет факт some_fact для указанного хоста при выполнении playbook.

Ответ: `12`
```
PLAY [Print os facts] ********************************************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************************
ok: [localhost]

TASK [Print OS] **************************************************************************************************************************************************************
ok: [localhost] => {
    "msg": "Linux Mint"
}

TASK [Print fact] ************************************************************************************************************************************************************
ok: [localhost] => {
    "msg": 12
}

PLAY RECAP *******************************************************************************************************************************************************************
localhost                  : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```
### Задача 2:

---

Найдите файл с переменными (group_vars), в котором задаётся найденное в первом пункте значение, и поменяйте его на all default fact.

Ответ:
```
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-01-base$ cat ./playbook/group_vars/all/examp.yml 
---
  some_fact: all default fact
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-01-base$ ansible-playbook -i ./playbook/inventory/test.yml ./playbook/site.yml

PLAY [Print os facts] ********************************************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************************
ok: [localhost]

TASK [Print OS] **************************************************************************************************************************************************************
ok: [localhost] => {
    "msg": "Linux Mint"
}

TASK [Print fact] ************************************************************************************************************************************************************
ok: [localhost] => {
    "msg": "all default fact"
}

PLAY RECAP *******************************************************************************************************************************************************************
localhost                  : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```
### Задача 3:

---
Воспользуйтесь подготовленным (используется docker) или создайте собственное окружение для проведения дальнейших испытаний.
Ответ:
```
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-01-base$ sudo ansible-playbook -i ./playbook/inventory/prod.yml ./playbook/site.yml

PLAY [Print os facts] ********************************************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************************
ok: [ubuntu]
ok: [centos7]

TASK [Print OS] **************************************************************************************************************************************************************
ok: [centos7] => {
    "msg": "CentOS"
}
ok: [ubuntu] => {
    "msg": "Ubuntu"
}

TASK [Print fact] ************************************************************************************************************************************************************
ok: [centos7] => {
    "msg": "el"
}
ok: [ubuntu] => {
    "msg": "deb"
}

PLAY RECAP *******************************************************************************************************************************************************************
centos7                    : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
ubuntu                     : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-01-base$
```
### Задача 4:

---
Проведите запуск playbook на окружении из prod.yml. Зафиксируйте полученные значения some_fact для каждого из managed host.

Ответ: `el`,`deb`
### Задача 5:

---
Добавьте факты в group_vars каждой из групп хостов так, чтобы для some_fact получились значения: для deb — deb default fact, для el — el default fact.
```
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-01-base$ cat ./playbook/group_vars/deb/examp.yml
---
  some_fact: "deb default fact"
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-01-base$ cat ./playbook/group_vars/el/examp.yml
---
  some_fact: "el default fact"
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-01-base$
```
### Задача 6:

---
Повторите запуск playbook на окружении prod.yml. Убедитесь, что выдаются корректные значения для всех хостов.
```
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-01-base$ sudo ansible-playbook -i ./playbook/inventory/prod.yml ./playbook/site.yml

PLAY [Print os facts] ********************************************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************************
ok: [ubuntu]
ok: [centos7]

TASK [Print OS] **************************************************************************************************************************************************************
ok: [centos7] => {
    "msg": "CentOS"
}
ok: [ubuntu] => {
    "msg": "Ubuntu"
}

TASK [Print fact] ************************************************************************************************************************************************************
ok: [centos7] => {
    "msg": "el default fact"
}
ok: [ubuntu] => {
    "msg": "deb default fact"
}

PLAY RECAP *******************************************************************************************************************************************************************
centos7                    : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
ubuntu                     : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-01-base$
```
### Задача 7:

---
При помощи ansible-vault зашифруйте факты в group_vars/deb и group_vars/el с паролем netology.
```
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-01-base$ ansible-vault encrypt ./playbook/group_vars/deb/examp.yml
New Vault password: 
Confirm New Vault password: 
Encryption successful
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-01-base$ ansible-vault encrypt ./playbook/group_vars/el/examp.yml 
New Vault password: 
Confirm New Vault password: 
Encryption successful
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-01-base$ cat ./playbook/group_vars/deb/examp.yml
$ANSIBLE_VAULT;1.1;AES256
37353964303563326335363337393438616234636466373364653362316630623431613532653339
3230346263623736393837306664323133613963323461660a636535386536303936396566336438
34303636623139396361646463613130313233336366646538633962363631346662376238326461
6463623761653563630a613935323135323130356264616632333536356235356432633537343838
63383632666235623433376335643233316637633238393639633264393034623032343834383866
3130336162323033313939313332366332663564346637393134
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-01-base$ cat ./playbook/group_vars/el/examp.yml
$ANSIBLE_VAULT;1.1;AES256
62323738373364623963356535373535393139613566316261306239653265363466633930613530
6462633930376364316330646566613838336665303865350a356461353465303063356432343863
32653838333539666532393964383636383064646133643261636433646131643232366438313531
6336313834646130350a653165353665356566393838656239313335376264306138366434396639
37613339393136326161656566363963346332393965303938353436323433643731363564363634
3634613162363466633662323561316163306431386634336236
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-01-base$
```
### Задача 8:

---
Запустите playbook на окружении prod.yml. При запуске ansible должен запросить у вас пароль. Убедитесь в работоспособности.
```
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-01-base$ sudo ansible-playbook --ask-vault-pass -i ./playbook/inventory/prod.yml ./playbook/site.yml
Vault password: 

PLAY [Print os facts] ********************************************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************************
ok: [ubuntu]
ok: [centos7]

TASK [Print OS] **************************************************************************************************************************************************************
ok: [centos7] => {
    "msg": "CentOS"
}
ok: [ubuntu] => {
    "msg": "Ubuntu"
}

TASK [Print fact] ************************************************************************************************************************************************************
ok: [centos7] => {
    "msg": "el default fact"
}
ok: [ubuntu] => {
    "msg": "deb default fact"
}

PLAY RECAP *******************************************************************************************************************************************************************
centos7                    : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
ubuntu                     : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-01-base$
```
### Задача 9:

---
Посмотрите при помощи ansible-doc список плагинов для подключения. Выберите подходящий для работы на control node.

Ответ: `ansible.builtin.local`
```
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-01-base$ ansible-doc -t connection -l
ansible.builtin.local          execute on controller                                                                                                                     
ansible.builtin.paramiko_ssh   Run tasks via python ssh (paramiko)                                                                                                       
ansible.builtin.psrp           Run tasks over Microsoft PowerShell Remoting Protocol                                                                                     
ansible.builtin.ssh            connect via SSH client binary                                                                                                             
ansible.builtin.winrm          Run tasks over Microsoft's WinRM                                                                                                          
ansible.netcommon.grpc         Provides a persistent connection using the gRPC protocol                                                                                  
ansible.netcommon.httpapi      Use httpapi to run command on network appliances                                                                                          
ansible.netcommon.libssh       Run tasks using libssh for ssh connection                                                                                                 
ansible.netcommon.netconf      Provides a persistent connection using the netconf protocol                                                                               
ansible.netcommon.network_cli  Use network_cli to run command on network appliances                                                                                      
ansible.netcommon.persistent   Use a persistent unix socket for connection                                                                                               
community.aws.aws_ssm          connect to EC2 instances via AWS Systems Manager                                                                                          
community.docker.docker        Run tasks in docker containers                                                                                                            
community.docker.docker_api    Run tasks in docker containers                                                                                                            
community.docker.nsenter       execute on host running controller container                                                                                              
community.general.chroot       Interact with local chroot                                                                                                                
community.general.funcd        Use funcd to connect to target                                                                                                            
community.general.iocage       Run tasks in iocage jails                                                                                                                 
community.general.jail         Run tasks in jails                                                                                                                        
community.general.lxc          Run tasks in lxc containers via lxc python library                                                                                        
community.general.lxd          Run tasks in lxc containers via lxc CLI                                                                                                   
community.general.qubes        Interact with an existing QubesOS AppVM                                                                                                   
community.general.saltstack    Allow ansible to piggyback on salt minions                                                                                                
community.general.zone         Run tasks in a zone instance                                                                                                              
community.libvirt.libvirt_lxc  Run tasks in lxc containers via libvirt                                                                                                   
community.libvirt.libvirt_qemu Run tasks on libvirt/qemu virtual machines                                                                                                
community.okd.oc               Execute tasks in pods running on OpenShift                                                                                                
community.vmware.vmware_tools  Execute tasks inside a VM via VMware Tools                                                                                                
containers.podman.buildah      Interact with an existing buildah container                                                                                               
containers.podman.podman       Interact with an existing podman container                                                                                                
kubernetes.core.kubectl        Execute tasks in pods running on Kubernetes                                                                                               
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-01-base$
```
### Задача 10:

---
В prod.yml добавьте новую группу хостов с именем local, в ней разместите localhost с необходимым типом подключения.
```
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-01-base$ cat ./playbook/inventory/prod.yml 
---
  el:
    hosts:
      centos7:
        ansible_connection: docker
  deb:
    hosts:
      ubuntu:
        ansible_connection: docker
  local:
    hosts:
      localhost:
        ansible_connection: local
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-01-base$
```

### Задача 11:

---
Запустите playbook на окружении prod.yml. При запуске ansible должен запросить у вас пароль. Убедитесь, что факты some_fact для каждого из хостов определены из верных group_vars.
```
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-01-base$ sudo ansible-playbook --ask-vault-pass -i ./playbook/inventory/prod.yml ./playbook/site.yml
Vault password: 

PLAY [Print os facts] ********************************************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************************
ok: [ubuntu]
ok: [localhost]
ok: [centos7]

TASK [Print OS] **************************************************************************************************************************************************************
ok: [centos7] => {
    "msg": "CentOS"
}
ok: [ubuntu] => {
    "msg": "Ubuntu"
}
ok: [localhost] => {
    "msg": "Linux Mint"
}

TASK [Print fact] ************************************************************************************************************************************************************
ok: [centos7] => {
    "msg": "el default fact"
}
ok: [ubuntu] => {
    "msg": "deb default fact"
}
ok: [localhost] => {
    "msg": "all default fact"
}

PLAY RECAP *******************************************************************************************************************************************************************
centos7                    : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
localhost                  : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
ubuntu                     : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-01-base$ cat ./playbook/inventory/prod.yml
```

### Задача 12:

---
Заполните README.md ответами на вопросы. Сделайте git push в ветку master. В ответе отправьте ссылку на ваш открытый репозиторий с изменённым playbook и заполненным README.md.


## Необязательная часть
### Задача 1:

---
При помощи ansible-vault расшифруйте все зашифрованные файлы с переменными.
```
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-01-base$ ansible-vault decrypt ./playbook/group_vars/deb/examp.yml
Vault password: 
Decryption successful
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-01-base$ ansible-vault decrypt ./playbook/group_vars/el/examp.yml
Vault password: 
Decryption successful
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-01-base$ cat ./playbook/group_vars/deb/examp.yml
---
  some_fact: "deb default fact"
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-01-base$ cat ./playbook/group_vars/el/examp.yml
---
  some_fact: "el default fact"
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-01-base$
```
### Задача 2:

---
Зашифруйте отдельное значение PaSSw0rd для переменной some_fact паролем netology. Добавьте полученное значение в group_vars/all/exmp.yml.
```
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-01-base$ cat ./playbook/group_vars/all/examp.yml 
---
  some_fact: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          39386337386431623430383137653365366466313166613530323336633862346139663465313661
          6134386336643439666636333561336435363266633533390a353266363539356332393432323630
          36313533306537643066386137323033373864333037366230333734646231613765613664353730
          6337333037383566620a323731373737336464363765623333383637356264373139373665363431
          3232
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-01-base$
```

### Задача 3:

---
Запустите playbook, убедитесь, что для нужных хостов применился новый fact.
```
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-01-base$ sudo ansible-playbook --ask-vault-pass -i ./playbook/inventory/prod.yml ./playbook/site.yml
Vault password: 

PLAY [Print os facts] ********************************************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************************
ok: [ubuntu]
ok: [localhost]
ok: [centos7]

TASK [Print OS] **************************************************************************************************************************************************************
ok: [centos7] => {
    "msg": "CentOS"
}
ok: [ubuntu] => {
    "msg": "Ubuntu"
}
ok: [localhost] => {
    "msg": "Linux Mint"
}

TASK [Print fact] ************************************************************************************************************************************************************
ok: [centos7] => {
    "msg": "el default fact"
}
ok: [ubuntu] => {
    "msg": "deb default fact"
}
ok: [localhost] => {
    "msg": "PaSSw0rd"
}

PLAY RECAP *******************************************************************************************************************************************************************
centos7                    : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
localhost                  : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
ubuntu                     : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-01-base$
```
### Задача 4:

---
Добавьте новую группу хостов fedora, самостоятельно придумайте для неё переменную. В качестве образа можно использовать этот вариант.
```
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-01-base$ cat ./playbook/inventory/prod.yml 
---
  el:
    hosts:
      centos7:
        ansible_connection: docker
  deb:
    hosts:
      ubuntu:
        ansible_connection: docker
  fedora:
    hosts:
      fedora37:
        ansible_connection: docker
  local:
    hosts:
      localhost:
        ansible_connection: local
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-01-base$ cat ./playbook/group_vars/fedora/examp.yml
---
  some_fact: "fedora default fact"
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-01-base$ sudo ansible-playbook --ask-vault-pass -i ./playbook/inventory/prod.yml ./playbook/site.yml
Vault password: 

PLAY [Print os facts] ********************************************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************************
ok: [ubuntu]
ok: [fedora37]
ok: [localhost]
ok: [centos7]

TASK [Print OS] **************************************************************************************************************************************************************
ok: [centos7] => {
    "msg": "CentOS"
}
ok: [ubuntu] => {
    "msg": "Ubuntu"
}
ok: [fedora37] => {
    "msg": "Fedora"
}
ok: [localhost] => {
    "msg": "Linux Mint"
}

TASK [Print fact] ************************************************************************************************************************************************************
ok: [centos7] => {
    "msg": "el default fact"
}
ok: [ubuntu] => {
    "msg": "deb default fact"
}
ok: [fedora37] => {
    "msg": "fedora default fact"
}
ok: [localhost] => {
    "msg": "PaSSw0rd"
}

PLAY RECAP *******************************************************************************************************************************************************************
centos7                    : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
fedora37                   : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
localhost                  : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
ubuntu                     : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-01-base$
```
### Задача 5:

---
Напишите скрипт на bash: автоматизируйте поднятие необходимых контейнеров, запуск ansible-playbook и остановку контейнеров.

Ответ: [script.sh](script.sh)
```
#!/bin/bash

sudo docker start fedora37 ubuntu centos7
sudo ansible-playbook --ask-vault-pass -i ./playbook/inventory/prod.yml ./playbook/site.yml
sudo docker stop fedora37 ubuntu centos7
```
### Задача 6:

---
Все изменения должны быть зафиксированы и отправлены в ваш личный репозиторий.
