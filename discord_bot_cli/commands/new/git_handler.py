import zipfile
from io import BytesIO
from pathlib import Path

import requests


class Branch:
    def __init__(self, branch: dict):
        self.name = branch["name"]
        self.protected = branch["protected"]
        self.sha = branch["commit"]["sha"]
        self.short_sha = self.sha[:7]
        self.url = branch["commit"]["url"]

    def __repr__(self):
        return f"<Branch name={self.name}>"


class GitHandler:
    def __init__(self, cwd: Path):
        self.cwd = cwd

    BASE_URL = "https://api.github.com"

    def _get_response(self, endpoint, js=True) -> requests.Response:
        try:
            response = requests.get(self.BASE_URL + endpoint)
            if response.status_code == 200:
                return response
        except Exception as error:
            return

    def unzip(self, project_name: str, branch: Branch):
        project_directory = self.cwd.joinpath(project_name)
        if not project_directory.is_dir():
            project_directory.mkdir()
        sub = f"stroupbslayen-discord-bot-{branch.short_sha}"
        with zipfile.ZipFile(BytesIO(self._get_zip(branch))) as archive:
            for file in archive.infolist():
                if all(
                    name not in file.filename
                    for name in ("LICENSE", "gitignore", "README")
                ):
                    file.filename = file.filename.replace(sub, "")
                    archive.extract(file, project_directory)

        example = project_directory.joinpath("config.yaml.example")
        config = project_directory.joinpath("config.yaml")
        if not config.is_file():
            config.write_bytes(example.read_bytes())

    def _get_zip(self, branch: Branch) -> bytes:
        url = f"/repos/stroupbslayen/discord-bot/zipball/{branch.name}"
        zip_file = self._get_response(url)
        if zip_file:
            return zip_file.content

    def _get_branches(self) -> list:
        url = "/repos/stroupbslayen/discord-bot/branches"
        try:
            branches = self._get_response(url)
            branches = [Branch(branch) for branch in branches.json()]
            branches.reverse()
            return branches
        except:
            return []

    def get_latest_branch(self) -> Branch:
        branches = self._get_branches()
        if branches:
            return branches[0]

    def get_branch(self, version: str) -> Branch:
        branches = self._get_branches()
        for branch in branches:
            if branch.name == version:
                return branch
