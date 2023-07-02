
# Описание решения домашнего задания 2 «Работа с Playbook»

Playbook находится в файле [site.yml](playbook/site.yml).

Inventory находится в файле [prod.yml](playbook/inventory/prod.yml).

Переменные находятся в файле [vars.yml](playbook/group_vars/clickhouse/vars.yml).

Playbook устанавливает сервисы **clickhouse** и **vector**.

Для установки сервиса **clickhouse** с сайта разработчика устанавливаются пакеты:
- clickhouse-common-static
- clickhouse-server
- clickhouse-client

После этого создаётся БД **logs**.
Ввиду того, что доступ к СУБД появляется не сразу после запуска сервиса **clickhouse-server**,
попытки создания БД выполняются в цикле, пока не увенчаются успехом.

Для установки сервиса **vector** с сайта разработчика устанавливаются пакеты:
- vector

Playbook использует следующие переменные:

- **clickhouse_version** - требуемая версия **clickhouse**
- **vector_version** - требуемая версия **vector**


