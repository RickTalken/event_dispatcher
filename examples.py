from dispatcher import Message, event_dispatcher


@event_dispatcher
def handle_event(message: Message):
    """
    This is the base handler. Calling it will dispatch events/messages to the handler function registered to handle that event.
    If there is no handler registered for the event type, it will handle the event itself.
    """
    print("This event type was not handled!")


@handle_event.register("PersonEvent")
def handle_person_event(message: Message):
    """ This is an example of a handler that has been registered for a single event type."""
    print(f"You triggered a person event for {message.data['name']}!")


@handle_event.register("DogEvent", "CatEvent")
def handle_pet_event(message: Message):
    """ This is an example of a handler that has been registered for a multiple event types."""
    print(
        f"You triggered a pet event for {message.data['name']} ({message.data['breed']})!"
    )