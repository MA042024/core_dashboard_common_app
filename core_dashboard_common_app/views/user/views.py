"""
    Views available for the user
"""

import copy

import core_main_app.components.data.api as workspace_data_api
import core_main_app.components.workspace.api as workspace_api
from core_dashboard_common_app import constants as dashboard_constants
from core_dashboard_common_app.views.common.forms import UserForm
from core_main_app.components.user import api as user_api
from core_main_app.utils.access_control.exceptions import AccessControlError
from core_main_app.views.common.views import CommonView


class DashboardWorkspaceRecords(CommonView):
    """ List the records of a workspace.
    """

    template = dashboard_constants.DASHBOARD_TEMPLATE
    data_template = dashboard_constants.DASHBOARD_RECORDS_TEMPLATE_TABLE_DATATABLE

    def get(self, request, workspace_id, *args, **kwargs):
        workspace = workspace_api.get_by_id(workspace_id)

        try:
            workspace_data = workspace_data_api.get_all_by_workspace(workspace, request.user)
        except AccessControlError, ace:
            workspace_data = []

        user_can_read = workspace_api.can_user_read_workspace(workspace, request.user)
        user_can_write = workspace_api.can_user_write_workspace(workspace, request.user)
        detailed_user_data = self._format_data_context(workspace_data, request.user, user_can_read, user_can_write)

        # Add user_form for change owner
        user_form = UserForm(request.user)
        context = {
            'user_data': detailed_user_data,
            'user_form': user_form,
            'document': dashboard_constants.FUNCTIONAL_OBJECT_ENUM.RECORD,
            'template': self.data_template,
            'number_columns': 5,
            'administration': False
        }

        # Get all username and corresponding ids
        user_names = dict((str(x.id), x.username) for x in user_api.get_all_users())
        context.update({'usernames': user_names})
        context.update({'title': 'List of records of workspace: ' + workspace.title})

        modals = ["core_main_app/user/workspaces/list/modals/assign_workspace.html"]

        assets = self._get_assets()

        _handle_asset_modals(assets, modals, delete=True, change_owner=True)

        return self.common_render(request, self.template,
                                  context=context,
                                  assets=assets,
                                  modals=modals)

    def _format_data_context(self, data_list, user, user_can_read, user_can_write):
        detailed_user_data = []
        for data in data_list:
            is_owner = str(data.user_id) == str(user.id)
            detailed_user_data.append({'data': data,
                                       'can_read': user_can_read or is_owner,
                                       'can_write': user_can_write or is_owner,
                                       'is_owner': is_owner})

    def _get_assets(self):
        assets = {
            "css": copy.deepcopy(dashboard_constants.CSS_COMMON),

            "js": [{
                "path": 'core_main_app/user/js/workspaces/list/modals/assign_workspace.js',
                "is_raw": False
            },
                {
                    "path": 'core_main_app/common/js/backtoprevious.js',
                    "is_raw": True
                },
                {
                    "path": dashboard_constants.USER_VIEW_RECORD_RAW,
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
        return assets


def _handle_asset_modals(assets, modal, delete=False, change_owner=False):
    """ Add needed assets.

    Args:
        assets
        modal
        delete
        change_owner

    Return:
    """

    # Admin or user assets
    assets['js'].append({
                            "path": dashboard_constants.JS_INIT_USER,
                            "is_raw": True
                       })
    assets['js'].append({
                            "path": dashboard_constants.JS_USER_TABLE,
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
                            "path": dashboard_constants.JS_USER_SELECTED_ELEMENT,
                            "is_raw": True
                        })
