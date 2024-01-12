import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from flask import Blueprint
from ckanext.glab.controller import MyLogic


class MyCoolPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IBlueprint)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates/cool_temp')
        toolkit.add_public_directory(config_, 'public/cool_static')

    
    def get_blueprint(self):
        
        blueprint = Blueprint(self.name, self.__module__)        

        blueprint.add_url_rule(
            u'/cool_plugin/do_something',
            u'do_something',
            MyLogic.do_something,
            methods=['GET']
        )

        return blueprint


