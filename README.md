# Ansible Collection: Db0 Hitachi OPS Center


This collection contains roles which help perform operations using the Hitachi OPS Center using the Configuration Manager REST API

Check the documentation included for each role for usage details.

This collection was created to help me perform operations in my previous job's setup. 
Some code, particularly in the filter plugins, is expected to be extended to handle your particular business' setup.

## Roles

### cached_uri

This role will retrieve and cache a REST API result from the specified URI, using the ansible uri module, then store it in a predefined location. If the specified URI has already been cached and within its TTL, it will use the cached version.

### job_uri

This role will initiate a REST API call which is expected to start and return a job result uri. Then it will poll that URI a specified number of times, until the operation is completed, then return the result.

### flush_cache

This role will flush all or just part of the cache created by the cached_uri role.

### keep_alive

This role will keep alive a logged-in session against the configuration manager until the PID of the current
ansible-playbook execution finishes. This ensures that during long operations working on a pair of arrays in tandem,
a slow API response in one of the arrays will not cause the playbook to abort because the session on the other array 
expired after 5 minutes

### lock_resource_groups

This role will lock the resource groups where the current user has admin access. It can also be used to simply check for existing locks only.

### lookup_hostgroups

This role will go through all arrays defined in the hitachi_ops_center and look for any hostgroups which match the given name.

## Example

Here's a sample playbook using many roles of this collection to retrieve information about hitachi arrays

```
---

- hosts: all
  collections:
    - db0.hitachi_ops_center

  tasks:

  - name: Discover arrays in which host/cluster is zoned
    include_role:
      name: lookup_hostgroups

  - debug:
      var: arrays_zoned
```

Then execute it like so:

```
ansible-playbook -i storageadmin.example.com, add-standard-lun.yml -e HUSER=${HUSER} -e HPASS=${HPASS} -e NAME=clustername
```

You can then use the information stored in arrays_zoned to do further tasks in hitachi arrays, such as adding LUNS etc. You can use the `job_uri` role for performing operations