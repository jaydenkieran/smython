# smite-python

Simple wrapper around Smite's API, allowing basic functionality and the ability to make various calls. All method calls will return as a `JSON` string which can then be iterated over.

## Prerequisites

+ Python 3.5

## How to use

If you do not already have a developer ID and API key, you can obtain one by filling out [this form](https://fs12.formsite.com/HiRez/form48/secure_index.html)

### Setup

- Place `smite.py` into the project path you would like to use it in.
- Import `SmiteClient` into your project (and `Endpoint` if you want to switch between endpoints)
```python
from smite import SmiteClient
from smite import Endpoint
```
- Initialise the `SmiteClient` class
```python
smite = SmiteClient(devId, authKey)
```

### Switching endpoints
To switch endpoints, simply call `_switch_endpoint(Endpoint)` with a valid `Endpoint` enum

```python
smite._switch_endpoint(Endpoint.PC) # Switch endpoint to PC
smite._switch_endpoint(Endpoint.PS4) # Switch endpoint to PS4
smite._switch_endpoint(Endpoint.XBOX) # Switch endpoint to Xbox
```

### Examples
#### Testing connectivity to SmiteAPI
```python
ping = smite.ping()
print(ping)
```
#### Printing a player's account level
```python
player = smite.get_player("JaydenKieran")
for i in player:
    print(i['Account_Level'])
```

### Exceptions
When making requests, the following exceptions can be raised

+ `urllib.error.HTTPError` - Generic HTTP error
+ `smite.SmiteError` - Generic `smite.py` error

## FAQ
+ Why am I getting a null dataset for a player that exists?

If a player has Hide My Profile enabled in-game, you will get a null dataset.

+ When using methods such as `get_match(id)`, some player names/information is missing. Why?

If a player has Hide My Profile enabled in-game, most of their data will be unavailable. There are slight exceptions to this, such as obtaining the name of the god that was played by that person.

## Credits

+ **Developer** - [Jayden Bailey](http://twitter.com/jaydenkieran)
+ Fork of [smython](https://github.com/RichardJTorres/smython)

## License

`smite-python` is provided under the MIT License, which you can view in `license.txt`. Essentially, you can do what you want with the code as long as it is attributed back to myself/this project page.
