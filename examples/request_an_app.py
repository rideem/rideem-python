import rideem

if __name__ == "__main__":
    redeem = rideem.API()
    count, status = redeem.request('app')

    print(count, status)
