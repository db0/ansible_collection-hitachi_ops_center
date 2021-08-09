# Ansible Collection: Db0 Hitachi OPS Center


This collection contains roles which help perform operations using the Hitachi OPS Center using the Configuration Manager REST API

Check the documentation included for each role for usage details.

## cached_uri

This role will retrieve and cache a REST API result from the specified URI, using the ansible uri module, then store it in a predefined location. If the specified URI has already been cached and within its TTL, it will use the cached version.

## job_uri

This role will initiate a REST API call which is expected to start and return a job result uri. Then it will poll that URI a specified number of times, until the operation is completed, then return the result.

## flush_cache

This role will flush all or just part of the cache created by the cached_uri role.

## keep_alive

This role will keep alive a logged-in session against the configuration manager until the PID of the current
ansible-playbook execution finishes. This ensures that during long operations working on a pair of arrays in tandem,
a slow API response in one of the arrays will not cause the playbook to abort because the session on the other array 
expired after 5 minutes

## lock_resource_groups

This role will lock the resource groups where the current user has admin access. It can also be used to simply check for existing locks only.

## lookup_hostgroups

This role will go through all arrays defined in the hitachi_ops_center and look for any hostgroups which match the given name.