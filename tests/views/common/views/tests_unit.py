""" Unit tests on common dashboard views.
"""
from unittest import TestCase
from unittest.mock import patch

from core_dashboard_common_app.views.common import views as common_views
from core_main_app.utils.tests_tools.RequestMock import RequestMock
from core_main_app.components.workspace import api as workspace_api
from core_main_app.components.data import api as data_api
from core_main_app.components.user import api as user_api


class TestDashboardWorkspaceRecordsGet(TestCase):
    @staticmethod
    def mock_render_only_context(
        request, template_name, modals=None, assets=None, context=None
    ):
        return context

    def setUp(self) -> None:
        self.workspace_records_view = common_views.DashboardWorkspaceRecords

    @patch.object(workspace_api, "get_by_id")
    @patch.object(data_api, "get_all_by_workspace")
    @patch.object(workspace_api, "can_user_read_workspace")
    @patch.object(workspace_api, "can_user_write_workspace")
    @patch.object(common_views, "ResultsPaginator")
    @patch.object(
        common_views.DashboardWorkspaceRecords, "_format_data_context"
    )
    @patch.object(common_views, "UserForm")
    @patch.object(common_views.DashboardWorkspaceRecords, "_get_modals")
    @patch.object(common_views.DashboardWorkspaceRecords, "_get_assets")
    @patch.object(user_api, "get_user_by_id")
    @patch.object(common_views.DashboardWorkspaceRecords, "common_render")
    def test_user_side_context_has_no_owner_info(
        self,
        mock_common_render,
        mock_get_user_by_id,
        mock_get_assts,
        mock_get_modals,
        mock_user_form,
        mock_format_data_context,
        mock_results_paginator,
        mock_can_user_write_workspace,
        mock_can_user_read_workspace,
        mock_get_all_by_workspace,
        mock_workspace_get_by_id,
    ):
        mock_common_render.side_effect = self.mock_render_only_context

        self.workspace_records_view.administration = False
        response = RequestMock.do_request_get(
            self.workspace_records_view.as_view(),
            None,
            param={"workspace_id": 42},
        )

        self.assertNotIn("owner", response.keys())
        self.assertNotIn("owner_change_url", response.keys())

    @patch.object(workspace_api, "get_by_id")
    @patch.object(data_api, "get_all_by_workspace")
    @patch.object(workspace_api, "can_user_read_workspace")
    @patch.object(workspace_api, "can_user_write_workspace")
    @patch.object(common_views, "ResultsPaginator")
    @patch.object(
        common_views.DashboardWorkspaceRecords, "_format_data_context"
    )
    @patch.object(common_views, "UserForm")
    @patch.object(common_views.DashboardWorkspaceRecords, "_get_modals")
    @patch.object(common_views.DashboardWorkspaceRecords, "_get_assets")
    @patch.object(user_api, "get_user_by_id")
    @patch.object(common_views, "reverse")
    @patch.object(common_views.DashboardWorkspaceRecords, "common_render")
    def test_admin_side_context_has_owner_info(
        self,
        mock_common_render,
        mock_reverse,
        mock_get_user_by_id,
        mock_get_assts,
        mock_get_modals,
        mock_user_form,
        mock_format_data_context,
        mock_results_paginator,
        mock_can_user_write_workspace,
        mock_can_user_read_workspace,
        mock_get_all_by_workspace,
        mock_workspace_get_by_id,
    ):
        mock_common_render.side_effect = self.mock_render_only_context

        self.workspace_records_view.administration = True
        response = RequestMock.do_request_get(
            self.workspace_records_view.as_view(),
            None,
            param={"workspace_id": 42},
        )

        self.assertIn("owner", response.keys())
        self.assertIn("owner_change_url", response.keys())
