import rideem

if __name__ == "__main__":
    redeem = rideem.API()
    code, status = redeem.code_from('app')

    print(code, status)
