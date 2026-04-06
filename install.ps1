# Install hci-office-hours-with-mike skill for Claude Code, Codex, and/or Gemini CLI (Windows)
param(
    [string]$Host_ = "auto"
)

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$SkillSrcDir = Join-Path $ScriptDir "hci-office-hours-with-mike"
$VersionFile = Join-Path $SkillSrcDir "VERSION"
if (-not (Test-Path $VersionFile)) {
    $VersionFile = Join-Path $ScriptDir "VERSION"
}
$Version = (Get-Content $VersionFile -Raw).Trim()

function Install-SkillFiles($Dir) {
    New-Item -ItemType Directory -Force -Path $Dir | Out-Null
    Copy-Item -Recurse -Force "$SkillSrcDir\*" $Dir
}

function Install-Claude {
    $Dir = Join-Path $env:USERPROFILE ".claude\skills\hci-office-hours-with-mike"
    Install-SkillFiles $Dir
    Write-Host "  Claude Code: $Dir"
}

function Install-Codex {
    $Dir = Join-Path $env:USERPROFILE ".codex\skills\hci-office-hours-with-mike"
    Install-SkillFiles $Dir
    Write-Host "  Codex: $Dir"
}

function Install-Gemini {
    $Dir = Join-Path $env:USERPROFILE ".gemini\skills\hci-office-hours-with-mike"
    Install-SkillFiles $Dir
    Write-Host "  Gemini CLI: $Dir"
}

Write-Host "Installing hci-office-hours-with-mike v$Version..."

switch ($Host_) {
    "claude"  { Install-Claude }
    "codex"   { Install-Codex }
    "gemini"  { Install-Gemini }
    "auto" {
        $Installed = 0
        if (Test-Path (Join-Path $env:USERPROFILE ".claude")) {
            Install-Claude; $Installed = 1
        }
        if (Test-Path (Join-Path $env:USERPROFILE ".codex")) {
            Install-Codex; $Installed = 1
        }
        if (Test-Path (Join-Path $env:USERPROFILE ".gemini")) {
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
Write-Host "hci-office-hours-with-mike v$Version ready."
Write-Host "Claude: /hci-office-hours-with-mike"
Write-Host "Codex: `$hci-office-hours-with-mike"
Write-Host "Gemini: /hci-office-hours-with-mike"
