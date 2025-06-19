import pygame
from rotary_class import RotaryEncoder

PLAYERNAME = "Markuspwn"
PLAYERLEVEL = 10
app = None #This will be set later from main.py
PLAYERNAME = "Arkangel"
PLAYERLEVEL = 15
WIDTH = 480
HEIGHT = 320

minSwipe = 50
maxClick = 15
longPressTime = 200
touchScale = 1
invertPosition = False
GPIO_AVAILABLE = True
RADIO_PLAYING = True
QUICKLOAD = False
LOAD_CACHED_MAP = True
QUICKLOAD = True
LOAD_CACHED_MAP = False
# Main

TINTCOLOUR = pygame.Color(26, 255, 128) # Green
# TINTCOLOUR = pygame.Color (46, 207, 255) # Blue
# TINTCOLOUR = pygame.Color (255, 182, 66) # Amber
# TINTCOLOUR = pygame.Color (192, 255, 255) # White


#MAP_FOCUS = (-5.9347681, 54.5889076)
#MAP_FOCUS = (-102.3016145, 21.8841274) #Old Default?
#MAP_FOCUS = (-118.5723894,34.3917171)#CodeNinjasValencia
#MAP_FOCUS = (32.7157, 117.1611)
MAP_FOCUS = (-92.1943197, 38.5653437)
#MAP_FOCUS = (-92.1943197, 38.5653437)
MAP_FOCUS = (-84.386176, 33.7604616)

WORLD_MAP_FOCUS = 0.07 #Needed to handle the 50k node limit from OSM

LOAD_CACHED_MAP = True
LOAD_CACHED_MAP = False
SOUND_ENABLED = True

EVENTS = {
    'SONG_END': pygame.USEREVENT + 1
}

MODULES = {
    0: "stats",
    1: "items",
    2: "data"
}

ACTIONS = {
    pygame.K_F1: "module_stats",
    pygame.K_F2: "module_items",
    pygame.K_F3: "module_data",
    pygame.K_1:	"knob_1",
    pygame.K_2: "knob_2",
    pygame.K_1:	"knob_down",
    pygame.K_2: "knob_up",
    pygame.K_3: "knob_3",
    pygame.K_4: "knob_4",
    pygame.K_5: "knob_5",
    pygame.K_UP: "dial_up",
    pygame.K_DOWN: "dial_down",
    pygame.K_PLUS: "zoom_in",
    pygame.K_MINUS: "zoom_out",
    pygame.K_KP_PLUS: "zoom_in",
    pygame.K_KP_MINUS: "zoom_out"
}

# Using GPIO.BCM as mode
#GPIO 23 pin16 reboot
#GPIO 25 pin 22 blank screen do not use
GPIO_ACTIONS = {
	4: "dial_down", #GPIO 23
	17: "dial_up", #GPIO 24
	22: "knob_down", #GPIO 4
	27: "knob_up", #GPIO 17
	#4: "dial_down", #GPIO 23
	#17: "dial_up", #GPIO 24
	#22: "knob_down", #GPIO 4
	#27: "knob_up", #GPIO 17
    21: "module_data", #GPIO 21
    20: "module_items", #GPIO 20
}

# Define GPIO inputs
dial_up = 26 	# Pin 8 
dial_down = 19	# Pin 10
Data = 21	# Pin 7
knob_up = 27 #GPIO 27
knob_down = 22 #GPIO 22
Items = 20 #GPIO 20

# These are the rotary knob events
def dial_event(event):
    print(f"[DIAL] Event triggered: {event}")
    if app:
        app.handle_action(event)
        
def knob_event(event):
    print(f"[KNOB] Event triggered: {event}")
    if app:
        app.handle_action(event)
    return

# Define the switch
dial = RotaryEncoder(dial_up,dial_down,"Dial",dial_event)
knob = RotaryEncoder(knob_up,knob_down,"Knob",knob_event)

#print("Pin A "+ str(dial_up))
#print("Pin B "+ str(dial_down))
#print("BUTTON "+ str(Data))

#print("Pin A "+ str(knob_up))
#print("Pin B "+ str(knob_down))
#print("BUTTON "+ str(Items))

# Listen

#while True:
	#time.sleep(0.5)

# LEDs
# pin 18, 23, 24,

MAP_ICONS = {
    "camp": 		pygame.image.load('images/map_icons/camp.png'),
    "factory": 		pygame.image.load('images/map_icons/factory.png'),
    "metro": 		pygame.image.load('images/map_icons/metro.png'),
    "misc": 		pygame.image.load('images/map_icons/misc.png'),
    "monument": 	pygame.image.load('images/map_icons/monument.png'),
    "vault": 		pygame.image.load('images/map_icons/vault.png'),
    "settlement": 	pygame.image.load('images/map_icons/settlement.png'),
    "ruin": 		pygame.image.load('images/map_icons/ruin.png'),
    "cave": 		pygame.image.load('images/map_icons/cave.png'),
    "landmark": 	pygame.image.load('images/map_icons/landmark.png'),
    "city": 		pygame.image.load('images/map_icons/city.png'),
    "office": 		pygame.image.load('images/map_icons/office.png'),
    "sewer": 		pygame.image.load('images/map_icons/sewer.png'),
    "camp": 		pygame.image.load('/home/pi/pypboy3000/images/map_icons/camp.png'),
    "factory": 		pygame.image.load('/home/pi/pypboy3000/images/map_icons/factory.png'),
    "metro": 		pygame.image.load('/home/pi/pypboy3000/images/map_icons/metro.png'),
    "misc": 		pygame.image.load('/home/pi/pypboy3000/images/map_icons/misc.png'),
    "monument": 	pygame.image.load('/home/pi/pypboy3000/images/map_icons/monument.png'),
    "vault": 		pygame.image.load('/home/pi/pypboy3000/images/map_icons/vault.png'),
    "settlement": 	pygame.image.load('/home/pi/pypboy3000/images/map_icons/settlement.png'),
    "ruin": 		pygame.image.load('/home/pi/pypboy3000/images/map_icons/ruin.png'),
    "cave": 		pygame.image.load('/home/pi/pypboy3000/images/map_icons/cave.png'),
    "landmark": 	pygame.image.load('/home/pi/pypboy3000/images/map_icons/landmark.png'),
    "city": 		pygame.image.load('/home/pi/pypboy3000/images/map_icons/city.png'),
    "office": 		pygame.image.load('/home/pi/pypboy3000/images/map_icons/office.png'),
    "sewer": 		pygame.image.load('/home/pi/pypboy3000/images/map_icons/sewer.png'),
}

AMENITIES = {
    'pub': 				MAP_ICONS['vault'],
    'nightclub': 		MAP_ICONS['vault'],
    'bar': 				MAP_ICONS['vault'],
    'fast_food': 		MAP_ICONS['settlement'],
	'cafe': 			MAP_ICONS['settlement'],
#	'drinking_water': 	MAP_ICONS['sewer'],
    'restaurant': 		MAP_ICONS['settlement'],
    'cinema': 			MAP_ICONS['office'],
    'pharmacy': 		MAP_ICONS['office'],
    'school': 			MAP_ICONS['office'],
    'bank': 			MAP_ICONS['monument'],
    'townhall': 		MAP_ICONS['monument'],
#	'bicycle_parking': 	MAP_ICONS['misc'],
    'pub': 				MAP_ICONS['city'],
    'nightclub': 		MAP_ICONS['settlement'],
    'bar': 				MAP_ICONS['city'],
    'conference_centre':MAP_ICONS['vault'],
#   'fast_food': 		MAP_ICONS['settlement'],
#	'cafe': 			MAP_ICONS['settlement'],
#	'drinking_water':  	MAP_ICONS['sewer'],
#   'restaurant': 		MAP_ICONS['settlement'],
#   'cinema': 			MAP_ICONS['office'],
    'pharmacy': 		MAP_ICONS['camp'],
#   'school': 			MAP_ICONS['office'],
#   'bank': 			MAP_ICONS['monument'],
#   'townhall': 		MAP_ICONS['monument'],
#   'bicycle_parking': 	MAP_ICONS['misc'],
#	'place_of_worship': MAP_ICONS['misc'],
#	'theatre': 			MAP_ICONS['office'],
#	'bus_station': 		MAP_ICONS['misc'],
#	'parking': 			MAP_ICONS['misc'],
#	'fountain': 		MAP_ICONS['misc'],
#	'marketplace': 		MAP_ICONS['misc'],
#	'atm': 				MAP_ICONS['misc'],
    'misc':             MAP_ICONS['misc']
	'parking': 			MAP_ICONS['metro'],
	'fountain': 		MAP_ICONS['sewer'],
	'arts_centre': 		MAP_ICONS['monument'],
	'atm': 				MAP_ICONS['misc'],
#   'misc':             MAP_ICONS['misc']
}

INVENTORY_OLD = [
"Ranger Sequoia",
"Anti-Materiel Rifle ",
"Deathclaw Gauntlet",
"Flamer",
"NCR dogtag",
".45-70 Gov't(20)",
".44 Magnum(20)",
"Pulse Grenade (2)"
]

WEAPONS = [
    "10mm Pistol",
    "Combat Knife",
    "Fragmentation Grenade (2)",
    "Laser Pistol",
    "Plasma Mine (3)"
]

ARMOR = [
    "Eyeglasses",
    "Vault 111 Jumpsuit",
    "Wedding Ring"
]

AID = [
    "Purified Water (3)",
    "Rad Away (2)",
    "Stim Pack (2)"
]

MISC = [
    "Pencil",
    "Pre-War Money (250)",
    "Super Glue",
    "Toy Mini-Nuke"
]

AMMO = [
    "10mm Rounds (15)",
    "Fusion Cells (28)"
]

QUESTS = [
    "Cosplacon",
    "Cosplay Royale",
    "Drink n Draw",
    "Queens of Cosplay"
]

SKILLS = [
    "Action Boy",
    "Animal Friend",
    "Awareness",
    "Gunslinger"
    "Hacker",
    "Mysterious Stranger",
    "Rifleman",
    "Science"   
]

PERKS = [
    "Action Boy",
    "Animal Friend",
    "Awareness",
    "Gunslinger"
    "Hacker",
    "Mysterious Stranger",
    "Rifleman",
    "Science"   
]


pygame.font.init()
FONTS = {}
for x in range(10, 28):
    FONTS[x] = pygame.font.Font('monofonto.ttf', x)
    FONTS[x] = pygame.font.Font('/home/pi/pypboy3000/fonts/monofonto.ttf', x)


kernedFontName = 'fonts/monofonto-kerned.ttf'
monoFontName = 'fonts/monofonto.ttf'
kernedFontName = '/home/pi/pypboy3000/fonts/monofonto-kerned.ttf'
monoFontName = '/home/pi/pypboy3000/fonts/monofonto.ttf'

# Scale font-sizes to chosen resolution:
FONT_SML = pygame.font.Font(kernedFontName, int (HEIGHT * (12.0 / 360)))
FONT_MED = pygame.font.Font(kernedFontName, int (HEIGHT * (16.0 / 360.0)))
FONT_LRG = pygame.font.Font(kernedFontName, int (HEIGHT * (18.0 / 360.0)))
MONOFONT = pygame.font.Font(monoFontName, int (HEIGHT * (16.0 / 360.0)))
# Find monofont's character-size:
tempImg = MONOFONT.render("X", True, TINTCOLOUR, (0, 0, 0))
charHeight = tempImg.get_height()
charWidth = tempImg.get_width()
del tempImgdel tempImg
