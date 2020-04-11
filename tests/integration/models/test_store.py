from models.store import StoreModel
from models.item import ItemModel
from tests.base_test import BaseTest

class StoreTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.name = 'test'

    def test_create_store_items_empty(self):
        store = StoreModel(self.name)

        self.assertListEqual(store.items.all(), [])

    def test_crud(self):
        with self.app_context():
            store = StoreModel(self.name)

            self.assertIsNone(StoreModel.find_by_name(self.name))

            store.save_to_db()

            self.assertIsNotNone(StoreModel.find_by_name(self.name))

            store.delete_from_db()

            self.assertIsNone(StoreModel.find_by_name(self.name))

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('test')
            item = ItemModel('test_item', 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(store.items.count(), 1)
            self.assertEqual(store.items.first().name, item.name)

    def test_store_json_no_items(self):
        store = StoreModel('test')
        expected = {
            'name': 'test',
            'items': []
        }

        self.assertDictEqual(store.json(), expected)

    def test_store_json_one_item(self):
        with self.app_context():
            store = StoreModel('test')
            item = ItemModel('test_item', 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            expected = {
                'name': 'test',
                'items': [{'name': 'test_item', 'price': 19.99}]
            }

            self.assertDictEqual(store.json(), expected)
            