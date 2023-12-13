from collections import Counter
from importlib.metadata import metadata
from pathlib import Path


def _package_metadata_as_dict(distribution_name: str = None,
                              exclude_keys: list = ['Classifier']
                              ) -> dict:
    """Get (distribution) package metadata and return it as a dict.

    If Distribution and Import package do have indentical names the argument
    distribution_name can be empty and is determined by the import package.
    """

    if distribution_name:
        # We need to use the name of the Distribution Package here!
        m = metadata(distribution_name)
    else:
        # Usually you can use this if the Import Package is the same as
        # the Distribution Package
        m = metadata(__name__)

    result = {}

    for key, count in Counter(m.keys()).items():

        if key in exclude_keys:
            continue

        # single value key
        if count == 1:
            result[key] = m[key]
            continue

        # multi value key
        result[key] = []
        for val in m.get_all(key):
            result[key].append(val)

    # post process project URLs
    try:
        urls = result['Project-URL']
    except KeyError:
        pass
    else:
        result['Project-URL'] = {}
        for entry in urls:
            key, val = entry.split(',')
            result['Project-URL'][key.strip()] = val.strip()

    return result

meta = _package_metadata_as_dict(distribution_name='hellocentralapp')

__license__ = '{}\nSee License file "{}".'.format(
    meta['License'].split('\n\n')[0],
    meta['License-File'])

__version__ = meta['Version']
__name__ = f'{__name__} in {meta["Name"]}'

# contact details
__author__ = meta['Author-email']
__maintainer__ = __author__
__website__ = meta['Project-URL']['homepage']

