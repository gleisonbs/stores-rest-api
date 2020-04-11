from models.store import StoreModel
from tests.unit.base_test import UnitBaseTest


class StoreTest(UnitBaseTest):
    def setUp(self):
        self.name = 'test'

    def test_create_store(self):
        store = StoreModel(self.name)

        self.assertEqual(
            store.name, 
            self.name, 
            'The name of the store after creation does not equal the constructor argument')
