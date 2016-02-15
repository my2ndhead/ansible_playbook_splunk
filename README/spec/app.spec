############################################
#
# Possible values for apps
# 
############################################

<appname>
* Application Name (Path name)

  [apps|deployment_apps|master_apps|shcluster_apps]:
  * Installation destination
  * Note: Underscore instead of dash/slash needed due to YAML Syntax

    install: <bool>
    * Should the app be installed.
    * Used to uninstall app

    clean_install: <bool>
    * Should the app directory be purged before (re-)installation

    bundle: <filename>
    * The file that contains the app (tar.gz/spl)
    * File must reside unter splunk_repository.repository_root/<appname>/<filename>
 
    git_repo: <url>
    * The path to the git repository

    git_version: <string>
    * The git branch or tag
    * Defaults to "HEAD" if unset

<appname>
...
