Lighthouse
=========

This role installs lighthouse on Ubuntu Linux.

Role Variables
--------------
| Variable Name | Variable Description          |
|---------------|-------------------------------|
| var_http_port | HTTP server port              |
| var_html_root | HTML documents root directory |

Example Playbook
----------------
    - hosts: servers
      roles:
         - { role: lighthouse }

License
-------
MIT

Author Information
------------------
Fedor Metsger