# Firewall Configuration Project

This project aims to implement and configure a firewall using `ufw` (Uncomplicated Firewall) on a web server (`web-01`). The firewall rules will be set up to block all incoming traffic except for specific TCP ports. Additionally, advanced configuration will be done to enable port forwarding from port 8080 to port 80.

## Table of Contents

- [Introduction](#introduction)
- [Tasks](#tasks)
  - [Block all incoming traffic but](#block-all-incoming-traffic-but)
  - [Port forwarding](#port-forwarding)
- [Repo Structure](#repo-structure)
- [Usage](#usage)
- [License](#license)

## Introduction

Firewalls are essential components of network security, acting as barriers between a trusted internal network and untrusted external networks such as the internet. In this project, we'll be configuring a firewall on the web server `web-01` using `ufw`, a user-friendly interface for managing firewall rules on Ubuntu systems.
# Tasks

# Block all incoming traffic but

In this task, the objective is to configure the `ufw` firewall on `web-01` to block all incoming traffic except for specific TCP ports: 22 (SSH), 443 (HTTPS SSL), and 80 (HTTP).

# Port forwarding

In this advanced task, we'll configure `web-01`'s firewall to forward incoming traffic from port 8080 to port 80. This allows users to access web services on port 80 through an alternative port, enhancing flexibility and security.

# Repo Structure

The project repository (`alx-system_engineering-devops`) contains the following directories and files relevant to the firewall configuration tasks:

- `0x13-firewall/`
  - `0-block_all_incoming_traffic_but`: Contains the `ufw` commands used to block all incoming traffic except for specified TCP ports.
  - `100-port_forwarding`: Includes the modified `ufw` configuration file enabling port forwarding from 8080 to 80.

