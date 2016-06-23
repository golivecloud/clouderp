import gce.tests

@gce.tests.common.at_install(False)
@gce.tests.common.post_install(True)
class TestUi(gce.tests.HttpCase):
    def test_01_admin_forum_tour(self):
        self.phantom_js("/", "clouderp.__DEBUG__.services['web.Tour'].run('question', 'test')", "clouderp.__DEBUG__.services['web.Tour'].tours.question", login="admin")

    def test_02_demo_question(self):
        self.phantom_js("/", "clouderp.__DEBUG__.services['web.Tour'].run('forum_question', 'test')", "clouderp.__DEBUG__.services['web.Tour'].tours.forum_question", login="demo")

