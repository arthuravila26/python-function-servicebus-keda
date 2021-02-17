import os
import sys
import time
from logger import logger
from azure.servicebus import ServiceBusClient, ServiceBusMessage

connection_string = os.environ['AzureWebJobsStorage']
queue_name = os.environ['QUEUE_NAME']

queue = ServiceBusClient.from_connection_string(conn_str=connection_string, queue_name=queue_name)


def send_a_list_of_messages(sender):
    messages = [ServiceBusMessage("Message in list") for _ in range(100)]
    sender.send_messages(messages)
    logger.info("Sent a list of 100 messages")


with queue:
    sender = queue.get_queue_sender(queue_name=queue_name)
    with sender:
        send_a_list_of_messages(sender)

logger.info("Done sending messages")
logger.info("-----------------------")
