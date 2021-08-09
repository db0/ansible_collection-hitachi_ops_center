# Db0 Hitachi OPS Center role: keep_alive

This role will keep-alive a logged-in session against the Hitachi Configuration Manager 
until the Process ID of the current ansible-playbook execution finishes. 

This ensures that during long operations working on a pair of arrays in tandem, 
a slow or long API response in one of the arrays will not cause the playbook to abort 
because the session on the other array expired after 5 minutes

## Requirements 

Has only been tested in Red Hat GNU/Linux OS. But should theoretically work in all GNU/Linux.

This has only been tested using private key authentication.

## Expected variables

These variables must be passed to the role during import.

* array_id (String): The Array ID in the configuration manager
* session_id (String): The session ID which to keep alive
* auth_token (String): The authentication token for the session

## Optional variables

None