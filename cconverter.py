import requests
cache = dict()


def main_cache():
    usd_get = dict(usd=requests.get("http://www.floatrates.com/daily/usd.json").json())
    cache.update(usd_get)
    eur_get = dict(eur=requests.get("http://www.floatrates.com/daily/eur.json").json())
    return cache.update(eur_get)


def check_cache(first, second, val):
    if second in cache and first in cache[second]:
        print("Oh! It is in the cache!")
        return print(f"You received {round(val / cache[second][first]['rate'], 2)} {second.upper()}.")
    else:
        print("Sorry, but it is not in the cache!")
        update_cache(second)
        return print(f"You received {round(val / cache[second][first]['rate'], 2)} {second.upper()}.")


def update_cache(change_to):
    req = {f"{change_to}": requests.get(f"http://www.floatrates.com/daily/{change_to}.json").json()}
    return cache.update(req)


def main():
    main_cache()
    user_input_from = input().lower()
    while True:
        user_input_to = input().lower()
        if not user_input_to:
            exit()
        value = input()
        print("Checking the cache...")
        check_cache(user_input_from, user_input_to, float(value))


if __name__ == "__main__":
    main()
