""" Test access to views
"""
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from core_main_app.utils.integration_tests.integration_base_test_case import (
    IntegrationBaseTestCase,
)
from core_main_app.utils.tests_tools.MockUser import create_mock_user
from core_dashboard_common_app.views.common.views import DashboardForms

from tests.views.fixtures import (
    DataStructureFixtures,
)


class TestViewDashboardForms(IntegrationBaseTestCase):
    """Test View Dashboard Forms"""

    def setUp(self):
        """setUp

        Returns:

        """
        self.factory = RequestFactory()
        self.user1 = create_mock_user(user_id="1")
        self.anonymous = AnonymousUser()
        self.fixture = DataStructureFixtures()
        self.fixture.insert_data()

    def test_user_can_access_forms_if_owner(self):
        """test_user_can_access_forms_if_owner

        Returns:

        """
        request = self.factory.get("core_dashboard_common_forms")
        request.user = self.user1
        response = DashboardForms.as_view()(request)
        self.assertEqual(response.status_code, 200)
