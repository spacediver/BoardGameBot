import re
import datetime

from collections import OrderedDict

# BOT
botUsername = "BoardGameTestBot"
botName = "BoardGameTestBot"
"""Default bot name, it is set at startup using Telegram API."""

# LOG
logfileName = "log/logfile_" + str(datetime.date.today()) + ".log"

# HTTP
DEFAULT_API_PATH = "http://www.boardgamegeek.com/xmlapi2/"
DEFAULT_REQUEST_TIMEOUT = 60
REQUEST_KEYWORDS = {"id_search": "thing", "name_search": "search"}
"""Dictionary used by the :mod:`tools.http` module to construct BGG API queries."""
ATTEMPTS_LIMIT = 3

BOARDGAMEGEEK_BASE_ADDRESS = r"https://www.boardgamegeek.com/boardgame/"

# COMMANDS
COMMAND_DESCRIPTIONS = OrderedDict([
            ("/b", "Search for a boardgame by name and returns a list of matches."),
            ("/e", "Same as the previous one, but only returns exact matches."),
            ("/n", "Get info about the n-th boardgame in a list. EXAMPLE: /12 looks for the 12-th result. RESTRICTION: Only works with the most recent list search."),
            ("/i", "Search for a boardgame by ID and returns game info."),
            ("/help", "Print this help.")
        ])
"""A description of the bot normal commands, to display to users."""

INLINE_COMMAND_DESCRIPTIONS = OrderedDict([
    ("r", "Returns the list of the most recent boardgames found chatting with the bot in the private chat."),
    ("i", "Search for a boardgame by ID and returns game info.")
])
"""A description of the bot inline commands, to display to users."""

# INPUT
def defineREGEXPs():
    # Postpones REGEXPs definition until later, when botUsername and botName will be know
    global COMMAND_REGEXP
    global ARGUMENT_REGEXP
    global QUERY_REGEXP
    global CALLBACK_DATA_SEPARATOR
    global CALLBACK_GAME_DATA
    global CALLBACK_LIST_DATA
    global INLINE_COMMAND_REGEXP
    global INLINE_QUERY_REGEXP    
    global QUERY_LIST_REGEXP

    COMMAND_REGEXP = r"^\/([a-zA-Z]+)(?:@(?:" + re.escape(botUsername) + "|" + re.escape(botName) + "))?"
    ARGUMENT_REGEXP = r"(?: (.*))?"
    QUERY_REGEXP = re.compile(COMMAND_REGEXP + ARGUMENT_REGEXP)

    CALLBACK_DATA_SEPARATOR = "--"
    CALLBACK_GAME_DATA = re.compile(r"^(l|m)([0-9]+)$")
    CALLBACK_LIST_DATA = re.compile(r"^(p|n)(.*)" + CALLBACK_DATA_SEPARATOR + r"([0-9]+)$")

    INLINE_COMMAND_REGEXP = r"(?:\/)?([a-z])"
    INLINE_QUERY_REGEXP = re.compile(INLINE_COMMAND_REGEXP + ARGUMENT_REGEXP)

    QUERY_LIST_REGEXP = re.compile(r"^\/([0-9]+)(?:@" + botName + ")?$")

# BGG OBJECTS
BGG_TYPES = ["g", "l"]
"""Types of :class:`.objects.game.BggObject`."""

# ANSWER
LIST_SIZE_LIMIT=150
LIST_PAGE_SIZE = 10
MARKUP_KEYBOARD_ROW_LENGTH = 3
ANSWER_METHOD_TYPES = ["n", "c", "i", "e"]
"""Types of :class:`.objects.answer.Answer`. This must contain the same keys which are in
ANSWER_METHODS in :class:`.asyncbot.BggBot`.
"""

# HISTORY
CHAT_HISTORY_PATH = "resources/chat_history.dat"
USER_HISTORY_PATH = "resources/user_history.dat"
HISTORY_SAVING_INTERVAL = 300
RECENT_GAMES_LIMIT = 5
HISTORY_WARNING_SIZE = 268435456
"""Size in byte of the history after which a warning will be produced."""

# INLINE
INLINE_DEFAULT_PATH = "resources/inline_default.dat"
INLINE_DEFAULT = None
