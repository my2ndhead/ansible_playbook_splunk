#############################################################
#
# Possible values for group_vars/all/ansible
# 
############################################################

ansible_conf:
  host: <THE-ANSIBLE-SERVER-NAME | FQDN>
  * Set a name to identify this ansible instance. It will be used in several places e.g. in 
    the deploy_systemconfigs playbook

