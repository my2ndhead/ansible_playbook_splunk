############################################
#
# Possible values for conf/distsearch role
# 
# Follows Splunk distsearch.conf.spec closely
#
############################################

splunk_distsearch_conf:
  distributedSearch:
    disabled: [True | False]
    * Defaults to false
  server: 
    - "{{ groups['<groupname1>'] }}"
    - "{{ groups['<groupname2>'] }}"
    - ...
    - "{{ groups['<groupnameN>'] }}"
   * List of inventory groups used for distributed search
