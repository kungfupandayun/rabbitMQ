# rabbitMQ — Python examples

Small collection of Python example scripts that demonstrate common RabbitMQ messaging patterns using the `pika` library.

Contents
- `basic/` — simple producer/consumer example showing a single queue.
- `publisherSubscriber/` — publish/subscribe (fanout) example with a publisher and subscriber.
- `routing/` — routing (direct exchange) example demonstrating routing keys.
- `topic/` — topic exchange example using wildcard routing.
- `workQueue/` — work queues example (task producer + worker) for load distribution.
- `RPC/` — RPC-style request/response example (client and server).

Requirements
- Python 3.7+
- RabbitMQ server running locally or accessible over the network (default host `localhost`, port `5672`).
- `pika` Python package — install with:

```
pip install pika
```

Quick start

1. Start RabbitMQ (local Docker example):

```
docker run -d --hostname rabbit --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```

2. Open two terminals for simple producer/consumer examples. From the repository root run the scripts in the example folder you want to try. Examples:

- Basic (producer/consumer):
  - `python basic/producer.py` (producer)
  - `python basic/consumer.py` (consumer)

- Publisher/Subscriber (fanout):
  - `python publisherSubscriber/publisher.py`
  - `python publisherSubscriber/subscriber.py`

- Routing (direct exchange):
  - `python routing/publisher.py`
  - `python routing/subscriber.py`

- Topic exchange:
  - `python topic/publisher.py`
  - `python topic/subscriber.py`

- Work queue:
  - `python workQueue/taskProducer.py`
  - `python workQueue/worker.py` (run multiple workers to see load distribution)

- RPC (request/response):
  - `python RPC/response.py` (run the RPC server)
  - `python RPC/request.py` (run the client/requester)

Notes
- The examples are intentionally small and rely on the default RabbitMQ settings (guest/guest, `localhost:5672`). Update connection parameters in the scripts if your server differs.
- Each script is a minimal demonstration and not production hardened — use secure credentials, TLS, and connection/backoff handling for production.

Suggested next steps
- Add a `requirements.txt` (`pika`) and a `.gitignore` for Python (`__pycache__/`, `.vscode/`, `*.pyc`), then initialize a git repo and push to your remote.

License
- No license specified. Add a `LICENSE` file if you want to clarify reuse terms.
