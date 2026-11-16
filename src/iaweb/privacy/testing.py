from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer

import iaweb.privacy


class IawebPrivacyLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=iaweb.privacy)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "iaweb.privacy:default")


IAWEB_PRIVACY_FIXTURE = IawebPrivacyLayer()


IAWEB_PRIVACY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(IAWEB_PRIVACY_FIXTURE,), name="IawebPrivacyLayer:IntegrationTesting"
)


IAWEB_PRIVACY_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(IAWEB_PRIVACY_FIXTURE,), name="IawebPrivacyLayer:FunctionalTesting"
)
