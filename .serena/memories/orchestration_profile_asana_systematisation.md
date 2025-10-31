# Orchestration Profile: Asana Systematisation Project

## Core Orchestration Model
**2-Phase Execution with Validation:**
1. **Execution Phase**: Subagent acknowledges scope → executes → delivers
2. **Validation Phase**: Dedicated Validation Agent (read-only) → ✅ PASS or ❌ FAIL
3. **Synthesis**: Orchestrator confirms or triggers re-execution

## Orchestrator Constraints
- **Role**: Task coordination, TodoWrite, memory management, thinking tools only
- **NEVER execute directly**: All execution delegated to subagents
- **Decision gate**: Invoke agents only after mutual orchestrator-user agreement on decisions + execution readiness

## Agent Specializations for This Project
Primary agents:
- Task/project management agents
- Architecture-focused design agents (backend-architect, api-architect preferred)
- Google Workspace MCP invocation agents
- Asana MCP invocation agents
- Sequential-thinking agents (preferred over native reasoning for complex problems)
- Serena MCP invocation agents
- Context7 MCP invocation agents
- Scripting agent (API calls to Asana)

Future specializations: TBD based on project evolution

## MCP Routing Rules
- **Always use MCP tools when available**: Invoked by subagents, never orchestrator
- **Sequential thinking**: Preferred for complex reasoning, delegated to subagent
- **Context7 before building**: Query documentation before implementation (not after)
- **Google Workspace/Asana operations**: Route through MCP tools via subagents
- **Asana start_on field**: ✅ Supported via `asana_update_task` with ISO 8601 date-only format (`YYYY-MM-DD`)
  - Example: `asana_update_task(task_id="...", start_on="2025-10-16")`
  - Format: No time component, date-only string
  - Verified: October 21, 2025 testing confirmed working

## Workflow Patterns
- **Mode selection**: Context-dependent, reassess each task
- **Checkpoints**: After every task completion (large or small)
- **Validation overhead**: ~110-140K tokens total (12.5% for quality assurance)
- **Context isolation**: Validation agent has fresh context, unbiased by implementation

## Decision Pattern
**When to Invoke Agents vs Discuss Inline:**
- Discuss inline: Until orchestrator & user achieve mutual agreement on decisions + execution readiness
- Invoke agent: Once mutual agreement confirmed + ready to execute

Pre-execution phase = facilitated decision alignment by orchestrator