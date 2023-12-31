# 0x0E. Web stack debugging #1

## Project Overview

This project focuses on web stack debugging and aims to resolve issues related to Nginx installation on an Ubuntu container. The tasks involve debugging, script creation, and automation.

## Concepts

- Network basics
- Web stack debugging

## Project Structure

- **0-nginx_likes_port_80**: Bash script to configure Nginx to listen on port 80.

- **1-debugging_made_short**: Shortened version of the fix for task #0 with specific requirements.

## Task Details

### 0. Nginx likes port 80

- Find out and fix why Nginx installation on the Ubuntu container is not listening on port 80.
- Write a Bash script to automate the fix.
- Requirements:
  - Nginx must be running, and listening on port 80 of all the server’s active IPv4 IPs.

### 1. Make it sweet and short

- Shorten the fix from task #0 to 5 lines or less.
- Service (init) must indicate that Nginx is not running.
- Additional requirements mentioned in the task details.
