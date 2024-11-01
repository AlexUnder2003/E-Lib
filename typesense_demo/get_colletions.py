import typesense

client = typesense.Client({
  'nodes': [{
    'host': 'localhost',  # Если используете Typesense Cloud, используйте хост вашего кластера
    'port': '8108',       # Для Typesense Cloud используйте 443
    'protocol': 'http'    # Для Typesense Cloud используйте https
  }],
  'api_key': 'xyz',
  'connection_timeout_seconds': 2
})

# Получение списка коллекций
collections = client.collections.retrieve()
print(collections)