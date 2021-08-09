# Db0 Hitachi OPS Center role: lock_resource_groups

This role will lock the resource groups where the current user has admin access. 

It can also be used to simply check for existing locks only.

## Requirements 

None

## Expected variables

These variables must be passed to the role (or be set in the ansible environment) during import.

* array_details: A dictionary holding information about the array we want to lock. The following keys are expected inside
   * storage_array: The Array ID as known by the configuration manager
	* existing_token: A valid session authentication token for this array
	* resource_group: The resource group which we want to ensure is unlocked. If not set, it will check if any RG is locked.
* base_uri: The configuration manager base URI (i.e. the url until the part where the array ID is added). This will be used to construct the lock-check and lock-job URIs.

## Optional variables

These variables have predefined defaults but they can be overriden during role import.

* check_for_lock_only (bool): If set to true, the play will wait until existing locks are released but will not lock the resource groups.

