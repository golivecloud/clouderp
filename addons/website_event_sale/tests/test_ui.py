import gce.tests

@gce.tests.common.at_install(False)
@gce.tests.common.post_install(True)
class TestUi(gce.tests.HttpCase):
    def test_admin(self):
        self.phantom_js("/", "clouderp.__DEBUG__.services['web.Tour'].run('event_buy_tickets', 'test')", "clouderp.__DEBUG__.services['web.Tour'].tours.event_buy_tickets", login="admin")

    def test_demo(self):
        self.phantom_js("/", "clouderp.__DEBUG__.services['web.Tour'].run('event_buy_tickets', 'test')", "clouderp.__DEBUG__.services['web.Tour'].tours.event_buy_tickets", login="demo")

    def test_public(self):
        self.phantom_js("/", "clouderp.__DEBUG__.services['web.Tour'].run('event_buy_tickets', 'test')", "clouderp.__DEBUG__.services['web.Tour'].tours.event_buy_tickets")
