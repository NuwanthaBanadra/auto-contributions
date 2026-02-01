# 🤖 Auto Contributions

[![Auto Contribution](https://github.com/NuwanthaBanadra/auto-contributions/actions/workflows/auto-commit.yml/badge.svg)](https://github.com/NuwanthaBanadra/auto-contributions/actions/workflows/auto-commit.yml)

An automated GitHub contribution system that generates commits **4 times per day** (every 6 hours) with inspiring programming quotes and interesting tech facts.

> **Note:** This project is created for learning and practice purposes to understand GitHub Actions, automation workflows, and Python scripting.

> **⚠️ IMPORTANT:** This repository **must be PUBLIC** for contributions to appear on your GitHub profile! Private repository contributions are not visible on your public contribution graph. See [Repository Visibility Requirements](#repository-visibility-requirements) for details.

## 📋 Table of Contents

- [Overview](#overview)
- [Repository Visibility Requirements](#repository-visibility-requirements)
- [How It Works](#how-it-works)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Customization](#customization)
- [Project Structure](#project-structure)
- [Examples](#examples)
- [Disabling/Enabling Automation](#disablingenabling-automation)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This repository automatically commits programming wisdom and tech knowledge to maintain an active contribution graph. The system:

- **Runs automatically** every 6 hours (00:00, 06:00, 12:00, 18:00 UTC)
- **Generates unique content** from a collection of 25+ programming quotes and 25+ tech facts
- **Commits to GitHub** with timestamps and formatted content
- **Works completely hands-free** via GitHub Actions

## 🔓 Repository Visibility Requirements

### ⚠️ Your Repository MUST Be Public

For this automation to work as intended and show contributions on your GitHub profile, **your repository must be public**. Here's why:

#### Why Public Repository is Required:

1. **Contribution Graph Visibility** 🟢
   - GitHub's public contribution graph **only counts contributions from public repositories**
   - Private repository contributions are hidden from your public profile
   - Even if you own the private repo, those commits won't show as green squares on your profile

2. **GitHub Actions Minutes** ⏱️
   - Public repositories get **unlimited** GitHub Actions minutes
   - Private repositories have limited minutes (2,000/month on free tier)
   - Running 4 times daily = ~120 workflow runs/month, which uses significant minutes on private repos

3. **Purpose of This Project** 🎯
   - This tool is designed to maintain a visible, active contribution graph
   - A private repository defeats this purpose entirely

#### How to Make Your Repository Public:

If your repository is currently private, follow these steps to make it public:

1. Go to your repository on GitHub
2. Click **Settings** (top right)
3. Scroll down to the **Danger Zone** section (bottom of the page)
4. Click **Change visibility**
5. Select **Make public**
6. Type the repository name to confirm
7. Click **I understand, make this repository public**

#### What About Privacy?

- ✅ **Safe to make public:** This repository only contains:
  - Automated workflow configuration
  - Python script with quotes/facts
  - Generated contribution JSON files
  - No sensitive data or credentials

- ⚠️ **Never commit:** 
  - Personal information
  - API keys or secrets
  - Private code or proprietary information

### Checking Your Repository Status

To verify your repository is public:
- Look for a **Public** label next to your repository name on GitHub
- Public repos have an "open book" icon 📖
- Private repos have a "lock" icon 🔒

## ⚙️ How It Works

The automation system consists of three main components:

### 1. GitHub Actions Workflow (`.github/workflows/auto-commit.yml`)

The workflow is scheduled to run every 6 hours using a cron expression:
```yaml
schedule:
  - cron: '0 */6 * * *'  # Every 6 hours at :00 minutes
```

**Workflow Steps:**
1. ✅ Checks out the repository
2. 🐍 Sets up Python 3.x environment
3. 🎲 Runs the contribution script (`scripts/contribute.py`)
4. 🔧 Configures Git with bot credentials
5. 📝 Commits and pushes new contributions
6. 🔄 Handles cases with no changes gracefully

### 2. Contribution Script (`scripts/contribute.py`)

A Python script that:
- Randomly selects between programming quotes and tech facts
- Generates a JSON file with:
  - Timestamp (ISO format)
  - Content type (quote or fact)
  - The actual quote/fact
  - Attribution (author or category)
- Saves to the `contributions/` directory with timestamped filename

### 3. Data Storage (`contributions/`)

All automated contributions are stored as individual JSON files in this directory. Each file contains structured data about the contribution, making it easy to track and analyze over time.

## ✨ Features

- 🎯 **25+ Programming Quotes** from legendary programmers:
  - Donald Knuth, Linus Torvalds, Martin Fowler, and more
  - Timeless wisdom about coding, debugging, and software engineering

- 🔍 **25+ Tech Facts** covering:
  - Programming language history and trivia
  - Internet and computing milestones
  - Software development insights
  - Computer science fundamentals

- ⏰ **Flexible Scheduling:**
  - Runs every 6 hours by default (4 times daily)
  - Manual trigger option via GitHub Actions UI
  - Easy to customize schedule

- 📊 **Clean Data Organization:**
  - Each contribution saved as individual JSON file
  - Timestamped filenames for easy sorting
  - Human-readable and machine-parseable format

- 🤖 **Fully Automated:**
  - No manual intervention required
  - Self-maintaining
  - Handles edge cases gracefully

## 🚀 Setup Instructions

### Prerequisites
- A GitHub account
- A **PUBLIC** GitHub repository (this one!)
- GitHub Actions enabled (free for public repositories)

> **⚠️ CRITICAL:** Ensure your repository is **public** before proceeding! See [Repository Visibility Requirements](#repository-visibility-requirements) above.

### Quick Start

1. **Verify Repository is Public** ⚠️
   - Go to your repository on GitHub
   - Check for the **Public** label next to the repository name
   - If it shows **Private**, follow the instructions in [Repository Visibility Requirements](#repository-visibility-requirements) to make it public

2. **Fork or Clone this repository**
   ```bash
   git clone https://github.com/NuwanthaBanadra/auto-contributions.git
   cd auto-contributions
   ```

3. **Ensure GitHub Actions is enabled**
   - Go to your repository's **Settings** → **Actions** → **General**
   - Under "Actions permissions", select "Allow all actions and reusable workflows"
   - Under "Workflow permissions", select "Read and write permissions"
   - Click "Save"

4. **That's it!** 🎉
   - The workflow will run automatically every 6 hours
   - You can also trigger it manually from the Actions tab
   - Verify contributions appear on your profile after the first run

### Manual Trigger

To manually run the workflow:
1. Go to the **Actions** tab in your repository
2. Select **Auto Contribution** workflow
3. Click **Run workflow**
4. Select the branch and click **Run workflow**

## 🎨 Customization

### Change Schedule Frequency

Edit `.github/workflows/auto-commit.yml` and modify the cron expression:

```yaml
schedule:
  - cron: '0 */6 * * *'  # Current: Every 6 hours
```

**Common Cron Schedules:**
```yaml
- cron: '0 */4 * * *'   # Every 4 hours (6 times/day)
- cron: '0 */12 * * *'  # Every 12 hours (2 times/day)
- cron: '0 9 * * *'     # Once daily at 9:00 AM UTC
- cron: '0 */1 * * *'   # Every hour (24 times/day)
- cron: '*/30 * * * *'  # Every 30 minutes
```

**Cron Syntax Guide:**
```
┌───────────── minute (0 - 59)
│ ┌───────────── hour (0 - 23)
│ │ ┌───────────── day of month (1 - 31)
│ │ │ ┌───────────── month (1 - 12)
│ │ │ │ ┌───────────── day of week (0 - 6) (Sunday to Saturday)
│ │ │ │ │
* * * * *
```

### Add Your Own Quotes or Facts

Edit `scripts/contribute.py` and add to the `PROGRAMMING_QUOTES` or `TECH_FACTS` lists:

```python
PROGRAMMING_QUOTES = [
    {
        "quote": "Your custom quote here",
        "author": "Author Name"
    },
    # ... more quotes
]

TECH_FACTS = [
    {
        "fact": "Your interesting tech fact here",
        "category": "Category Name"
    },
    # ... more facts
]
```

### Change Output Format

Currently contributions are saved as JSON. To use a different format, modify the `save_contribution()` function in `scripts/contribute.py`.

### Customize Git Commit Message

Edit the commit message in `.github/workflows/auto-commit.yml`:

```yaml
- name: Commit and push changes
  run: |
    git add contributions/
    if git diff --staged --quiet; then
      echo "No changes to commit"
    else
      git commit -m "Your custom commit message here: $(date +'%Y-%m-%d %H:%M:%S UTC')"
      git push
    fi
```

## 📁 Project Structure

```
auto-contributions/
├── .github/
│   └── workflows/
│       └── auto-commit.yml      # GitHub Actions workflow configuration
├── contributions/               # Generated contribution files (JSON)
│   ├── contribution_20240101_000000.json
│   ├── contribution_20240101_060000.json
│   └── ...
├── scripts/
│   └── contribute.py           # Python script to generate contributions
└── README.md                   # This file
```

## 📝 Examples

### Example Quote Output
```json
{
  "timestamp": "2024-01-01T12:00:00.123456",
  "content": {
    "type": "quote",
    "text": "Programs must be written for people to read, and only incidentally for machines to execute.",
    "author": "Harold Abelson"
  }
}
```

### Example Fact Output
```json
{
  "timestamp": "2024-01-01T18:00:00.123456",
  "content": {
    "type": "fact",
    "text": "The first computer bug was an actual bug - a moth found in the Harvard Mark II computer in 1947.",
    "category": "History"
  }
}
```

## 🔧 Disabling/Enabling Automation

### Temporarily Disable
1. Go to **Actions** tab
2. Select **Auto Contribution** workflow
3. Click the **...** menu → **Disable workflow**

### Re-enable
1. Go to **Actions** tab
2. Select **Auto Contribution** workflow
3. Click **Enable workflow**

### Permanently Remove
Delete or rename the workflow file:
```bash
git rm .github/workflows/auto-commit.yml
git commit -m "Disable auto contributions"
git push
```

## ❓ Troubleshooting

### Contributions Not Showing on My Profile

**Problem:** The workflow runs successfully, but I don't see green squares on my contribution graph.

**Solution:** 
1. ✅ **Check repository visibility:** Your repository MUST be public
   - Go to Settings → scroll to "Danger Zone" → verify it says "Change repository visibility" with current status "Public"
   - If it's private, see [Repository Visibility Requirements](#repository-visibility-requirements)

2. ✅ **Wait for the next UTC day:** Contributions may take up to 24 hours to appear on your graph

3. ✅ **Verify commits are being made:**
   - Go to your repository
   - Check the "Commits" section
   - Look for commits from `github-actions[bot]`

4. ✅ **Check workflow runs:**
   - Go to Actions tab
   - Verify recent runs show green checkmarks (successful)
   - If red X appears, click to see error details

### Workflow Fails with Permission Error

**Problem:** Workflow runs but fails at the "Commit and push changes" step.

**Solution:**
1. Go to Settings → Actions → General → Workflow permissions
2. Select "Read and write permissions"
3. Click "Save"
4. Re-run the failed workflow from the Actions tab

### Running Out of GitHub Actions Minutes

**Problem:** "You have exceeded your GitHub Actions minutes."

**Solution:**
- This should NOT happen with public repositories (unlimited minutes)
- If you see this error, verify your repository is **public**, not private
- Private repos have limited minutes; making it public solves this

## 🤝 Contributing

While this is a personal learning project, suggestions and improvements are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add some improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Quotes and facts collected from various public sources and common knowledge
- Inspired by the developer community's love for automation
- Built with GitHub Actions and Python

---

**Made with ❤️ for learning and practice**

*Remember: This is a practice project. Real contributions come from meaningful code, documentation, and collaboration!* 🚀