from libcloud.container.utils.docker import HubClient
from st2actions.runners.pythonrunner import Action

__all__ = [
    'DockerHubSearchAction'
]


class DockerHubSearchAction (Action):
    def run(self, search):
        client = HubClient()
        images = client.list_images(search)
        return [{"name": image.name, "version": image.version} for image in images]
