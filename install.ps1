# Install all hci-stack skills for Claude Code, Codex, and/or Gemini CLI (Windows)
param(
    [string]$Host_ = "auto"
)

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$Skills = @("hci-office-hours-with-mike")
$VersionFile = Join-Path $ScriptDir "VERSION"
$Version = (Get-Content $VersionFile -Raw).Trim()
$InstallHome = if ($env:HCI_STACK_INSTALL_HOME) { $env:HCI_STACK_INSTALL_HOME } else { $env:USERPROFILE }

function Install-SkillFiles($Skill, $Root) {
    $SkillSrcDir = Join-Path $ScriptDir $Skill
    $Dir = Join-Path $Root $Skill
    if (Test-Path $Dir) {
        Remove-Item -Recurse -Force $Dir
    }
    New-Item -ItemType Directory -Force -Path $Dir | Out-Null
    Copy-Item -Recurse -Force "$SkillSrcDir\*" $Dir
    return $Dir
}

function Install-Claude {
    $Root = Join-Path $InstallHome ".claude\skills"
    foreach ($Skill in $Skills) {
        $Dir = Install-SkillFiles $Skill $Root
        Write-Host "  Claude Code: $Dir"
    }
}

function Install-Codex {
    $Root = Join-Path $InstallHome ".codex\skills"
    foreach ($Skill in $Skills) {
        $Dir = Install-SkillFiles $Skill $Root
        Write-Host "  Codex: $Dir"
    }
}

function Install-Gemini {
    $Root = Join-Path $InstallHome ".gemini\skills"
    foreach ($Skill in $Skills) {
        $Dir = Install-SkillFiles $Skill $Root
        Write-Host "  Gemini CLI: $Dir"
    }
}

Write-Host "Installing hci-stack v$Version..."

switch ($Host_) {
    "claude"  { Install-Claude }
    "codex"   { Install-Codex }
    "gemini"  { Install-Gemini }
    "auto" {
        $Installed = 0
        if (Test-Path (Join-Path $InstallHome ".claude")) {
            Install-Claude; $Installed = 1
        }
        if (Test-Path (Join-Path $InstallHome ".codex")) {
            Install-Codex; $Installed = 1
        }
        if (Test-Path (Join-Path $InstallHome ".gemini")) {
            Install-Gemini; $Installed = 1
        }
        if ($Installed -eq 0) {
            Install-Claude
        }
    }
    default {
        Write-Host "Usage: .\install.ps1 [claude|codex|gemini|auto]"
        exit 1
    }
}

Write-Host ""
Write-Host "hci-stack v$Version ready."
Write-Host "Claude: /hci-office-hours-with-mike"
Write-Host "Codex: `$hci-office-hours-with-mike"
Write-Host "Gemini: /hci-office-hours-with-mike"
