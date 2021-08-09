# Db0 Hitachi OPS Center role: lookup_hostgroups

This role will go through all arrays defined in the hitachi_ops_center and look for any hostgroups which match the given name.

It will create a fact `arrays_zoned` which is a list of all arrays in which hostgroups matching the given name have been discovered.

Each element in that list is a dictionary containing details about that array. The details in each element are:

* storage_array: The Array ID as known by the hitachi_ops_manager and used in the REST API
* serial_number: The array serial number
* host_group_ids: the hostgroup IDs of the hostgroups matching the provided name
* canonical_hg_name: the hostgroup names, stripped of all GAD Datacenter identifications
* existing_token: The authentification token to use for this session on this array
* session_id: The authentification session for this array
* host_groups: All the hostgroups discovered in this array (i.e. including ones which don't match the name).
* name: The array human-readable name
* resource_group: All resource groups defined in the array
* vsm: the VSM ID to use for GAD requests, if relevant
* remote_pair: The array ID of which this array is paired with, for mirroring.

This role will also initiate a keep-alive operation on arrays in which matching hostgroup are discovered (see role: db0.hitachi_ops_center.keep_alive)

## Expected variables

These variables must be passed to the role during import.

* NAME (String): The name of the cluster/host for which to look for hostgroups.
* HUSER: The username with which to login to the REST API
* HPASS: The password with which to login to the REST API

## Optional variables

These variables have predefined defaults but they can be overriden during role import.
See defaults/main.yml explanations

* base_uri (String)
* IS_THIRD_VOTING_DISK (bool)
* expected_zoning_count (int)
* base_uri (String)
* service_uri (String)
* NON_PAIRED_ARRAYS (List): A list of storage arrays which are not paired. List can be empty.

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