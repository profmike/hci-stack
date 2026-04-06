# hci-stack

Prof. Mike Chen's exploration of agent skills for HCI research.

***As AI accelerates much of the research lifecycle by 10-100×, how should HCI research and education redefine their purpose, priorities, and practice?***

hci-stack turns HCI research mentoring workflows into AI skills. The goal is not just to make research faster. It is to use AI to help researchers choose better problems, build stronger motivation, frame contributions more clearly, and improve the quality of what they study and build.

This repository is one step in that exploration. It is inspired by [gstack](https://github.com/garrytan/gstack) by Garry Tan, President and CEO of [Y Combinator](https://www.ycombinator.com/), and informed by my experience mentoring Master's students at NTU to publish 30+ ACM CHI papers, including 2 CHI Best Paper Awards (top 1%, in 2022 and 2026) and 4 CHI Honorable Mention Awards (top 5%).

It also reflects how I approach research problems based on experience across startups, accelerators ([IK12](https://ik12.org/) + [YC](https://www.ycombinator.com/)), academic research (systems research with [Prof. Eric Brewer](https://people.eecs.berkeley.edu/~brewer/) and [Prof. David Patterson](https://www2.eecs.berkeley.edu/Faculty/Homepages/patterson.html) at Berkeley), and corporate research (ubiquitous computing research at Intel Research Seattle with [Prof. James Landay](https://profiles.stanford.edu/james-landay)). Their examples have strongly shaped how I think about ambitious problems, rigorous research, and work that matters in practice.


## Skills

| Skill | What it does |
|-------|-------------|
| `/hci-office-hours-with-mike` | HCI research mentoring — problem definition, motivation, related work, and contribution positioning. Six forcing questions, competitive positioning with 2-axis charts, evidence quality assessment, simulated CHI reviewer objections, and a structured research brief. |

## Install

Open your AI coding agent and paste the install command. The agent does the rest.

### Claude Code

> Install hci-stack: run **`git clone https://github.com/profmike/hci-stack.git ~/.claude/skills/hci-stack && cd ~/.claude/skills/hci-stack && ./install claude`** then add an "HCI Research Skills" section to CLAUDE.md that lists the available skill: /hci-office-hours-with-mike.

### Codex

> Install hci-stack: run **`git clone https://github.com/profmike/hci-stack.git ~/.codex/skills/hci-stack && cd ~/.codex/skills/hci-stack && ./install codex`**

### Gemini CLI

> Install hci-stack: run **`git clone https://github.com/profmike/hci-stack.git ~/.gemini/skills/hci-stack && cd ~/.gemini/skills/hci-stack && ./install gemini`**

### Windows (PowerShell)

```powershell
git clone https://github.com/profmike/hci-stack.git $env:USERPROFILE\hci-stack
cd $env:USERPROFILE\hci-stack
.\install.ps1
```

### Auto-detect

If you have multiple agents installed, the install script detects all of them:

```bash
git clone https://github.com/profmike/hci-stack.git ~/hci-stack
cd ~/hci-stack && ./install
```

## Quick start

1. Install hci-stack (see above)
2. Run `/hci-office-hours-with-mike`
3. Describe what you're researching
4. The mentor walks you through problem definition, related work, competitive positioning, and produces a research brief

## License

[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
