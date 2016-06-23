import gce.tests

class WebSuite(gce.tests.HttpCase):
    def test_01_js(self):
        self.phantom_js('/web/tests?mod=web',"","", login='admin')
