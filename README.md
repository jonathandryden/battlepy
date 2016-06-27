# BattleNet API Wrapper in Python
#### Version 0.1.0

Register for an API key at https://dev.battle.net

## Versions
### 0.1.0
 - WoW API

## Todo
 - Community API
 - D3 API
 - SC2 API
 - OAuth

## Requirements
 - requests install via  ```pip install requests```

## Usage
```
from battlepy.api_client import Client

bnet = Client(API_KEY, REGION, LOCALE)
resp = bnet.wow.get_quest(13146)
```

This will return a JSON object like below

```
{
    "id": 13146,
    "title": "Generosity Abounds",
    "reqLevel": 77,
    "suggestedPartyMembers": 0,
    "category": "Icecrown",
    "level": 80
}
```

## License
This library is copyright Jonathan Dryden and licensed for use under MIT.
Please see LICENSE for more information.

Battle.net, Warcraft, World of Warcraft, StarCraft and Diablo are copyrighted by Blizzard Entertainment, Inc.
This library is neither endorsed by nor associated with Blizzard Entertainment, Inc.