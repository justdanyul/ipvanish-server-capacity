import argparse
from ipvanish.services import IPVanishService


def print_results(results):
    for result in results:
        print(result)


def main():
    parser = argparse.ArgumentParser(prog='ipvcap', description='Prints the status of IPVanish servers.')
    parser.add_argument('-c', '--country', help='Show servers in this country only')
    args = parser.parse_args()

    ipvanish = IPVanishService()
    print_results(ipvanish.search('http://www.ipvanish.com/api/servers.geojson', args))


if __name__ == "__main__":
    main()
