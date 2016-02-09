def app_default (app):

   empty_dict = {}

   if type(app) is dict:
     return app
   else:
     return empty_dict

class FilterModule(object):
 def filters(self):
   return {'app_default': app_default}
