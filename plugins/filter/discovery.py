import re


def parse_hostgroup_name(discovered_hg_name):
	"""Overridable function which for extra formating of the hostgroup name.
	"""
	host_group_name = discovered_hg_name
	return(host_group_name)


def hostgroup_matches(discovered_host_group_name, cluster_name):
	"""Returns true if a specified cluster name exists in a hostgroup name
	else returns false
	"""
	host_group_name = parse_hostgroup_name(discovered_host_group_name)
	if re.search(rf'{cluster_name}$', host_group_name, re.IGNORECASE):
		return(True)
	return(False)


def get_host_group_id(hostgroup_dict, cluster_name):
	"""Returns a list with all the hostgroup numbers of a specific cluster name for this array
	"""
	host_group_ids = {}
	for group in hostgroup_dict:
		if hostgroup_matches(group["hostGroupName"], cluster_name):
			host_group_ids[group["hostGroupNumber"]] = group["hostGroupName"]
	return(host_group_ids)


def get_host_group_name(hostgroup_dict, cluster_name):
	"""Returns the canonical name of the hostgroup name
	Stripped from the DC location at the end
	"""
	return_name = None
	for group in hostgroup_dict:
		if hostgroup_matches(group["hostGroupName"], cluster_name):
			host_group_name = parse_hostgroup_name(group["hostGroupName"])
			if return_name and return_name != host_group_name:
				return(None)
			return_name = host_group_name
	return(return_name)


def get_resource_group_id(resource_groups, hostgroup_dict, cluster_name):
	"""Returns a list with all the resource group IDs where this cluster is a member of
	"""
	host_group_pids = []
	for group in hostgroup_dict:
		if hostgroup_matches(group["hostGroupName"], cluster_name):
			host_group_pids.append(group["hostGroupId"])
	# set() returns only the unique values in the list
	# list() turns the set back into a list
	host_group_pids = list(set(host_group_pids))
	for rg in resource_groups:
		# To avoid failing when an RG does not have any HGs assigned
		if rg.get('hostGroupIds') == None: continue
		# Checks if any of the hostgroup-port IDs is in the Resource groups hostgroup-port IDs.
		if any(hpid in host_group_pids for hpid in rg['hostGroupIds']):
			# I'm assuming a cluster cannot be a member of more than 1 resource group
			resource_group = rg['resourceGroupId']
			break
	return(resource_group)


def check_if_GAD(hostgroup_dict, cluster_name):
	"""Checks if the cluster currently being processed is of type GAD.
	This function is expected to be overridden based on the way this organization
	determines GAD hosts.
	Returns true if the cluster is GAD, else returns false
	"""
	is_gad = False
	return(is_gad)


class FilterModule(object):
    def filters(self):
      return {
				'get_host_group_id': get_host_group_id,
				'get_host_group_name': get_host_group_name,
				'get_resource_group_id': get_resource_group_id,
				'hostgroup_matches': hostgroup_matches,
				'check_if_GAD': check_if_GAD,
		}