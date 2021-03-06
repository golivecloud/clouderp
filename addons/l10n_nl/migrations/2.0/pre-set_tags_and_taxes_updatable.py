from gce.modules.registry import RegistryManager


def migrate(cr, version):
    registry = RegistryManager.get(cr.dbname)
    from gce.addons.account.models.chart_template import migrate_set_tags_and_taxes_updatable
    migrate_set_tags_and_taxes_updatable(cr, registry, 'l10n_nl')
