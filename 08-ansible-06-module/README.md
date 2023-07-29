# Ответы по домашнему заданию к занятию 6 «Создание собственных модулей»

## Основная часть

**Шаг 1.** В виртуальном окружении создайте новый `my_own_module.py` файл.

**Шаг 2.** Наполните его содержимым:

**Шаг 3.** Заполните файл в соответствии с требованиями Ansible так, чтобы он выполнял основную задачу: module должен создавать текстовый файл на удалённом хосте по пути, определённом в параметре `path`, с содержимым, определённым в параметре `content`.

**Шаг 4.** Проверьте module на исполняемость локально.
```
(venv) fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/ansible_collection/ansible$ python -m ansible.modules.my_own_module /tmp/params.json 

{"changed": false, "ok": false, "failed": true, "path": "", "message": "Failed", "msg": "Exception while creating a file: [Errno 13] Permission denied: '/file'", "invocation": {"module_args": {"path": "/file", "content": "qwerqwerqwer"}}}
(venv) fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/ansible_collection/ansible$
```

**Шаг 5.** Напишите single task playbook и используйте module в нём.
```
---
- name: Test module
  hosts: localhost
  tasks:
    - name: Call my_test_module
      my_own_module:
        path: /tmp/file1
        content: qweqweqweqwe
```

**Шаг 6.** Проверьте через playbook на идемпотентность.
```
(venv) fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/ansible_collection/ansible$ ansible-playbook site.yml
[WARNING]: You are running the development version of Ansible. You should only run Ansible from "devel" if you are modifying the Ansible engine, or trying out features under
development. This is a rapidly changing source of code and can become unstable at any point.
[WARNING]: No inventory was parsed, only implicit localhost is available
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'

PLAY [Test module] ***********************************************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************************
ok: [localhost]

TASK [Call my_test_module] ***************************************************************************************************************************************************
changed: [localhost]

PLAY RECAP *******************************************************************************************************************************************************************
localhost                  : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

(venv) fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/ansible_collection/ansible$ ansible-playbook site.yml
[WARNING]: You are running the development version of Ansible. You should only run Ansible from "devel" if you are modifying the Ansible engine, or trying out features under
development. This is a rapidly changing source of code and can become unstable at any point.
[WARNING]: No inventory was parsed, only implicit localhost is available
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'

PLAY [Test module] ***********************************************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************************
ok: [localhost]

TASK [Call my_test_module] ***************************************************************************************************************************************************
ok: [localhost]

PLAY RECAP *******************************************************************************************************************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

(venv) fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/ansible_collection/ansible$
```

**Шаг 7.** Выйдите из виртуального окружения.

**Шаг 8.** Инициализируйте новую collection: `ansible-galaxy collection init my_own_namespace.yandex_cloud_elk`.
```
(venv) fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/ansible_collection/ansible$ ansible-galaxy collection init my_own_namespace.yandex_cloud_elk
[WARNING]: You are running the development version of Ansible. You should only run Ansible from "devel" if you are modifying the Ansible engine, or trying out features under
development. This is a rapidly changing source of code and can become unstable at any point.
- Collection my_own_namespace.yandex_cloud_elk was created successfully
(venv) fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/ansible_collection/ansible$
```
**Шаг 9.** В эту collection перенесите свой module в соответствующую директорию.

**Шаг 10.** Single task playbook преобразуйте в single task role и перенесите в collection. У role должны быть default всех параметров module.

**Шаг 11.** Создайте playbook для использования этой role.
```
---
- name: Test module
  hosts: localhost
  collections:
    - my_own_namespace.yandex_cloud_elk

  roles:
    - my_own_role
```
**Шаг 12.** Заполните всю документацию по collection, выложите в свой репозиторий, поставьте тег `1.0.0` на этот коммит.

**Шаг 13.** Создайте .tar.gz этой collection: `ansible-galaxy collection build` в корневой директории collection.

**Шаг 14.** Создайте ещё одну директорию любого наименования, перенесите туда single task playbook и архив c collection.

**Шаг 15.** Установите collection из локального архива: `ansible-galaxy collection install <archivename>.tar.gz`.
```
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/ansible_collection/test$ ansible-galaxy collection install my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz 
[WARNING]: You are running the development version of Ansible. You should only run Ansible from "devel" if you are modifying the Ansible engine, or trying out features under
development. This is a rapidly changing source of code and can become unstable at any point.
Starting galaxy collection install process
Process install dependency map
Starting collection install process
Installing 'my_own_namespace.yandex_cloud_elk:1.0.0' to '/home/fedor/.ansible/collections/ansible_collections/my_own_namespace/yandex_cloud_elk'
my_own_namespace.yandex_cloud_elk:1.0.0 was installed successfully
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/ansible_collection/test$
```
**Шаг 16.** Запустите playbook, убедитесь, что он работает.
```
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/ansible_collection/test$ ansible-playbook site.yml 
[WARNING]: You are running the development version of Ansible. You should only run Ansible from "devel" if you are modifying the Ansible engine, or trying out features under
development. This is a rapidly changing source of code and can become unstable at any point.
[WARNING]: No inventory was parsed, only implicit localhost is available
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'

PLAY [Test module] ***********************************************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************************
ok: [localhost]

TASK [my_own_namespace.yandex_cloud_elk.my_own_role : Call my_test_module] ***************************************************************************************************
changed: [localhost]

PLAY RECAP *******************************************************************************************************************************************************************
localhost                  : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/ansible_collection/test$ ansible-playbook site.yml 
[WARNING]: You are running the development version of Ansible. You should only run Ansible from "devel" if you are modifying the Ansible engine, or trying out features under
development. This is a rapidly changing source of code and can become unstable at any point.
[WARNING]: No inventory was parsed, only implicit localhost is available
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'

PLAY [Test module] ***********************************************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************************
ok: [localhost]

TASK [my_own_namespace.yandex_cloud_elk.my_own_role : Call my_test_module] ***************************************************************************************************
ok: [localhost]

PLAY RECAP *******************************************************************************************************************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/ansible_collection/test$
```
**Шаг 17.** В ответ необходимо прислать ссылки на collection и tar.gz архив, а также скриншоты выполнения пунктов 4, 6, 15 и 16.

[my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz](https://github.com/fedor-metsger/mnt-homeworks/blob/master/my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz)

[Collection](https://github.com/fedor-metsger/yandex_cloud_elk)
