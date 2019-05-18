import asyncio
import random
import logging
from collections import namedtuple
import uuid
import string

logging.basicConfig(level=logging.INFO)

Message = namedtuple("Message", ["msg_id", "inst_name"])


def main():
    queue = asyncio.Queue()
    loop = asyncio.get_event_loop()

    try:
        loop.create_task(publisher(queue))
        loop.create_task(consumer(queue))
        loop.run_forever()
    except KeyboardInterrupt:
        logging.info("Process interrupted")
    finally:
        logging.info("Cleaning up")
        loop.close()


async def publisher(queue):
    choices = string.ascii_lowercase + string.digits
    while True:
        data = "".join(random.choices(choices, k=4))
        msg = Message(msg_id=str(uuid.uuid4()), inst_name=f"{data}")
        asyncio.create_task(queue.put(msg))
        logging.info(f"Published {msg}")
        # simulate randomness of publishing messages
        await asyncio.sleep(random.random())


async def consumer(queue):
    while True:
        msg = await queue.get()
        logging.info(f"Consumed {msg}")

        asyncio.create_task(save_data(msg))


async def save_data(msg):
    # simulation of IO operation
    await asyncio.sleep(random.random())
    logging.info(f"data {msg} has been saved")


asyncio.run(main())
