import gce.tests

@gce.tests.common.at_install(False)
@gce.tests.common.post_install(True)
class TestUi(gce.tests.HttpCase):
    def test_01_admin_widget_x2many(self):
        self.phantom_js("/web#action=test_new_api.action_discussions",
                        "clouderp.__DEBUG__.services['web.Tour'].run('widget_x2many', 'test')",
                        "clouderp.__DEBUG__.services['web.Tour'].tours.widget_x2many",
                        login="admin")
