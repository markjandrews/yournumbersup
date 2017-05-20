import csv
import os

import requests


def pull_results(name, url, remote=False):

    results_file = '%s_results.csv' % name

    if remote is True:
        if os.path.exists(results_file):
            os.unlink(results_file)

    if not os.path.exists(results_file):
        print('Retrieving results from: %s' % url)
        response = requests.get(url)
        with open(results_file, 'w') as outf:
            outf.write(response.text.replace('\r', ''))

    with open(results_file, 'r') as inf:
        reader = csv.reader(inf)
        next(reader)

        return [x for x in reader]
