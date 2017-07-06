###################################################################
#
# Possible values for group_vars/<targetgroup>/system_local_configs
# 
###################################################################

system_local_configs:
  system:
    remove_absent_files: [True | False]
    * Dangerous setting. This removes unmanaged files on the remote host. 
      unmanaged means: missing Ansible header at the top of the file.
      When you run the system local deployment a header will be placed at the top
      of each file automatically but for those files created in the meantime manually
      <remove_absent_files: True> will remove those manually created ones.
      Default is False.
