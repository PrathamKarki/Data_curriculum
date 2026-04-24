from confluent_kafka import Producer
import json

# setting up the producer
p = Producer(
    {
        'bootstrap.servers': 'localhost:9092'
    }
)

fake_api = {"name": "Test Concert", "city": "London", "attendance": 9903}


# definign funcition for checking

def test_function(err, msg):
    if err is not None:
        print(f"Message is delivered {msg}" )
    else:
        print(f"Success! Message delivered to {msg.topic()}")


print("Attempting to send message")
p.produce('metro_events',
          json.dumps(fake_api).encode('utf-8'),
          callback = test_function)