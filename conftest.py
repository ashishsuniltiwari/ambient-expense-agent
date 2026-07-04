import sys
from unittest.mock import MagicMock

class MockCredentials:
    def __init__(self):
        self.token = "mock-token"
        self.expiry = None
        self.expired = False  # Added this field so the client checker doesn't crash!
        self.service_account_email = "mock@mock.iam.gserviceaccount.com"
        self.project_id = "mock-project-id"
        self.quota_project_id = "mock-project-id"

    def refresh(self, request):
        pass

    def apply(self, headers):
        headers["Authorization"] = "Bearer mock-token"

# Override the default engine lookup
import google.auth
google.auth.default = lambda *args, **kwargs: (MockCredentials(), "mock-project-id")