import yaml
import csv

class JunoGuardConverter:
    def __init__(self):
        self.juniper_filters = []

    def add_filter(self, name, rules):
        self.juniper_filters.append({'name': name, 'rules': rules})

    def convert_to_yaml(self, filename):
        with open(filename, 'w') as yaml_file:
            yaml.dump(self.juniper_filters, yaml_file, default_flow_style=False)

    def convert_to_csv(self, filename):
        with open(filename, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Filter Name', 'Source IP', 'Destination IP', 'Port', 'Protocol'])
            for filter_data in self.juniper_filters:
                filter_name = filter_data['name']
                for rule in filter_data['rules']:
                    csv_writer.writerow([filter_name, rule['source_ip'], rule['destination_ip'], rule['port'], rule['protocol']])

# Example usage
if __name__ == "__main__":
    converter = JunoGuardConverter()
    
    # Add Junos firewall filter data
    filter1_rules = [
        {'source_ip': '10.0.0.0/24', 'destination_ip': '0.0.0.0/0', 'port': '80', 'protocol': 'tcp'},
        {'source_ip': '192.168.0.0/16', 'destination_ip': '0.0.0.0/0', 'port': '443', 'protocol': 'tcp'}
    ]
    converter.add_filter('filter1', filter1_rules)
    
    filter2_rules = [
        {'source_ip': '10.1.1.0/24', 'destination_ip': '0.0.0.0/0', 'port': '22', 'protocol': 'tcp'}
    ]
    converter.add_filter('filter2', filter2_rules)
    
    # Convert to YAML
    converter.convert_to_yaml('juno_filters.yaml')
    
    # Convert to CSV
    converter.convert_to_csv('juno_filters.csv')
