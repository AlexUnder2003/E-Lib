import typesense


client = typesense.Client({
  'nodes': [{
    'host': 'localhost',  # Заменить на свой хост для Typesense
    'port': '8108',       # Порт сервера
    'protocol': 'http'    # 'https' если используешь Typesense Cloud
  }],
  'api_key': 'xyz',  # Указать свой API ключ
  'connection_timeout_seconds': 2
})

def create_collection(schema):

    books_schema = {
        'name': 'books',
        'fields': [
            {'name': 'sorting_id', 'type': 'int32'},
            {'name': 'title', 'type': 'string'},
            {'name': 'author', 'type': 'string'},
            {'name': 'description', 'type': 'string'},
            {'name': 'published_date', 'type': 'string'},
            {'name': 'file', 'type': 'string'},
            {'name': 'image', 'type': 'string'}
        ],
        'default_sorting_field': 'sorting_id'
    }

    try:
        client.collections.create(schema)
    except Exception as e:
        print(f"Коллекция уже существует или ошибка: {e}")


def get_collections():
    collections = client.collections.retrieve()
    print(collections)



