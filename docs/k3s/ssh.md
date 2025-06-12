# SSH

ssh key must exist, ex. `~/.ssh/id_rsa.pub`. Use `ssh-keygen` to create a private and public key pair.

```bash
ssh-keygen -t rsa -b 4096 -C "comment"
```

Copy the SSH key to the target server

```bash
ssh-copy-id -i ~/.ssh/id_rsa.pub pi@192.168.1.11
```

Test the SSH connection

```bash
ssh -i ~/.ssh/id_rsa pi@192.168.1.11
```
