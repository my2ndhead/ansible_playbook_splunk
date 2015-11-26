def create_shcluster_mgmt_uri_servers (serverlist):

  servers_normalized = []

  for item in serverlist:
   if type(item) is str:
     item=[item]
   for sublist in item:
     servers_normalized.append(sublist)

  servers = []
  [servers.append(item) for item in servers_normalized if item not in servers]


  servers = ["https://"+server+":8089" for server in servers ]
  servers = ','.join(servers)
  return servers

class FilterModule(object):
 def filters(self):
   return {'create_shcluster_mgmt_uri_servers': create_shcluster_mgmt_uri_servers}
