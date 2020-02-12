'''

import openshift as oc

print('OpenShift client version: {}'.format(oc.get_client_version()))
print('OpenShift server version: {}'.format(oc.get_server_version()))

# Set a project context for all inner `oc` invocations and limit execution to 10 minutes
with oc.project('openshift-infra'), oc.timeout(10*60):
    # Print the list of qualified pod names (e.g. ['pod/xyz', 'pod/abc', ...]  in the current project
    print('Found the following pods in {}: {}'.format(oc.get_project_name(), oc.selector('pods').qnames()))
    

