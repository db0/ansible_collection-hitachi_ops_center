# Db0 Hitachi OPS Center role: job_uri

This role will initiate a REST API call which is expected to start and return a job result uri. Then it will poll that URI a specified number of times, until the operation is completed.

If the job fails, it will display the job output, before aborting the play with an informative message.

## Requirements 

None

## Expected variables

These variables must be passed to the role during import.

* full_uri (String): The complete URI from which to retrieve the content
* uri_auth_token (String): The authentication token to use to connect to HOPSC
* uri_method (String): The method to use (PUT, POST etc)
* uri_body (Dictionary): The body dictionary to send to the request
* task_description (String): The task description to use in is the job fails.

## Optional variables

These variables have predefined defaults but they can be overriden during role import.

* timeout (int): The amount of seconds to wait for the API to respond.
* uri_remote_auth_token (String): In case the API call requires authentication on two arrays, you pass the remote array's auth token as this variable. If this is not passed, this header will be skipped.
* ensure_unlocked (bool): If set to true, it will utilize [lock_resource_groups](../lock_resource_groups) role functionality to check and wait until the relevant resource group is unlocked, before executing the job. If this is set to true, the following 2 variables **have** to also be set. Check lock_resource_groups for their details
   * array_details (Dictionary)
   * base_uri (String)
