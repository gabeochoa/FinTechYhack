from keys import fiscalnotekey
import fiscalnote as fn
from pprint import pprint


def main():
    client = fn.FiscalNoteClient(fiscalnotekey)
    john_data = client.legislators(q='john')
    pprint(john_data)


if __name__ == '__main__':
    main()
