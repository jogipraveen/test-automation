# test-automation
Integrate the scripts to CI to post failed test results to a PR on Stash/Bitbucket

#### Fetch failed unit
- DIR_NAME - directory path of unit test results
- URL - URL of stash/bitbucket

```bash
$ ./fetch_junit.py <DIR_NAME> <URL>
```

#### Fetch failed functional tests
- TESTNG_FILE - functional tests result file
- URL - URL of stash/bitbucket

```bash
$ ./fetch_testng.py <TESTNG_FILE> <URL>
```
