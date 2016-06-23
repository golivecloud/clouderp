import gce.tests


class TestUi(gce.tests.HttpCase):
    def test_01_admin_rte(self):
        self.phantom_js("/web", "clouderp.__DEBUG__.services['web.Tour'].run('rte', 'test')", "clouderp.__DEBUG__.services['web.Tour'].tours.rte", login='admin')

    def test_02_admin_rte_inline(self):
        self.phantom_js("/web", "clouderp.__DEBUG__.services['web.Tour'].run('rte_inline', 'test')", "clouderp.__DEBUG__.services['web.Tour'].tours.rte", login='admin')
