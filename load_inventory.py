from ansible_runner import Runner

# Define the path to your Ansible playbook directory
playbook_dir = '/workspaces/ensf400-lab5-ansible/'

# Define the path to your inventory file
inventory_path = '/workspaces/ensf400-lab5-ansible/hosts.yml'

# Define the path to your playbook YAML file
playbook_path = '/workspaces/ensf400-lab5-ansible/hello.yml'

# Task 1: Load inventory using Python code and print host information
def load_inventory_and_print_info():
    runner = Runner(
        playbook=['-'],  # Use '-' to read the playbook from stdin
        inventory=inventory_path,
        host_pattern='all',
        playbook_dir=playbook_dir
    )

    # Execute the runner with an empty playbook to retrieve inventory information
    result = runner.run(play='{}')
    
    # Extract host information from the inventory
    hosts = result.events[0]['event_data']['host_inventory']
    
    print("Host Information:")
    for hostname, info in hosts.items():
        print(f"Name: {hostname}, IP: {info['ansible_host']}, Groups: {info['group_names']}")

# Task 2: Ping all hosts and output the results
def ping_all_hosts():
    runner = Runner(
        playbook=playbook_path,
        inventory=inventory_path,
        playbook_dir=playbook_dir
    )

    # Execute the runner to run the playbook (ping)
    result = runner.run()

    # Output ping results
    print("\nPing Results:")
    for event in result.events:
        if event['event'] == 'runner_on_ok':
            print(f"Host: {event['event_data']['host']}, Result: {event['event_data']['res']['ping']}")

if __name__ == "__main__":
    load_inventory_and_print_info()
    ping_all_hosts()