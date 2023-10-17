from dataclasses import dataclass
from functools import wraps


@dataclass
class Message:
    event_type: str
    data: dict


def event_dispatcher(func):
    """
    The event_dispatcher decorator is based on the functools.singledispatch decorator.
    It accepts any number of event types to be registered to a single handler.
    """
    registry = {}

    def register(*event_types, handler_func=None):
        """
        Register handler for each event type.

        Recursion is done to get the true name of the wrapped function that is being registered. I think this was done 
        to allow this decorator to work stacked on top of other decoraters.
        """
        if handler_func is None:
            return lambda f: register(*event_types, handler_func=f)
        for event_type in event_types:
            registry[event_type] = handler_func
        return handler_func

    @wraps(func)
    def wrapper(message):
        """
        Lookup the handler function for the event type from the message and invoke that handler.
        If the event type isn't registered, call the generic handler to process the message (or ignore it).
        """
        handler = registry.get(message.event_type, func)
        return handler(message)

    registry[None] = func
    wrapper.register = register  # add the nested register() function to the registry
    return wrapper
