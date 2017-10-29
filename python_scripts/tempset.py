## Adjust heating threshold in location.
# Locations are House or Hutch
# Works in conjunction with turning on the heating switch
# and turning off the weekday only switch to allow it to fire
# on a weekend
# Expected input format from intent_script
#  {"Room": "a.hutch",
#   "temperature": "a.20"}

tempIn = data.get('temperature')
roomIn = data.get('Room')
temp = tempIn.split(".")
room = roomIn.split(".")
entity_id = "climate." + room[1]
data = { "entity_id" : entity_id, "temperature" : temp[1] }
hass.services.call('climate', 'set_temperature', data)