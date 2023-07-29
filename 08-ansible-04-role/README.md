# Ответы к домашнему заданию 4 «Работа с roles»

## Основная часть


1. Создайте в старой версии playbook файл `requirements.yml` и заполните его содержимым:

   ```yaml
   ---
     - src: git@github.com:AlexeySetevoi/ansible-clickhouse.git
       scm: git
       version: "1.11.0"
       name: clickhouse 
   ```
   
Ответ: [requirements.yml](playbook/requirements.yml)

2. При помощи `ansible-galaxy` скачайте себе эту роль.

Ответ: [clickhouse](playbook/roles/clickhouse)

3. Создайте новый каталог с ролью при помощи `ansible-galaxy role init vector-role`.
4. На основе tasks из старого playbook заполните новую role. Разнесите переменные между `vars` и `default`. 
5. Перенести нужные шаблоны конфигов в `templates`.
6. Опишите в `README.md` обе роли и их параметры.

Ответ: [vector-role](https://github.com/fedor-metsger/vector-role)

7. Повторите шаги 3–6 для LightHouse. Помните, что одна роль должна настраивать один продукт.

Ответ: [lighthouse-role](https://github.com/fedor-metsger/lighthouse-role)

8. Выложите все roles в репозитории. Проставьте теги, используя семантическую нумерацию. Добавьте roles в `requirements.yml` в playbook.

Ответ: [requirements.yml](playbook/requirements.yml)

9. Переработайте playbook на использование roles. Не забудьте про зависимости LightHouse и возможности совмещения `roles` с `tasks`.

Ответ: [site.yml](playbook/site.yml)

10. Выложите playbook в репозиторий.
11. В ответе дайте ссылки на оба репозитория с roles и одну ссылку на репозиторий с playbook.

Ответ:
- [playbook](https://github.com/fedor-metsger/mnt-homeworks/tree/master/08-ansible-04-role/playbook)
- [lighthouse-role](https://github.com/fedor-metsger/lighthouse-role)
- [vector-role](https://github.com/fedor-metsger/vector-role)
