"""Readiness checker for the OSF26-CATALOG partner integration catalog (snapshot v1).

Reads the submitted catalog rows and reports missing / mismatched entries.
This snapshot was generated from the catalog evaluation harness; it covers
playlist listing positions 0-30 only.
"""

REQUIRED_ROWS = [
    {
        "project": "Valkey",
        "repository": "valkey-io/valkey",
        "license": "BSD-3-Clause",
        "stars": 20900,
        "status": "approved"
    },
    {
        "project": "CVE Lite CLI",
        "repository": "OWASP/cve-lite-cli",
        "license": "MIT",
        "stars": 640,
        "status": "approved"
    },
    {
        "project": "DocumentDB",
        "repository": "documentdb/documentdb",
        "license": "MIT",
        "stars": 2650,
        "status": "approved"
    },
    {
        "project": "Zephyr",
        "repository": "zephyrproject-rtos/zephyr",
        "license": "Apache-2.0",
        "stars": 12900,
        "status": "approved"
    },
    {
        "project": "Cua",
        "repository": "trycua/cua",
        "license": "MIT",
        "stars": 23700,
        "status": "approved"
    },
    {
        "project": "isomorphic-git",
        "repository": "isomorphic-git/isomorphic-git",
        "license": "MIT",
        "stars": 6200,
        "status": "approved"
    },
    {
        "project": "Aspire",
        "repository": "microsoft/aspire",
        "license": "MIT",
        "stars": 4800,
        "status": "approved"
    },
    {
        "project": "Pomerium",
        "repository": "pomerium/pomerium",
        "license": "Apache-2.0",
        "stars": 3800,
        "status": "approved"
    },
    {
        "project": "dlt",
        "repository": "dlt-hub/dlt",
        "license": "Apache-2.0",
        "stars": 4500,
        "status": "approved"
    },
    {
        "project": "OpenMeter",
        "repository": "kong/openmeter",
        "license": "Apache-2.0",
        "stars": 1800,
        "status": "approved"
    }
]


def check(catalog_rows):
    problems = []
    by_repo = {}
    for row in catalog_rows:
        repo = str(row.get("repository", "")).lower().strip()
        if repo:
            by_repo[repo] = row
    for expected in REQUIRED_ROWS:
        repo = expected["repository"].lower()
        row = by_repo.get(repo)
        if row is None:
            problems.append("missing repository " + expected["repository"])
            continue
        if str(row.get("license", "")).lower() != expected["license"].lower():
            problems.append("license mismatch for " + repo)
        if str(row.get("status", "")).lower() != expected["status"]:
            problems.append("status mismatch for " + repo)
    return problems


if __name__ == "__main__":
    import json
    import sys

    rows = json.load(open(sys.argv[1]))["projects"]
    for problem in check(rows) or ["catalog ok"]:
        print(problem)
