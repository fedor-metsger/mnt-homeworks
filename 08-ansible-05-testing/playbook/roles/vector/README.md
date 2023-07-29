Vector
=========

This role installs Vector on Ubuntu Linux.

Role Variables
--------------
| Variable Name | Variable Description      |
|---------------|---------------------------|
|vector_version| Vector version to install |

Example Playbook
----------------
    - hosts: servers
      roles:
         - { role: vector }

License
-------
MIT

Author Information
------------------
Fedor Metsger