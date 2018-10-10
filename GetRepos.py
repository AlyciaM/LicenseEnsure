import json
import requests

def GetMissingLicenses(org):

    api_get_repos_url = "https://api.github.com/orgs/{organization}/repos"
    repo_ids_missing_licenses = {}

    api_get_repos_url = api_get_repos_url.format(organization=org)
    #Add in code from SetLicense.py to return license data of license requested.

    response = requests.get(api_get_repos_url)
    decoded_json = json.loads(response.content)
    for repo in decoded_json:
        if repo["license"] == None:
            repo_ids_missing_licenses[repo["id"]] = repo["name"]

    ''' No longer need to save or return the repo_ids_missing_licenses dictionary, if integrate the finding and updating
    In the above if method, I would remove the line creating the dictionary entries (as well as removing the dictionary altogether).
    Then I would take the license data previously requested and move it into the current repo's license fields.
    Next, I would do a PUT call to update the repo without the license.
    After that I would continue on in the current for loop, until all items have been updated.'''
    #return repo_ids_missing_licenses