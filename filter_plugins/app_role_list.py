def app_role_list (app):
  
  if "app.template" in app: app.remove("app.template")

  rolepath = 'apps/'

  app=[rolepath + role for role in app]
   
  return app

class FilterModule(object):
 def filters(self):
   return {'app_role_list': app_role_list}
