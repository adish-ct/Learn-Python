import threading


def background_task():
    pass


def main():
    thread = threading.Thread(target=background_task)
    thread.start()
    return True

