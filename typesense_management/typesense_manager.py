import typesense


class Manager:
    def __init__(self, schema):
        self.schema = schema
        self.client = typesense.Client({
            'nodes': [{
                'host': 'localhost',
                'port': '8108',
                'protocol': 'http'
            }],
            'api_key': 'xyz',
            'connection_timeout_seconds': 2
        })

    def create_collection(self):
        try:
            self.client.collections.create(self.schema)
            print("Коллекция успешно создана.")
        except Exception as e:
            print(f"Коллекция уже существует или ошибка: {e}")

    def get_collections(self):
        try:
            collections = self.client.collections.retrieve()
            print(collections)
        except Exception as e:
            print(f"Ошибка при получении коллекций: {e}")
