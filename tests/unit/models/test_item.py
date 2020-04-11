from models.item import ItemModel
from tests.unit.base_test import UnitBaseTest


class ItemTest(UnitBaseTest):
    def setUp(self):
        self.name = 'Test'
        self.price = 10.99
        self.store_id = 1
        self.item = ItemModel(self.name, self.price, self.store_id)

    def test_create_item(self):
        self.assertEqual(self.item.name, self.name)
        self.assertEqual(self.item.price, self.price)
        self.assertEqual(self.item.store_id, self.store_id)
        self.assertIsNone(self.item.store)

    def test_item_json(self):
        self.assertEqual(self.item.json(), {
                         'name': self.name, 'price': self.price})
