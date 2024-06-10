import yaml

def remove_affiliation_from_authors(citation_file):
    with open(citation_file, 'r') as file:
        data = yaml.safe_load(file)

    if 'authors' in data:
        for author in data['authors']:
            if 'affiliation' in author:
                del author['affiliation']

    with open(citation_file, 'w') as file:
        yaml.safe_dump(data, file, sort_keys=False)

if __name__ == "__main__":
    citation_file = 'CITATION.cff'
    remove_affiliation_from_authors(citation_file)
    print(f"'affiliation' field removed from authors in {citation_file}")
