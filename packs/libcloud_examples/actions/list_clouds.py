from st2actions.runners.pythonrunner import Action
import yaml

__all__ = [
    'ListCloudsAction'
]


class ListCloudsAction(Action):

    def run(self, type):
        conf = None
        with open('/opt/stackstorm/packs/libcloud/config.yaml', 'r') as outfile:
            conf = yaml.load(outfile)
        out_creds = {}
        for name, cred in conf['credentials'].iteritems():
            try:
                cred['api_secret'] = ''
            except KeyError:
                pass
            try:
                cred['api_key'] = ''
            except KeyError:
                pass
            if type == 'all' or type == cred['type']:
                out_creds[name] = cred
        return out_creds
