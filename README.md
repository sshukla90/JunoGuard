# JunoGuard: Convert Junos Firewall Filters to AWS Security Groups


JunoGuard is a Python script that simplifies the process of converting Junos firewall filters used in Juniper MX devices to AWS security groups. This tool automates the translation of rule definitions, making it easier to migrate your network security configurations to AWS.

## Features

- Seamlessly converts Junos firewall filters to AWS security group rules.
- Supports translation of source IPs, destination IPs, ports, and protocols.
- Easy-to-use Python script with customization options.
- Streamlines the migration of security configurations to AWS.

## Requirements

- Python 3.x
- AWS Boto3 library
- AWS credentials with appropriate permissions

## Getting Started

1. Clone this repository to your local machine.
2. Install the required Python packages: `pip install boto3`.
3. Configure your AWS credentials using the AWS CLI or environment variables.
4. Modify the `juniper_filters` list in the script with your Junos firewall filter rules.
5. Run the script: `python junoguard.py`.

## Usage

1. Customize the `juniper_filters` list in the script to match your Junos firewall filter rules.
2. Run the script to generate AWS security groups based on your Junos rules.
3. Thoroughly test the generated security groups to ensure they meet your requirements.
4. Fine-tune the generated security groups as needed.

## Contributions

Contributions are welcome! If you find a bug or want to enhance JunoGuard, feel free to open an issue or submit a pull request.



**Disclaimer:** JunoGuard is provided as-is without any warranties. Use at your own risk.

For questions or inquiries, contact [your.email@example.com](mailto:sshukla90@outlook.com).

