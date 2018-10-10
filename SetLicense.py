import json
import requests

def SetLicense(org, repos_needing_license, license):
    #disregard all this code except for the port under the if license: which will be used over in the new GetRepos.py
    update_license_url = "https://api.github.com/repos/{organization}/{repo}?license={key}&name={name}&spdx_id={spdx_id}&url={url}&node_id={node_id}"
    response = None

    #update_license_url = update_license_url.format(organization=org)
    if license:
        license_url = "https://api.github.com/licenses/" + license
        response = requests.get(license_url)
        decoded_license = json.loads(response.content)

    for repo in repos_needing_license:
        print(repo)
        #response = requests.patch("https://api.github.com/orgs/stradivarii",)
        '''I was hoping to use a patch, but it doesn't seem to be working.  I believe I would have to use a PUT instead.  
        However, it appears as if PATCH does not work for licenses (if at all).  Therefore, I would have to save the entire
        repo object and modify it's license area specifically, then do a PUT of the object to overwrite the previous object.
        In this case, depending on the domain expert's needs, it would make most sense to have this all in one spot.  See
        the GetRepos.py to see pseudo code of how I would change it'''
    #decoded_json = json.loads(response.content)