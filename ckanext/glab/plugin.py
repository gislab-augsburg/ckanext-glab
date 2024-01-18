
# encoding: utf-8

from ckan import plugins
from ckan.plugins import implements, SingletonPlugin
from . import auth_functions as auth, helpers


class GDPR_Plugin(SingletonPlugin):
    """
    Apply custom functions for GDPR conformity.
    ``ITemplateHelpers`` lets us add helper functions for template rendering.
    ``IAuthFunctions`` lets us override authorisation checks.
    """
    implements(plugins.ITemplateHelpers, inherit=True)
    implements(plugins.IAuthFunctions, inherit=True)


    # ITemplateHelpers

    def get_helpers(self):
        """ A dictionary of extra helpers that will be available
        to provide specific helpers to the templates.
        """
        return {
            'data_qld_user_has_admin_access': helpers.user_has_admin_access
        }


    # IAuthFunctions

    def get_auth_functions(self):
        """ Override the some auth functions with our own.
        """
        auth_functions = {
            'user_list': auth.user_list,
            'user_show': auth.user_show,
            'group_show': auth.group_show
        }
        return auth_functions


