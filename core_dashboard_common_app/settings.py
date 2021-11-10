""" Django settings for core_dashboard_common_app app.

Settings with the following syntax can be overwritten at the project level:
SETTING_NAME = getattr(settings, "SETTING_NAME", "Default Value")
"""

from django.conf import settings

if not settings.configured:
    settings.configure()

SERVER_URI = getattr(settings, "SERVER_URI", "http://localhost")

INSTALLED_APPS = getattr(settings, "INSTALLED_APPS", [])

# Number of records to display per page for pagination
RECORD_PER_PAGE_PAGINATION = getattr(settings, "RESULTS_PER_PAGE", 10)

# Number of files to display per page for pagination
FILE_PER_PAGE_PAGINATION = getattr(settings, "RESULTS_PER_PAGE", 10)

# Number of records to display per page for pagination
QUERY_PER_PAGE_PAGINATION = getattr(settings, "RESULTS_PER_PAGE", 10)

# Set Workspace public
CAN_SET_WORKSPACE_PUBLIC = getattr(settings, "CAN_SET_WORKSPACE_PUBLIC", True)
