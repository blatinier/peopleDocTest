from flask_testing import TestCase
from backend.main import create_flask_app


class AppTest(TestCase):

    def create_app(self):
        app = create_flask_app(test=True)
        return app

    def test_e2e(self):
        # Feed some new restaurants
        self.assert_200(self.client.post('/pipo'))
        self.assert_200(self.client.post('/pouet'))

        # Check we can get them
        get_res = self.client.get('/pipo')
        self.assert_200(get_res)
        self.assertEqual(get_res.json, {"name": "pipo"})

        get_res = self.client.get('/list')
        self.assert_200(get_res)
        self.assertEqual(get_res.json, [{"name": "pipo"}, {"name": "pouet"}])
        # Check random fetch an existing estaurant
        get_res = self.client.get('/random')
        self.assert_200(get_res)
        self.assertIn(get_res.json, [{"name": "pipo"}, {"name": "pouet"}])

        # Check delete works
        self.assert_200(self.client.delete('/pipo'))
        self.assert_404(self.client.get('/pipo'))
        self.assert_200(self.client.delete('/pouet'))
        self.assert_404(self.client.get('/pouet'))

        # Check no restaurant available
        list_res = self.client.get('/list')
        self.assert_200(list_res)
        self.assertEqual(list_res.json, [])
