import rideem

import sys
import time

if __name__ == "__main__":
    redeem = rideem.API()

    app, status = redeem.get_app('app')
    if status == 200: # app exists
        print('App already exists.')
        print(redeem.verify('app', 'token')) # verify an app without link
        sys.exit(1)

    app, status = redeem.create_app('app') # create it
    print(app, status)

    app['email'] = 'test@example.com' # modify it
    print(redeem.update_app(app)) # update it

    # create a promo
    promo, status = redeem.create_promo_for(app, codes = ['code1', 'code2'],
                                            delay = 1)
    print(promo, status)

    # redeem some codes
    print()
    code, status = redeem.code_from(app, promo)
    print(code, status)
    if status == 200:
        time.sleep(code['delay'])
    print(redeem.code_from(app))
    print()

    # update promo
    promo['private'] = True
    print(redeem.update_promo_for(app, promo))

    print(redeem.delete_promo_from(app, promo))

    promo, status = redeem.create_promo_for(app, name = 'promo',
                                            codes = ['code1', 'code2', 'code3'],
                                            delay = 1,
                                            private = True)
    print(promo, status)

    print()
    print(redeem.code_from('app', 'promo')) # will fail without app or promo key
    print(redeem.code_from('app', 'promo', key = promo['key']))
    print(redeem.code_from(app, promo)) # promo key used automatically
    print(redeem.code_from(app, 'promo')) # may fail without delaying; app key used
    print()

    print(redeem.get_promo_from(app, 'promo'))
    print(redeem.delete_promo_from(app, promo))

    print(redeem.request('app'))
    print(redeem.request(app))
    print(redeem.request('app', True))
    print(redeem.request(app, True))

    print(redeem.delete_app(app))

    print(redeem.code_from('app'))
    print(redeem.code_from('app', 'promo'))
    print(redeem.code_from('app', key = 'key'))
