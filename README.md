[![Termux Compatible](https://img.shields.io/badge/Termux-Compatible-brightgreen?logo=termux)](https://termux.com)
[![Python Version](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org)
[![License](https://img.shields.io/badge/License-MIT-green?logo=opensourceinitiative)](LICENSE)
[![Latest Release](https://img.shields.io/github/v/release/alAgent/alAgent?logo=github)](https://github.com/alAgent/alAgent/releases)
[![Build Status](https://img.shields.io/github/actions/workflow/status/alAgent/alAgent/ci.yml?logo=githubactions)](https://github.com/alAgent/alAgent/actions)

# 🤖 alAgent
## Your Intelligent, Creative AI Assistant for Termux

> A next-generation AI agent purpose-built for Termux environments, combining natural language understanding, autonomous task execution, and deep integration with Termux's CLI ecosystem to boost your productivity and unlock creative workflows.

## 📑 Table of Contents
- [✨ Introduction](#-introduction)
- [🚀 Key Features](#-key-features)
- [📦 Installation](#-installation)
  - [Prerequisites](#prerequisites)
  - [Quick Install (Termux Only)](#quick-install-termux-only)
  - [Manual Installation](#manual-installation)
- [💡 Usage](#-usage)
  - [Basic Commands](#basic-commands)
  - [Advanced Workflows](#advanced-workflows)
  - [Example Tasks](#example-tasks)
- [⚙️ Configuration](#-configuration)
  - [Environment Variables](#environment-variables)
  - [Custom Agent Persona](#custom-agent-persona)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [📬 Support & Contact](#-support--contact)

## ✨ Introduction
alAgent is a lightweight, high-performance AI agent designed exclusively for Termux users. It bridges the gap between natural language intent and Termux's powerful command-line tools, allowing you to automate complex tasks, query system information, generate scripts, and even build custom workflows using simple conversational prompts.

Unlike generic AI chatbots, alAgent is deeply integrated with Termux's filesystem, package manager (pkg/apt), and environment variables, enabling it to execute actions directly on your device with proper permission handling and safety checks.

## 🚀 Key Features
| Feature | Description |
|---------|-------------|
| 🧠 **Conversational Task Execution** | Run Termux commands, install packages, and manage files using plain English prompts |
| 🔄 **Autonomous Workflow Automation** | Chain multiple tasks into reusable workflows triggered by custom commands or events |
| 📝 **Smart Script Generation** | Auto-generate Python, Bash, or JavaScript scripts tailored to your Termux environment |
| 🔍 **Context-Aware Assistance** | Retains conversation context to handle multi-step queries without repetition |
| 🛡️ **Safety-First Execution** | Validates all commands before execution, prompts for confirmation on high-risk actions |
| 🎨 **Creative Content Generation** | Generate README files, documentation, code comments, or even ASCII art directly in Termux |
| 🔌 **Extensible Plugin System** | Add custom tools, API integrations, or persona tweaks via a simple plugin architecture |

## 📦 Installation
### Prerequisites
- Termux (latest version, installed from F-Droid or official GitHub release)
- Python 3.10 or higher
- ~50MB free storage space
- Active internet connection (for initial setup)

### Quick Install (Termux Only)
Run the following one-liner in your Termux terminal to install alAgent and all dependencies automatically:
bash
curl -fsSL https://raw.githubusercontent.com/alAgent/alAgent/main/install.sh | bash

This script will:
1. Update Termux repositories
2. Install required Python packages
3. Configure alAgent environment variables
4. Add the `alagent` command to your PATH

### Manual Installation
1. Update Termux packages:
bash
pkg update && pkg upgrade -y

2. Install Python and git:
bash
pkg install python git -y

3. Clone the alAgent repository:
bash
git clone https://github.com/alAgent/alAgent.git

4. Navigate to the project directory:
bash
cd alAgent

5. Install dependencies:
bash
pip install -r requirements.txt

6. Run the setup script:
bash
python setup.py install --user


## 💡 Usage
### Basic Commands
Start the alAgent interactive shell by running:
bash
alagent

Once in the shell, you can use natural language prompts or shortcut commands:
| Shortcut | Description |
|----------|-------------|
| `/help` | Display all available commands |
| `/clear` | Clear conversation context |
| `/exec <command>` | Directly execute a Termux command |
| `/script <task>` | Generate a script for a specific task |
| `/exit` | Quit alAgent |

### Advanced Workflows
alAgent supports workflow definitions stored in `~/.config/alagent/workflows/`. Create a JSON file like `backup-workflow.json`:
json
{
  "name": "daily-backup",
  "trigger": "backup my files",
  "steps": [
    "create backup directory in ~/backups",
    "copy all files from ~/documents to backup directory",
    "compress backup directory to tar.gz",
    "notify me when done"
  ]
}

Then trigger the workflow with: `alagent run backup-workflow`

### Example Tasks
<details>
<summary>Click to see example prompts</summary>

1. "Install the latest version of ffmpeg and show me how to convert an MP4 to GIF"
2. "Generate a Python script that scans my Termux home directory for large files over 100MB"
3. "Set up a cron job to update Termux packages every Sunday at 2AM"
4. "Create a README.md for my new Python project in ~/my-project"
5. "Show me all running processes and kill the ones using more than 500MB RAM"

</details>

## ⚙️ Configuration
alAgent stores its configuration in `~/.config/alagent/config.yaml`. You can edit this file directly or use the `alagent config` command.

### Environment Variables
| Variable | Default | Description |
|----------|---------|-------------|
| `ALAGENT_API_KEY` | None | Your AI provider API key (OpenAI, Anthropic, etc.) |
| `ALAGENT_MODEL` | `gpt-3.5-turbo` | The AI model to use for processing prompts |
| `ALAGENT_SAFE_MODE` | `true` | Enable/disable safety checks for command execution |
| `ALAGENT_LOG_LEVEL` | `info` | Logging verbosity (debug, info, warn, error) |

### Custom Agent Persona
You can customize alAgent's tone and behavior by editing the `persona.yaml` file in the config directory. Example:
yaml
name: alAgent
tone: professional
expertise: Termux CLI, Python, Bash, Automation
language: English
creative_level: high


## 🤝 Contributing
We welcome contributions from the community! To contribute:
1. Fork the repository
2. Create a new branch for your feature/bugfix: `git checkout -b feat/your-feature`
3. Commit your changes with descriptive messages
4. Push to your fork and open a Pull Request
5. Follow the [Contribution Guidelines](CONTRIBUTING.md)

Please report bugs or request features via the [GitHub Issues](https://github.com/alAgent/alAgent/issues) page.

## 📄 License
alAgent is licensed under the MIT License. See the [LICENSE](LICENSE) file for full details.

## 📬 Support & Contact
- GitHub Issues: [Report a Bug](https://github.com/alAgent/alAgent/issues/new?template=bug_report.md)
- Discussions: [Join the Community](https://github.com/alAgent/alAgent/discussions)
- Email: support@alagent.io (for security-related queries only)

---

> Built with ❤️ for the Termux community.
