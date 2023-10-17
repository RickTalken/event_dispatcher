from dispatcher import Message
from handlers import handle_event

# Create a rain event which will get handled by handlers.handle_precipitation_event()
# >> A RainEvent was triggered: Bring an umbrella today.
rain_event = Message(event_type="RainEvent", data={"volume": "light"})
handle_event(rain_event)

# Create a snow event which also will get handled by handlers.handle_precipitation_event()
# >> A SnowEvent was triggered: Bring an umbrella today.
snow_event = Message(event_type="SnowEvent", data={"volume": "medium"})
handle_event(snow_event)

# Create a tornado event which will get handled by handlers.handle_tornado_event()
# >> A TornadoEvent was triggered: Take cover!
tornado_event = Message(
    event_type="TornadoEvent", data={"class": "EF1", "mph_wind_speed": 100}
)
handle_event(tornado_event)

# Create a blizzard event which will get handled by handlers.handle_blizzard_event()
# >> A BlizzardEvent was triggered: Find your snow shovel!
blizzard_event = Message(
    event_type="BlizzardEvent", data={"mph_wind_speed": 45, "visibility": 0}
)
handle_event(blizzard_event)

# Create a hurricane event. No handler was registered for this event so it will get
# handled by the default handlers.handle_event()
# >> This event type was not handled!
hurricane_event = Message(
    event_type="HurricaneEvent", data={"category": 4, "mph_wind_speed": 145}
)
handle_event(hurricane_event)
