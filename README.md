# Event Dispatcher Example

This example demonstrates using *dictionary dispatching* to implement event handlers. Rather than a block of conditional logic (`if/else` statements), I use a dictionary to register, lookup, and invoke event handlers (functions) given a key. This pattern is used by popular Python libraries like Flask and FastAPI to dispatch requests. It is also used by the [functools.singledispatch()](https://docs.python.org/3/library/functools.html#functools.singledispatch) decorator to implement function overloading based on the type of the function's first argument.

This example is a simplified version of an event dispatacher I built to register event handlers for events arriving from Kafka in an event-driven architecture. Metadata in each Kafka message (event) includes a key to identify the event type which is then used to dispatch the event to the appropriate handler.

- `dispatcher.py` defines the `@event_dispatcher` decorator. The `registry` function member is the dictionary from which handlers are registered and invoked. The `Message` dataclass is also defined here for simplicity.
- `handlers.py` defines the event handler functions for the events that we intend to handle as well as a default handler.
- `examples.py` provides an example of using this event dispatcher. It creates some example messages and then calls the `handlers.handle_event()` function to lookup the event handler based on the event type in the `Message`.