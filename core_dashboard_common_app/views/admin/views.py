"""
    Views available for the user
"""

import copy

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy

import core_main_app.components.data.api as workspace_data_api
import core_main_app.components.workspace.api as workspace_api
from core_dashboard_common_app import constants as dashboard_constants
from core_dashboard_common_app.views.common.forms import UserForm
from core_main_app.components.user import api as user_api
from core_main_app.utils.access_control.exceptions import AccessControlError
from core_main_app.utils.rendering import admin_render
from core_main_app.views.user.forms import WorkspaceForm
from core_dashboard_common_app import settings


@login_required(login_url=reverse_lazy("core_main_app_login"))
def dashboard_workspace_records(request, workspace_id):
    """ List the records of a workspace.

    Args:
        request:
    Return:
    """
    workspace = workspace_api.get_by_id(workspace_id)

    try:
        workspace_data = workspace_data_api.get_all_by_workspace(workspace, request.user)
    except AccessControlError, ace:
        workspace_data = []

    detailed_user_data = []
    user_can_read = workspace_api.can_user_read_workspace(workspace, request.user)
    user_can_write = workspace_api.can_user_write_workspace(workspace, request.user)
    for data in workspace_data:
        detailed_user_data.append({'data': data,
                                   'can_read': user_can_read,
                                   'can_write': user_can_write,
                                   'is_owner': True,
                                   'template_name': data.template._display_name
                                   })

    # Add user_form for change owner
    user_form = UserForm(request.user)
    context = {
        'other_users_data': detailed_user_data,
        'user_form': user_form,
        'document': dashboard_constants.FUNCTIONAL_OBJECT_ENUM.RECORD,
        'template': dashboard_constants.DASHBOARD_RECORDS_TEMPLATE_TABLE_DATATABLE,
        'number_columns': 5,
        'administration': True
    }

    # Get all username and corresponding ids
    user_names = dict((str(x.id), x.username) for x in user_api.get_all_users())
    context.update({'usernames': user_names})
    context.update({'title': 'List of records of workspace: ' + workspace.title})

    modals = ["core_main_app/user/workspaces/list/modals/assign_workspace.html"]

    assets = {
        "css": copy.deepcopy(dashboard_constants.CSS_COMMON),

        "js": [{
                    "path": 'core_main_app/user/js/workspaces/list/modals/assign_workspace.js',
                    "is_raw": False
               },
               {
                    "path": dashboard_constants.ADMIN_VIEW_RECORD_RAW,
                    "is_raw": True
               },
               {
                    "path": 'core_main_app/common/js/backtoprevious.js',
                    "is_raw": True
               },
               {
                    "path": dashboard_constants.JS_EDIT_RECORD,
                    "is_raw": False
               },
               {
                    "path": dashboard_constants.JS_VIEW_RECORD,
                    "is_raw": False
               }
        ]
    }

    _handle_asset_modals(assets, modals, delete=True, change_owner=True, menu=False,
                         workspace=workspace.title)

    return admin_render(request, dashboard_constants.ADMIN_DASHBOARD_TEMPLATE,
                        context=context,
                        assets=assets,
                        modals=modals)


@login_required(login_url=reverse_lazy("core_main_app_login"))
def dashboard_workspaces(request):
    """ List the workspaces.

    Args:
        request:
    Return:
    """

    user_workspaces = workspace_api.get_all()
    detailed_user_workspaces = []
    for user_workspace in user_workspaces:
        detailed_user_workspaces.append({'user': user_api.get_user_by_id(user_workspace.owner).username if not workspace_api.is_workspace_global(user_workspace) else "GLOBAL",
                                         'is_owner': True,
                                         'name': user_workspace.title,
                                         'workspace': user_workspace,
                                         'can_read': True,
                                         'can_write': True,
                                         'is_public': workspace_api.is_workspace_public(user_workspace),
                                         })

    context = {
        'workspace_form': WorkspaceForm(),
        'other_users_data': detailed_user_workspaces,
        'document': dashboard_constants.FUNCTIONAL_OBJECT_ENUM.WORKSPACE,
        'template': dashboard_constants.DASHBOARD_WORKSPACES_TEMPLATE_TABLE,
        'number_columns': 6,
        'create_workspace': False,
        'can_set_public': settings.CAN_SET_WORKSPACE_PUBLIC
    }

    modals = ["core_main_app/user/workspaces/list/create_workspace.html",
              "core_main_app/user/workspaces/list/modals/set_public.html"]

    assets = {
        "css": copy.deepcopy(dashboard_constants.CSS_COMMON),

        "js": []
    }

    if settings.CAN_SET_WORKSPACE_PUBLIC:
        assets['js'].append({
                                "path": 'core_main_app/user/js/workspaces/list/modals/set_public.js',
                                "is_raw": False
                            })

    _handle_asset_modals(assets,
                         modals,
                         delete=True,
                         change_owner=False,
                         menu=False)

    return admin_render(request,
                        dashboard_constants.ADMIN_DASHBOARD_TEMPLATE,
                        context=context,
                        assets=assets,
                        modals=modals)


def _handle_asset_modals(assets, modal, delete=False, change_owner=False, menu=False, workspace=False):
    """ Add needed assets.

    Args:
        assets
        modal
        delete
        change_owner
        menu

    Return:
    """

    assets['js'].append({
                            "path": dashboard_constants.JS_INIT_ADMIN,
                            "is_raw": True
                        })
    assets['js'].append({
                            "path": dashboard_constants.JS_ADMIN_ACTION_DASHBOARD,
                            "is_raw": True
                        })
    assets['js'].append({
                            "path": dashboard_constants.JS_ADMIN_TABLE,
                            "is_raw": False
                        })

    # Common asset
    assets['js'].extend(dashboard_constants.JS_COMMON)
    if delete:
        assets['js'].append({
                                "path": dashboard_constants.JS_COMMON_FUNCTION_DELETE,
                                "is_raw": False
                             })
        modal.append(dashboard_constants.MODALS_COMMON_DELETE)
    if change_owner:
        assets['js'].append({
                              "path": dashboard_constants.JS_COMMON_FUNCTION_CHANGE_OWNER,
                              "is_raw": False
                            })
        modal.append(dashboard_constants.MODALS_COMMON_CHANGE_OWNER)

    # Menu
    assets['js'].append({
                            "path": dashboard_constants.JS_ADMIN_COUNT_CHECK,
                            "is_raw": True
                        })
    assets['js'].append({
                            "path": dashboard_constants.JS_ADMIN_RESET_CHECKBOX,
                            "is_raw": True
                        })
    assets['js'].append({
                            "path": dashboard_constants.JS_ADMIN_SELECT_ALL,
                            "is_raw": True
                        })
    assets['js'].append({
                            "path": dashboard_constants.JS_ADMIN_SELETED_ELEMENT,
                            "is_raw": False
                        })
    assets['js'].append({
                            "path": dashboard_constants.JS_ADMIN_INIT_MENU,
                            "is_raw": False
                        })
