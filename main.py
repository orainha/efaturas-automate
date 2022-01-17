import argparse

import module.helpers as h
import module.selenium as s

FILEPATH = f"listagem"

def parse_cmdline():
    description = 'e-faturas insert automate '
    parser = argparse.ArgumentParser(description=description)
    required_group = parser.add_argument_group('required arguments')
    required_group.add_argument('--user', required=True, help='--user Bob')
    args = parser.parse_args()
    return args

def run(args):
    user = args.user
    faturas = h.get_faturas(FILEPATH)
    s.run(faturas, user)

def main():
    args = parse_cmdline()
    run(args)

if __name__ == '__main__':
    main()