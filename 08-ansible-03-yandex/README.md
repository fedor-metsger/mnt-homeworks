
# Описание решения домашнего задания 2 «Работа с Playbook»

Playbook находится в файле [site.yml](playbook/site.yml).

Inventory находится в файле [prod.yml](playbook/inventory/prod.yml).

Переменные находятся в файлах:
- [playbook/group_vars/clickhouse/vars.yml](playbook/group_vars/clickhouse/vars.yml)
- [playbook/group_vars/lighthouse/vars.yml](playbook/group_vars/lighthouse/vars.yml)
- [playbook/group_vars/vector/vars.yml](playbook/group_vars/vector/vars.yml)
- [playbook/group_vars/all/vars.yml](playbook/group_vars/all/vars.yml)

Playbook устанавливает сервисы **clickhouse** и **vector**.

Для установки сервиса **clickhouse** с сайта разработчика устанавливаются пакеты:
- clickhouse-common-static
- clickhouse-server
- clickhouse-client

В конфигурационный `/etc/clickhouse-server/config.xml` файл вносится изменение,
с тем, чтобы возможно было осуществлять подключение к **clickhouse с внешних адресов.

После этого создаётся БД **logs**.
Ввиду того, что доступ к СУБД появляется не сразу после запуска сервиса **clickhouse-server**,
попытки создания БД выполняются в цикле, пока не увенчаются успехом.

В заключение в БД **logs** создаётся таблица **logs**, с полями, которые позволяют загружать туда
записи из **syslog**-а:
```
CREATE TABLE IF NOT EXISTS logs.logs (
    apname String,
    facility String,
    hostname String,
    message String,
    msgid String,
    procid Int,
    severity String,
    timestamp String,
    version Int
) ENGINE = MergeTree ORDER BY timestamp;'
```

Для установки сервиса **vector** с сайта разработчика устанавливаются пакеты:
- vector

Затем из шаблона создаётся конфигурационный файл `/etc/vector/vector.toml`,
который содержит набор команд для загрузки данных из **syslog** в БД **clickhouse**.

В качестве веб сервера используется **Apache2**. Он устанавливается с помощью команды **apt**.

В завершение устанавливается **Lighthouse** из репозитория [VKCOM/lighthouse](https://github.com/VKCOM/lighthouse).
К сожалению, в этом репозитории нет версий, поэтому устанавливается **HEAD**.

Playbook использует следующие переменные:

- **clickhouse_version** - требуемая версия **clickhouse**
- **vector_version** - требуемая версия **vector**
- **var_ansible_connection** - тип соединения ansible
- **var_ansible_user** - имя пользователя для соединения по **ssh** протоколу
- **var_ansible_ssh_pass**  - пароль для соединения по **ssh** протоколу
- **var_ansible_ssh_common_args** - параметры подключения по **ssh** протоколу
- **var_ansible_python_interpreter** - имя исполняемого файла интерпретатора **Python**
- **var_clickhouse_host** - IP адрес хоста с **clickhouse**
- **var_lighthouse_host** - IP адрес хоста с **lighthouse**
- **var_vector_host** - IP адрес хоста с **vactor**
- **var_http_port** - порт для конфигурации HTTP сервера
- **var_html_root** - корневой каталог для документов HTTP сервера 


