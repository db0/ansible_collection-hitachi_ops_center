import re
import itertools

def extract_ansible_playbook_process_info(awk_stdout):
	"""Extracts the private key path given to ansible-playbook with the --private-key arg, if any
	Extracts the login user given to ansible-playbook with the -u arg, if any
	Combines them together to one command-line arg to pass an nested ansible-playbook called via the shell module.
	"""
	all_cmd_list = awk_stdout.split()
	pid = all_cmd_list[0].split(',')[1]
	command = all_cmd_list[1]
	auth_args = ''
	priv_key_regex  = re.search(r'--private-key ([^\s]+)', awk_stdout)
	if priv_key_regex:
		auth_args += '--private-key ' + priv_key_regex.group(1) + ' '
	priv_key_user  = re.search(r'-u ([^\s]+)', awk_stdout)
	if priv_key_user:
		auth_args += '-u ' + priv_key_user.group(1)
	ret = {
		"pid": pid,
		"cmd": command,
		"auth": auth_args
	}
	return(ret)



class FilterModule(object):
    def filters(self):
      return {
				'extract_ansible_playbook_process_info': extract_ansible_playbook_process_info,
		}