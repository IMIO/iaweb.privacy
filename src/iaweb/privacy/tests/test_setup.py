"""Setup tests for this package."""

from iaweb.privacy.testing import IAWEB_PRIVACY_INTEGRATION_TESTING  # noqa
from plone.base.utils import get_installer

import unittest


class TestSetup(unittest.TestCase):
    """Test that iaweb.privacy is properly installed."""

    layer = IAWEB_PRIVACY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])

    def test_product_installed(self):
        """Test if iaweb.privacy is installed."""
        self.assertTrue(self.installer.is_product_installed("iaweb.privacy"))

    def test_browserlayer(self):
        """Test that IIawebPrivacyLayer is registered."""
        from iaweb.privacy.interfaces import IIawebPrivacyLayer
        from plone.browserlayer import utils

        self.assertIn(IIawebPrivacyLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = IAWEB_PRIVACY_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])
        self.installer.uninstall_product("iaweb.privacy")

    def test_product_uninstalled(self):
        """Test if iaweb.privacy is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed("iaweb.privacy"))

    def test_browserlayer_removed(self):
        """Test that IIawebPrivacyLayer is removed."""
        from iaweb.privacy.interfaces import IIawebPrivacyLayer
        from plone.browserlayer import utils

        self.assertNotIn(IIawebPrivacyLayer, utils.registered_layers())
