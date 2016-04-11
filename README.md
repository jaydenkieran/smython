# smite-python

Simple wrapper around Smite's API, allowing basic functionality and the ability to make various calls.

## Prerequisites

+ Python 3.5

## How to use

If you do not already have a developer ID and API key, you can obtain one by filling out [this form](https://fs12.formsite.com/HiRez/form48/secure_index.html)

1. Place `smite.py` into the project path you would like to use it in.
2. Import the `SmiteClient` class, e.g `from test.smite import SmiteClient`
3. Initialize the class, e.g `smite = SmiteClient(devID, apiKey)`
4. Call the method you want to use, e.g `data = client.get_player("JaydenKieran")`

After obtaining the data, you can do what you want with it, such as print specific keys to the console.

## Credits

+ Jayden Bailey - **Developer**
+ Originally forked from [RichardJTorres/smython](https://github.com/RichardJTorres/smython)

## License

`smite-python` is provided under the MIT License, which you can view in `license.txt`. Essentially, you can do what you want with the code as long as it is attributed back to myself/this project page.
