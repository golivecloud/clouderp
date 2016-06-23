import gce.tests
# Part of clouderp. See LICENSE file for full copyright and licensing details.


@gce.tests.common.at_install(False)
@gce.tests.common.post_install(True)
class TestUi(gce.tests.HttpCase):

    def test_01_admin_survey_tour(self):
        self.phantom_js("/", "clouderp.__DEBUG__.services['web.Tour'].run('test_survey', 'test')", "clouderp.__DEBUG__.services['web.Tour'].tours.test_survey", login="admin")

    def test_02_demo_survey_tour(self):
        self.phantom_js("/", "clouderp.__DEBUG__.services['web.Tour'].run('test_survey', 'test')", "clouderp.__DEBUG__.services['web.Tour'].tours.test_survey", login="demo")

    def test_03_public_survey_tour(self):
        self.phantom_js("/", "clouderp.__DEBUG__.services['web.Tour'].run('test_survey', 'test')", "clouderp.__DEBUG__.services['web.Tour'].tours.test_survey")
