import json
import requests
import GetRepos
import SetLicense

org="stradivarii"
license = "gpl-3.0"

missing_licenses = GetRepos.GetMissingLicenses(org)
SetLicense.SetLicense(org, missing_licenses, license)
