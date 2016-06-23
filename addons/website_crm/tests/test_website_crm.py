from gce.api import Environment
import gce.tests
@gce.tests.common.at_install(False)
@gce.tests.common.post_install(True)
class TestWebsiteCrm(gce.tests.HttpCase):
    def test_tour(self):
        self.phantom_js("/", "clouderp.__DEBUG__.services['web.Tour'].run('website_crm_tour', 'test')", "clouderp.__DEBUG__.services['web.Tour'].tours.website_crm_tour")

        # need environment using the test cursor as it's not committed
        cr = self.registry.cursor()
        assert cr is self.registry.test_cr
        env = Environment(cr, self.uid, {})
        record = env['crm.lead'].search([('description', '=', '### TOUR DATA ###')])
        assert len(record) == 1
        assert record.contact_name == 'John Smith'
        assert record.email_from == 'john@smith.com'
        assert record.partner_name == 'clouderp S.A.'
