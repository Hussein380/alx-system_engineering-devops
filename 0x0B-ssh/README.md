# SSH Configuration and Automation

## Overview

This repository contains scripts and configuration files for SSH configuration and automation tasks, aimed at enhancing security and efficiency in remote server access. These tasks are part of the ALX System Engineering & DevOps program curriculum.

# Table of Contents

1. [Description](#description)
2. [Tasks](#tasks)
3. [Usage](#usage)
4. [File Structure](#file-structure)
5. [Author](#author)



# Description

SSH (Secure Shell) is a cryptographic network protocol for operating network services securely over an unsecured network. It provides a secure channel over an unsecured network by using a pair of cryptographic keys.

This project focuses on implementing SSH best practices, including key pair generation, configuration, and automation using Puppet. The tasks encompass:

1. Using a Private Key: Script to establish SSH connection using a private key.
2. Generating SSH Key Pair: Script to create an RSA key pair with passphrase protection.
3. Client Configuration File: Configuration file to set up SSH client for passwordless authentication.
4. Adding Public Key to Server: Public key to be added to servers for authorized access.
5. Automating SSH Configuration with Puppet: Puppet script to automate SSH client configuration.


# Tasks

# 0. Use a Private Key

This script establishes an SSH connection to a server using a private key.

# 1. Create an SSH Key Pair

Generates an RSA key pair with a passphrase for enhanced security.

# 2. Client Configuration File

Configures the local SSH client to enable passwordless authentication using the private key.

# 3. Let Me In!

Provides the SSH public key to be added to servers for authorized access.
# 4. Client Configuration File (w/ Puppet)

Automates the SSH client configuration using Puppet for efficient management.

---

# Usage

# Prerequisites

- Ubuntu 20.04 LTS environment.
- Access to the intranet profile for server information.

# Running Scripts

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/ssh-configuration.git
   ```

2. Navigate to the directory:

   ```bash
   cd ssh-configuration/0x0B-ssh
   ```

3. Execute the desired script:

   ```bash
   ./script_name
   ```

# Applying Puppet Script

1. Navigate to the directory containing the Puppet script:

   ```bash
   cd ssh-configuration/0x0B-ssh
   ```

2. Apply the Puppet script:

   bash
   sudo puppet apply 100-puppet_ssh_config.pp

# File Structure

```
0x0B-ssh/
│
├── 0-use_a_private_key
├── 1-create_ssh_key_pair
├── 2-ssh_config
├── 3-let_me_in
├── 100-puppet_ssh_config.pp
│
├── README.md

## Author

Hussein
