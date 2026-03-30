# Engineer Agent Dispatcher Instructions

## Overview

This skill acts as an intelligent entry point for Engineer Agent. It analyzes project state and user intent to automatically select and execute appropriate engineering skills.

## Available Skills

- `codebase-analyzer` - Analyze project structure and tech stack
- `project-bootstrap` - Initialize new project based on TRD
- `feature-implementor` - Implement features based on PM docs
- `test-writer` - Write tests based on Test Spec
- `debugger` - Debug and fix issues
- `delivery` - Git workflow, commits, PRs

## Execution Steps

### Step 1: Analyze Context

Check project state:
- Is this a new project or existing codebase?
- Are there PM documents available?
- Is there existing code to analyze?
- What is the current git status?

### Step 2: Determine User Intent

| User Intent | Skills to Execute |
|-------------|------------------|
| "分析项目" | codebase-analyzer |
| "初始化项目" | project-bootstrap |
| "实现功能" | feature-implementor |
| "编写测试" | test-writer |
| "修复 bug" | debugger |
| "创建 PR/交付" | delivery |
| "完整开发流程" | codebase-analyzer → feature-implementor → test-writer → delivery |

### Step 3: Execute Skills

Execute selected skills in appropriate order based on dependencies.

### Step 4: Present Results

Summarize execution results and output locations.
