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
5. Создайте облегчённый сценарий для `molecule` с драйвером `molecule_podman`. Проверьте его на исполнимость.
6. Пропишите правильную команду в `tox.ini`, чтобы запускался облегчённый сценарий.
8. Запустите команду `tox`. Убедитесь, что всё отработало успешно.
9. Добавьте новый тег на коммит с рабочим сценарием в соответствии с семантическим версионированием.

После выполнения у вас должно получится два сценария molecule и один tox.ini файл в репозитории. Не забудьте указать в ответе теги решений Tox и Molecule заданий. В качестве решения пришлите ссылку на  ваш репозиторий и скриншоты этапов выполнения задания. 

