from dispatcher import Message
from handlers import handle_event


rain_event = Message(event_type="RainEvent", data={"volume": "light"})
snow_event = Message(event_type="SnowEvent", data={"volume": "medium"})
tornado_event = Message("TornadoEvent", {"class": "EF1", "mph_wind_speed": 100})
blizzard_event = Message("BlizzardEvent", {"mph_wind_speed": 45, "visibility": 0})
hurricane_event = Message("HurricaneEvent", {"category": 4, "mph_wind_speed": 145})

handle_event(rain_event)
handle_event(snow_event)
handle_event(tornado_event)
handle_event(blizzard_event)
handle_event(hurricane_event)
