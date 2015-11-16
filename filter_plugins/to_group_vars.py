from ansible import errors, runner
import json

def to_group_vars(host_vars, groups, target = 'all'):
    if type(host_vars) != runner.HostVars:
        raise errors.AnsibleFilterError("|failed expects a HostVars")

    if type(groups) != dict:
        raise errors.AnsibleFilterError("|failed expects a Dictionary")

    data = []
    for host in groups[target]:
        data.append(host_vars[host])
    return data

class FilterModule (object):
    def filters(self):
        return {"to_group_vars": to_group_vars}
