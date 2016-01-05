########################################################
#
# Possible values for all/splunk_installation group_vars
#
########################################################

splunk_installation:
  splunk_home_path: 
  * Mandatory
  * Typically /opt/splunk

  version: <version>
  * Optional / Not used yet
  * Version number to be installed

  ssh_public_key: <string>
  * Optional
  * The SSH public key Ansible uses to connect to Splunk hosts

  package_format: [rpm|tgz]
  * Mandatory
  * The package format used to install Splunk

  package_file: <filename> 
  * Mandatory
  * The file name of the Splunk package. Files has to exist in <splunk_repository>/packages

  remote_package_temp_path: <path>
  * Mandatory
  * The path where Ansible copies the Splunk package to
  * Typcially /tmp

  delete_package_after_install: <boolean>
  * Mandatory
  * Should the remote Splunk Packages be deleted after installation

  remote_app_temp_path: <path>
  * Mandatory
  * The path where Ansible copies the apps to
  * Typically /tmp
 
  admin_password: <string>
  * Mandatory
  * The Splunk admin password in cleartext
  * Use Ansible Vault to keep this protected

  splunk_secret: <string>
  * Mandatory
  * The splunk.secret in cleartext
  * Use Ansible Vault to keep this protected
  
  firewalld_open_port:
    port: "<portnumber1>/tcp"
    port: "<portnumber2>/tcp"
    ... 
    port: "<portnumberN>/tcp"
  * Optional
  * List of ports to open, if firewalld is used.
