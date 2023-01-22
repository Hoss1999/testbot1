def messages(client, message):
    if message.author.id == client.user:
        return
    print(f'New Message from {message.author}: {message.content}')
