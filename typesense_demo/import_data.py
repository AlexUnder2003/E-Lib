import typesense


# Настройка клиента Typesense
client = typesense.Client({
    'nodes': [{
        'host': 'localhost',
        'port': '8108',
        'protocol': 'http'
    }],
    'api_key': 'YOUR_API_KEY',
    'connection_timeout_seconds': 2
})

# Получение всех книг из базы данных
books = Book.objects.all()

# Формирование данных для Typesense
documents = []
for book in books:
    documents.append({
        'sorting_id': book.id,
        'title': book.title,
        'author': book.author,
        'description': book.description,
        'published_date': book.published_date.isoformat(),
        'file': book.file.url,
        'image': book.image.url
    })

# Добавление документов в коллекцию Typesense
if documents:
    client.collections['books'].documents.create(documents)
