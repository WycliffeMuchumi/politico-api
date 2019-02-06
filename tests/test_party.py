from .base import *
from .helper_data import *
from .helper_methods import *
class PartyTestCase(BaseTestCase):
    """ This class represents the party test case and inherits from BaseTestCase class """
    
    def setUp(self):
        super(PartyTestCase, self).setUp()

    def test_create_party(self):
        """ Test API can create party """

        response = create_party(self, party)
        self.assertEqual(response.status_code, 201)
        response_content =  json.loads(response.data.decode())
        self.assertTrue(response_content['status'] == 201)

    def test_get_all_parties(self):
        """ Test API can retrieve all parties """
        create_party(self, party)
        response = get_all_parties(self)
        self.assertEqual(response.status_code, 200)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content['message'] == "Success")

if __name__ == "__main__":
    unittest.main()