# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles, TEST_USER_ID
from plone.ORM.testing import PLONE_ORM_INTEGRATION_TESTING  # noqa: E501

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that plone.ORM is properly installed."""

    layer = PLONE_ORM_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if plone.ORM is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'plone.ORM'))

    def test_browserlayer(self):
        """Test that IPloneOrmLayer is registered."""
        from plone.ORM.interfaces import (
            IPloneOrmLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IPloneOrmLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONE_ORM_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['plone.ORM'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if plone.ORM is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'plone.ORM'))

    def test_browserlayer_removed(self):
        """Test that IPloneOrmLayer is removed."""
        from plone.ORM.interfaces import \
            IPloneOrmLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IPloneOrmLayer,
            utils.registered_layers())
