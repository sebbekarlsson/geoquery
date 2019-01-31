from geoquery import query
import argparse
import json


def run():
    ap = argparse.ArgumentParser()

    ap.add_argument('--country_code', type=str, required=True)
    ap.add_argument('--latitude', type=float, required=True)
    ap.add_argument('--longitude', type=float, required=True)

    args = ap.parse_args()

    for row in query(
        args.country_code,
        dict(
            latitude=args.latitude,
            longitude=args.longitude
        )
    ):
        print(json.dumps(row, indent=4, sort_keys=True))
