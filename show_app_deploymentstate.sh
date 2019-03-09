#!/bin/bash
##################################################################################
#
# Desc:		Show the deployed apps for each type
# Autor:	Thomas Fischer <mail@se-di.de>
#
##################################################################################

# define fancy color output
RED=$(tput setaf 1)
BLUE=$(tput setaf 4)
MAGENTA=$(tput setaf 5)
ENDC=$(tput sgr0)


F_COLORS(){
	cat <<EOFCOL

    Colors and types:

        ${BLUE}ansible hosted		The app is hosted on the ansible server (this server)
                                Usually 3rd party apps$ENDC

        ${MAGENTA}git hosted		The app is defined in the central git server
                                Usually your / custom apps$ENDC

        ${RED}DISABLED		Means the app is defined for this target group but
                                the deployment is disabled (therefore the app is not
                                installed on the target)$ENDC

EOFCOL
}

F_USAGE(){
	cat <<_EOUSAGE

    Usage info:

	-h|--help|help		this output
	targetname		a valid target name (group_vars/xxx)
				you can define multiple target names separated by 
				space and the whole list quoted
				e.g. "dmc heavyforwarder"
				if no targetname is given ALL targets are show
	Examples:
	
	$0 deploymentserver	(will show all apps for deploymentserver group)
	$0 			(will show all apps for all groups)
	$0 "deployer dmc"	(will show all apps for both deployer and dmc group)
_EOUSAGE

	F_COLORS
}

# check for calling
case "$1" in
	-h|--help|help)
	F_USAGE
	exit
	;;
	*)
	TARGET="$1"
	;;
esac

F_COLORS

# do the magic
if [ -z "$TARGET" ];then
  echo -e "\nNo specific target group(s) given. Will show all (give me a second..)\n"
    # walk through all var folders,
    # catch all app definition files,
    # check for enabled or disabled state
    # write the list into APPLIST variable
    APPLIST=$(for i in $(ls group_vars/ |grep -v templates);do 
	      echo -e "\nApps configured on $i";
              for a in $(egrep -l '(bundle|git_repo)' group_vars/$i/*);do
	        egrep -ql "(\s+install:\s+[fF]alse)" $a
	        if [ $? -eq 0 ];then
	           echo "$RED${a##*/} (DISABLED)$ENDC"
                else
	          egrep -ql 'bundle' $a 
	          if [ $? -eq 0 ];then
                    echo "$BLUE${a##*/} (ansible hosted)$ENDC"
                  else
                    egrep -ql 'git_repo' $a
                    if [ $? -eq 0 ];then
                       echo "$MAGENTA${a##*/} (git hosted)$ENDC"
		    fi
                  fi
	        fi
	      done
	     done)
else
 echo -e "\nOne or multiple target group(s) given."
 for dir in $TARGET; do
    echo "Processing $dir..."
    if [ -d "group_vars/$dir" ];then
     APPLIST="${APPLIST}\n$(for i in $(ls group_vars/ |grep $dir);do 
              echo -e "\nApps configured on $i";
              for a in $(egrep -l '(bundle|git_repo)' group_vars/$i/*);do
                egrep -ql "(\s+install:\s+[fF]alse)" $a
                if [ $? -eq 0 ];then
                   echo "$RED${a##*/} (DISABLED)$ENDC"
                else
                  egrep -ql 'bundle' $a 
                  if [ $? -eq 0 ];then
                    echo "$BLUE${a##*/} (ansible hosted)$ENDC"
                  else
                    egrep -ql 'git_repo' $a
                    if [ $? -eq 0 ];then
                       echo "$MAGENTA${a##*/} (git hosted)$ENDC"
                    fi
                  fi
                fi
              done
             done)"
    else
      echo -e "\n${RED}**********************************************************\n\nTarget: >group_vars/$dir< does not exists!!!\n\n**********************************************************$ENDC\n"
    fi
  done
fi

# Show the wonderful app list ;-)
echo -e "$APPLIST\n\n"

