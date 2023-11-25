# 0x0B. SSH - DevOps Project

🚀 Welcome to the SSH Odyssey! Dive into the world of Secure Shell (SSH) with this ALX System Engineering & DevOps project.

![SSH](https://media.giphy.com/media/LOuFz8uZp8gFpN2hnr/giphy.gif)

## Brief Overview 🌟

In this cosmic adventure, you've been gifted an Ubuntu server in a distant galaxy. Your mission? Master the art of SSH, embrace RSA key authentication, and dance with the stars in the world of secure server connections.

## Tasks 🚀

### 0. Use a private key
**Location:** [0-use_a_private_key](0-use_a_private_key)

Write a Bash script to connect to the server using the private key `~/.ssh/school` with the user `ubuntu`.

### 1. Create an SSH key pair
**Location:** [1-create_ssh_key_pair](1-create_ssh_key_pair)

Craft a Bash script to generate an RSA key pair named `school` (4096 bits) protected by the passphrase 'betty'.

### 2. Client configuration file
**Location:** [2-ssh_config](2-ssh_config)

Configure your local SSH client to use the private key `~/.ssh/school` and reject password authentication.

### 3. Let me in!
**Location:** [3-let_me_in](3-let_me_in)

Add a provided SSH public key to your server, enabling connection using the `ubuntu` user.

### 4. Client configuration file (w/ Puppet)
**Location:** [4-puppet_ssh_config.pp](4-puppet_ssh_config.pp)

Employ Puppet to configure the SSH client, setting it to use the private key `~/.ssh/school` and disallow password authentication.

---
