import gce.tests

@gce.tests.common.at_install(False)
@gce.tests.common.post_install(True)
class TestUi(gce.tests.HttpCase):
    def test_admin(self):
        self.phantom_js("/", "clouderp.__DEBUG__.services['web.Tour'].run('event', 'test')", "clouderp.__DEBUG__.services['web.Tour'].tours.event", login='admin')
