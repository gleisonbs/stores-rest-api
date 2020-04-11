from models.item import ItemModel
from models.store import StoreModel
from tests.base_test import BaseTest


class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            StoreModel('test').save_to_db()

            name = 'test'
            price = 19.99
            store_id = 1
            item = ItemModel(name, price, store_id)

            self.assertIsNone(ItemModel.find_by_name(name),
                              f'Item "{name}" already exists in the database')

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name(name),
                                 f'save_to_db failed: Item "{name}"')

            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name(name),
                              f'delete_from_db failed: Item "{name}"')

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('test_store')
            item = ItemModel('test', 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(item.store.name, 'test_store')
