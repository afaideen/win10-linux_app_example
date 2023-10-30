
# In win10 wsl linux:debian turn on redis server (Make sure redis server is installed!).
# Test below script under win10 environment.
import redis

# Create a connection to the Redis server
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
conn = None
try:
    # Ping the Redis server
    response = redis_client.ping()

    if response:
        print("Connection to Redis is OK.")
        conn = 1
    else:
        print("Failed to connect to Redis.")
except redis.exceptions.ConnectionError as e:
    print("Connection error:", str(e))
except Exception as e:
    print("An error occurred:", str(e))

if conn == 1:
    # Set a key-value pair in Redis
    redis_client.set('my_key', 'Hello, Redis!')

    # Retrieve the value by key
    value = redis_client.get('my_key')
    print("Retrieved value:", value.decode('utf-8'))


    e = 1

    # Increment a key's value
    redis_client.incr('counter')
    counter_value = redis_client.get('counter')
    print("Counter value:", counter_value.decode('utf-8'))

    # List example: Push values to a list
    redis_client.rpush('my_list', 'Item 1', 'Item 2', 'Item 3')

    # Retrieve values from the list
    list_values = redis_client.lrange('my_list', 0, -1)
    print("List values:", [value.decode('utf-8') for value in list_values])

    # Set example: Add values to a set
    redis_client.sadd('my_set', 'Value 1', 'Value 2', 'Value 3')

    # Retrieve values from the set
    set_values = redis_client.smembers('my_set')
    print("Set values:", [value.decode('utf-8') for value in set_values])

e = 1