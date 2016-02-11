# rideem API - Python client

A python client for interacting with https://rideem.io — a free, simple promo code distribution service

### Use It

Import rideem and create an API instance.
```python
import rideem
redeem = rideem.API()
```

Using an existing app key.
```python
redeem = rideem.API('68775d9fd015c55268b043cdc12b0b3fe7535b08fef454b60a22b5e149cd439d')
```

All operations return a tuple of (dict, status).

### Redeeming Codes

Redeem a code from an app named.
```python
>>> redeem.code_from('app')
({u'code': u'code_value_3', u'delay': 10}, 200)
```

Redeem a code from an app for a promo.
```python
>>> redeem.code_from('app', 'promo')
({u'code': u'code_value_3', u'delay': 10}, 200)
```

Redeem a code from an app for a private promo using a promo key.
```python
>>> redeem.code_from('app', 'promo', key = '2864b4dc5be1e7390dd709abe1ea47e4e9017677')
({u'code': u'code_value_2', u'delay': 10}, 200)
```

### Requesting Apps

Request to add this app.
```python
>>> redeem.request('app')
({u'count': 28}, 201)
```

### Create An App

Create an app named 'app'.
```python
redeem.create_app('app')
({u'created': u'2016-02-11T19:11:58.771943',
  u'email': None,
  u'key': u'68775d9fd015c55268b043cdc12b0b3fe7535b08fef454b60a22b5e149cd439d',
  u'name': u'app',
  u'promos': [],
  u'valid': False},
 201)
```

### Create A Promo for an App

Create a promo for an app.
```python
>>> redeem.create_promo_for(app, codes = ['code_value_1', 'code_value_2', 'code_value_3'])
({u'codes': [u'code_value_1', u'code_value_2', u'code_value_3'],
  u'created': u'2016-02-11T22:28:59.800970',
  u'delay': 60,
  u'end': None,
  u'key': u'ffb1a1202d9cfa80e65e8693b2da98cdc81706ad',
  u'last': u'2016-02-11T22:28:59.800977',
  u'name': u'promo',
  u'private': False,
  u'start': None,
  u'uri': u'/from/app'},
 201)
```

Create promo 'promo' for an app with a 10 second delay between codes.
```python
>>> redeem.create_promo_for(app, 'promo', ['code_value_1', 'code_value_2', 'code_value_3'], delay = 10)
({u'codes': [u'code_value_1', u'code_value_2', u'code_value_3'],
  u'created': u'2016-02-11T22:28:59.800970',
  u'delay': 10,
  u'end': None,
  u'key': u'b419b058fffad8e7e7e41287d8f5a0f8e9cf9b6f',
  u'last': u'2016-02-11T22:28:59.800977',
  u'name': u'promo',
  u'private': False,
  u'start': None,
  u'uri': u'/from/app/for/promo'},
 201)
```

### Update a Promo for an App

```python
redeem.update_promo_for(app, promo)
```

### Get Promos from an App

```python
redeem.get_promo_from(app)
```

```python
redeem.get_promo_from(app, name = 'promo')
```

### Delete Promos from an App

```python
redeem.delete_promo_from(app, promo)
```

### Example

Check the examples/ folder for an example.


