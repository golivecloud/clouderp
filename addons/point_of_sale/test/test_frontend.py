
import gce.tests

@gce.tests.common.at_install(False)
@gce.tests.common.post_install(True)
class TestUi(gce.tests.HttpCase):
    def test_01_pos_basic_order(self):
        self.phantom_js("/", "clouderp.__DEBUG__.services['web.Tour'].run('pos_basic_order', 'test')", "clouderp.__DEBUG__.services['web.Tour'].tours.pos_basic_order", login="admin")
