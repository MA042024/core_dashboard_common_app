"""
    Url router for the dashboard common
"""
from django.contrib.auth.decorators import login_required
from django.urls import re_path

from core_dashboard_common_app.views.common import (
    ajax,
    views as dashboard_common_app_common_views,
)
from core_main_app.components.blob import api as blob_api
from core_main_app.views.user import ajax as main_user_ajax

urlpatterns = [
    re_path(
        r"^delete-document",
        ajax.delete_document,
        name="core_dashboard_delete_document",
    ),
    re_path(
        r"^change-owner",
        ajax.change_owner_document,
        name="core_dashboard_change_owner_document",
    ),
    re_path(
        r"^assign-blob-workspace",
        main_user_ajax.AssignView.as_view(api=blob_api),
        name="core_main_assign_blob_workspace",
    ),
    re_path(
        r"^change-workspace",
        main_user_ajax.LoadFormChangeWorkspace.as_view(),
        name="core_main_change_workspace",
    ),
    re_path(
        r"^edit-record", ajax.edit_record, name="core_dashboard_edit_record"
    ),
    re_path(
        r"^forms$",
        login_required(
            dashboard_common_app_common_views.DashboardForms.as_view(),
        ),
        name="core_dashboard_common_forms",
    ),
]
