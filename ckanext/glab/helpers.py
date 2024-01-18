# encoding: utf-8

from ckan.plugins import toolkit
from ckan.plugins.toolkit import _, g, h, get_action


def organisation_list():
    """Returns a list of organisations with all the organisation fields

    :rtype: Array of organisations

    """
    return toolkit.get_action('organization_list')(data_dict={'all_fields': True})


def user_has_admin_access(include_editor_access):
    user = toolkit.c.userobj
    # If user is "None" - they are not logged in.
    if not user:
        return False
    if user.sysadmin:
        return True

    groups_admin = user.get_groups('organization', 'admin')
    groups_editor = user.get_groups('organization', 'editor') if include_editor_access else []
    groups_list = groups_admin + groups_editor
    organisation_list = [g for g in groups_list if g.type == 'organization']
    return len(organisation_list) > 0
