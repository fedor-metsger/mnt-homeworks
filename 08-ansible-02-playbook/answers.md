# Ответы к домашнему заданию 2 «Работа с Playbook»

## Основная часть

1. Подготовьте свой inventory-файл `prod.yml`.
```
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-02-playbook/playbook/inventory$ cat prod.yml 
---
clickhouse:
  hosts:
    clickhouse-01:
      ansible_host: 192.168.0.5
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-02-playbook/playbook/inventory$
```
2. Допишите playbook: нужно сделать ещё один play, который устанавливает и настраивает [vector](https://vector.dev).
3. При создании tasks рекомендую использовать модули: `get_url`, `template`, `unarchive`, `file`.
4. Tasks должны: скачать дистрибутив нужной версии, выполнить распаковку в выбранную директорию, установить vector.

Ответ: [site.yml](playbook/site.yml)
```
---
- name: Install Clickhouse
  hosts: clickhouse
  handlers:
    - name: Start clickhouse service
      ansible.builtin.systemd:
        name: clickhouse-server
        state: started
        enabled: true
      become: true
      become_user: root
  tasks:
    - name: Install clickhouse amd64 packages from internet
      become: true
      become_user: root
      ansible.builtin.apt:
        deb: "https://packages.clickhouse.com/deb/pool/main/c/clickhouse-common-static/clickhouse-common-static_{{ clickhouse_version }}_amd64.deb"
      with_items: "{{ clickhouse_amd64_packages }}"
      notify: Start clickhouse service
    - name: Install clickhouse noarch packages from internet
      become: true
      become_user: root
      ansible.builtin.apt:
        deb: "https://packages.clickhouse.com/deb/pool/main/c/{{ item }}/{{ item }}_{{ clickhouse_version }}_all.deb"
      with_items: "{{ clickhouse_noarch_packages }}"
      notify: Start clickhouse service
    - name: Flush handlers
      ansible.builtin.meta: flush_handlers
    - name: Create database
      ansible.builtin.command: "clickhouse-client -q 'create database logs;'"
      register: create_db
      failed_when: create_db.rc != 0 and create_db.rc != 82
      changed_when: create_db.rc == 0
      retries: 10
      delay: 3
      until: create_db.rc == 0 or create_db.rc == 82
- name: Install Vector
  hosts: clickhouse
  handlers:
    - name: Start vector service
      ansible.builtin.systemd:
        name: vector
        state: started
        enabled: true
      become: true
      become_user: root
  tasks:
    - name: Install vector packages from internet
      become: true
      become_user: root
      ansible.builtin.apt:
        deb: "https://packages.timber.io/vector/{{ vector_version }}/vector_{{ vector_version }}-1_amd64.deb"
      notify: Start vector service
    - name: Flush handlers
      ansible.builtin.meta: flush_handlers
```
5. Запустите `ansible-lint site.yml` и исправьте ошибки, если они есть.
```
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-02-playbook$ ansible-lint playbook/site.yml

Passed: 0 failure(s), 0 warning(s) on 1 files. Last profile that met the validation criteria was 'production'.
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-02-playbook$
```
6. Попробуйте запустить playbook на этом окружении с флагом `--check`.
```
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-02-playbook$ ansible-playbook -i ./playbook/inventory/prod.yml ./playbook/site.yml --check

PLAY [Install Clickhouse] ****************************************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************************
ok: [clickhouse-01]

TASK [Install clickhouse amd64 packages from internet] ***********************************************************************************************************************
changed: [clickhouse-01] => (item=clickhouse-common-static)

TASK [Install clickhouse noarch packages from internet] **********************************************************************************************************************
failed: [clickhouse-01] (item=clickhouse-client) => {"ansible_loop_var": "item", "changed": false, "item": "clickhouse-client", "msg": "Dependency is not satisfiable: clickhouse-common-static (= 22.3.3.44)\n"}
failed: [clickhouse-01] (item=clickhouse-server) => {"ansible_loop_var": "item", "changed": false, "item": "clickhouse-server", "msg": "Dependency is not satisfiable: clickhouse-common-static (= 22.3.3.44)\n"}

PLAY RECAP *******************************************************************************************************************************************************************
clickhouse-01              : ok=2    changed=1    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0   

fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-02-playbook$
```
7. Запустите playbook на `prod.yml` окружении с флагом `--diff`. Убедитесь, что изменения на системе произведены.
```
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-02-playbook$ ansible-playbook -i ./playbook/inventory/prod.yml ./playbook/site.yml --diff

PLAY [Install Clickhouse] ****************************************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************************
ok: [clickhouse-01]

TASK [Install clickhouse amd64 packages from internet] ***********************************************************************************************************************
Selecting previously unselected package clickhouse-common-static.
(Reading database ... 72003 files and directories currently installed.)
Preparing to unpack .../clickhouse-common-static_22.3.3.44_amd64ij3070bx.deb ...
Unpacking clickhouse-common-static (22.3.3.44) ...
Setting up clickhouse-common-static (22.3.3.44) ...
changed: [clickhouse-01] => (item=clickhouse-common-static)

TASK [Install clickhouse noarch packages from internet] **********************************************************************************************************************
Selecting previously unselected package clickhouse-client.
(Reading database ... 72017 files and directories currently installed.)
Preparing to unpack .../clickhouse-client_22.3.3.44_allqa7wvgow.deb ...
Unpacking clickhouse-client (22.3.3.44) ...
Setting up clickhouse-client (22.3.3.44) ...
changed: [clickhouse-01] => (item=clickhouse-client)
Selecting previously unselected package clickhouse-server.
(Reading database ... 72028 files and directories currently installed.)
Preparing to unpack .../clickhouse-server_22.3.3.44_allkg4jimez.deb ...
Unpacking clickhouse-server (22.3.3.44) ...
Setting up clickhouse-server (22.3.3.44) ...
Processing triggers for systemd (245.4-4ubuntu3.20) ...
changed: [clickhouse-01] => (item=clickhouse-server)

TASK [Flush handlers] ********************************************************************************************************************************************************

RUNNING HANDLER [Start clickhouse service] ***********************************************************************************************************************************
changed: [clickhouse-01]

TASK [Create database] *******************************************************************************************************************************************************
FAILED - RETRYING: [clickhouse-01]: Create database (10 retries left).
ok: [clickhouse-01]

PLAY [Install Vector] ********************************************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************************
ok: [clickhouse-01]

TASK [Install vector packages from internet] *********************************************************************************************************************************
Selecting previously unselected package vector.
(Reading database ... 72039 files and directories currently installed.)
Preparing to unpack .../vector_0.30.0-1_amd64kmtlkiz6.deb ...
Unpacking vector (0.30.0-1) ...
Setting up vector (0.30.0-1) ...
systemd-journal:x:101:vector
changed: [clickhouse-01]

TASK [Flush handlers] ********************************************************************************************************************************************************

RUNNING HANDLER [Start vector service] ***************************************************************************************************************************************
changed: [clickhouse-01]

PLAY RECAP *******************************************************************************************************************************************************************
clickhouse-01              : ok=8    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-02-playbook$
```
8. Повторно запустите playbook с флагом `--diff` и убедитесь, что playbook идемпотентен.
```
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-02-playbook$ ansible-playbook -i ./playbook/inventory/prod.yml ./playbook/site.yml --diff

PLAY [Install Clickhouse] ****************************************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************************
ok: [clickhouse-01]

TASK [Install clickhouse amd64 packages from internet] ***********************************************************************************************************************
ok: [clickhouse-01] => (item=clickhouse-common-static)

TASK [Install clickhouse noarch packages from internet] **********************************************************************************************************************
ok: [clickhouse-01] => (item=clickhouse-client)
ok: [clickhouse-01] => (item=clickhouse-server)

TASK [Flush handlers] ********************************************************************************************************************************************************

TASK [Create database] *******************************************************************************************************************************************************
ok: [clickhouse-01]

PLAY [Install Vector] ********************************************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************************
ok: [clickhouse-01]

TASK [Install vector packages from internet] *********************************************************************************************************************************
ok: [clickhouse-01]

TASK [Flush handlers] ********************************************************************************************************************************************************

PLAY RECAP *******************************************************************************************************************************************************************
clickhouse-01              : ok=6    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-02-playbook$
```
9. Подготовьте README.md-файл по своему playbook. В нём должно быть описано: что делает playbook, какие у него есть параметры и теги.
10. Готовый playbook выложите в свой репозиторий, поставьте тег `08-ansible-02-playbook` на фиксирующий коммит, в ответ предоставьте ссылку на него.

---

### Как оформить решение задания

Выполненное домашнее задание пришлите в виде ссылки на .md-файл в вашем репозитории.

---
