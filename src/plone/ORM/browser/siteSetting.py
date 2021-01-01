from plone.ORM import _
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper

from plone.z3cform import layout
from z3c.form import form
from zope.interface import Interface
from zope import schema


class ISiteSetting(Interface):

    dbString = schema.TextLine(
        title=_(u"Path of database"),
        description=_(u"https://docs.sqlalchemy.org/en/13/core/connections.html#sqlalchemy.engine.Engine"),
        required=False,
    )

class SiteSettingControlPanelForm(RegistryEditForm):
    form.extends(RegistryEditForm)
    schema = ISiteSetting


SiteSettingControlPanelView = layout.wrap_form(SiteSettingControlPanelForm, ControlPanelFormWrapper)
SiteSettingControlPanelView.label = _(u"Site Setting")