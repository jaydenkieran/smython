# smite-python

Simple wrapper around Smite's API, allowing basic functionality and the ability to make various calls.

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

## Credits

+ **Developer** - [Jayden Bailey](http://twitter.com/jaydenkieran)
+ Fork of [smython](https://github.com/RichardJTorres/smython)

## License

`smite-python` is provided under the MIT License, which you can view in `license.txt`. Essentially, you can do what you want with the code as long as it is attributed back to myself/this project page.
