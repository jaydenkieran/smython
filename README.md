# smite-python
Simple wrapper around Smite's API, allowing basic functionality and the ability to make various calls. All method calls will return as a `JSON` string which can then be iterated over.

## Prerequisites
- Python 3.5
- `smite-python` uses libraries that *should* come packaged with Python

## How to use
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

## FAQ
### How do I get a devId and authKey?

If you do not already have a developer ID and API key, you can obtain one by filling out [this form](https://fs12.formsite.com/HiRez/form48/secure_index.html). Hi-Rez Studios usually responds within a few days.

### Why am I getting a null dataset for a player that exists?

If a player has `Hide My Profile` enabled in-game, you will get a null dataset.

### When using methods such as `get_match(id)`, some player names/information is missing. Why?

If a player has `Hide My Profile` enabled in-game, most of their data will be unavailable. There are slight exceptions to this, such as obtaining the name of the god that was played by that person.

### Does smite-python support older versions of Python?

`smite-python` only supports Python 3.5 and higher. However, if you are using Python 3.4 then you can use [smython](https://github.com/RichardJTorres/smython), which is the original project that was forked. Be aware though that `smython` is outdated and does not contain all possible API calls. It also, unlike this project, does not support the Xbox and PS4 gateways.

### Why do some functions break when using different endpoints?

Not all functions are supported by all endpoints. The only endpoint guaranteed to work with all functions is the default, PC.

## License
`smite-python` is provided under the MIT License, which you can view in `license.txt`. Essentially, you can do what you want with the code as long as it is attributed back to [Jayden Bailey](http://twitter.com/jaydenkieran), and where possible, the [GitHub page](http://github.com/jaydenkieran/smite-python).

Information obtained by this script is provided by Hi-Rez Studios' `SmiteAPI` and is thus their property. According to Section 11a of the API Terms of Use, you must attribute any data provided as below.

> Data provided by Hi-Rez. © 2015 Hi-Rez Studios, Inc. All rights reserved.
