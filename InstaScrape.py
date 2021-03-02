from time import sleep
from instapy import InstaPy
from instapy.util import smart_run
from lib import Scrape
import argparse

def main():
    thread_count = None

    parser = argparse.ArgumentParser(description="Input Thread")
    parser.add_argument('-tc', metavar='--thread', type=int, help='thread number')
    parser.add_argument('-u', metavar='--username', type=str, help='Username Instagram')
    parser.add_argument('-p', metavar='--password', type=str, help='Password Instagram')
    parser.add_argument('-t', metavar='--target', type=str, help='Password Instagram')
    args = parser.parse_args()
    thread_count = args.tc
    username = args.u
    password = args.p
    target = args.t

    session = InstaPy(username=username,
                  password=password,
                  headless_browser=True)
    with smart_run(session):
        followers = session.grab_followers(username=target, amount='full', live_match=True)

    scrape = Scrape.Scrape(username, target, thread_count)
    scrape.run()

if __name__ == '__main__':
    main()