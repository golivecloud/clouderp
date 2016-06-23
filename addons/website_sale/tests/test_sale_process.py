import gce.tests

@gce.tests.common.at_install(False)
@gce.tests.common.post_install(True)
class TestUi(gce.tests.HttpCase):
    def test_01_admin_shop_tour(self):
        self.phantom_js("/", "clouderp.__DEBUG__.services['web.Tour'].run('shop', 'test')", "clouderp.__DEBUG__.services['web.Tour'].tours.shop", login="admin")

    def test_02_admin_checkout(self):
        self.phantom_js("/", "clouderp.__DEBUG__.services['web.Tour'].run('shop_buy_product', 'test')", "clouderp.__DEBUG__.services['web.Tour'].tours.shop_buy_product", login="admin")

    def test_03_demo_checkout(self):
        self.phantom_js("/", "clouderp.__DEBUG__.services['web.Tour'].run('shop_buy_product', 'test')", "clouderp.__DEBUG__.services['web.Tour'].tours.shop_buy_product", login="demo")

    def test_04_public_checkout(self):
        self.phantom_js("/", "clouderp.__DEBUG__.services['web.Tour'].run('shop_buy_product', 'test')", "clouderp.__DEBUG__.services['web.Tour'].tours.shop_buy_product")
