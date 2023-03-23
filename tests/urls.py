"""
    Url router for the dashboard common
"""
from django.conf.urls import include
from django.contrib.auth.decorators import login_required
from django.urls import re_path

from core_dashboard_common_app.views.common import (
    ajax,
    views as dashboard_common_app_common_views,
)

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
        r"^edit-record", ajax.edit_record, name="core_dashboard_edit_record"
    ),
    re_path(
        r"^forms$",
        login_required(
            dashboard_common_app_common_views.DashboardForms.as_view(),
        ),
        name="core_dashboard_common_forms",
    ),
    re_path(r"^tz_detect/", include("tz_detect.urls")),
]
