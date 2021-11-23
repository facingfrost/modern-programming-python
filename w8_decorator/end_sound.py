from playsound import playsound
from functools import wraps


def music(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        playsound(u"song.mp3")

    return wrapper


@music
def print_happy():
    print("happy!")


if __name__ == "__main__":
    print_happy()
