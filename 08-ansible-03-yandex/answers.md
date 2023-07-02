# Ответы к домашнему заданию 3 «Использование Ansible»

## Основная часть

1. Допишите playbook: нужно сделать ещё один play, который устанавливает и настраивает LightHouse.
2. При создании tasks рекомендую использовать модули: `get_url`, `template`, `yum`, `apt`.
3. Tasks должны: скачать статику LightHouse, установить Nginx или любой другой веб-сервер, настроить его конфиг для открытия LightHouse, запустить веб-сервер.
4. Подготовьте свой inventory-файл `prod.yml`.
```

```
5. Запустите `ansible-lint site.yml` и исправьте ошибки, если они есть.
```
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-03-yandex$ ansible-lint playbook/site.yml
WARNING  Listing 1 violation(s) that are fatal
latest[git]: Result of the command may vary on subsequent runs.
playbook/site.yml:130 Task/Handler: Lighthouse - clone repository

Read documentation for instructions on how to ignore specific rule violations.

             Rule Violation Summary             
 count tag         profile rule associated tags 
     1 latest[git] safety  idempotency          

Failed: 1 failure(s), 0 warning(s) on 1 files. Last profile that met the validation criteria was 'moderate'. Rating: 2/5 star
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-03-yandex$
```
6. Попробуйте запустить playbook на этом окружении с флагом `--check`.
```
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-03-yandex$ ansible-playbook -i ./playbook/inventory/prod.yml ./playbook/site.yml --check 

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

fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-03-yandex$
```
7. Запустите playbook на `prod.yml` окружении с флагом `--diff`. Убедитесь, что изменения на системе произведены.
```
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-03-yandex$ ansible-playbook -i ./playbook/inventory/prod.yml ./playbook/site.yml --diff

PLAY [Install Clickhouse] ****************************************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************************
ok: [clickhouse-01]

TASK [Install clickhouse amd64 packages from internet] ***********************************************************************************************************************
Selecting previously unselected package clickhouse-common-static.
(Reading database ... 71995 files and directories currently installed.)
Preparing to unpack .../clickhouse-common-static_22.3.3.44_amd64lyhf6104.deb ...
Unpacking clickhouse-common-static (22.3.3.44) ...
Setting up clickhouse-common-static (22.3.3.44) ...
changed: [clickhouse-01] => (item=clickhouse-common-static)

TASK [Install clickhouse noarch packages from internet] **********************************************************************************************************************
Selecting previously unselected package clickhouse-client.
(Reading database ... 72009 files and directories currently installed.)
Preparing to unpack .../clickhouse-client_22.3.3.44_all4z2e4tqa.deb ...
Unpacking clickhouse-client (22.3.3.44) ...
Setting up clickhouse-client (22.3.3.44) ...
changed: [clickhouse-01] => (item=clickhouse-client)
Selecting previously unselected package clickhouse-server.
(Reading database ... 72022 files and directories currently installed.)
Preparing to unpack .../clickhouse-server_22.3.3.44_alliedxr06s.deb ...
Unpacking clickhouse-server (22.3.3.44) ...
Setting up clickhouse-server (22.3.3.44) ...
Processing triggers for systemd (245.4-4ubuntu3.20) ...
changed: [clickhouse-01] => (item=clickhouse-server)

TASK [Template a config to /etc/clickhouse-server/config.xml] ****************************************************************************************************************
--- before: /etc/clickhouse-server/config.xml
+++ after: /home/fedor/.ansible/tmp/ansible-local-99683lzrlypos/tmp5fo3eqpg/config.xml
@@ -180,12 +180,12 @@
 
 
     <!-- Same for hosts without support for IPv6: -->
-    <!-- <listen_host>0.0.0.0</listen_host> -->
+    <listen_host>0.0.0.0</listen_host>
 
     <!-- Default values - try listen localhost on IPv4 and IPv6. -->
     <!--
     <listen_host>::1</listen_host>
-    <listen_host>127.0.0.1</listen_host>
+    <listen_host>0.0.0.0</listen_host>
     -->
 
     <!-- Don't exit if IPv6 or IPv4 networks are unavailable while trying to listen. -->

changed: [clickhouse-01]

TASK [Flush handlers] ********************************************************************************************************************************************************

RUNNING HANDLER [Start clickhouse service] ***********************************************************************************************************************************
changed: [clickhouse-01]

TASK [Create database] *******************************************************************************************************************************************************
FAILED - RETRYING: [clickhouse-01]: Create database (10 retries left).
changed: [clickhouse-01]

TASK [Create table] **********************************************************************************************************************************************************
changed: [clickhouse-01]

PLAY [Install Vector] ********************************************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************************
ok: [vector-01]

TASK [Install vector packages from internet] *********************************************************************************************************************************
Selecting previously unselected package vector.
(Reading database ... 71995 files and directories currently installed.)
Preparing to unpack .../vector_0.30.0-1_amd64qkhre5pk.deb ...
Unpacking vector (0.30.0-1) ...
Setting up vector (0.30.0-1) ...
systemd-journal:x:101:
changed: [vector-01]

TASK [Template a config to /etc/vector/vector.toml] **************************************************************************************************************************
--- before: /etc/vector/vector.toml
+++ after: /home/fedor/.ansible/tmp/ansible-local-99683lzrlypos/tmpzizi0246/vector.toml
@@ -1,44 +1,38 @@
-#                                    __   __  __
-#                                    \ \ / / / /
-#                                     \ V / / /
-#                                      \_/  \/
-#
-#                                    V E C T O R
-#                                   Configuration
-#
-# ------------------------------------------------------------------------------
-# Website: https://vector.dev
-# Docs: https://vector.dev/docs
-# Chat: https://chat.vector.dev
-# ------------------------------------------------------------------------------
-
-# Change this to use a non-default directory for Vector data storage:
-# data_dir = "/var/lib/vector"
-
 # Random Syslog-formatted logs
-[sources.dummy_logs]
-type = "demo_logs"
-format = "syslog"
-interval = 1
+[sources.syslog]
+type = "file"
+#type = "demo_logs"
+include = [ "/var/log/syslog" ]
+read_from = "end"
+#format = "syslog"
+#interval = 1
 
 # Parse Syslog logs
 # See the Vector Remap Language reference for more info: https://vrl.dev
-[transforms.parse_logs]
+[transforms.parse_syslog]
 type = "remap"
-inputs = ["dummy_logs"]
+inputs = ["syslog"]
 source = '''
 . = parse_syslog!(string!(.message))
 '''
 
 # Print parsed logs to stdout
-[sinks.print]
-type = "console"
-inputs = ["parse_logs"]
-encoding.codec = "json"
+#[sinks.print]
+#type = "console"
+#inputs = ["parse_logs"]
+#encoding.codec = "json"
 
 # Vector's GraphQL API (disabled by default)
 # Uncomment to try it out with the `vector top` command or
 # in your browser at http://localhost:8686
-#[api]
-#enabled = true
-#address = "127.0.0.1:8686"
+[api]
+enabled = true
+address = "0.0.0.0:8686"
+
+[sinks.clickhouse]
+type = "clickhouse"
+inputs = ["syslog"]
+endpoint = "http://192.168.1.39:8123"
+database = "logs"
+table = "logs"
+skip_unknown_fields = true

changed: [vector-01]

RUNNING HANDLER [Restart vector service] *************************************************************************************************************************************
changed: [vector-01]

PLAY [Install apache2 web server] ********************************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************************
ok: [lighthouse-01]

TASK [Install Apache] ********************************************************************************************************************************************************
The following additional packages will be installed:
  apache2-bin apache2-data apache2-utils libapr1 libaprutil1
  libaprutil1-dbd-sqlite3 libaprutil1-ldap libjansson4 liblua5.2-0 ssl-cert
Suggested packages:
  apache2-doc apache2-suexec-pristine | apache2-suexec-custom www-browser
  openssl-blacklist
The following NEW packages will be installed:
  apache2 apache2-bin apache2-data apache2-utils libapr1 libaprutil1
  libaprutil1-dbd-sqlite3 libaprutil1-ldap libjansson4 liblua5.2-0 ssl-cert
0 upgraded, 11 newly installed, 0 to remove and 84 not upgraded.
changed: [lighthouse-01]

TASK [UFW - Allow HTTP on port 80] *******************************************************************************************************************************************
changed: [lighthouse-01]

PLAY [Install Lighthouse] ****************************************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************************
ok: [lighthouse-01]

TASK [Delete /var/www/html content & directory] ******************************************************************************************************************************
--- before
+++ after
@@ -1,10 +1,4 @@
 {
     "path": "/var/www/html",
-    "path_content": {
-        "directories": [],
-        "files": [
-            "/var/www/html/index.html"
-        ]
-    },
-    "state": "directory"
+    "state": "absent"
 }

changed: [lighthouse-01]

TASK [Lighthouse - clone repository] *****************************************************************************************************************************************
>> Newly checked out d701335c25cd1bb9b5155711190bad8ab852c2ce
changed: [lighthouse-01]

PLAY RECAP *******************************************************************************************************************************************************************
clickhouse-01              : ok=7    changed=6    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
lighthouse-01              : ok=6    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
vector-01                  : ok=4    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-03-yandex$
```
8. Повторно запустите playbook с флагом `--diff` и убедитесь, что playbook идемпотентен.
```
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-03-yandex$ ansible-playbook -i ./playbook/inventory/prod.yml ./playbook/site.yml --diff

PLAY [Install Clickhouse] ****************************************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************************
ok: [clickhouse-01]

TASK [Install clickhouse amd64 packages from internet] ***********************************************************************************************************************
ok: [clickhouse-01] => (item=clickhouse-common-static)

TASK [Install clickhouse noarch packages from internet] **********************************************************************************************************************
ok: [clickhouse-01] => (item=clickhouse-client)
ok: [clickhouse-01] => (item=clickhouse-server)

TASK [Template a config to /etc/clickhouse-server/config.xml] ****************************************************************************************************************
ok: [clickhouse-01]

TASK [Flush handlers] ********************************************************************************************************************************************************

TASK [Create database] *******************************************************************************************************************************************************
ok: [clickhouse-01]

TASK [Create table] **********************************************************************************************************************************************************
changed: [clickhouse-01]

PLAY [Install Vector] ********************************************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************************
ok: [vector-01]

TASK [Install vector packages from internet] *********************************************************************************************************************************
ok: [vector-01]

TASK [Template a config to /etc/vector/vector.toml] **************************************************************************************************************************
ok: [vector-01]

PLAY [Install apache2 web server] ********************************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************************
ok: [lighthouse-01]

TASK [Install Apache] ********************************************************************************************************************************************************
ok: [lighthouse-01]

TASK [UFW - Allow HTTP on port 80] *******************************************************************************************************************************************
ok: [lighthouse-01]

PLAY [Install Lighthouse] ****************************************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************************
ok: [lighthouse-01]

TASK [Delete /var/www/html content & directory] ******************************************************************************************************************************
--- before
+++ after
@@ -1,444 +1,4 @@
 {
     "path": "/var/www/html",
-    "path_content": {
-        "directories": [
-            "/var/www/html/.git",
-            "/var/www/html/img",
-            "/var/www/html/css",
-            "/var/www/html/js",
-            "/var/www/html/.git/objects",
-            "/var/www/html/.git/info",
-            "/var/www/html/.git/refs",
-            "/var/www/html/.git/branches",
-            "/var/www/html/.git/hooks",
-            "/var/www/html/.git/logs",
-            "/var/www/html/.git/objects/info",
-            "/var/www/html/.git/objects/pack",
-            "/var/www/html/.git/refs/tags",
-            "/var/www/html/.git/refs/heads",
-            "/var/www/html/.git/refs/remotes",
-            "/var/www/html/.git/refs/remotes/origin",
-            "/var/www/html/.git/logs/refs",
-            "/var/www/html/.git/logs/refs/heads",
-            "/var/www/html/.git/logs/refs/remotes",
-            "/var/www/html/.git/logs/refs/remotes/origin",
-            "/var/www/html/js/ace-min",
-            "/var/www/html/js/ace-min/snippets"
-        ],
-        "files": [
-            "/var/www/html/app.js",
-            "/var/www/html/LICENSE",
-            "/var/www/html/README.md",
-            "/var/www/html/jquery.js",
-            "/var/www/html/index.html",
-            "/var/www/html/.git/index",
-            "/var/www/html/.git/ORIG_HEAD",
-            "/var/www/html/.git/description",
-            "/var/www/html/.git/config",
-            "/var/www/html/.git/packed-refs",
-            "/var/www/html/.git/HEAD",
-            "/var/www/html/.git/objects/pack/pack-c26c4b039309de105dc44d40161d03d6380410e6.pack",
-            "/var/www/html/.git/objects/pack/pack-c26c4b039309de105dc44d40161d03d6380410e6.idx",
-            "/var/www/html/.git/info/exclude",
-            "/var/www/html/.git/refs/heads/master",
-            "/var/www/html/.git/refs/remotes/origin/HEAD",
-            "/var/www/html/.git/hooks/pre-rebase.sample",
-            "/var/www/html/.git/hooks/commit-msg.sample",
-            "/var/www/html/.git/hooks/applypatch-msg.sample",
-            "/var/www/html/.git/hooks/pre-receive.sample",
-            "/var/www/html/.git/hooks/update.sample",
-            "/var/www/html/.git/hooks/fsmonitor-watchman.sample",
-            "/var/www/html/.git/hooks/pre-applypatch.sample",
-            "/var/www/html/.git/hooks/pre-merge-commit.sample",
-            "/var/www/html/.git/hooks/pre-push.sample",
-            "/var/www/html/.git/hooks/pre-commit.sample",
-            "/var/www/html/.git/hooks/prepare-commit-msg.sample",
-            "/var/www/html/.git/hooks/post-update.sample",
-            "/var/www/html/.git/logs/HEAD",
-            "/var/www/html/.git/logs/refs/heads/master",
-            "/var/www/html/.git/logs/refs/remotes/origin/HEAD",
-            "/var/www/html/img/loading.svg",
-            "/var/www/html/img/glyphicons-halflings.png",
-            "/var/www/html/img/glyphicons-halflings-white.png",
-            "/var/www/html/css/bootstrap.min.css",
-            "/var/www/html/css/bootstrap-responsive.min.css",
-            "/var/www/html/css/bootstrap-responsive.css",
-            "/var/www/html/css/bootstrap.css",
-            "/var/www/html/js/ag-grid.min.js",
-            "/var/www/html/js/bootstrap.js",
-            "/var/www/html/js/bootstrap.min.js",
-            "/var/www/html/js/ace-min/theme-clouds.js",
-            "/var/www/html/js/ace-min/ch_completions_help.js",
-            "/var/www/html/js/ace-min/mode-turtle.js",
-            "/var/www/html/js/ace-min/mode-php.js",
-            "/var/www/html/js/ace-min/mode-haskell.js",
-            "/var/www/html/js/ace-min/theme-textmate.js",
-            "/var/www/html/js/ace-min/theme-sqlserver.js",
-            "/var/www/html/js/ace-min/mode-lua.js",
-            "/var/www/html/js/ace-min/mode-csound_document.js",
-            "/var/www/html/js/ace-min/worker-xquery.js",
-            "/var/www/html/js/ace-min/mode-d.js",
-            "/var/www/html/js/ace-min/mode-coffee.js",
-            "/var/www/html/js/ace-min/mode-haml.js",
-            "/var/www/html/js/ace-min/worker-xml.js",
-            "/var/www/html/js/ace-min/ext-statusbar.js",
-            "/var/www/html/js/ace-min/mode-ruby.js",
-            "/var/www/html/js/ace-min/mode-apache_conf.js",
-            "/var/www/html/js/ace-min/mode-wollok.js",
-            "/var/www/html/js/ace-min/mode-c_cpp.js",
-            "/var/www/html/js/ace-min/mode-logiql.js",
-            "/var/www/html/js/ace-min/mode-latex.js",
-            "/var/www/html/js/ace-min/mode-cirru.js",
-            "/var/www/html/js/ace-min/mode-gherkin.js",
-            "/var/www/html/js/ace-min/mode-tsx.js",
-            "/var/www/html/js/ace-min/mode-julia.js",
-            "/var/www/html/js/ace-min/mode-vbscript.js",
-            "/var/www/html/js/ace-min/mode-golang.js",
-            "/var/www/html/js/ace-min/mode-mushcode.js",
-            "/var/www/html/js/ace-min/ext-error_marker.js",
-            "/var/www/html/js/ace-min/ext-textarea.js",
-            "/var/www/html/js/ace-min/mode-toml.js",
-            "/var/www/html/js/ace-min/mode-livescript.js",
-            "/var/www/html/js/ace-min/mode-razor.js",
-            "/var/www/html/js/ace-min/mode-gobstones.js",
-            "/var/www/html/js/ace-min/mode-abc.js",
-            "/var/www/html/js/ace-min/theme-mono_industrial.js",
-            "/var/www/html/js/ace-min/ext-settings_menu.js",
-            "/var/www/html/js/ace-min/theme-monokai.js",
-            "/var/www/html/js/ace-min/worker-php.js",
-            "/var/www/html/js/ace-min/mode-red.js",
-            "/var/www/html/js/ace-min/mode-erlang.js",
-            "/var/www/html/js/ace-min/keybinding-emacs.js",
-            "/var/www/html/js/ace-min/mode-vala.js",
-            "/var/www/html/js/ace-min/mode-elm.js",
-            "/var/www/html/js/ace-min/mode-graphqlschema.js",
-            "/var/www/html/js/ace-min/ext-split.js",
-            "/var/www/html/js/ace-min/mode-batchfile.js",
-            "/var/www/html/js/ace-min/mode-python.js",
-            "/var/www/html/js/ace-min/mode-nsis.js",
-            "/var/www/html/js/ace-min/mode-pascal.js",
-            "/var/www/html/js/ace-min/mode-pig.js",
-            "/var/www/html/js/ace-min/theme-kuroir.js",
-            "/var/www/html/js/ace-min/theme-twilight.js",
-            "/var/www/html/js/ace-min/mode-tcl.js",
-            "/var/www/html/js/ace-min/mode-matlab.js",
-            "/var/www/html/js/ace-min/theme-chaos.js",
-            "/var/www/html/js/ace-min/ext-options.js",
-            "/var/www/html/js/ace-min/theme-chrome.js",
-            "/var/www/html/js/ace-min/mode-twig.js",
-            "/var/www/html/js/ace-min/mode-sh.js",
-            "/var/www/html/js/ace-min/mode-coldfusion.js",
-            "/var/www/html/js/ace-min/mode-haxe.js",
-            "/var/www/html/js/ace-min/mode-elixir.js",
-            "/var/www/html/js/ace-min/mode-sjs.js",
-            "/var/www/html/js/ace-min/ext-searchbox.js",
-            "/var/www/html/js/ace-min/mode-mask.js",
-            "/var/www/html/js/ace-min/ext-elastic_tabstops_lite.js",
-            "/var/www/html/js/ace-min/ext-linking.js",
-            "/var/www/html/js/ace-min/mode-jade.js",
-            "/var/www/html/js/ace-min/mode-nix.js",
-            "/var/www/html/js/ace-min/mode-csp.js",
-            "/var/www/html/js/ace-min/mode-drools.js",
-            "/var/www/html/js/ace-min/mode-bro.js",
-            "/var/www/html/js/ace-min/mode-tex.js",
-            "/var/www/html/js/ace-min/mode-rust.js",
-            "/var/www/html/js/ace-min/mode-less.js",
-            "/var/www/html/js/ace-min/mode-protobuf.js",
-            "/var/www/html/js/ace-min/worker-lua.js",
-            "/var/www/html/js/ace-min/mode-ada.js",
-            "/var/www/html/js/ace-min/mode-c9search.js",
-            "/var/www/html/js/ace-min/mode-ftl.js",
-            "/var/www/html/js/ace-min/theme-idle_fingers.js",
-            "/var/www/html/js/ace-min/worker-javascript.js",
-            "/var/www/html/js/ace-min/theme-dreamweaver.js",
-            "/var/www/html/js/ace-min/mode-hjson.js",
-            "/var/www/html/js/ace-min/mode-lsl.js",
-            "/var/www/html/js/ace-min/mode-dart.js",
-            "/var/www/html/js/ace-min/ext-keybinding_menu.js",
-            "/var/www/html/js/ace-min/worker-html.js",
-            "/var/www/html/js/ace-min/mode-ejs.js",
-            "/var/www/html/js/ace-min/worker-json.js",
-            "/var/www/html/js/ace-min/ace.js",
-            "/var/www/html/js/ace-min/ext-whitespace.js",
-            "/var/www/html/js/ace-min/mode-mysql.js",
-            "/var/www/html/js/ace-min/mode-jssm.js",
-            "/var/www/html/js/ace-min/theme-dawn.js",
-            "/var/www/html/js/ace-min/mode-csound_score.js",
-            "/var/www/html/js/ace-min/mode-csound_orchestra.js",
-            "/var/www/html/js/ace-min/worker-coffee.js",
-            "/var/www/html/js/ace-min/mode-glsl.js",
-            "/var/www/html/js/ace-min/mode-mixal.js",
-            "/var/www/html/js/ace-min/theme-tomorrow.js",
-            "/var/www/html/js/ace-min/theme-terminal.js",
-            "/var/www/html/js/ace-min/mode-dot.js",
-            "/var/www/html/js/ace-min/theme-vibrant_ink.js",
-            "/var/www/html/js/ace-min/mode-html.js",
-            "/var/www/html/js/ace-min/theme-gob.js",
-            "/var/www/html/js/ace-min/mode-abap.js",
-            "/var/www/html/js/ace-min/ext-static_highlight.js",
-            "/var/www/html/js/ace-min/mode-swift.js",
-            "/var/www/html/js/ace-min/mode-markdown.js",
-            "/var/www/html/js/ace-min/mode-clojure.js",
-            "/var/www/html/js/ace-min/ext-spellcheck.js",
-            "/var/www/html/js/ace-min/ext-emmet.js",
-            "/var/www/html/js/ace-min/mode-autohotkey.js",
-            "/var/www/html/js/ace-min/mode-velocity.js",
-            "/var/www/html/js/ace-min/ext-modelist.js",
-            "/var/www/html/js/ace-min/mode-stylus.js",
-            "/var/www/html/js/ace-min/mode-json.js",
-            "/var/www/html/js/ace-min/mode-css.js",
-            "/var/www/html/js/ace-min/mode-xquery.js",
-            "/var/www/html/js/ace-min/theme-merbivore.js",
-            "/var/www/html/js/ace-min/mode-jack.js",
-            "/var/www/html/js/ace-min/mode-scss.js",
-            "/var/www/html/js/ace-min/theme-tomorrow_night.js",
-            "/var/www/html/js/ace-min/clickhouse_highlight_rules.js",
-            "/var/www/html/js/ace-min/mode-soy_template.js",
-            "/var/www/html/js/ace-min/mode-gcode.js",
-            "/var/www/html/js/ace-min/ext-beautify.js",
-            "/var/www/html/js/ace-min/mode-liquid.js",
-            "/var/www/html/js/ace-min/mode-django.js",
-            "/var/www/html/js/ace-min/theme-pastel_on_dark.js",
-            "/var/www/html/js/ace-min/mode-java.js",
-            "/var/www/html/js/ace-min/mode-javascript.js",
-            "/var/www/html/js/ace-min/theme-katzenmilch.js",
-            "/var/www/html/js/ace-min/mode-typescript.js",
-            "/var/www/html/js/ace-min/mode-eiffel.js",
-            "/var/www/html/js/ace-min/theme-solarized_light.js",
-            "/var/www/html/js/ace-min/mode-snippets.js",
-            "/var/www/html/js/ace-min/theme-xcode.js",
-            "/var/www/html/js/ace-min/theme-merbivore_soft.js",
-            "/var/www/html/js/ace-min/mode-assembly_x86.js",
-            "/var/www/html/js/ace-min/theme-gruvbox.js",
-            "/var/www/html/js/ace-min/mode-scheme.js",
-            "/var/www/html/js/ace-min/mode-edifact.js",
-            "/var/www/html/js/ace-min/mode-rdoc.js",
-            "/var/www/html/js/ace-min/theme-eclipse.js",
-            "/var/www/html/js/ace-min/theme-dracula.js",
-            "/var/www/html/js/ace-min/theme-tomorrow_night_eighties.js",
-            "/var/www/html/js/ace-min/mode-csharp.js",
-            "/var/www/html/js/ace-min/mode-maze.js",
-            "/var/www/html/js/ace-min/mode-xml.js",
-            "/var/www/html/js/ace-min/theme-cobalt.js",
-            "/var/www/html/js/ace-min/mode-clickhouse.js",
-            "/var/www/html/js/ace-min/mode-textile.js",
-            "/var/www/html/js/ace-min/theme-ambiance.js",
-            "/var/www/html/js/ace-min/mode-jsp.js",
-            "/var/www/html/js/ace-min/mode-lucene.js",
-            "/var/www/html/js/ace-min/mode-text.js",
-            "/var/www/html/js/ace-min/mode-sql.js",
-            "/var/www/html/js/ace-min/theme-github.js",
-            "/var/www/html/js/ace-min/mode-ini.js",
-            "/var/www/html/js/ace-min/mode-verilog.js",
-            "/var/www/html/js/ace-min/mode-yaml.js",
-            "/var/www/html/js/ace-min/mode-html_elixir.js",
-            "/var/www/html/js/ace-min/mode-html_ruby.js",
-            "/var/www/html/js/ace-min/theme-iplastic.js",
-            "/var/www/html/js/ace-min/mode-fortran.js",
-            "/var/www/html/js/ace-min/mode-powershell.js",
-            "/var/www/html/js/ace-min/mode-mel.js",
-            "/var/www/html/js/ace-min/mode-space.js",
-            "/var/www/html/js/ace-min/mode-makefile.js",
-            "/var/www/html/js/ace-min/mode-pgsql.js",
-            "/var/www/html/js/ace-min/mode-sass.js",
-            "/var/www/html/js/ace-min/mode-properties.js",
-            "/var/www/html/js/ace-min/mode-plain_text.js",
-            "/var/www/html/js/ace-min/mode-smarty.js",
-            "/var/www/html/js/ace-min/theme-crimson_editor.js",
-            "/var/www/html/js/ace-min/mode-scad.js",
-            "/var/www/html/js/ace-min/keybinding-vim.js",
-            "/var/www/html/js/ace-min/mode-prolog.js",
-            "/var/www/html/js/ace-min/mode-kotlin.js",
-            "/var/www/html/js/ace-min/mode-cobol.js",
-            "/var/www/html/js/ace-min/worker-css.js",
-            "/var/www/html/js/ace-min/mode-scala.js",
-            "/var/www/html/js/ace-min/mode-vhdl.js",
-            "/var/www/html/js/ace-min/mode-praat.js",
-            "/var/www/html/js/ace-min/mode-dockerfile.js",
-            "/var/www/html/js/ace-min/mode-rst.js",
-            "/var/www/html/js/ace-min/theme-solarized_dark.js",
-            "/var/www/html/js/ace-min/mode-objectivec.js",
-            "/var/www/html/js/ace-min/mode-handlebars.js",
-            "/var/www/html/js/ace-min/mode-r.js",
-            "/var/www/html/js/ace-min/mode-forth.js",
-            "/var/www/html/js/ace-min/theme-clouds_midnight.js",
-            "/var/www/html/js/ace-min/mode-lisp.js",
-            "/var/www/html/js/ace-min/mode-perl.js",
-            "/var/www/html/js/ace-min/mode-jsoniq.js",
-            "/var/www/html/js/ace-min/mode-haskell_cabal.js",
-            "/var/www/html/js/ace-min/mode-sparql.js",
-            "/var/www/html/js/ace-min/mode-applescript.js",
-            "/var/www/html/js/ace-min/mode-groovy.js",
-            "/var/www/html/js/ace-min/mode-ocaml.js",
-            "/var/www/html/js/ace-min/mode-luapage.js",
-            "/var/www/html/js/ace-min/ext-language_tools.js",
-            "/var/www/html/js/ace-min/theme-tomorrow_night_blue.js",
-            "/var/www/html/js/ace-min/mode-rhtml.js",
-            "/var/www/html/js/ace-min/ext-themelist.js",
-            "/var/www/html/js/ace-min/mode-curly.js",
-            "/var/www/html/js/ace-min/mode-actionscript.js",
-            "/var/www/html/js/ace-min/mode-sqlserver.js",
-            "/var/www/html/js/ace-min/theme-tomorrow_night_bright.js",
-            "/var/www/html/js/ace-min/mode-io.js",
-            "/var/www/html/js/ace-min/mode-jsx.js",
-            "/var/www/html/js/ace-min/mode-diff.js",
-            "/var/www/html/js/ace-min/mode-redshift.js",
-            "/var/www/html/js/ace-min/theme-kr_theme.js",
-            "/var/www/html/js/ace-min/mode-svg.js",
-            "/var/www/html/js/ace-min/mode-asciidoc.js",
-            "/var/www/html/js/ace-min/mode-gitignore.js",
-            "/var/www/html/js/ace-min/snippets/csharp.js",
-            "/var/www/html/js/ace-min/snippets/lisp.js",
-            "/var/www/html/js/ace-min/snippets/dockerfile.js",
-            "/var/www/html/js/ace-min/snippets/jade.js",
-            "/var/www/html/js/ace-min/snippets/red.js",
-            "/var/www/html/js/ace-min/snippets/groovy.js",
-            "/var/www/html/js/ace-min/snippets/edifact.js",
-            "/var/www/html/js/ace-min/snippets/swift.js",
-            "/var/www/html/js/ace-min/snippets/xquery.js",
-            "/var/www/html/js/ace-min/snippets/smarty.js",
-            "/var/www/html/js/ace-min/snippets/graphqlschema.js",
-            "/var/www/html/js/ace-min/snippets/luapage.js",
-            "/var/www/html/js/ace-min/snippets/csound_score.js",
-            "/var/www/html/js/ace-min/snippets/elixir.js",
-            "/var/www/html/js/ace-min/snippets/css.js",
-            "/var/www/html/js/ace-min/snippets/coldfusion.js",
-            "/var/www/html/js/ace-min/snippets/razor.js",
-            "/var/www/html/js/ace-min/snippets/mixal.js",
-            "/var/www/html/js/ace-min/snippets/r.js",
-            "/var/www/html/js/ace-min/snippets/c_cpp.js",
-            "/var/www/html/js/ace-min/snippets/lucene.js",
-            "/var/www/html/js/ace-min/snippets/io.js",
-            "/var/www/html/js/ace-min/snippets/cirru.js",
-            "/var/www/html/js/ace-min/snippets/glsl.js",
-            "/var/www/html/js/ace-min/snippets/jsoniq.js",
-            "/var/www/html/js/ace-min/snippets/plain_text.js",
-            "/var/www/html/js/ace-min/snippets/c9search.js",
-            "/var/www/html/js/ace-min/snippets/scheme.js",
-            "/var/www/html/js/ace-min/snippets/haxe.js",
-            "/var/www/html/js/ace-min/snippets/matlab.js",
-            "/var/www/html/js/ace-min/snippets/snippets.js",
-            "/var/www/html/js/ace-min/snippets/erlang.js",
-            "/var/www/html/js/ace-min/snippets/sql.js",
-            "/var/www/html/js/ace-min/snippets/textile.js",
-            "/var/www/html/js/ace-min/snippets/haskell.js",
-            "/var/www/html/js/ace-min/snippets/praat.js",
-            "/var/www/html/js/ace-min/snippets/vala.js",
-            "/var/www/html/js/ace-min/snippets/sh.js",
-            "/var/www/html/js/ace-min/snippets/redshift.js",
-            "/var/www/html/js/ace-min/snippets/drools.js",
-            "/var/www/html/js/ace-min/snippets/forth.js",
-            "/var/www/html/js/ace-min/snippets/xml.js",
-            "/var/www/html/js/ace-min/snippets/liquid.js",
-            "/var/www/html/js/ace-min/snippets/wollok.js",
-            "/var/www/html/js/ace-min/snippets/ini.js",
-            "/var/www/html/js/ace-min/snippets/pascal.js",
-            "/var/www/html/js/ace-min/snippets/eiffel.js",
-            "/var/www/html/js/ace-min/snippets/gobstones.js",
-            "/var/www/html/js/ace-min/snippets/lua.js",
-            "/var/www/html/js/ace-min/snippets/jack.js",
-            "/var/www/html/js/ace-min/snippets/yaml.js",
-            "/var/www/html/js/ace-min/snippets/vhdl.js",
-            "/var/www/html/js/ace-min/snippets/jssm.js",
-            "/var/www/html/js/ace-min/snippets/pig.js",
-            "/var/www/html/js/ace-min/snippets/html_elixir.js",
-            "/var/www/html/js/ace-min/snippets/sqlserver.js",
-            "/var/www/html/js/ace-min/snippets/rust.js",
-            "/var/www/html/js/ace-min/snippets/rdoc.js",
-            "/var/www/html/js/ace-min/snippets/sass.js",
-            "/var/www/html/js/ace-min/snippets/lsl.js",
-            "/var/www/html/js/ace-min/snippets/abc.js",
-            "/var/www/html/js/ace-min/snippets/nsis.js",
-            "/var/www/html/js/ace-min/snippets/actionscript.js",
-            "/var/www/html/js/ace-min/snippets/stylus.js",
-            "/var/www/html/js/ace-min/snippets/html.js",
-            "/var/www/html/js/ace-min/snippets/golang.js",
-            "/var/www/html/js/ace-min/snippets/less.js",
-            "/var/www/html/js/ace-min/snippets/svg.js",
-            "/var/www/html/js/ace-min/snippets/gcode.js",
-            "/var/www/html/js/ace-min/snippets/makefile.js",
-            "/var/www/html/js/ace-min/snippets/turtle.js",
-            "/var/www/html/js/ace-min/snippets/coffee.js",
-            "/var/www/html/js/ace-min/snippets/markdown.js",
-            "/var/www/html/js/ace-min/snippets/verilog.js",
-            "/var/www/html/js/ace-min/snippets/json.js",
-            "/var/www/html/js/ace-min/snippets/toml.js",
-            "/var/www/html/js/ace-min/snippets/scala.js",
-            "/var/www/html/js/ace-min/snippets/vbscript.js",
-            "/var/www/html/js/ace-min/snippets/python.js",
-            "/var/www/html/js/ace-min/snippets/d.js",
-            "/var/www/html/js/ace-min/snippets/tex.js",
-            "/var/www/html/js/ace-min/snippets/kotlin.js",
-            "/var/www/html/js/ace-min/snippets/dart.js",
-            "/var/www/html/js/ace-min/snippets/batchfile.js",
-            "/var/www/html/js/ace-min/snippets/jsp.js",
-            "/var/www/html/js/ace-min/snippets/csound_orchestra.js",
-            "/var/www/html/js/ace-min/snippets/sjs.js",
-            "/var/www/html/js/ace-min/snippets/clojure.js",
-            "/var/www/html/js/ace-min/snippets/objectivec.js",
-            "/var/www/html/js/ace-min/snippets/rhtml.js",
-            "/var/www/html/js/ace-min/snippets/perl.js",
-            "/var/www/html/js/ace-min/snippets/latex.js",
-            "/var/www/html/js/ace-min/snippets/asciidoc.js",
-            "/var/www/html/js/ace-min/snippets/php.js",
-            "/var/www/html/js/ace-min/snippets/bro.js",
-            "/var/www/html/js/ace-min/snippets/ruby.js",
-            "/var/www/html/js/ace-min/snippets/haml.js",
-            "/var/www/html/js/ace-min/snippets/mushcode.js",
-            "/var/www/html/js/ace-min/snippets/haskell_cabal.js",
-            "/var/www/html/js/ace-min/snippets/mysql.js",
-            "/var/www/html/js/ace-min/snippets/abap.js",
-            "/var/www/html/js/ace-min/snippets/tsx.js",
-            "/var/www/html/js/ace-min/snippets/ejs.js",
-            "/var/www/html/js/ace-min/snippets/dot.js",
-            "/var/www/html/js/ace-min/snippets/mel.js",
-            "/var/www/html/js/ace-min/snippets/maze.js",
-            "/var/www/html/js/ace-min/snippets/typescript.js",
-            "/var/www/html/js/ace-min/snippets/applescript.js",
-            "/var/www/html/js/ace-min/snippets/soy_template.js",
-            "/var/www/html/js/ace-min/snippets/ocaml.js",
-            "/var/www/html/js/ace-min/snippets/jsx.js",
-            "/var/www/html/js/ace-min/snippets/julia.js",
-            "/var/www/html/js/ace-min/snippets/html_ruby.js",
-            "/var/www/html/js/ace-min/snippets/java.js",
-            "/var/www/html/js/ace-min/snippets/twig.js",
-            "/var/www/html/js/ace-min/snippets/diff.js",
-            "/var/www/html/js/ace-min/snippets/elm.js",
-            "/var/www/html/js/ace-min/snippets/prolog.js",
-            "/var/www/html/js/ace-min/snippets/rst.js",
-            "/var/www/html/js/ace-min/snippets/curly.js",
-            "/var/www/html/js/ace-min/snippets/properties.js",
-            "/var/www/html/js/ace-min/snippets/sparql.js",
-            "/var/www/html/js/ace-min/snippets/javascript.js",
-            "/var/www/html/js/ace-min/snippets/assembly_x86.js",
-            "/var/www/html/js/ace-min/snippets/logiql.js",
-            "/var/www/html/js/ace-min/snippets/ftl.js",
-            "/var/www/html/js/ace-min/snippets/pgsql.js",
-            "/var/www/html/js/ace-min/snippets/mask.js",
-            "/var/www/html/js/ace-min/snippets/clickhouse.js",
-            "/var/www/html/js/ace-min/snippets/text.js",
-            "/var/www/html/js/ace-min/snippets/gitignore.js",
-            "/var/www/html/js/ace-min/snippets/cobol.js",
-            "/var/www/html/js/ace-min/snippets/ada.js",
-            "/var/www/html/js/ace-min/snippets/autohotkey.js",
-            "/var/www/html/js/ace-min/snippets/nix.js",
-            "/var/www/html/js/ace-min/snippets/powershell.js",
-            "/var/www/html/js/ace-min/snippets/scss.js",
-            "/var/www/html/js/ace-min/snippets/scad.js",
-            "/var/www/html/js/ace-min/snippets/hjson.js",
-            "/var/www/html/js/ace-min/snippets/csp.js",
-            "/var/www/html/js/ace-min/snippets/csound_document.js",
-            "/var/www/html/js/ace-min/snippets/django.js",
-            "/var/www/html/js/ace-min/snippets/handlebars.js",
-            "/var/www/html/js/ace-min/snippets/gherkin.js",
-            "/var/www/html/js/ace-min/snippets/tcl.js",
-            "/var/www/html/js/ace-min/snippets/fortran.js",
-            "/var/www/html/js/ace-min/snippets/space.js",
-            "/var/www/html/js/ace-min/snippets/protobuf.js",
-            "/var/www/html/js/ace-min/snippets/livescript.js",
-            "/var/www/html/js/ace-min/snippets/apache_conf.js",
-            "/var/www/html/js/ace-min/snippets/velocity.js"
-        ]
-    },
-    "state": "directory"
+    "state": "absent"
 }

changed: [lighthouse-01]

TASK [Lighthouse - clone repository] *****************************************************************************************************************************************
>> Newly checked out d701335c25cd1bb9b5155711190bad8ab852c2ce
changed: [lighthouse-01]

PLAY RECAP *******************************************************************************************************************************************************************
clickhouse-01              : ok=6    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
lighthouse-01              : ok=6    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
vector-01                  : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/08-ansible-03-yandex$
```
9. Подготовьте README.md-файл по своему playbook. В нём должно быть описано: что делает playbook, какие у него есть параметры и теги.

Ответ: [README.md](README.md)

10. Готовый playbook выложите в свой репозиторий, поставьте тег `08-ansible-03-yandex` на фиксирующий коммит, в ответ предоставьте ссылку на него.

---

### Как оформить решение задания

Выполненное домашнее задание пришлите в виде ссылки на .md-файл в вашем репозитории.

---
