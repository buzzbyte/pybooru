# Pybooru - Library for Danbooru/Moebooru API.
A fork of [Pybooru](http://github.com/LuqueDaniel/pybooru) by Daniel Luque.

**Pybooru** is a Python library to access API of Danbooru/Moebooru based sites.

This fork adds the missing API for Danbooru v2 and a few others.

- Version: **3.1.0**
- Licensed under: **MIT License**

## Dependencies.
- Python: >= 2.6 or Python: >= 3
- [requests.](http://docs.python-requests.org/en/latest/)

## Installation

### Manual installation
```bash
git clone git://github.com/luquedaniel/pybooru.git
cd pybooru
sudo python setup.py build
sudo python setup.py install
```

## Examples of use
```python
from pybooru import Pybooru

client = Pybooru('Konachan')

artists = client.artists('ma')

for artist in artists:
    print("Name: {0}".format(artist['name']))
```

### Login example
#### Default sites
```python
from pybooru import Pybooru

client = Pybooru('Konachan', username='your-username', password='your-password')

client.comments_create(post_id=id, comment_body='Comment content')
```

#### Other sites
```python
from pybooru import Pybooru

client = Pybooru('konachan.com', username='your-username', password='your-password',
                 hashString='So-I-Heard-You-Like-Mupkids-?--{0}--')

client.comments_create(post_id=id, comment_body='Comment content')
```

[More examples.](https://github.com/buzzbyte/pybooru/tree/master/examples)

## License
- **[See MIT License](https://github.com/LuqueDaniel/pybooru/blob/master/LICENSE)**
