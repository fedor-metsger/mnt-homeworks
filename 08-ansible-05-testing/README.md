# Ответы к домашнему заданию 5 «Тестирование roles»

## Основная часть

### Molecule

1. Запустите  `molecule test -s centos_7` внутри корневой директории clickhouse-role, посмотрите на вывод команды. Данная команда может отработать с ошибками, это нормально. Наша цель - посмотреть как другие в реальном мире используют молекулу.
2. Перейдите в каталог с ролью vector-role и создайте сценарий тестирования по умолчанию при помощи `molecule init scenario --driver-name docker`.
3. Добавьте несколько разных дистрибутивов (centos:8, ubuntu:latest) для инстансов и протестируйте роль, исправьте найденные ошибки, если они есть.

Ответ: [molecule.yml](https://github.com/fedor-metsger/vector-role/blob/main/molecule/default/molecule.yml)



Вывод команды **molecule test**:
```
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/vector-role$ molecule test
WARNING  The scenario config file ('/home/fedor/CODE/Netology/DevOps/vector-role/molecule/default/molecule.yml') has been modified since the scenario was created. If recent changes are important, reset the scenario with 'molecule destroy' to clean up created items or 'molecule reset' to clear current configuration.
WARNING  Driver docker does not provide a schema.
INFO     default scenario test matrix: dependency, cleanup, destroy, syntax, create, prepare, converge, idempotence, side_effect, verify, cleanup, destroy
INFO     Performing prerun with role_name_check=0...
INFO     Set ANSIBLE_LIBRARY=/home/fedor/.cache/ansible-compat/f5bcd7/modules:/home/fedor/.ansible/plugins/modules:/usr/share/ansible/plugins/modules
INFO     Set ANSIBLE_COLLECTIONS_PATH=/home/fedor/.cache/ansible-compat/f5bcd7/collections:/home/fedor/.ansible/collections:/usr/share/ansible/collections
INFO     Set ANSIBLE_ROLES_PATH=/home/fedor/.cache/ansible-compat/f5bcd7/roles:/home/fedor/.ansible/roles:/usr/share/ansible/roles:/etc/ansible/roles
INFO     Running default > dependency
WARNING  Skipping, missing the requirements file.
WARNING  Skipping, missing the requirements file.
INFO     Running default > cleanup
WARNING  Skipping, cleanup playbook not configured.
INFO     Running default > destroy
INFO     Sanity checks: 'docker'

PLAY [Destroy] *****************************************************************

TASK [Set async_dir for HOME env] **********************************************
ok: [localhost]

TASK [Destroy molecule instance(s)] ********************************************
changed: [localhost] => (item=ubuntu-20.04)
changed: [localhost] => (item=ubuntu-22.04)

TASK [Wait for instance(s) deletion to complete] *******************************
ok: [localhost] => (item=ubuntu-20.04)
ok: [localhost] => (item=ubuntu-22.04)

TASK [Delete docker networks(s)] ***********************************************
skipping: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=1    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0

INFO     Running default > syntax

playbook: /home/fedor/CODE/Netology/DevOps/vector-role/molecule/default/converge.yml
INFO     Running default > create

PLAY [Create] ******************************************************************

TASK [Set async_dir for HOME env] **********************************************
ok: [localhost]

TASK [Log into a Docker registry] **********************************************
skipping: [localhost] => (item=None) 
skipping: [localhost] => (item=None) 
skipping: [localhost]

TASK [Check presence of custom Dockerfiles] ************************************
ok: [localhost] => (item={'cgroupns_mode': 'host', 'command': '/lib/systemd/systemd', 'image': 'geerlingguy/docker-ubuntu2004-ansible:latest', 'name': 'ubuntu-20.04', 'pre_build_image': True, 'privileged': True, 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup:rw']})
ok: [localhost] => (item={'cgroupns_mode': 'host', 'command': '/lib/systemd/systemd', 'image': 'geerlingguy/docker-ubuntu2204-ansible:latest', 'name': 'ubuntu-22.04', 'pre_build_image': True, 'privileged': True, 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup:rw']})

TASK [Create Dockerfiles from image names] *************************************
skipping: [localhost] => (item={'cgroupns_mode': 'host', 'command': '/lib/systemd/systemd', 'image': 'geerlingguy/docker-ubuntu2004-ansible:latest', 'name': 'ubuntu-20.04', 'pre_build_image': True, 'privileged': True, 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup:rw']})
skipping: [localhost] => (item={'cgroupns_mode': 'host', 'command': '/lib/systemd/systemd', 'image': 'geerlingguy/docker-ubuntu2204-ansible:latest', 'name': 'ubuntu-22.04', 'pre_build_image': True, 'privileged': True, 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup:rw']})
skipping: [localhost]

TASK [Synchronization the context] *********************************************
skipping: [localhost] => (item={'cgroupns_mode': 'host', 'command': '/lib/systemd/systemd', 'image': 'geerlingguy/docker-ubuntu2004-ansible:latest', 'name': 'ubuntu-20.04', 'pre_build_image': True, 'privileged': True, 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup:rw']})
skipping: [localhost] => (item={'cgroupns_mode': 'host', 'command': '/lib/systemd/systemd', 'image': 'geerlingguy/docker-ubuntu2204-ansible:latest', 'name': 'ubuntu-22.04', 'pre_build_image': True, 'privileged': True, 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup:rw']})
skipping: [localhost]

TASK [Discover local Docker images] ********************************************
ok: [localhost] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False', 'false_condition': 'not item.pre_build_image | default(false)', 'item': {'cgroupns_mode': 'host', 'command': '/lib/systemd/systemd', 'image': 'geerlingguy/docker-ubuntu2004-ansible:latest', 'name': 'ubuntu-20.04', 'pre_build_image': True, 'privileged': True, 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup:rw']}, 'ansible_loop_var': 'item', 'i': 0, 'ansible_index_var': 'i'})
ok: [localhost] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False', 'false_condition': 'not item.pre_build_image | default(false)', 'item': {'cgroupns_mode': 'host', 'command': '/lib/systemd/systemd', 'image': 'geerlingguy/docker-ubuntu2204-ansible:latest', 'name': 'ubuntu-22.04', 'pre_build_image': True, 'privileged': True, 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup:rw']}, 'ansible_loop_var': 'item', 'i': 1, 'ansible_index_var': 'i'})

TASK [Build an Ansible compatible image (new)] *********************************
skipping: [localhost] => (item=molecule_local/geerlingguy/docker-ubuntu2004-ansible:latest) 
skipping: [localhost] => (item=molecule_local/geerlingguy/docker-ubuntu2204-ansible:latest) 
skipping: [localhost]

TASK [Create docker network(s)] ************************************************
skipping: [localhost]

TASK [Determine the CMD directives] ********************************************
ok: [localhost] => (item={'cgroupns_mode': 'host', 'command': '/lib/systemd/systemd', 'image': 'geerlingguy/docker-ubuntu2004-ansible:latest', 'name': 'ubuntu-20.04', 'pre_build_image': True, 'privileged': True, 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup:rw']})
ok: [localhost] => (item={'cgroupns_mode': 'host', 'command': '/lib/systemd/systemd', 'image': 'geerlingguy/docker-ubuntu2204-ansible:latest', 'name': 'ubuntu-22.04', 'pre_build_image': True, 'privileged': True, 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup:rw']})

TASK [Create molecule instance(s)] *********************************************
changed: [localhost] => (item=ubuntu-20.04)
changed: [localhost] => (item=ubuntu-22.04)

TASK [Wait for instance(s) creation to complete] *******************************
changed: [localhost] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': 'j841945251946.148241', 'results_file': '/home/fedor/.ansible_async/j841945251946.148241', 'changed': True, 'item': {'cgroupns_mode': 'host', 'command': '/lib/systemd/systemd', 'image': 'geerlingguy/docker-ubuntu2004-ansible:latest', 'name': 'ubuntu-20.04', 'pre_build_image': True, 'privileged': True, 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup:rw']}, 'ansible_loop_var': 'item'})
FAILED - RETRYING: [localhost]: Wait for instance(s) creation to complete (300 retries left).
changed: [localhost] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': 'j375554929027.148276', 'results_file': '/home/fedor/.ansible_async/j375554929027.148276', 'changed': True, 'item': {'cgroupns_mode': 'host', 'command': '/lib/systemd/systemd', 'image': 'geerlingguy/docker-ubuntu2204-ansible:latest', 'name': 'ubuntu-22.04', 'pre_build_image': True, 'privileged': True, 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup:rw']}, 'ansible_loop_var': 'item'})

PLAY RECAP *********************************************************************
localhost                  : ok=6    changed=2    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0

INFO     Running default > prepare
WARNING  Skipping, prepare playbook not configured.
INFO     Running default > converge

PLAY [Converge] ****************************************************************

TASK [Gathering Facts] *********************************************************
ok: [ubuntu-20.04]
ok: [ubuntu-22.04]

TASK [Include vector-role] *****************************************************

TASK [vector-role : Install vector packages from internet] *********************
changed: [ubuntu-20.04]
changed: [ubuntu-22.04]

TASK [vector-role : Template a config to /etc/vector/vector.toml] **************
changed: [ubuntu-20.04]
changed: [ubuntu-22.04]

RUNNING HANDLER [vector-role : Restart vector service] *************************
changed: [ubuntu-22.04]
changed: [ubuntu-20.04]

PLAY RECAP *********************************************************************
ubuntu-20.04               : ok=4    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
ubuntu-22.04               : ok=4    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

INFO     Running default > idempotence

PLAY [Converge] ****************************************************************

TASK [Gathering Facts] *********************************************************
ok: [ubuntu-20.04]
ok: [ubuntu-22.04]

TASK [Include vector-role] *****************************************************

TASK [vector-role : Install vector packages from internet] *********************
ok: [ubuntu-22.04]
ok: [ubuntu-20.04]

TASK [vector-role : Template a config to /etc/vector/vector.toml] **************
ok: [ubuntu-20.04]
ok: [ubuntu-22.04]

PLAY RECAP *********************************************************************
ubuntu-20.04               : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
ubuntu-22.04               : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

INFO     Idempotence completed successfully.
INFO     Running default > side_effect
WARNING  Skipping, side effect playbook not configured.
INFO     Running default > verify
INFO     Running Ansible Verifier

PLAY [Verify] ******************************************************************

TASK [Example assertion] *******************************************************
ok: [ubuntu-20.04] => {
    "changed": false,
    "msg": "All assertions passed"
}
ok: [ubuntu-22.04] => {
    "changed": false,
    "msg": "All assertions passed"
}

PLAY RECAP *********************************************************************
ubuntu-20.04               : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
ubuntu-22.04               : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

INFO     Verifier completed successfully.
INFO     Running default > cleanup
WARNING  Skipping, cleanup playbook not configured.
INFO     Running default > destroy

PLAY [Destroy] *****************************************************************

TASK [Set async_dir for HOME env] **********************************************
ok: [localhost]

TASK [Destroy molecule instance(s)] ********************************************
changed: [localhost] => (item=ubuntu-20.04)
changed: [localhost] => (item=ubuntu-22.04)

TASK [Wait for instance(s) deletion to complete] *******************************
FAILED - RETRYING: [localhost]: Wait for instance(s) deletion to complete (300 retries left).
changed: [localhost] => (item=ubuntu-20.04)
changed: [localhost] => (item=ubuntu-22.04)

TASK [Delete docker networks(s)] ***********************************************
skipping: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=2    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0

INFO     Pruning extra files from scenario ephemeral directory
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/vector-role$
```

5. Добавьте несколько assert в verify.yml-файл для  проверки работоспособности vector-role (проверка, что конфиг валидный, проверка успешности запуска и др.).

Ответ: [verify.yml](https://github.com/fedor-metsger/vector-role/blob/main/molecule/default/verify.yml)

Вывод команды **molecule verify**:
```
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/vector-role$ molecule verify
WARNING  Driver docker does not provide a schema.
INFO     default scenario test matrix: verify
INFO     Performing prerun with role_name_check=0...
INFO     Set ANSIBLE_LIBRARY=/home/fedor/.cache/ansible-compat/f5bcd7/modules:/home/fedor/.ansible/plugins/modules:/usr/share/ansible/plugins/modules
INFO     Set ANSIBLE_COLLECTIONS_PATH=/home/fedor/.cache/ansible-compat/f5bcd7/collections:/home/fedor/.ansible/collections:/usr/share/ansible/collections
INFO     Set ANSIBLE_ROLES_PATH=/home/fedor/.cache/ansible-compat/f5bcd7/roles:/home/fedor/.ansible/roles:/usr/share/ansible/roles:/etc/ansible/roles
INFO     Running default > verify
INFO     Running Ansible Verifier
INFO     Sanity checks: 'docker'

PLAY [Verify installation] *****************************************************

TASK [Gathering Facts] *********************************************************
ok: [ubuntu-20.04]
ok: [ubuntu-22.04]

TASK [Check that the /etc/vector/vector.toml exists] ***************************
ok: [ubuntu-20.04]
ok: [ubuntu-22.04]

TASK [Fail if the /etc/vector/vector.toml not created] *************************
ok: [ubuntu-20.04] => {
    "changed": false,
    "msg": "The /etc/vector/vector.toml repo was created"
}
ok: [ubuntu-22.04] => {
    "changed": false,
    "msg": "The /etc/vector/vector.toml repo was created"
}

TASK [Populate service facts] **************************************************
ok: [ubuntu-22.04]
ok: [ubuntu-20.04]

TASK [Assert that vector service is running] ***********************************
ok: [ubuntu-20.04] => {
    "changed": false,
    "msg": "All assertions passed"
}
ok: [ubuntu-22.04] => {
    "changed": false,
    "msg": "All assertions passed"
}

PLAY RECAP *********************************************************************
ubuntu-20.04               : ok=5    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
ubuntu-22.04               : ok=5    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

INFO     Verifier completed successfully.
```

7. Запустите тестирование роли повторно и проверьте, что оно прошло успешно.
```
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/vector-role$ molecule test
WARNING  Driver docker does not provide a schema.
INFO     default scenario test matrix: dependency, cleanup, destroy, syntax, create, prepare, converge, idempotence, side_effect, verify, cleanup, destroy
INFO     Performing prerun with role_name_check=0...
INFO     Set ANSIBLE_LIBRARY=/home/fedor/.cache/ansible-compat/f5bcd7/modules:/home/fedor/.ansible/plugins/modules:/usr/share/ansible/plugins/modules
INFO     Set ANSIBLE_COLLECTIONS_PATH=/home/fedor/.cache/ansible-compat/f5bcd7/collections:/home/fedor/.ansible/collections:/usr/share/ansible/collections
INFO     Set ANSIBLE_ROLES_PATH=/home/fedor/.cache/ansible-compat/f5bcd7/roles:/home/fedor/.ansible/roles:/usr/share/ansible/roles:/etc/ansible/roles
INFO     Running default > dependency
WARNING  Skipping, missing the requirements file.
WARNING  Skipping, missing the requirements file.
INFO     Running default > cleanup
WARNING  Skipping, cleanup playbook not configured.
INFO     Running default > destroy
INFO     Sanity checks: 'docker'

PLAY [Destroy] *****************************************************************

TASK [Set async_dir for HOME env] **********************************************
ok: [localhost]

TASK [Destroy molecule instance(s)] ********************************************
changed: [localhost] => (item=ubuntu-20.04)
changed: [localhost] => (item=ubuntu-22.04)

TASK [Wait for instance(s) deletion to complete] *******************************
FAILED - RETRYING: [localhost]: Wait for instance(s) deletion to complete (300 retries left).
changed: [localhost] => (item=ubuntu-20.04)
changed: [localhost] => (item=ubuntu-22.04)

TASK [Delete docker networks(s)] ***********************************************
skipping: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=2    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0

INFO     Running default > syntax

playbook: /home/fedor/CODE/Netology/DevOps/vector-role/molecule/default/converge.yml
INFO     Running default > create

PLAY [Create] ******************************************************************

TASK [Set async_dir for HOME env] **********************************************
ok: [localhost]

TASK [Log into a Docker registry] **********************************************
skipping: [localhost] => (item=None) 
skipping: [localhost] => (item=None) 
skipping: [localhost]

TASK [Check presence of custom Dockerfiles] ************************************
ok: [localhost] => (item={'cgroupns_mode': 'host', 'command': '/lib/systemd/systemd', 'image': 'geerlingguy/docker-ubuntu2004-ansible:latest', 'name': 'ubuntu-20.04', 'pre_build_image': True, 'privileged': True, 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup:rw']})
ok: [localhost] => (item={'cgroupns_mode': 'host', 'command': '/lib/systemd/systemd', 'image': 'geerlingguy/docker-ubuntu2204-ansible:latest', 'name': 'ubuntu-22.04', 'pre_build_image': True, 'privileged': True, 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup:rw']})

TASK [Create Dockerfiles from image names] *************************************
skipping: [localhost] => (item={'cgroupns_mode': 'host', 'command': '/lib/systemd/systemd', 'image': 'geerlingguy/docker-ubuntu2004-ansible:latest', 'name': 'ubuntu-20.04', 'pre_build_image': True, 'privileged': True, 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup:rw']})
skipping: [localhost] => (item={'cgroupns_mode': 'host', 'command': '/lib/systemd/systemd', 'image': 'geerlingguy/docker-ubuntu2204-ansible:latest', 'name': 'ubuntu-22.04', 'pre_build_image': True, 'privileged': True, 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup:rw']})
skipping: [localhost]

TASK [Synchronization the context] *********************************************
skipping: [localhost] => (item={'cgroupns_mode': 'host', 'command': '/lib/systemd/systemd', 'image': 'geerlingguy/docker-ubuntu2004-ansible:latest', 'name': 'ubuntu-20.04', 'pre_build_image': True, 'privileged': True, 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup:rw']})
skipping: [localhost] => (item={'cgroupns_mode': 'host', 'command': '/lib/systemd/systemd', 'image': 'geerlingguy/docker-ubuntu2204-ansible:latest', 'name': 'ubuntu-22.04', 'pre_build_image': True, 'privileged': True, 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup:rw']})
skipping: [localhost]

TASK [Discover local Docker images] ********************************************
ok: [localhost] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False', 'false_condition': 'not item.pre_build_image | default(false)', 'item': {'cgroupns_mode': 'host', 'command': '/lib/systemd/systemd', 'image': 'geerlingguy/docker-ubuntu2004-ansible:latest', 'name': 'ubuntu-20.04', 'pre_build_image': True, 'privileged': True, 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup:rw']}, 'ansible_loop_var': 'item', 'i': 0, 'ansible_index_var': 'i'})
ok: [localhost] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False', 'false_condition': 'not item.pre_build_image | default(false)', 'item': {'cgroupns_mode': 'host', 'command': '/lib/systemd/systemd', 'image': 'geerlingguy/docker-ubuntu2204-ansible:latest', 'name': 'ubuntu-22.04', 'pre_build_image': True, 'privileged': True, 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup:rw']}, 'ansible_loop_var': 'item', 'i': 1, 'ansible_index_var': 'i'})

TASK [Build an Ansible compatible image (new)] *********************************
skipping: [localhost] => (item=molecule_local/geerlingguy/docker-ubuntu2004-ansible:latest) 
skipping: [localhost] => (item=molecule_local/geerlingguy/docker-ubuntu2204-ansible:latest) 
skipping: [localhost]

TASK [Create docker network(s)] ************************************************
skipping: [localhost]

TASK [Determine the CMD directives] ********************************************
ok: [localhost] => (item={'cgroupns_mode': 'host', 'command': '/lib/systemd/systemd', 'image': 'geerlingguy/docker-ubuntu2004-ansible:latest', 'name': 'ubuntu-20.04', 'pre_build_image': True, 'privileged': True, 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup:rw']})
ok: [localhost] => (item={'cgroupns_mode': 'host', 'command': '/lib/systemd/systemd', 'image': 'geerlingguy/docker-ubuntu2204-ansible:latest', 'name': 'ubuntu-22.04', 'pre_build_image': True, 'privileged': True, 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup:rw']})

TASK [Create molecule instance(s)] *********************************************
changed: [localhost] => (item=ubuntu-20.04)
changed: [localhost] => (item=ubuntu-22.04)

TASK [Wait for instance(s) creation to complete] *******************************
changed: [localhost] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': 'j179626780838.166080', 'results_file': '/home/fedor/.ansible_async/j179626780838.166080', 'changed': True, 'item': {'cgroupns_mode': 'host', 'command': '/lib/systemd/systemd', 'image': 'geerlingguy/docker-ubuntu2004-ansible:latest', 'name': 'ubuntu-20.04', 'pre_build_image': True, 'privileged': True, 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup:rw']}, 'ansible_loop_var': 'item'})
FAILED - RETRYING: [localhost]: Wait for instance(s) creation to complete (300 retries left).
changed: [localhost] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': 'j537174168060.166113', 'results_file': '/home/fedor/.ansible_async/j537174168060.166113', 'changed': True, 'item': {'cgroupns_mode': 'host', 'command': '/lib/systemd/systemd', 'image': 'geerlingguy/docker-ubuntu2204-ansible:latest', 'name': 'ubuntu-22.04', 'pre_build_image': True, 'privileged': True, 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup:rw']}, 'ansible_loop_var': 'item'})

PLAY RECAP *********************************************************************
localhost                  : ok=6    changed=2    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0

INFO     Running default > prepare
WARNING  Skipping, prepare playbook not configured.
INFO     Running default > converge

PLAY [Converge] ****************************************************************

TASK [Gathering Facts] *********************************************************
ok: [ubuntu-20.04]
ok: [ubuntu-22.04]

TASK [Include vector-role] *****************************************************

TASK [vector-role : Install vector packages from internet] *********************
changed: [ubuntu-20.04]
changed: [ubuntu-22.04]

TASK [vector-role : Template a config to /etc/vector/vector.toml] **************
changed: [ubuntu-20.04]
changed: [ubuntu-22.04]

RUNNING HANDLER [vector-role : Restart vector service] *************************
changed: [ubuntu-20.04]
changed: [ubuntu-22.04]

PLAY RECAP *********************************************************************
ubuntu-20.04               : ok=4    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
ubuntu-22.04               : ok=4    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

INFO     Running default > idempotence

PLAY [Converge] ****************************************************************

TASK [Gathering Facts] *********************************************************
ok: [ubuntu-22.04]
ok: [ubuntu-20.04]

TASK [Include vector-role] *****************************************************

TASK [vector-role : Install vector packages from internet] *********************
ok: [ubuntu-22.04]
ok: [ubuntu-20.04]

TASK [vector-role : Template a config to /etc/vector/vector.toml] **************
ok: [ubuntu-20.04]
ok: [ubuntu-22.04]

PLAY RECAP *********************************************************************
ubuntu-20.04               : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
ubuntu-22.04               : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

INFO     Idempotence completed successfully.
INFO     Running default > side_effect
WARNING  Skipping, side effect playbook not configured.
INFO     Running default > verify
INFO     Running Ansible Verifier

PLAY [Verify installation] *****************************************************

TASK [Gathering Facts] *********************************************************
ok: [ubuntu-22.04]
ok: [ubuntu-20.04]

TASK [Check that the /etc/vector/vector.toml exists] ***************************
ok: [ubuntu-20.04]
ok: [ubuntu-22.04]

TASK [Fail if the /etc/vector/vector.toml not created] *************************
ok: [ubuntu-20.04] => {
    "changed": false,
    "msg": "The /etc/vector/vector.toml repo was created"
}
ok: [ubuntu-22.04] => {
    "changed": false,
    "msg": "The /etc/vector/vector.toml repo was created"
}

TASK [Populate service facts] **************************************************
ok: [ubuntu-22.04]
ok: [ubuntu-20.04]

TASK [Assert that vector service is running] ***********************************
ok: [ubuntu-20.04] => {
    "changed": false,
    "msg": "All assertions passed"
}
ok: [ubuntu-22.04] => {
    "changed": false,
    "msg": "All assertions passed"
}

PLAY RECAP *********************************************************************
ubuntu-20.04               : ok=5    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
ubuntu-22.04               : ok=5    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

INFO     Verifier completed successfully.
INFO     Running default > cleanup
WARNING  Skipping, cleanup playbook not configured.
INFO     Running default > destroy

PLAY [Destroy] *****************************************************************

TASK [Set async_dir for HOME env] **********************************************
ok: [localhost]

TASK [Destroy molecule instance(s)] ********************************************
changed: [localhost] => (item=ubuntu-20.04)
changed: [localhost] => (item=ubuntu-22.04)

TASK [Wait for instance(s) deletion to complete] *******************************
FAILED - RETRYING: [localhost]: Wait for instance(s) deletion to complete (300 retries left).
changed: [localhost] => (item=ubuntu-20.04)
changed: [localhost] => (item=ubuntu-22.04)

TASK [Delete docker networks(s)] ***********************************************
skipping: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=2    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0

INFO     Pruning extra files from scenario ephemeral directory
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/vector-role$
```
5. Добавьте новый тег на коммит с рабочим сценарием в соответствии с семантическим версионированием.

Ответ: **[1.1.0](https://github.com/fedor-metsger/vector-role/releases/tag/1.1.0)**

### Tox

1. Добавьте в директорию с vector-role файлы из [директории](./example).
2. Запустите `docker run --privileged=True -v <path_to_repo>:/opt/vector-role -w /opt/vector-role -it aragast/netology:latest /bin/bash`, где path_to_repo — путь до корня репозитория с vector-role на вашей файловой системе.
3. Внутри контейнера выполните команду `tox`, посмотрите на вывод.
```
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/vector-role$ docker run --privileged=True -v `pwd`:/opt/vector-role -w /opt/vector-role -it aragast/netology:latest /bin/bash
[root@16faf128e37f vector-role]# tox
py37-ansible210 create: /opt/vector-role/.tox/py37-ansible210
py37-ansible210 installdeps: -rtox-requirements.txt, ansible<3.0
py37-ansible210 installed: ansible==2.10.7,ansible-base==2.10.17,ansible-compat==1.0.0,ansible-lint==5.1.3,arrow==1.2.3,bcrypt==4.0.1,binaryornot==0.4.4,bracex==2.3.post1,cached-property==1.5.2,Cerberus==1.3.2,certifi==2023.7.22,cffi==1.15.1,chardet==5.1.0,charset-normalizer==3.2.0,click==8.1.6,click-help-colors==0.9.1,cookiecutter==2.2.3,cryptography==41.0.2,distro==1.8.0,enrich==1.2.7,idna==3.4,importlib-metadata==6.7.0,Jinja2==3.1.2,jmespath==1.0.1,lxml==4.9.3,markdown-it-py==2.2.0,MarkupSafe==2.1.3,mdurl==0.1.2,molecule==3.4.0,molecule-podman==1.0.1,packaging==23.1,paramiko==2.12.0,pathspec==0.11.1,pluggy==0.13.1,pycparser==2.21,Pygments==2.15.1,PyNaCl==1.5.0,python-dateutil==2.8.2,python-slugify==8.0.1,PyYAML==5.4.1,requests==2.31.0,rich==13.4.2,ruamel.yaml==0.17.32,ruamel.yaml.clib==0.2.7,selinux==0.2.1,six==1.16.0,subprocess-tee==0.3.5,tenacity==8.2.2,text-unidecode==1.3,typing_extensions==4.7.1,urllib3==2.0.4,wcmatch==8.4.1,yamllint==1.26.3,zipp==3.15.0
py37-ansible210 run-test-pre: PYTHONHASHSEED='53447615'
py37-ansible210 run-test: commands[0] | molecule test -s compatibility --destroy always
CRITICAL 'molecule/compatibility/molecule.yml' glob failed.  Exiting.
ERROR: InvocationError for command /opt/vector-role/.tox/py37-ansible210/bin/molecule test -s compatibility --destroy always (exited with code 1)
py37-ansible30 create: /opt/vector-role/.tox/py37-ansible30
py37-ansible30 installdeps: -rtox-requirements.txt, ansible<3.1
py37-ansible30 installed: ansible==3.0.0,ansible-base==2.10.17,ansible-compat==1.0.0,ansible-lint==5.1.3,arrow==1.2.3,bcrypt==4.0.1,binaryornot==0.4.4,bracex==2.3.post1,cached-property==1.5.2,Cerberus==1.3.2,certifi==2023.7.22,cffi==1.15.1,chardet==5.1.0,charset-normalizer==3.2.0,click==8.1.6,click-help-colors==0.9.1,cookiecutter==2.2.3,cryptography==41.0.2,distro==1.8.0,enrich==1.2.7,idna==3.4,importlib-metadata==6.7.0,Jinja2==3.1.2,jmespath==1.0.1,lxml==4.9.3,markdown-it-py==2.2.0,MarkupSafe==2.1.3,mdurl==0.1.2,molecule==3.4.0,molecule-podman==1.0.1,packaging==23.1,paramiko==2.12.0,pathspec==0.11.1,pluggy==0.13.1,pycparser==2.21,Pygments==2.15.1,PyNaCl==1.5.0,python-dateutil==2.8.2,python-slugify==8.0.1,PyYAML==5.4.1,requests==2.31.0,rich==13.4.2,ruamel.yaml==0.17.32,ruamel.yaml.clib==0.2.7,selinux==0.2.1,six==1.16.0,subprocess-tee==0.3.5,tenacity==8.2.2,text-unidecode==1.3,typing_extensions==4.7.1,urllib3==2.0.4,wcmatch==8.4.1,yamllint==1.26.3,zipp==3.15.0
py37-ansible30 run-test-pre: PYTHONHASHSEED='53447615'
py37-ansible30 run-test: commands[0] | molecule test -s compatibility --destroy always
CRITICAL 'molecule/compatibility/molecule.yml' glob failed.  Exiting.
ERROR: InvocationError for command /opt/vector-role/.tox/py37-ansible30/bin/molecule test -s compatibility --destroy always (exited with code 1)
py39-ansible210 create: /opt/vector-role/.tox/py39-ansible210
py39-ansible210 installdeps: -rtox-requirements.txt, ansible<3.0
py39-ansible210 installed: ansible==2.10.7,ansible-base==2.10.17,ansible-compat==4.1.5,ansible-core==2.15.2,ansible-lint==5.1.3,arrow==1.2.3,attrs==23.1.0,bcrypt==4.0.1,binaryornot==0.4.4,bracex==2.3.post1,Cerberus==1.3.2,certifi==2023.7.22,cffi==1.15.1,chardet==5.1.0,charset-normalizer==3.2.0,click==8.1.6,click-help-colors==0.9.1,cookiecutter==2.2.3,cryptography==41.0.2,distro==1.8.0,enrich==1.2.7,idna==3.4,importlib-resources==5.0.7,Jinja2==3.1.2,jmespath==1.0.1,jsonschema==4.18.4,jsonschema-specifications==2023.7.1,lxml==4.9.3,markdown-it-py==3.0.0,MarkupSafe==2.1.3,mdurl==0.1.2,molecule==3.4.0,molecule-podman==1.0.1,packaging==23.1,paramiko==2.12.0,pathspec==0.11.1,pluggy==0.13.1,pycparser==2.21,Pygments==2.15.1,PyNaCl==1.5.0,python-dateutil==2.8.2,python-slugify==8.0.1,PyYAML==5.4.1,referencing==0.30.0,requests==2.31.0,resolvelib==1.0.1,rich==13.4.2,rpds-py==0.9.2,ruamel.yaml==0.17.32,ruamel.yaml.clib==0.2.7,selinux==0.3.0,six==1.16.0,subprocess-tee==0.4.1,tenacity==8.2.2,text-unidecode==1.3,typing_extensions==4.7.1,urllib3==2.0.4,wcmatch==8.4.1,yamllint==1.26.3
py39-ansible210 run-test-pre: PYTHONHASHSEED='53447615'
py39-ansible210 run-test: commands[0] | molecule test -s compatibility --destroy always
CRITICAL 'molecule/compatibility/molecule.yml' glob failed.  Exiting.
ERROR: InvocationError for command /opt/vector-role/.tox/py39-ansible210/bin/molecule test -s compatibility --destroy always (exited with code 1)
py39-ansible30 create: /opt/vector-role/.tox/py39-ansible30
py39-ansible30 installdeps: -rtox-requirements.txt, ansible<3.1
py39-ansible30 installed: ansible==3.0.0,ansible-base==2.10.17,ansible-compat==4.1.5,ansible-core==2.15.2,ansible-lint==5.1.3,arrow==1.2.3,attrs==23.1.0,bcrypt==4.0.1,binaryornot==0.4.4,bracex==2.3.post1,Cerberus==1.3.2,certifi==2023.7.22,cffi==1.15.1,chardet==5.1.0,charset-normalizer==3.2.0,click==8.1.6,click-help-colors==0.9.1,cookiecutter==2.2.3,cryptography==41.0.2,distro==1.8.0,enrich==1.2.7,idna==3.4,importlib-resources==5.0.7,Jinja2==3.1.2,jmespath==1.0.1,jsonschema==4.18.4,jsonschema-specifications==2023.7.1,lxml==4.9.3,markdown-it-py==3.0.0,MarkupSafe==2.1.3,mdurl==0.1.2,molecule==3.4.0,molecule-podman==1.0.1,packaging==23.1,paramiko==2.12.0,pathspec==0.11.1,pluggy==0.13.1,pycparser==2.21,Pygments==2.15.1,PyNaCl==1.5.0,python-dateutil==2.8.2,python-slugify==8.0.1,PyYAML==5.4.1,referencing==0.30.0,requests==2.31.0,resolvelib==1.0.1,rich==13.4.2,rpds-py==0.9.2,ruamel.yaml==0.17.32,ruamel.yaml.clib==0.2.7,selinux==0.3.0,six==1.16.0,subprocess-tee==0.4.1,tenacity==8.2.2,text-unidecode==1.3,typing_extensions==4.7.1,urllib3==2.0.4,wcmatch==8.4.1,yamllint==1.26.3
py39-ansible30 run-test-pre: PYTHONHASHSEED='53447615'
py39-ansible30 run-test: commands[0] | molecule test -s compatibility --destroy always
CRITICAL 'molecule/compatibility/molecule.yml' glob failed.  Exiting.
ERROR: InvocationError for command /opt/vector-role/.tox/py39-ansible30/bin/molecule test -s compatibility --destroy always (exited with code 1)
__________________________________________________________________________________ summary ___________________________________________________________________________________
ERROR:   py37-ansible210: commands failed
ERROR:   py37-ansible30: commands failed
ERROR:   py39-ansible210: commands failed
ERROR:   py39-ansible30: commands failed
[root@16faf128e37f vector-role]#
```

5. Создайте облегчённый сценарий для `molecule` с драйвером `molecule_podman`. Проверьте его на исполнимость.

Ответ: [molecule.yml](https://github.com/fedor-metsger/vector-role/blob/main/molecule/podman/molecule.yml)
```
---
dependency:
  name: galaxy
driver:
  name: podman
platforms:
  - name: ubuntu-22.04
    hostname: ubuntu-22.04
    image: geerlingguy/docker-ubuntu2204-ansible:latest
    cgroupns_mode: host
    volumes:
      - /sys/fs/cgroup:/sys/fs/cgroup:rw
    privileged: true
    command: /lib/systemd/systemd
    pre_build_image: true
provisioner:
  name: ansible
verifier:
  name: ansible
scenario:
  test_sequence:
    - destroy
    - create
    - converge
    - destroy
```
7. Пропишите правильную команду в `tox.ini`, чтобы запускался облегчённый сценарий.

Ответ: [tox.ini](https://github.com/fedor-metsger/vector-role/blob/main/tox.ini)
```
[tox]
minversion = 1.8
basepython = python3.6
envlist = py{37}-ansible{210,30}
skipsdist = true

[testenv]
passenv = *
deps =
    -r tox-requirements.txt
    ansible210: ansible<3.0
    ansible30: ansible<3.1
commands =
    {posargs:molecule test -s podman --destroy always}
```
9. Запустите команду `tox`. Убедитесь, что всё отработало успешно.
```
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/vector-role$ docker run --privileged=True -v `pwd`:/opt/vector-role -w /opt/vector-role -it aragast/netology:latest /bin/bash
[root@54d0d51e2ac9 vector-role]# tox
py37-ansible210 installed: ansible==2.10.7,ansible-base==2.10.17,ansible-compat==1.0.0,ansible-lint==5.1.3,arrow==1.2.3,bcrypt==4.0.1,binaryornot==0.4.4,bracex==2.3.post1,cached-property==1.5.2,Cerberus==1.3.2,certifi==2023.7.22,cffi==1.15.1,chardet==5.1.0,charset-normalizer==3.2.0,click==8.1.6,click-help-colors==0.9.1,cookiecutter==2.2.3,cryptography==41.0.2,distro==1.8.0,enrich==1.2.7,idna==3.4,importlib-metadata==6.7.0,Jinja2==3.1.2,jmespath==1.0.1,lxml==4.9.3,markdown-it-py==2.2.0,MarkupSafe==2.1.3,mdurl==0.1.2,molecule==3.4.0,molecule-podman==1.0.1,packaging==23.1,paramiko==2.12.0,pathspec==0.11.1,pluggy==0.13.1,pycparser==2.21,Pygments==2.15.1,PyNaCl==1.5.0,python-dateutil==2.8.2,python-slugify==8.0.1,PyYAML==5.4.1,requests==2.31.0,rich==13.4.2,ruamel.yaml==0.17.32,ruamel.yaml.clib==0.2.7,selinux==0.2.1,six==1.16.0,subprocess-tee==0.3.5,tenacity==8.2.2,text-unidecode==1.3,typing_extensions==4.7.1,urllib3==2.0.4,wcmatch==8.4.1,yamllint==1.26.3,zipp==3.15.0
py37-ansible210 run-test-pre: PYTHONHASHSEED='3500449315'
py37-ansible210 run-test: commands[0] | molecule test -s podman --destroy always
INFO     podman scenario test matrix: destroy, create, converge, destroy
INFO     Performing prerun...
WARNING  Failed to locate command: [Errno 2] No such file or directory: 'git': 'git'
INFO     Guessed /opt/vector-role as project root directory
INFO     Running podman > destroy
INFO     Sanity checks: 'podman'

PLAY [Destroy] *****************************************************************

TASK [Destroy molecule instance(s)] ********************************************
changed: [localhost] => (item={'cgroupns_mode': 'host', 'command': '/lib/systemd/systemd', 'hostname': 'ubuntu-22.04', 'image': 'geerlingguy/docker-ubuntu2204-ansible:latest', 'name': 'ubuntu-22.04', 'pre_build_image': True, 'privileged': True, 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup:rw']})

TASK [Wait for instance(s) deletion to complete] *******************************
changed: [localhost] => (item={'started': 1, 'finished': 0, 'ansible_job_id': '686203302411.60', 'results_file': '/root/.ansible_async/686203302411.60', 'changed': True, 'failed': False, 'item': {'cgroupns_mode': 'host', 'command': '/lib/systemd/systemd', 'hostname': 'ubuntu-22.04', 'image': 'geerlingguy/docker-ubuntu2204-ansible:latest', 'name': 'ubuntu-22.04', 'pre_build_image': True, 'privileged': True, 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup:rw']}, 'ansible_loop_var': 'item'})

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

INFO     Running podman > create

PLAY [Create] ******************************************************************

TASK [get podman executable path] **********************************************
ok: [localhost]

TASK [save path to executable as fact] *****************************************
ok: [localhost]

TASK [Log into a container registry] *******************************************
skipping: [localhost] => (item="ubuntu-22.04 registry username: None specified") 

TASK [Check presence of custom Dockerfiles] ************************************
ok: [localhost] => (item=Dockerfile: None specified)

TASK [Create Dockerfiles from image names] *************************************
skipping: [localhost] => (item="Dockerfile: None specified; Image: geerlingguy/docker-ubuntu2204-ansible:latest") 

TASK [Discover local Podman images] ********************************************
ok: [localhost] => (item=ubuntu-22.04)

TASK [Build an Ansible compatible image] ***************************************
skipping: [localhost] => (item=geerlingguy/docker-ubuntu2204-ansible:latest) 

TASK [Determine the CMD directives] ********************************************
ok: [localhost] => (item="ubuntu-22.04 command: /lib/systemd/systemd")

TASK [Remove possible pre-existing containers] *********************************
changed: [localhost]

TASK [Discover local podman networks] ******************************************
skipping: [localhost] => (item=ubuntu-22.04: None specified) 

TASK [Create podman network dedicated to this scenario] ************************
skipping: [localhost]

TASK [Create molecule instance(s)] *********************************************
changed: [localhost] => (item=ubuntu-22.04)

TASK [Wait for instance(s) creation to complete] *******************************
FAILED - RETRYING: Wait for instance(s) creation to complete (300 retries left).
FAILED - RETRYING: Wait for instance(s) creation to complete (299 retries left).
FAILED - RETRYING: Wait for instance(s) creation to complete (298 retries left).
FAILED - RETRYING: Wait for instance(s) creation to complete (297 retries left).
FAILED - RETRYING: Wait for instance(s) creation to complete (296 retries left).
FAILED - RETRYING: Wait for instance(s) creation to complete (295 retries left).
FAILED - RETRYING: Wait for instance(s) creation to complete (294 retries left).
FAILED - RETRYING: Wait for instance(s) creation to complete (293 retries left).
FAILED - RETRYING: Wait for instance(s) creation to complete (292 retries left).
FAILED - RETRYING: Wait for instance(s) creation to complete (291 retries left).
FAILED - RETRYING: Wait for instance(s) creation to complete (290 retries left).
changed: [localhost] => (item=ubuntu-22.04)

PLAY RECAP *********************************************************************
localhost                  : ok=8    changed=3    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0

INFO     Running podman > converge

PLAY [Converge] ****************************************************************

TASK [Gathering Facts] *********************************************************
ok: [ubuntu-22.04]

TASK [Copy something to test use of synchronize module] ************************
changed: [ubuntu-22.04]

TASK [Include vector-role] *****************************************************

TASK [vector-role : Install vector packages from internet] *********************
changed: [ubuntu-22.04]

TASK [vector-role : Template a config to /etc/vector/vector.toml] **************
changed: [ubuntu-22.04]

RUNNING HANDLER [vector-role : Restart vector service] *************************
changed: [ubuntu-22.04]

PLAY RECAP *********************************************************************
ubuntu-22.04               : ok=5    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

INFO     Running podman > destroy

PLAY [Destroy] *****************************************************************

TASK [Destroy molecule instance(s)] ********************************************
changed: [localhost] => (item={'cgroupns_mode': 'host', 'command': '/lib/systemd/systemd', 'hostname': 'ubuntu-22.04', 'image': 'geerlingguy/docker-ubuntu2204-ansible:latest', 'name': 'ubuntu-22.04', 'pre_build_image': True, 'privileged': True, 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup:rw']})

TASK [Wait for instance(s) deletion to complete] *******************************
FAILED - RETRYING: Wait for instance(s) deletion to complete (300 retries left).
changed: [localhost] => (item={'started': 1, 'finished': 0, 'ansible_job_id': '584977767359.2139', 'results_file': '/root/.ansible_async/584977767359.2139', 'changed': True, 'failed': False, 'item': {'cgroupns_mode': 'host', 'command': '/lib/systemd/systemd', 'hostname': 'ubuntu-22.04', 'image': 'geerlingguy/docker-ubuntu2204-ansible:latest', 'name': 'ubuntu-22.04', 'pre_build_image': True, 'privileged': True, 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup:rw']}, 'ansible_loop_var': 'item'})

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

INFO     Pruning extra files from scenario ephemeral directory
py37-ansible30 installed: ansible==3.0.0,ansible-base==2.10.17,ansible-compat==1.0.0,ansible-lint==5.1.3,arrow==1.2.3,bcrypt==4.0.1,binaryornot==0.4.4,bracex==2.3.post1,cached-property==1.5.2,Cerberus==1.3.2,certifi==2023.7.22,cffi==1.15.1,chardet==5.1.0,charset-normalizer==3.2.0,click==8.1.6,click-help-colors==0.9.1,cookiecutter==2.2.3,cryptography==41.0.2,distro==1.8.0,enrich==1.2.7,idna==3.4,importlib-metadata==6.7.0,Jinja2==3.1.2,jmespath==1.0.1,lxml==4.9.3,markdown-it-py==2.2.0,MarkupSafe==2.1.3,mdurl==0.1.2,molecule==3.4.0,molecule-podman==1.0.1,packaging==23.1,paramiko==2.12.0,pathspec==0.11.1,pluggy==0.13.1,pycparser==2.21,Pygments==2.15.1,PyNaCl==1.5.0,python-dateutil==2.8.2,python-slugify==8.0.1,PyYAML==5.4.1,requests==2.31.0,rich==13.4.2,ruamel.yaml==0.17.32,ruamel.yaml.clib==0.2.7,selinux==0.2.1,six==1.16.0,subprocess-tee==0.3.5,tenacity==8.2.2,text-unidecode==1.3,typing_extensions==4.7.1,urllib3==2.0.4,wcmatch==8.4.1,yamllint==1.26.3,zipp==3.15.0
py37-ansible30 run-test-pre: PYTHONHASHSEED='3500449315'
py37-ansible30 run-test: commands[0] | molecule test -s podman --destroy always
INFO     podman scenario test matrix: destroy, create, converge, destroy
INFO     Performing prerun...
WARNING  Failed to locate command: [Errno 2] No such file or directory: 'git': 'git'
INFO     Guessed /opt/vector-role as project root directory
INFO     Running podman > destroy
INFO     Sanity checks: 'podman'

PLAY [Destroy] *****************************************************************

TASK [Destroy molecule instance(s)] ********************************************
changed: [localhost] => (item={'cgroupns_mode': 'host', 'command': '/lib/systemd/systemd', 'hostname': 'ubuntu-22.04', 'image': 'geerlingguy/docker-ubuntu2204-ansible:latest', 'name': 'ubuntu-22.04', 'pre_build_image': True, 'privileged': True, 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup:rw']})

TASK [Wait for instance(s) deletion to complete] *******************************
changed: [localhost] => (item={'started': 1, 'finished': 0, 'ansible_job_id': '3576405980.2284', 'results_file': '/root/.ansible_async/3576405980.2284', 'changed': True, 'failed': False, 'item': {'cgroupns_mode': 'host', 'command': '/lib/systemd/systemd', 'hostname': 'ubuntu-22.04', 'image': 'geerlingguy/docker-ubuntu2204-ansible:latest', 'name': 'ubuntu-22.04', 'pre_build_image': True, 'privileged': True, 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup:rw']}, 'ansible_loop_var': 'item'})

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

INFO     Running podman > create

PLAY [Create] ******************************************************************

TASK [get podman executable path] **********************************************
ok: [localhost]

TASK [save path to executable as fact] *****************************************
ok: [localhost]

TASK [Log into a container registry] *******************************************
skipping: [localhost] => (item="ubuntu-22.04 registry username: None specified") 

TASK [Check presence of custom Dockerfiles] ************************************
ok: [localhost] => (item=Dockerfile: None specified)

TASK [Create Dockerfiles from image names] *************************************
skipping: [localhost] => (item="Dockerfile: None specified; Image: geerlingguy/docker-ubuntu2204-ansible:latest") 

TASK [Discover local Podman images] ********************************************
ok: [localhost] => (item=ubuntu-22.04)

TASK [Build an Ansible compatible image] ***************************************
skipping: [localhost] => (item=geerlingguy/docker-ubuntu2204-ansible:latest) 

TASK [Determine the CMD directives] ********************************************
ok: [localhost] => (item="ubuntu-22.04 command: /lib/systemd/systemd")

TASK [Remove possible pre-existing containers] *********************************
changed: [localhost]

TASK [Discover local podman networks] ******************************************
skipping: [localhost] => (item=ubuntu-22.04: None specified) 

TASK [Create podman network dedicated to this scenario] ************************
skipping: [localhost]

TASK [Create molecule instance(s)] *********************************************
changed: [localhost] => (item=ubuntu-22.04)

TASK [Wait for instance(s) creation to complete] *******************************
FAILED - RETRYING: Wait for instance(s) creation to complete (300 retries left).
changed: [localhost] => (item=ubuntu-22.04)

PLAY RECAP *********************************************************************
localhost                  : ok=8    changed=3    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0

INFO     Running podman > converge

PLAY [Converge] ****************************************************************

TASK [Gathering Facts] *********************************************************
ok: [ubuntu-22.04]

TASK [Copy something to test use of synchronize module] ************************
changed: [ubuntu-22.04]

TASK [Include vector-role] *****************************************************

TASK [vector-role : Install vector packages from internet] *********************
changed: [ubuntu-22.04]

TASK [vector-role : Template a config to /etc/vector/vector.toml] **************
changed: [ubuntu-22.04]

RUNNING HANDLER [vector-role : Restart vector service] *************************
changed: [ubuntu-22.04]

PLAY RECAP *********************************************************************
ubuntu-22.04               : ok=5    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

INFO     Running podman > destroy

PLAY [Destroy] *****************************************************************

TASK [Destroy molecule instance(s)] ********************************************
changed: [localhost] => (item={'cgroupns_mode': 'host', 'command': '/lib/systemd/systemd', 'hostname': 'ubuntu-22.04', 'image': 'geerlingguy/docker-ubuntu2204-ansible:latest', 'name': 'ubuntu-22.04', 'pre_build_image': True, 'privileged': True, 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup:rw']})

TASK [Wait for instance(s) deletion to complete] *******************************
FAILED - RETRYING: Wait for instance(s) deletion to complete (300 retries left).
changed: [localhost] => (item={'started': 1, 'finished': 0, 'ansible_job_id': '907715835533.4066', 'results_file': '/root/.ansible_async/907715835533.4066', 'changed': True, 'failed': False, 'item': {'cgroupns_mode': 'host', 'command': '/lib/systemd/systemd', 'hostname': 'ubuntu-22.04', 'image': 'geerlingguy/docker-ubuntu2204-ansible:latest', 'name': 'ubuntu-22.04', 'pre_build_image': True, 'privileged': True, 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup:rw']}, 'ansible_loop_var': 'item'})

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

INFO     Pruning extra files from scenario ephemeral directory
__________________________________________________________________________________ summary ___________________________________________________________________________________
  py37-ansible210: commands succeeded
  py37-ansible30: commands succeeded
  congratulations :)
[root@54d0d51e2ac9 vector-role]#
```

10. Добавьте новый тег на коммит с рабочим сценарием в соответствии с семантическим версионированием.

Ответ: **[1.2.0](https://github.com/fedor-metsger/vector-role/releases/tag/1.2.0)**

После выполнения у вас должно получится два сценария molecule и один tox.ini файл в репозитории. Не забудьте указать в ответе теги решений Tox и Molecule заданий. В качестве решения пришлите ссылку на  ваш репозиторий и скриншоты этапов выполнения задания.

[molecule/default/molecule.yml](https://github.com/fedor-metsger/vector-role/blob/main/molecule/default/molecule.yml)

[molecule/podman/molecule.yml](https://github.com/fedor-metsger/vector-role/blob/main/molecule/podman/molecule.yml)

[tox.ini](https://github.com/fedor-metsger/vector-role/blob/main/tox.ini)


