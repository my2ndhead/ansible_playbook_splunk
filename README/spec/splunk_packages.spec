########################################################
#
# Possible values for all/splunk_packages group_vars
#
########################################################

splunk_packages:
  linux_64_rpm:
  * 64-bit Linux RPM Packages
  * Optional
    package:
      version: <version>
      * Version Number
      url: <url>
      * Package Source URL
    package:
    ...
    * List of packages

  linux_64_tgz:
  * 64-bit Linux TGZ Packages
  * Optional
    package:
      version: <version>
      * Version Number
      url: <url>
      * Package Source URL
    package:
    ...
    * List of packages
