import typesense
import json

client = typesense.Client({
    'nodes': [{
        'host': 'localhost',
        'port': '8108',
        'protocol': 'http'
    }],
    'api_key': 'xyz',
    'connection_timeout_seconds': 2
})

def load_books_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        fields = item['fields']
        document = {
            'sorting_id': item['pk'],
            'title': fields['title'],
            'author': fields['author'],
            'description': fields['description'],
            'published_date': fields['published_date'],
            'file': fields['file'],
            'image': fields['image']
        }

        try:
            client.collections['books'].documents.create(document)
            print(f"Документ добавлен: {document['title']}")
        except typesense.exceptions.RequestMalformed as e:
            print(f"Ошибка при добавлении документа {document['title']}: {e}")

load_books_from_json('database.json')
