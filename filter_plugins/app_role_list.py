def app_role_list (app):
  
  aignore = [ 'app.template','files','tasks','vars' ]
  for lsapp in aignore:
        if lsapp in app: app.remove(lsapp)

  rolepath = 'apps/'

  app=[rolepath + role for role in app]
   
  return app

class FilterModule(object):
 def filters(self):
   return {'app_role_list': app_role_list}
