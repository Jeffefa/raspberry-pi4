# Raspberry Pi Setup Guide

Step-by-step guide to configure the Raspberry Pi environment after cloning the repository.

## 1. Docker Installation and Configuration

Run the commands below to install Docker, configure user permissions, and enable the service on startup:

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
sudo systemctl enable docker
sudo systemctl start docker
```
> *Note: After adding the user to the docker group, close the session (`exit`) and reconnect via SSH to apply permissions.*

---

## 2. Validation of `.env` Files

Ensure that the global environment variables file `.env` is positioned at the root of the structure and that the necessary symbolic links are correctly configured in the service subfolders:

```bash
cd ~/Apps
# Example to ensure the .env symbolic link in child folders, if needed:
# ln -s ../.env .env
```

---

## 3. Configuring Shortcuts (`.bash_aliases`)

Create or edit the shortcut file in your user home directory to streamline container management:

```bash
nano ~/.bash_aliases
```

Add the following useful shortcuts:

```bash
alias dps='docker ps'
alias dcu='docker compose up -d'
alias dcd='docker compose down'
alias dlogs='docker compose logs -f'
```

Save the file and reload the terminal configurations:

```bash
source ~/.bashrc
```

---

## 4. Starting Services via Docker Compose

Navigate to the applications directory and start the containers in the background:

```bash
cd ~/Apps
docker compose up -d
```

Validate if the services are running correctly:

```bash
dps
```