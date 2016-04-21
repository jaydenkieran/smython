"""
    smite-python (github.com/jaydenkieran/smite-python)
    Distributed under the MIT License by Jayden Bailey
"""
import hashlib
from enum import Enum
from urllib.request import urlopen

import json

from datetime import datetime

class Endpoint(Enum):
    PC = "http://api.smitegame.com/smiteapi.svc/"
    PS4 = "http://api.ps4.smitegame.com/smiteapi.svc/"
    XBOX = "http://api.xbox.smitegame.com/smiteapi.svc/"

class SmiteClient(object):
    _BASE_URL = Endpoint.PC
    _RESPONSE_FORMAT = 'Json'

    def __init__(self, dev_id, auth_key, lang=1):
        """
        :param dev_id: Your private developer ID supplied by Hi-rez. Can be requested here: https://fs12.formsite.com/HiRez/form48/secure_index.html
        :param auth_key: Your authorization key
        :param lang: the language code needed by some queries, default to english.
        """
        self.dev_id = str(dev_id)
        self.auth_key = str(auth_key)
        self.lang = lang
        self._session = None


    def _make_request(self, methodname, parameters=None):
        if not self._session or not self._test_session(self._session):
            print("Creating new SmiteAPI session")
            self._session = self._create_session()

        url = self._build_request_url(methodname, parameters)
        html = urlopen(url).read()
        return json.loads(html.decode('utf-8'))

    def _build_request_url(self, methodname, parameters=()):
        signature = self._create_signature(methodname)
        timestamp = self._create_now_timestamp()
        session_id = self._session.get("session_id")


        path = [methodname + SmiteClient._RESPONSE_FORMAT, self.dev_id, signature, session_id, timestamp]
        if parameters:
            path += [str(param) for param in parameters]
        return SmiteClient._BASE_URL + '/'.join(path)

    def _create_session(self):
        signature = self._create_signature('createsession')
        url = '{0}/createsessionJson/{1}/{2}/{3}'.format(SmiteClient._BASE_URL, self.dev_id, signature, self._create_now_timestamp())
        html = urlopen(url).read()
        return json.loads(html.decode('utf-8'))

    def _create_now_timestamp(self):
        datime_now = datetime.utcnow()
        return datime_now.strftime("%Y%m%d%H%M%S")

    def _create_signature(self, methodname):
        now = self._create_now_timestamp()
        return hashlib.md5(self.dev_id.encode('utf-8') + methodname.encode('utf-8') + self.auth_key.encode('utf-8') + now.encode('utf-8')).hexdigest()

    def _test_session(self, session):
        methodname = 'testsession'
        timestamp = self._create_now_timestamp()
        signature = self._create_signature(methodname)
        path = "/".join(
            [methodname + self._RESPONSE_FORMAT, self.dev_id, signature, session.get("session_id"), timestamp])
        url = self._BASE_URL + path
        html = urlopen(url).read()
        return "successful" in json.loads(html.decode('utf-8'))

    def _switch_endpoint(self, endpoint):
        if not isinstance(endpoint, Endpoint):
            raise TypeError("Switch endpoint method requires Endpoint type argument")
        self._BASE_URL = endpoint.value

    def ping(self):
        """
        :return: Indicates whether the request was successful
        """
        url = '{0}/ping'.format(SmiteClient._BASE_URL)
        html = urlopen(url).read()
        return json.loads(html.decode('utf.8'))

    def get_data_used(self):
        """
        :return : Returns a dictionary of daily usage limits and the stats against those limits
        """
        return self._make_request('getdataused')

    def get_demo_details(self, match_id):
        """
        :param match_id: ID of the match
        :return: Returns information regarding a match (better to use get_match_details)
        """
        return self._make_request('getdemodetails', [match_id])

    def get_gods(self):
        """
        :return: Returns all smite Gods and their various attributes
        """
        return self._make_request('getgods', [self.lang])

    def get_items(self):
        """
        :return: Returns all Smite items and their various attributes
        """
        return self._make_request('getitems', [self.lang])

    def get_god_recommended_items(self, god_id):
        """
        :param god_id: ID of god you are quering against. Can be found in get_gods return result.
        :return: Returns a dictionary of recommended items for a particular god
        """
        return self._make_request('getgodrecommendeditems', [god_id])

    def get_esports_proleague_details(self):
        """
        :return: Returns the matchup information for each matchup of the current eSports pro league session.
        """
        return self._make_request('getesportsproleaguedetails')

    def get_top_matches(self):
        """
        :return: Returns the 50 most watch or most recent recorded matches
        """
        return self._make_request('gettopmatches')

    def get_match_details(self, match_id):
        """
        :param match_id: The id of the match
        :return: Returns a dictionary of the match and it's attributes.
        """
        return self._make_request('getmatchdetails', [match_id])

    def get_match_ids_by_queue(self, queue, date, hour=-1):
        """
        :param queue: The queue to obtain data from
        :param date: The date to obtain data from
        :param hour: The hour to obtain data from (0-23, -1 = all day)
        :return: Returns a list of all match IDs for a specific match queue for given time frame
        """
        return self._make_request('getmatchidsbyqueue', [queue, date, hour])

    def get_league_leaderboard(self, queue, tier, season):
        """
        :param queue: The queue to obtain data from
        :param tier: The tier to obtain data from
        :param season: The season to obtain data from
        :return: Returns the top players for a particular league
        """
        return self._make_request('getleagueleaderboard', [queue, tier, season])

    def get_league_seasons(self, queue):
        """
        :param queue: The queue to obtain data from
        :return: Returns a list of seasons for a match queue
        """
        return self._make_request('getleagueseasons', [queue])

    def get_team_details(self, clan_id):
        """
        :param clan_id: The id of the clan
        :return: Returns the details of the clan in a python dictionary
        """
        return self._make_request('getteamdetails', [clan_id])

    def get_team_match_history(self, clan_id):
        """
        :param clan_id: The ID of the clan.
        :return: Returns a history of matches from the given clan.

        NOTE: Be aware that this method is deprecated and will return a null dataset
        """
        return self._make_request('getteammatchhistory', [clan_id])

    def get_team_players(self, clan_id):
        """
        :param clan_id: The ID of the clan
        :return: Returns a list of players for the given clan.
        """
        return self._make_request('getteamplayers', [clan_id])

    def search_teams(self, search_team):
        """
        :param search_team: The string search term to search against
        :return: Returns high level information for clan names containing search_team string
        """
        return self._make_request('searchteams', [search_team])

    def get_player(self, player_name):
        """
        :param player_name: the string name of a player
        :return: Returns league and non-league high level data for a given player name
        """
        return self._make_request('getplayer', [player_name])

    def get_player_achievements(self, player_id):
        """
        :param player_id: ID of a player
        :return: Returns a select number of achievement totals for the specified player ID
        """
        return self._make_request('getplayerachievements', [player_id])

    def get_player_status(self, player_name):
        """
        :param player_name: the string name of a player
        :return: Returns the current online status of a player
        """
        return self._make_request('getplayerstatus', [player_name])

    def get_friends(self, player):
        """
        :param player: The player name or a player ID
        :return: Returns a list of friends
        """
        return self._make_request('getfriends', [player])

    def get_god_ranks(self, player):
        """
        :param player: The player name or player ID
        :return: Returns the rank and worshippers value for each God the player has played
        """
        return self._make_request('getgodranks', [player])

    def get_match_history(self, player):
        """
        :param player: The player name or player ID
        :return: Returns the recent matches and high level match statistics for a particular player.
        """
        return self._make_request('getmatchhistory', [str(player)])

    def get_match_player_details(self, match_id):
        """
        :param match_id: The ID of the match
        :return: Returns player information for a live match
        """
        return self._make_request('getmatchplayerdetails', [match_id])

    def get_motd(self):
        """
        :return: Returns information about the most recent Match of the Days
        """
        return self._make_request('getmotd')

    def get_queue_stats(self, player, queue):
        """
        :param player: The player name or player ID
        :param queue: The id of the game mode
        :return: Returns match summary statistics for a player and queue
        """
        return self._make_request('getqueuestats', [str(player), str(queue)])
