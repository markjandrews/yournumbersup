import argparse
import json
import os
import random
import sys

from config import configs
from yournumbersup import remote, stats

SCRIPT_DIR = os.path.dirname(__file__)

numpicks_per_file = 50


def chunked(iterable, chunksize):
    n = len(iterable) // chunksize
    if len(iterable) % chunksize != 0:
        n += 1

    return (iterable[i * chunksize:i * chunksize + chunksize]
            for i in range(n))


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser(description='Generate numbers to be played for drawing')
    parser.add_argument('game', choices=configs.keys())
    parser.add_argument('-s', '--total-spend', type=float, required=True)

    args = parser.parse_args(argv)

    # Get results
    config = configs[args.game]

    games_count = int(args.total_spend * 100) // int(config.cost_per_game * 100)

    processor = config.draw_klass()
    for result in remote.pull_results(args.game, config.uri, remote=True):
        processor.parse_previous_draw(result)

    # Get Previous numpicks_per_file
    previous_picked_list = []
    output_name = '%s_output' % args.game
    output_file = os.path.join(SCRIPT_DIR, 'picked_numbers', '%s_%s.json' % (output_name, int(args.total_spend)))

    if os.path.exists(output_file):
        with open(output_file, 'r') as inf:
            previous_picked_list = json.load(inf)

    # Check prevous picked list
    picked_list = []
    for balls, sups in previous_picked_list:

        if sups is not None and not isinstance(sups, list):
            sups = [sups]

        balls, sups = processor.valid_draw(balls, sups)
        picked_list.append([balls, sups])

    while games_count - len(picked_list) > 0:
        picked_list.append([*processor.valid_draw(None, None)])

    picked_list.sort()

    output_file = os.path.join(SCRIPT_DIR, 'picked_numbers', '%s_%s.json' % (output_name, int(args.total_spend)))
    with open(output_file, 'w') as outf:
        json.dump(picked_list, outf, separators=(',', ':'))

    output_file = os.path.join(SCRIPT_DIR, 'picked_numbers', '%s_%s.txt' % (output_name, int(args.total_spend)))
    with open(output_file, 'w') as outf:
        for balls, sups in picked_list:
            outf.write(', '.join([str(x) for x in balls]))

            if sups is not None:
                outf.write(' : ')
                outf.write(', '.join([str(x) for x in sups]))

            outf.write('\n')

if __name__ == '__main__':
    main()
