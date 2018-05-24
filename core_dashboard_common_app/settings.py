"""
    Django settings for core_dashboard_common_app app
"""

from django.conf import settings

if not settings.configured:
    settings.configure()

SERVER_URI = getattr(settings, 'SERVER_URI', "http://localhost")

INSTALLED_APPS = getattr(settings, 'INSTALLED_APPS', [])

# Number of records to display per page for pagination
RECORD_PER_PAGE_PAGINATION = getattr(settings, 'RESULTS_PER_PAGE', 10)

# Set Workspace public
CAN_SET_WORKSPACE_PUBLIC = getattr(settings, 'CAN_SET_WORKSPACE_PUBLIC', True)

DATA_DISPLAY_NAME = getattr(settings, 'DATA_DISPLAY_NAME', 'data')
DRAFT_DISPLAY_NAME = getattr(settings, 'DRAFT_DISPLAY_NAME', 'draft')
WORKSPACE_DISPLAY_NAME = getattr(settings, 'WORKSPACE_DISPLAY_NAME', 'workspace')
