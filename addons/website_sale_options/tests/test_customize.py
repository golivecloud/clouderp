import gce.tests

@gce.tests.common.at_install(False)
@gce.tests.common.post_install(True)
class TestUi(gce.tests.HttpCase):
    def test_01_admin_shop_customize_tour(self):
        self.phantom_js("/", "clouderp.__DEBUG__.services['web.Tour'].run('shop_customize', 'test')", "clouderp.__DEBUG__.services['web.Tour'].tours.shop_customize", login="admin")
