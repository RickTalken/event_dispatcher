from dispatcher import Message, event_dispatcher


@event_dispatcher
def handle_event(message: Message):
    """
    This is the base handler. Calling it will dispatch events/messages to the handler function registered to handle that event.
    If there is no handler registered for the event type, it will handle the event itself.
    """
    print("This event type was not handled!")


@handle_event.register("RainEvent", "SnowEvent")
def handle_precipitation_event(message: Message):
    """ This is an example of a handler that has been registered for a multiple event types."""
    print(f"A {message.event_type} was triggered: Bring an umbrella today.")

@handle_event.register("TornadoEvent")
def handle_tornado_event(message: Message):
    """ This is an example of a handler that has been registered for a single event type."""
    print(f"A {message.event_type} was triggered: Take cover!")


@handle_event.register("BlizzardEvent")
def handle_blizzard_event(message: Message):
    """ This is an example of a handler that has been registered for a single event type."""
    print(f"An {message.event_type} was triggered: Find your snow shovel!")


