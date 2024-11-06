import json
import os
from azure.eventhub import EventHubProducerClient, EventData
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Connect to Event Hub
    connection_str = os.getenv("EVENTHUB_CONNECTION")
    eventhub_name = os.getenv("EVENTHUB_NAME")
    producer = EventHubProducerClient.from_connection_string(connection_str, eventhub_name=eventhub_name)
    
    # Sample data to publish
    data = {"value": 20}
    
    # Send the event
    event_data_batch = producer.create_batch()
    event_data_batch.add(EventData(json.dumps(data)))
    producer.send_batch(event_data_batch)
    producer.close()

    return func.HttpResponse("Message sent to Event Hub", status_code=200)