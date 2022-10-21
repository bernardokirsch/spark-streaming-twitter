import socket
import tweepy
import time

HOST = 'localhost'
PORT = 9008

s = socket.socket()
s.bind((HOST, PORT))
print(f'Aguardando conexão na porta : {PORT}')

s.listen(5)
connection, address = s.accept()
print(f'Recebendo solicitação de {address}')

token = 'AAAAAAAAAAAAAAAAAAAAAKYffwEAAAAAli96fG%2B7RMc7onXoE4b6f1fjumY%3DSc6eOt6qRb41AQkz6y5r0LYZ7r7o2neoM9dq3ZvIHL89zIwhDI'
keyword = 'política'

class GetTweets(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.text)
        print('=' * 50)
        connection.send(tweet.text.encode('utf-8', 'ignore'))

printer = GetTweets(token)
printer.add_rules(tweepy.StreamRule(keyword))
printer.filter()

connection.close()