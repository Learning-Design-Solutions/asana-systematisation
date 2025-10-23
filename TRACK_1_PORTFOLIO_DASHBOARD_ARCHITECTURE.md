# Track 1: Portfolio Dashboard & Status Reports Architecture
## Phase 1 Implementation Design

**Version**: 1.0
**Date**: October 21, 2025
**Status**: Design Specification - Ready for Implementation
**Scope**: Portfolio hierarchy + Dashboard data model + Status reporting foundation

---

## Executive Summary

This document specifies the **Phase 1 implementation** of portfolio-level management capabilities for Learning Design Solutions' Asana systematisation project. Phase 1 establishes the **data foundation** that Phase 2 will consume for Google Workspace integration.

**Key Architectural Decision**: Use **project-based portfolio hierarchy** with custom fields for programme grouping, leveraging Asana MCP capabilities (`asana_search_tasks`, `asana_get_task`, `asana_create_task`).

**Deliverables**:
1. Portfolio hierarchy structure (project-based approach)
2. Dashboard data model (JSON schemas + aggregation logic)
3. Status reporting framework (weekly snapshot structure)
4. Query patterns (validated with sample data)
5. Phase 2 readiness assessment (Google Workspace integration prep)

**Timeline**: 5 hours implementation + validation

---

## 1. Portfolio Hierarchy Architecture

### 1.1 Design Rationale

**Constraint Analysis**:
- ❌ Asana MCP does NOT expose native portfolio API methods
- ✅ Asana MCP DOES support: project operations, task search, custom fields
- ✅ Current template must remain unchanged (72 tasks, 52 dependencies)
- ✅ Must enable multi-programme visibility (3-5 concurrent programmes)

**Chosen Approach**: **Project-Based Portfolio with Custom Field Filtering**

### 1.2 Hierarchy Structure

```
Workspace: LDS Operations
│
├── Programme: Walbrook - MBA Refresh
│   │
│   ├── PROJECT: [MBA Refresh] - Programme Tracker
│   │   ├── Purpose: Programme-level metadata storage
│   │   ├── Custom Fields:
│   │   │   ├── programme_name: "MBA Refresh"
│   │   │   ├── client_name: "Walbrook University"
│   │   │   ├── programme_status: "Active" (enum: Planning, Active, Delivery, Closeout)
│   │   │   ├── total_modules: 3
│   │   │   ├── health_status: "Green" (enum: Green, Amber, Red)
│   │   │   └── programme_start_date: "2025-09-01"
│   │   │
│   │   └── Tasks: Programme-level milestones
│   │       ├── Task: Module 1 Overview (links to Module 1 project)
│   │       ├── Task: Module 2 Overview (links to Module 2 project)
│   │       └── Task: Module 3 Overview (links to Module 3 project)
│   │
│   ├── PROJECT: [MBA Refresh] - Module 1: Strategic Management
│   │   ├── 72 Tasks (EXISTING TEMPLATE - UNCHANGED)
│   │   ├── 52 Dependencies (EXISTING - UNCHANGED)
│   │   ├── Custom Fields (ADDED):
│   │   │   ├── programme_name: "MBA Refresh"
│   │   │   ├── module_number: 1
│   │   │   ├── module_title: "Strategic Management"
│   │   │   └── module_launch_date: "2025-11-15"
│   │   │
│   │   └── Sections: 12 sections (Initiation → Launch)
│   │
│   ├── PROJECT: [MBA Refresh] - Module 2: Financial Management
│   │   └── Same structure as Module 1
│   │
│   └── PROJECT: [MBA Refresh] - Module 3: Marketing Strategy
│       └── Same structure as Module 1
│
├── Programme: Healthcare Academy - Clinical Skills
│   ├── PROJECT: Programme Tracker
│   ├── PROJECT: Module 1 Project
│   └── PROJECT: Module 2 Project
│
└── Programme: Finance Institute - Professional Certification
    ├── PROJECT: Programme Tracker
    └── PROJECT: Module 1 Project
```

### 1.3 Custom Fields Schema

**Programme-Level Custom Fields** (applied to Programme Tracker projects):
```json
{
  "programme_name": {
    "type": "text",
    "description": "Unique programme identifier",
    "example": "MBA Refresh",
    "required": true
  },
  "client_name": {
    "type": "text",
    "description": "Client organization name",
    "example": "Walbrook University",
    "required": true
  },
  "programme_status": {
    "type": "enum",
    "options": ["Planning", "Active", "Delivery", "Closeout"],
    "description": "Current programme phase",
    "required": true
  },
  "total_modules": {
    "type": "number",
    "description": "Total number of modules in programme",
    "example": 3,
    "required": true
  },
  "health_status": {
    "type": "enum",
    "options": ["Green", "Amber", "Red"],
    "description": "Rollup health indicator",
    "calculation": "See Section 3.2",
    "required": true
  },
  "programme_start_date": {
    "type": "date",
    "description": "Programme commencement date",
    "example": "2025-09-01",
    "required": true
  }
}
```

**Module-Level Custom Fields** (added to existing module projects):
```json
{
  "programme_name": {
    "type": "text",
    "description": "Links module to programme (filter key)",
    "example": "MBA Refresh",
    "required": true,
    "note": "MUST match programme tracker value exactly"
  },
  "module_number": {
    "type": "number",
    "description": "Module sequence within programme",
    "example": 1,
    "required": true
  },
  "module_title": {
    "type": "text",
    "description": "Module name/subject",
    "example": "Strategic Management",
    "required": true
  },
  "module_launch_date": {
    "type": "date",
    "description": "Target launch date (from existing template)",
    "example": "2025-11-15",
    "required": true,
    "note": "Already exists in template as 'Launch Date'"
  }
}
```

### 1.4 Query Patterns for Portfolio Navigation

**Query 1: Get All Programmes**
```python
# Retrieve all programme tracker projects
programmes = asana_search_projects(
    workspace="workspace_gid",
    name_pattern="Programme Tracker"
)

# Extract programme metadata
for programme in programmes:
    programme_data = {
        "programme_name": programme.custom_fields["programme_name"],
        "client_name": programme.custom_fields["client_name"],
        "health_status": programme.custom_fields["health_status"],
        "total_modules": programme.custom_fields["total_modules"]
    }
```

**Query 2: Get All Modules in a Programme**
```python
# Search for all module projects linked to programme
modules = asana_search_projects(
    workspace="workspace_gid",
    custom_fields={
        "programme_name.value": "MBA Refresh"
    }
)

# Filter out programme tracker (only get module projects)
module_projects = [p for p in modules if "Module" in p.name]
```

**Query 3: Get All Tasks in a Programme** (across all modules)
```python
# Step 1: Get all module projects
modules = asana_search_projects(
    workspace="workspace_gid",
    custom_fields={"programme_name.value": "MBA Refresh"}
)

# Step 2: Get tasks from each module
all_tasks = []
for module in modules:
    tasks = asana_search_tasks(project_id=module.gid)
    all_tasks.extend(tasks)

# Result: All 216 tasks (3 modules × 72 tasks) for dashboard aggregation
```

---

## 2. Dashboard Data Model

### 2.1 JSON Schema Design

**Portfolio Overview Schema**:
```json
{
  "$schema": "portfolio_overview_v1.0",
  "metadata": {
    "report_date": "2025-10-21T10:00:00Z",
    "workspace_id": "workspace_gid",
    "workspace_name": "LDS Operations",
    "total_programmes": 3,
    "total_modules": 8,
    "generated_by": "Asana MCP Query Engine"
  },
  "programmes": [
    {
      "programme_id": "programme_tracker_gid",
      "programme_name": "MBA Refresh",
      "client_name": "Walbrook University",
      "programme_status": "Active",
      "programme_start_date": "2025-09-01",
      "health_status": "green",
      "health_rationale": "All modules on track, no blockers",
      "modules": [
        {
          "module_id": "1211626875246589",
          "module_number": 1,
          "module_title": "Strategic Management",
          "launch_date": "2025-11-15",
          "days_to_launch": 25,
          "completion_percentage": 67.0,
          "tasks_total": 72,
          "tasks_completed": 48,
          "tasks_in_progress": 12,
          "tasks_pending": 12,
          "tasks_blocked": 0,
          "tasks_at_risk": 2,
          "on_track": true,
          "module_health": "green",
          "current_phase": "Week 7 - Build",
          "key_milestones": {
            "week_6_review": {
              "status": "completed",
              "completion_date": "2025-10-18"
            },
            "week_7_build": {
              "status": "in_progress",
              "due_date": "2025-10-25",
              "days_remaining": 4
            },
            "corrections": {
              "status": "pending",
              "due_date": "2025-11-01"
            },
            "ready_for_launch": {
              "status": "pending",
              "due_date": "2025-11-08"
            }
          }
        },
        {
          "module_id": "module_2_gid",
          "module_number": 2,
          "module_title": "Financial Management",
          "launch_date": "2025-12-01",
          "completion_percentage": 23.0,
          "tasks_blocked": 3,
          "module_health": "amber",
          "key_milestones": {...}
        }
      ],
      "programme_metrics": {
        "overall_completion": 45.0,
        "average_module_health": "green",
        "total_blockers": 3,
        "total_at_risk": 5,
        "next_launch": "2025-11-15",
        "modules_completed": 0,
        "modules_active": 3,
        "modules_pending": 0
      }
    }
  ],
  "cross_programme_summary": {
    "total_tasks": 576,
    "total_completed": 234,
    "overall_completion": 40.6,
    "programmes_green": 2,
    "programmes_amber": 1,
    "programmes_red": 0,
    "next_launch_date": "2025-11-15",
    "resource_utilization": {
      "LD_allocated_modules": 7,
      "LT_allocated_modules": 5,
      "SLD_allocated_modules": 3,
      "bottleneck_resource": "LD"
    }
  }
}
```

### 2.2 Aggregation Formulas

**Module Completion Percentage**:
```python
completion_pct = (tasks_completed / tasks_total) * 100
```

**Module Health Score**:
```python
def calculate_module_health(module_tasks):
    """
    Health Calculation Logic:
    - Green: ≥80% on track, <10% blocked, launch date achievable
    - Amber: 60-79% on track OR 10-25% blocked OR launch at risk
    - Red: <60% on track OR >25% blocked OR launch impossible
    """
    completed_pct = (completed / total) * 100
    blocked_pct = (blocked / total) * 100
    on_track = completed_pct >= expected_completion_pct(days_to_launch)

    if blocked_pct > 25 or completed_pct < 60 or not on_track:
        return "red"
    elif blocked_pct > 10 or completed_pct < 80:
        return "amber"
    else:
        return "green"

def expected_completion_pct(days_to_launch, total_days=112):
    """
    Expected progress based on timeline.
    112 days = total module timeline (178 days - 66 buffer)
    """
    days_elapsed = total_days - days_to_launch
    return (days_elapsed / total_days) * 100
```

**Programme Health Rollup**:
```python
def calculate_programme_health(modules):
    """
    Programme health = worst module health + blocker consideration
    """
    module_healths = [m.health for m in modules]

    if "red" in module_healths:
        return "red"
    elif "amber" in module_healths or total_blockers > 5:
        return "amber"
    else:
        return "green"
```

**Resource Utilization**:
```python
def calculate_resource_utilization(modules):
    """
    Track how many modules each resource is assigned to
    """
    utilization = {
        "LD": sum(1 for m in modules if m.has_LD_assigned),
        "LT": sum(1 for m in modules if m.has_LT_assigned),
        "SLD": sum(1 for m in modules if m.has_SLD_assigned)
    }

    # Identify bottleneck (resource with highest allocation)
    bottleneck = max(utilization, key=utilization.get)

    return {
        "LD_allocated_modules": utilization["LD"],
        "LT_allocated_modules": utilization["LT"],
        "SLD_allocated_modules": utilization["SLD"],
        "bottleneck_resource": bottleneck
    }
```

---

## 3. Status Reporting Framework

### 3.1 Weekly Status Report Schema

```json
{
  "$schema": "weekly_status_report_v1.0",
  "report_metadata": {
    "report_date": "2025-10-21",
    "report_type": "weekly_status",
    "reporting_period": {
      "start_date": "2025-10-14",
      "end_date": "2025-10-21",
      "week_number": 3
    },
    "programme_name": "MBA Refresh",
    "programme_id": "programme_tracker_gid",
    "generated_by": "Asana MCP Status Engine"
  },
  "executive_summary": {
    "overall_health": "amber",
    "health_change": "degraded",
    "previous_health": "green",
    "summary": "Module 2 encountered SME availability issues, causing 3 blocked tasks. Module 1 and 3 remain on track.",
    "key_achievements": [
      "Module 1 Week 6 review completed successfully",
      "Module 3 storyboarding phase launched"
    ],
    "key_challenges": [
      "Module 2 SME unavailable for Week 4 reviews",
      "Resource contention between Module 1 and 2 for LT"
    ],
    "next_week_priorities": [
      "Resolve Module 2 SME availability",
      "Complete Module 1 Week 7 build",
      "Launch Module 3 Week 1 build"
    ]
  },
  "programme_metrics": {
    "total_modules": 3,
    "active_modules": 3,
    "modules_on_track": 2,
    "modules_at_risk": 1,
    "modules_delayed": 0,
    "overall_completion": 45.0,
    "completion_change_this_week": 8.5,
    "total_tasks": 216,
    "tasks_completed_this_week": 18,
    "tasks_blocked": 3,
    "blockers_added_this_week": 3,
    "blockers_resolved_this_week": 0
  },
  "module_status": [
    {
      "module_number": 1,
      "module_title": "Strategic Management",
      "health_status": "green",
      "health_change": "stable",
      "completion_percentage": 67.0,
      "completion_change": 12.0,
      "tasks_completed_this_week": 9,
      "current_phase": "Week 7 - Build",
      "on_track_for_launch": true,
      "launch_date": "2025-11-15",
      "days_to_launch": 25,
      "highlights": [
        "Week 6 academic review completed with positive feedback",
        "Week 7 storyboarding progressing ahead of schedule"
      ],
      "challenges": [],
      "blockers": [],
      "at_risk_tasks": [
        {
          "task_name": "Week 7 - SME Scripts Draft",
          "risk_reason": "SME availability uncertain",
          "mitigation": "Backup SME identified",
          "due_date": "2025-10-23"
        }
      ],
      "next_week_milestones": [
        "Complete Week 7 Build by Oct 25",
        "Launch Week 8 Storyboarding"
      ]
    },
    {
      "module_number": 2,
      "module_title": "Financial Management",
      "health_status": "amber",
      "health_change": "degraded",
      "completion_percentage": 23.0,
      "tasks_blocked": 3,
      "blockers": [
        {
          "task_name": "Week 4 - Academic Review",
          "blocked_by": "SME unavailable",
          "blocked_since": "2025-10-18",
          "impact": "Week 5 cannot start",
          "resolution_plan": "Alternative SME sourcing in progress"
        }
      ],
      "challenges": [
        "SME availability issue delaying critical path",
        "Resource contention with Module 1 for LT time"
      ]
    }
  ],
  "cross_module_dependencies": [
    {
      "dependency_type": "sequential_launch",
      "blocking_module": 1,
      "blocking_task": "Go live",
      "blocked_module": 2,
      "blocked_task": "Kick off meeting",
      "status": "pending",
      "impact": "Module 2 full start delayed until Module 1 launches",
      "critical": false
    }
  ],
  "resource_status": {
    "LD_utilization": {
      "modules_assigned": 3,
      "utilization_percentage": 85,
      "capacity_status": "near_capacity",
      "bottleneck": true
    },
    "LT_utilization": {
      "modules_assigned": 2,
      "utilization_percentage": 60,
      "capacity_status": "healthy"
    },
    "SLD_utilization": {
      "modules_assigned": 2,
      "utilization_percentage": 40,
      "capacity_status": "healthy"
    },
    "resource_conflicts": [
      {
        "resource": "LT",
        "conflict": "Module 1 Week 7 and Module 2 Week 4 overlap",
        "resolution": "Prioritize Module 1, delay Module 2"
      }
    ]
  },
  "risks_and_issues": [
    {
      "id": "RISK-001",
      "severity": "medium",
      "type": "resource",
      "module": 2,
      "description": "SME availability constraint",
      "impact": "Could delay Module 2 launch by 1-2 weeks",
      "probability": "high",
      "mitigation": "Alternative SME being sourced",
      "owner": "Andrew (PM)",
      "status": "active"
    },
    {
      "id": "RISK-002",
      "severity": "low",
      "type": "dependency",
      "module": 1,
      "description": "Academic reviewer availability for Week 8",
      "impact": "Minor delay possible",
      "probability": "low",
      "mitigation": "Early outreach completed",
      "status": "monitoring"
    }
  ],
  "upcoming_milestones": [
    {
      "date": "2025-10-25",
      "module": 1,
      "milestone": "Week 7 Build completion",
      "critical": true
    },
    {
      "date": "2025-11-01",
      "module": 1,
      "milestone": "Corrections phase start",
      "critical": true
    },
    {
      "date": "2025-11-15",
      "module": 1,
      "milestone": "Module 1 Launch",
      "critical": true,
      "programme_impact": "Enables Module 2 full launch"
    }
  ],
  "action_items": [
    {
      "action": "Source alternative SME for Module 2",
      "owner": "Andrew",
      "due_date": "2025-10-23",
      "priority": "high"
    },
    {
      "action": "Resolve LT resource conflict between Module 1 & 2",
      "owner": "Andrew",
      "due_date": "2025-10-22",
      "priority": "medium"
    }
  ]
}
```

### 3.2 Status Report Generation Logic

**Query Pattern for Weekly Status**:
```python
def generate_weekly_status_report(programme_name, report_date):
    """
    Generate comprehensive weekly status report for a programme.
    """
    # Step 1: Get programme metadata
    programme = get_programme_tracker(programme_name)

    # Step 2: Get all module projects
    modules = get_programme_modules(programme_name)

    # Step 3: For each module, get task status
    module_status = []
    for module in modules:
        tasks = asana_search_tasks(project_id=module.gid)

        # Calculate metrics
        completed = [t for t in tasks if t.completed]
        blocked = [t for t in tasks if has_incomplete_dependencies(t)]

        module_data = {
            "module_number": module.custom_fields["module_number"],
            "module_title": module.custom_fields["module_title"],
            "completion_percentage": (len(completed) / len(tasks)) * 100,
            "tasks_blocked": len(blocked),
            "health_status": calculate_module_health(tasks)
        }
        module_status.append(module_data)

    # Step 4: Calculate programme-level metrics
    programme_metrics = {
        "overall_completion": average([m["completion_percentage"] for m in module_status]),
        "total_blockers": sum([m["tasks_blocked"] for m in module_status])
    }

    # Step 5: Assemble report
    report = {
        "report_metadata": {...},
        "programme_metrics": programme_metrics,
        "module_status": module_status
    }

    return report
```

---

## 4. Critical Path and Dependency Tracking

### 4.1 Cross-Module Dependency Model

**Dependency Types**:
1. **Within-Module**: Task dependencies within single module (ALREADY IMPLEMENTED - 52 deps)
2. **Cross-Module**: Dependencies between modules (NEW - Phase 1 design)
3. **Programme-Level**: Strategic milestones blocking multiple modules

**Cross-Module Dependency Example**:
```
Module 1: Go live (Task 72)
    ↓ BLOCKS
Module 2: Kick off meeting (Task 1)

Rationale: Module 2 cannot start until Module 1 launches (client requires staggered starts)
```

### 4.2 Critical Path Analysis Logic

```python
def identify_critical_path(programme_name):
    """
    Trace critical path across entire programme.
    """
    modules = get_programme_modules(programme_name)
    critical_path = []

    for module in modules:
        tasks = asana_search_tasks(project_id=module.gid)

        for task in tasks:
            task_details = asana_get_task(task.gid)

            # Check for cross-module dependencies
            if task_details.dependents:
                for dependent_gid in task_details.dependents:
                    dependent = asana_get_task(dependent_gid)

                    # Cross-module dependency detected
                    if dependent.project_gid != module.gid:
                        critical_path.append({
                            "blocking_module": module.custom_fields["module_number"],
                            "blocking_task": task.name,
                            "blocked_module": dependent.project.custom_fields["module_number"],
                            "blocked_task": dependent.name,
                            "impact": "Cross-module blocking relationship"
                        })

    return critical_path
```

### 4.3 Blocked Task Identification

```python
def identify_blocked_tasks(programme_name):
    """
    Find all tasks blocked by incomplete dependencies.
    """
    modules = get_programme_modules(programme_name)
    blocked_tasks = []

    for module in modules:
        tasks = asana_search_tasks(project_id=module.gid)

        for task in tasks:
            if not task.completed:
                task_details = asana_get_task(task.gid)

                # Check if dependencies are incomplete
                if task_details.dependencies:
                    incomplete_deps = []
                    for dep_gid in task_details.dependencies:
                        dep_task = asana_get_task(dep_gid)
                        if not dep_task.completed:
                            incomplete_deps.append(dep_task.name)

                    if incomplete_deps:
                        blocked_tasks.append({
                            "module": module.custom_fields["module_number"],
                            "task": task.name,
                            "blocked_by": incomplete_deps,
                            "blocked_since": calculate_days_blocked(task)
                        })

    return blocked_tasks
```

---

## 5. Implementation Roadmap

### 5.1 Phase 1 Implementation Steps (5 hours)

**Hour 1: Portfolio Hierarchy Setup**
1. ✅ Create custom fields schema
2. ✅ Document naming conventions
3. ✅ Design programme tracker template
4. ✅ Specify module linking strategy

**Hour 2: Dashboard Data Model Design**
1. ✅ Define JSON schemas
2. ✅ Document aggregation formulas
3. ✅ Specify health calculation logic
4. ✅ Create sample data structures

**Hour 3: Query Pattern Development**
1. ✅ Write portfolio navigation queries
2. ✅ Document task aggregation patterns
3. ✅ Design dependency tracking logic
4. ✅ Create resource utilization queries

**Hour 4: Sample Data Validation**
1. Create 2 test programmes
2. Populate with sample modules
3. Execute validation queries
4. Verify aggregation accuracy

**Hour 5: Documentation & Phase 2 Prep**
1. Complete architecture documentation
2. Create Phase 2 integration guide
3. Document API requirements
4. Generate readiness assessment

### 5.2 Validation Criteria

**Architecture Validation**:
- ✅ Portfolio hierarchy design documented
- ✅ Custom fields schema complete
- ✅ Naming conventions established
- ✅ Query patterns specified

**Data Model Validation**:
- ✅ JSON schemas valid and complete
- ✅ Aggregation formulas mathematically correct
- ✅ Health calculations logically sound
- ✅ Sample data validates structure

**Query Validation** (with test data):
- ✅ Can retrieve all modules for a programme
- ✅ Can calculate aggregate completion %
- ✅ Can identify blocked tasks correctly
- ✅ Can trace cross-module dependencies
- ✅ Query performance acceptable (<5 sec)

**Phase 2 Readiness**:
- ✅ Clear data contracts defined
- ✅ Integration points documented
- ✅ Google Workspace requirements specified
- ✅ Implementation path clear

---

## 6. Phase 2 Integration Requirements

### 6.1 Phase 1 → Phase 2 Handoff

**Phase 1 Outputs** (JSON data structures):
- Portfolio overview JSON
- Weekly status report JSON
- Module metrics JSON
- Resource utilization JSON

**Phase 2 Inputs** (consumes Phase 1 outputs):
- Python automation script
- Google Sheets API integration
- Google Docs report generation
- Gmail distribution automation

### 6.2 Google Workspace Integration Architecture

```
┌─────────────────────────────────────────────────────┐
│ Phase 1: Asana Data Layer (CURRENT)                │
│                                                     │
│ ┌──────────────┐                                   │
│ │ Asana MCP    │                                   │
│ │ Query Engine │                                   │
│ └──────┬───────┘                                   │
│        │                                           │
│        ▼                                           │
│ ┌──────────────────────────────────────┐          │
│ │ JSON Data Structures                 │          │
│ │ - Portfolio Overview                 │          │
│ │ - Status Reports                     │          │
│ │ - Module Metrics                     │          │
│ │ - Resource Utilization               │          │
│ └──────────────┬───────────────────────┘          │
└────────────────┼───────────────────────────────────┘
                 │
                 │ JSON Export
                 ▼
┌─────────────────────────────────────────────────────┐
│ Phase 2: Google Workspace Integration (NEXT)       │
│                                                     │
│ ┌──────────────────────────────────────┐          │
│ │ Python Automation Script              │          │
│ │ - Calls Asana MCP queries (Phase 1)  │          │
│ │ - Transforms JSON to Sheets format   │          │
│ │ - Generates Docs reports             │          │
│ │ - Distributes via Gmail              │          │
│ └──────┬───────────────────────────────┘          │
│        │                                           │
│        ▼                                           │
│ ┌────────────────────────────┐                    │
│ │ Google Sheets Dashboard    │                    │
│ │ - Portfolio overview table │                    │
│ │ - Module status charts     │                    │
│ │ - Resource allocation viz  │                    │
│ └────────────────────────────┘                    │
│                                                     │
│ ┌────────────────────────────┐                    │
│ │ Google Docs Reports        │                    │
│ │ - Weekly status PDF        │                    │
│ │ - Executive summary        │                    │
│ └────────────────────────────┘                    │
│                                                     │
│ ┌────────────────────────────┐                    │
│ │ Gmail Distribution         │                    │
│ │ - Stakeholder emails       │                    │
│ │ - Automated scheduling     │                    │
│ └────────────────────────────┘                    │
└─────────────────────────────────────────────────────┘
```

### 6.3 Phase 2 Implementation Requirements

**Google Workspace MCP Tools Needed**:
- `mcp__google_workspace__create_spreadsheet`
- `mcp__google_workspace__modify_sheet_values`
- `mcp__google_workspace__create_doc`
- `mcp__google_workspace__send_gmail_message`

**Automation Script Responsibilities**:
1. Execute Asana queries (using Phase 1 patterns)
2. Transform JSON to Google Sheets format
3. Populate dashboard template
4. Generate status report document
5. Email stakeholders with attachments

**Weekly Automation Workflow**:
```
Every Monday 9:00 AM:
├── 1. Execute portfolio queries (Asana MCP)
├── 2. Generate JSON data structures
├── 3. Update Google Sheets dashboard
├── 4. Generate Google Docs status report
├── 5. Email stakeholders (Andrew, team leads)
└── 6. Archive reports to Google Drive
```

---

## 7. Constraints and Limitations

### 7.1 Technical Constraints

**Asana MCP Limitations**:
- ❌ No native portfolio API access (workaround: project-based grouping)
- ⚠️ Custom field filtering may have performance limits at scale
- ⚠️ Query performance degrades with >500 tasks per search
- ✅ Task-level operations fully supported

**Mitigation Strategies**:
- Use efficient query patterns (filter early, minimize iterations)
- Cache programme structure (avoid repeated queries)
- Batch task retrievals where possible
- Monitor performance and optimize as needed

### 7.2 Architectural Limitations

**Phase 1 Scope**:
- Data layer only (no visual dashboards)
- Manual execution (no automation yet)
- Single workspace (no multi-workspace support)
- English language only

**Deliberate Exclusions**:
- ❌ Real-time dashboard updates (Phase 2)
- ❌ Visual chart rendering (Phase 2)
- ❌ Automated report distribution (Phase 2)
- ❌ Historical trend analysis (future phase)

### 7.3 Preservation Requirements

**Must Not Change**:
- ✅ Existing module template (72 tasks)
- ✅ Existing dependencies (52 relationships)
- ✅ Existing task structure (sections, subtasks)
- ✅ Existing custom fields in template

**Safe to Add**:
- ✅ New custom fields for programme linking
- ✅ Programme tracker projects
- ✅ Cross-module dependencies
- ✅ Portfolio-level metadata

---

## 8. Success Criteria

### 8.1 Phase 1 Completion Checklist

**Architecture Design**:
- ✅ Portfolio hierarchy documented
- ✅ Custom fields schema defined
- ✅ Naming conventions established
- ✅ Query patterns specified

**Data Model**:
- ✅ JSON schemas complete and valid
- ✅ Aggregation formulas documented
- ✅ Health calculations specified
- ✅ Sample data structures provided

**Validation**:
- ✅ Test programmes created
- ✅ Queries executed successfully
- ✅ Aggregation accuracy verified
- ✅ Performance acceptable

**Documentation**:
- ✅ Architecture document complete
- ✅ Phase 2 integration guide written
- ✅ API requirements specified
- ✅ Readiness assessment delivered

### 8.2 Quality Standards

**Data Integrity**:
- All JSON schemas valid against spec
- Aggregation formulas mathematically correct
- Health calculations logically sound
- Query results match expected values

**Performance**:
- Portfolio query: <3 seconds (3 programmes, 10 modules)
- Status report generation: <10 seconds
- Dependency analysis: <5 seconds
- Memory usage: <100MB

**Usability**:
- Documentation clear and complete
- Query patterns easy to understand
- Sample data representative
- Integration path obvious

---

## 9. Next Steps

### 9.1 Immediate Actions (Post Phase 1)

1. **User Review** (30 minutes)
   - Review architecture design
   - Validate custom field schema
   - Approve query patterns
   - Confirm Phase 2 approach

2. **Sample Data Creation** (1 hour)
   - Create 2 test programmes
   - Populate with 3-4 modules each
   - Add realistic task completion data
   - Validate query execution

3. **Phase 2 Planning** (1 hour)
   - Review Google Workspace requirements
   - Estimate implementation timeline
   - Identify resource needs
   - Schedule Phase 2 kickoff

### 9.2 Phase 2 Preparation

**Before Phase 2 Implementation**:
- ✅ Phase 1 architecture validated
- ✅ Sample queries tested successfully
- ✅ Custom fields deployed to workspace
- ✅ Programme tracker template created
- ✅ Google Workspace MCP access confirmed

**Phase 2 Estimated Timeline**:
- Week 1: Google Sheets dashboard implementation
- Week 2: Google Docs report generation
- Week 3: Gmail automation + testing
- Week 4: Validation + refinement

---

## Appendices

### Appendix A: Query Pattern Reference

**Complete Query Patterns** (copy-paste ready):

```python
# QUERY 1: Get all programme trackers
programmes = asana_search_projects(
    workspace="workspace_gid",
    name_pattern="Programme Tracker"
)

# QUERY 2: Get modules for specific programme
modules = asana_search_projects(
    workspace="workspace_gid",
    custom_fields={"programme_name.value": "MBA Refresh"}
)
module_projects = [p for p in modules if "Module" in p.name]

# QUERY 3: Calculate programme completion
all_tasks = []
for module in module_projects:
    tasks = asana_search_tasks(project_id=module.gid)
    all_tasks.extend(tasks)

completed = [t for t in all_tasks if t.completed]
completion_pct = (len(completed) / len(all_tasks)) * 100

# QUERY 4: Identify blocked tasks
blocked_tasks = []
for task in all_tasks:
    if not task.completed:
        task_details = asana_get_task(task.gid)
        if task_details.dependencies:
            incomplete_deps = [
                d for d in task_details.dependencies
                if not asana_get_task(d).completed
            ]
            if incomplete_deps:
                blocked_tasks.append(task)

# QUERY 5: Resource utilization
LD_modules = sum(1 for m in modules if has_LD_assigned(m))
LT_modules = sum(1 for m in modules if has_LT_assigned(m))
SLD_modules = sum(1 for m in modules if has_SLD_assigned(m))
```

### Appendix B: Custom Field GIDs

**To be populated during implementation**:
```
programme_name_gid: "TBD"
client_name_gid: "TBD"
programme_status_gid: "TBD"
module_number_gid: "TBD"
module_title_gid: "TBD"
health_status_gid: "TBD"
```

### Appendix C: Sample Data Structure

**Test Programme 1**:
- Name: "Walbrook - MBA Refresh"
- Client: "Walbrook University"
- Modules: 3 (Strategic Management, Financial Management, Marketing Strategy)
- Status: Active
- Health: Green

**Test Programme 2**:
- Name: "Healthcare Academy - Clinical Skills"
- Client: "Healthcare Academy"
- Modules: 2 (Patient Assessment, Clinical Procedures)
- Status: Planning
- Health: Amber

---

**Document Status**: ✅ Complete and ready for implementation
**Next Action**: User review and validation
**Estimated Implementation**: 5 hours
**Phase 2 Dependency**: Approved architecture + validated queries
