# hci-stack

Mike Chen's (opinionated) exploration of agent skills for HCI research.

***How should HCI research and education evolve with AI, when AI can accelerate many aspects of a research project's lifecycle by 10-100x?***

Related work research that used to take students days to report back — AI now completes it more thoroughly in minutes. Prototypes that used to wait weeks for students to build — AI now implements in hours. How do we use the 10-100x to increase research quality and impact?

This is my exploration of that question, inspired by [gstack](https://github.com/garrytan/gstack) by Garry Tan (President & CEO of [Y Combinator](https://www.ycombinator.com/)), and informed by my varied experience at startups, accelerators ([IK12](https://ik12.org/)+[YC](https://www.ycombinator.com/)), academic research (systems research with [Prof. Eric Brewer](https://people.eecs.berkeley.edu/~brewer/) and [Prof. David Patterson](https://www2.eecs.berkeley.edu/Faculty/Homepages/patterson.html) at Berkeley), and corporate research (ubicomp research at Intel Research Seattle with [Prof. James Landay](https://profiles.stanford.edu/james-landay)).

For the past 15 years, I've been an HCI professor at NTU, during which I have mentored Masters students to publish more than 30 ACM CHI papers, including 2 CHI Best Paper Awards (top 1%, in 2023 and 2026) and 4 CHI Honorable Mention Awards (top 5%).

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
