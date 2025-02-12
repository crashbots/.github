import json

README_FILE = "profile/README.md"
START_MARKER = "<!-- START_BOTS -->\n"
END_MARKER = "<!-- END_BOTS -->\n"

def fetch_repos():
    with open("repos.json", "r") as file:
        repos = json.load(file)
    return repos

def update_readme(repos):
    with open(README_FILE, "r") as file:
        content = file.readlines()

    start_index = content.index(START_MARKER) + 1
    end_index = content.index(END_MARKER)

    header = "| Префикс                  | Язык программирования | Описание                                                 |\n"
    separator = "|--------------------------|-----------------------|---------------------------------------------------------|\n"
    
    repo_lines = [
        f"| {repo['name']} | {repo.get('language', 'Unknown')} | {repo.get('description', 'No description')} |\n"
        for repo in repos
    ]
    
    content = content[:start_index] + [header, separator] + repo_lines + content[end_index:]

    with open(README_FILE, "w") as file:
        file.writelines(content)

if __name__ == "__main__":
    repositories = fetch_repos()
    update_readme(repositories)
