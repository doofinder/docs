#!/usr/bin/env python3
"""
Parses an OpenAPI YAML spec and updates the pages arrays in docs.json
for the given tab, matching each group name to its OpenAPI tag.

Usage: sync_openapi.py <yaml_file> <docs_json_file> <tab_name>
"""
import sys
import json
import yaml
from collections import defaultdict

HTTP_METHODS = {'get', 'post', 'put', 'patch', 'delete', 'head', 'options'}


def extract_ops_by_tag(spec):
    tag_ops = defaultdict(list)
    for path, path_item in spec.get('paths', {}).items():
        for method, operation in path_item.items():
            if method.lower() not in HTTP_METHODS:
                continue
            if not isinstance(operation, dict):
                continue
            for tag in operation.get('tags', []):
                tag_ops[tag].append(f"{method.upper()} {path}")
    return tag_ops


def main():
    yaml_file, docs_json_file, tab_name = sys.argv[1], sys.argv[2], sys.argv[3]

    with open(yaml_file) as f:
        spec = yaml.safe_load(f)

    tag_ops = extract_ops_by_tag(spec)

    with open(docs_json_file) as f:
        docs = json.load(f)

    for tab in docs.get('navigation', {}).get('tabs', []):
        if tab.get('tab') != tab_name:
            continue
        for group in tab.get('groups', []):
            if 'openapi' not in group:
                continue
            group_name = group['group']
            group['pages'] = tag_ops.get(group_name, [])
        break

    with open(docs_json_file, 'w') as f:
        json.dump(docs, f, indent=2)
        f.write('\n')


if __name__ == '__main__':
    main()
