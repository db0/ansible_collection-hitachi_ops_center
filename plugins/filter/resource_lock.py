def is_resource_group_locked(locked_rgs, resource_group = -1):
	"""Checks if the provided resource_group is returned among the list of all locked RGs
	If -1 is passed as the RG ID, it will check if any RG is locked.
	Returns True if locked. Else returns False.
	"""
	is_locked = False
	for rg in locked_rgs:
		# we need to compare as integers to make sure their types are the same.
		if int(resource_group) == -1 or int(rg['resourceGroupId']) == int(resource_group):
			is_locked = True
			break
	return(is_locked)
	

class FilterModule(object):
    def filters(self):
      return {
				'is_resource_group_locked': is_resource_group_locked,
		}