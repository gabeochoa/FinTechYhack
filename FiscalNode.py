from keys import fiscalnotekey
import fiscalnote as fn
from pprint import pprint


def main():
    client = fn.FiscalNoteClient(fiscalnotekey)
    #res = client.getFriends("CTL000104")
    res = client.getPersonFromID("CTL000104")

    pprint(res)

if __name__ == '__main__':
    main()
