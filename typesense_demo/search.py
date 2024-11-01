import typesense

# Подключаемся к Typesense
client = typesense.Client({
    'nodes': [{
        'host': 'localhost',  # или IP-адрес вашего сервера
        'port': '8108',
        'protocol': 'http'  # или 'https', если используется
    }],
    'api_key': 'xyz',  # ваш API ключ
})

# Функция для поиска книги по заголовку
def search_book(title):
    try:
        response = client.collections['books'].documents.search({
            'q': title,
            'query_by': 'title',
            'sort_by': 'sorting_id:asc'  # или другой сортировочный параметр
        })
        return response
    except Exception as e:
        print(f"Ошибка поиска: {e}")
        return None

# Пример использования функции
result = search_book('Огни')
if result:
    for book in result['hits']:
        print(book['document'])
