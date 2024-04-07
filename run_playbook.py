from ansible_runner import Runner

def run_playbook_and_print_results():
    # Define the path to your Ansible playbook directory
    playbook_dir = '/workspaces/ensf400-lab5-ansible'

    # Define the path to your inventory file
    inventory_path = '/workspaces/ensf400-lab5-ansible/hosts.yml'

    # Define the path to your playbook YAML file
    playbook_path = '/workspaces/ensf400-lab5-ansible/hello.yml'

    # Run the hello.yml playbook to install the app on the 'app' group
    runner = Runner(
        playbook=playbook_path,
        inventory=inventory_path,
        playbook_dir=playbook_dir,
        extravars={'group_to_install': 'app'}  # Pass extra variables to specify the group
    )

    # Execute the runner to run the playbook
    result = runner.run()

    # Print the results
    print("Playbook Execution Results:")
    for event in result.events:
        print(event['stdout'])

if __name__ == "__main__":
    run_playbook_and_print_results()
