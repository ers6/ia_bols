import os
import json
import sys
import csv


def main():
    file = "/Users/elizabethschwartz/Documents/ia-data/scan-center-ids/hongkong-ids.json"
    identifiers = json_unpacking(file)
    print(len(identifiers))
    results = []
    for this_id in identifiers[0:100]:
        results.append({'id': this_id['identifier'],
                        'metadata':get_metadata(this_id['identifier'])})
    makes_results_csv(results, "/Volumes/Samsung_T5/results.csv")


def makes_results_csv(results, outfile_name):
    headers = results[0].keys()
    rows = results
    print(rows)
    with open(outfile_name, 'w', encoding='UTF-8', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=headers)
        writer.writeheader()
        for row in rows:
            try:
                writer.writerow(row)
            except AttributeError:
                pass

def get_metadata(id):
    print(type(os.system('ia metadata ' + id)))
    # return str(os.system('ia metadata ' + id))

def json_unpacking(json_file):
    with open(json_file, 'r') as f:
        ids = json.load(f)
    return ids["docs"]
main()

