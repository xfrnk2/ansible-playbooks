from ansible.module_utils.basic import *
import os

def func_find_index(string, target):
        return string.find(target)
def main():
    fields = { 
            "dot_index" : {"required": True, "type": "str"}
    }
    module = AnsibleModule(argument_spec=fields)
    dot_index = os.path.expanduser(module.params['dot_index'])
    idx = func_find_index(dot_index, ".")
    str_after_found_idx = dot_index[(idx+1):]
    module.exit_json(msg=str_after_found_idx)

if __name__ == '__main__':
        main()
