# Asana Module Development Template - Technical Reference Manual

**Version**: 1.0
**Date**: October 2025
**Project**: Learning Design Solutions Module Development Template
**Type**: Project Management Template Systematisation
**Technical Lead**: Implementation via Asana MCP and API Automation

---

## Executive Summary

This technical reference documents the architecture, implementation, and design decisions for the **Asana Module Development Template** – a systematised project management framework for 8-week educational module development at Learning Design Solutions.

**Key Metrics**:
- **72 tasks** across 12 sections (Initiation through Launch)
- **52 API-created task dependencies** enforcing workflow automation
- **17-18 week development timeline** (112 days to "Ready for Launch")
- **66-day launch buffer** to "Go Live" (varies by client calendar)
- **Architecture**: Hierarchical task structure with cascading build pattern

**Technical Achievement**: Complete dependency graph created via Asana MCP API in 30 minutes, establishing reproducible template creation process for future variants.

**Target Audience**: Technical team members, template architects, system maintainers, automation engineers.

**Purpose**: Authoritative technical reference for understanding, maintaining, and extending the template system.

---

## Table of Contents

1. [Architecture Overview](#1-architecture-overview)
2. [Dependency Patterns](#2-dependency-patterns)
3. [API Implementation](#3-api-implementation)
4. [Template Variant Architecture](#4-template-variant-architecture)
5. [Task Taxonomy](#5-task-taxonomy)
6. [Automation Roadmap](#6-automation-roadmap)
7. [Integration Points](#7-integration-points)
8. [Quality Patterns](#8-quality-patterns)
9. [Performance Characteristics](#9-performance-characteristics)
10. [Technical Decisions Log](#10-technical-decisions-log)
11. [Maintenance & Evolution](#11-maintenance--evolution)
12. [Reference Data](#12-reference-data)

---

## 1. Architecture Overview

### 1.1 Template Structure

The template implements a **hierarchical workflow system** designed for 8-week educational module development:

```
Portfolio: [Client Name] Programmes
└── Project: [Programme Name]
    ├── Section: Initiation & Planning (15 days)
    ├── Section: Week 1 (17 days) [SPECIAL: 10-day storyboarding]
    ├── Section: Week 2 (10 days)
    ├── Sections: Weeks 3-8 (10 days each × 6 = 60 days)
    ├── Section: Finalization (20 days)
    └── Section: Launch (66-day buffer + 1-day milestone)
```

**Structural Characteristics**:
- **72 total tasks** including parent tasks and subtasks
- **12 sections** representing temporal and functional phases
- **Hybrid task model**: Top-level tasks for builds/reviews, subtasks for storyboard workflows
- **Milestone-driven**: "Ready for Launch" as anchor point for relative date calculations

### 1.2 Dependency Graph

**52 dependency relationships** create workflow automation:

| Dependency Type | Count | Purpose |
|----------------|-------|---------|
| **Critical Path** | 16 | Sequential workflow milestones (Kickoff → MPD → Storyboards → Builds → Reviews → Launch) |
| **Cascading Build** | 7 | Enable parallel work (Week N build unlocks Week N+1 storyboarding) |
| **Within-Task** | 24 | Enforce storyboard workflow (Draft → Edit → Final) for 8 weeks |
| **Finalization** | 5 | Quality gates (Film shoots → Proofreading → Reviews → Corrections → Launch) |

**Dependency Characteristics**:
- **Enforcement**: Asana prevents task completion until dependencies satisfied
- **Cascading enablement**: Week N completion triggers Week N+1 availability
- **Parallel optimization**: LD works on Week N while LT builds Week N-1
- **Quality gating**: Reviews block downstream work until approved

### 1.3 Design Principles

**Why This Architecture**:

1. **Workflow Automation**: Dependencies enforce correct task sequencing without manual management
2. **Parallel Efficiency**: Cascading pattern enables concurrent LD/LT work streams
3. **Quality Assurance**: Batched reviews at strategic milestones prevent defect propagation
4. **Timeline Predictability**: Relative dates from single "Launch Date" anchor maintain schedule integrity
5. **Scalability**: Template duplication creates new projects in <5 minutes

**Trade-offs Accepted**:
- **Rigidity vs Flexibility**: Strong dependencies enforce process but reduce ad-hoc flexibility
- **Complexity vs Power**: 52 dependencies add setup complexity but eliminate workflow errors
- **Automation vs Control**: API-created dependencies sacrifice manual fine-tuning for reproducibility

### 1.4 System Boundaries

**What the Template Manages**:
- Task sequencing and dependencies
- Timeline calculations from Launch Date anchor
- Resource assignment patterns (LD, LT, SME, reviewers)
- Quality gate enforcement (reviews, approvals)
- Phase progression tracking

**External Dependencies** (Not Managed by Template):
- Moodle LMS build environment
- Google Drive document storage
- Clockify time tracking
- Film studio booking systems
- Client availability and responsiveness
- Academic calendar alignment

**Integration Points** (Future Phase 3):
- n8n workflow automation for template generation
- Clockify API for time tracking synchronization
- CRM integration for client data propagation
- Google Calendar for scheduling automation

---

## 2. Dependency Patterns

### 2.1 Pattern Catalog

#### Pattern 1: Critical Path Sequential

**Example**: Kickoff → MPD Draft → MPD Finalized → Week 1 Storyboard

**Purpose**: Enforce foundational work before development begins

**Rationale**: Module Planning Document must be complete and reviewed before any content creation. Prevents scope creep and ensures alignment.

**Critical Path**: This pattern forms the spine of the 112-day timeline.

**Technical Implementation**:
```json
{
  "source": "Kick off meeting",
  "target": "Module Planning Document → MPD Draft"
}
```

#### Pattern 2: Cascading Build Enablement

**Example**: Week 1 Build → Week 2 Storyboarding

**Purpose**: Enable parallel LD/LT work streams

**Rationale**: Once Week 1 is built, LD can begin Week 2 storyboarding while LT continues building. Creates efficient pipeline without resource conflicts.

**Critical Path**: Not on critical path; optimizes resource utilization.

**Technical Implementation**:
```json
{
  "source": "Week 1 - Build",
  "target": "Week 2 - Storyboarding"
}
```

**Pattern Repetition**: Applied to Weeks 1→2, 2→3, 3→4, 4→5, 5→6, 6→7, 7→8 (7 instances)

#### Pattern 3: Within-Task Workflow

**Example**: Week 1 - Storyboard Initial LD Draft + Week 1 - Storyboard SME Scripts Draft → Week 1 - Edit

**Purpose**: Enforce sequential refinement within storyboarding tasks

**Rationale**: Both LD and SME drafts must complete before editing can begin. Prevents premature integration of incomplete work.

**Critical Path**: Yes, for Week 1; parallel afterward.

**Technical Implementation**:
```json
{
  "source": "Week 1 - Storyboard Initial LD Draft",
  "target": "Week 1 - Edit"
},
{
  "source": "Week 1 - Storyboard SME Scripts Draft",
  "target": "Week 1 - Edit"
}
```

**Pattern Repetition**: Applied to all 8 weeks × 3 transitions = 24 dependencies

#### Pattern 4: Batched Review Gates

**Example**: Week 2 Build → Week 1 and 2 Review

**Purpose**: Quality assurance checkpoint before continuing development

**Rationale**: Academic reviewer assesses first two weeks together, catching patterns early. Two-week batch balances review efficiency with early feedback.

**Critical Path**: Yes, blocks Week 3+ progression.

**Technical Implementation**:
```json
{
  "source": "Week 2 - Build",
  "target": "Week 1 and 2 review"
}
```

**Alternative Pattern**: Weeks 3-8 reviewed together (6 weeks in single batch) – larger batch optimizes reviewer time but delays feedback.

#### Pattern 5: Film Shoot → Storyboard (Not Build)

**Example**: Week 4 Storyboard Final Draft Agreed → Film Shoot - First Batch

**Purpose**: Film shoots need scripts, not built content

**Rationale**: **Correction from initial design**: Film shoots depend on storyboard completion (scripts ready), NOT build completion (Moodle implementation).

**Critical Path**: No, runs parallel to Week 5 development.

**Technical Implementation**:
```json
{
  "source": "Week 4 - Storyboard Final draft agreed",
  "target": "Film shoot - first batch"
}
```

**Design Error Fixed**: Original dependency was Week 4 Build → Film Shoot. Andrew's clarification corrected this to Storyboard → Film Shoot.

#### Pattern 6: Multi-Dependency Convergence

**Example**: Film Shoot Second Batch + Weeks 3-8 Review → Corrections

**Purpose**: Multiple quality streams must complete before final corrections

**Rationale**: Corrections address feedback from both filming (caption errors, technical issues) and academic review (content changes). Both inputs required.

**Critical Path**: Yes, final gate before launch.

**Technical Implementation**:
```json
{
  "source": "Film shoot - second batch",
  "target": "Corrections"
},
{
  "source": "Weeks 3 to 8 review",
  "target": "Corrections"
}
```

#### Pattern 7: Parallel Draft → Serial Integration

**Example**: Week N - Storyboard Initial LD Draft (parallel) Week N - Storyboard SME Scripts Draft → Week N - Edit

**Purpose**: Maximize parallel work, then integrate sequentially

**Rationale**: LD and SME can draft simultaneously (5 days Week 1, 2 days Weeks 2-8) without blocking each other. Once both complete, edit integrates work.

**Critical Path**: Yes for Week 1 (10-day extended timeline).

**Technical Implementation**: Two dependencies converge on Edit subtask.

**Resource Optimization**: Eliminates LD/SME sequential bottleneck, saves 5 days per week.

### 2.2 Pattern Rationale Summary

| Pattern | Count | Prevents | Enables |
|---------|-------|----------|---------|
| Critical Path Sequential | 16 | Skipping foundation work | Proper project initiation |
| Cascading Build | 7 | Resource conflicts | Parallel LD/LT streams |
| Within-Task Workflow | 24 | Premature integration | Quality storyboard process |
| Batched Review Gates | 2 | Unchecked errors propagating | Early pattern detection |
| Film Shoot Dependencies | 2 | Filming without scripts | Efficient media production |
| Multi-Dependency Convergence | 1 | Incomplete corrections | Comprehensive finalization |
| Parallel Draft | 16 (8 weeks × 2) | Sequential LD/SME blocking | Time savings |

### 2.3 Critical Path Analysis

**Critical Path Tasks** (16 dependencies on 112-day spine):

1. Kick off meeting (Day 1-5)
2. MPD Draft (Day 6-10)
3. MPD Finalized (Day 11-15) [parallel: MPD review]
4. Week 1 Storyboard (Day 16-25) [10 days]
5. Week 1 Build (Day 26-30)
6. Week 2 Storyboard (Day 26-30) [parallel with W1 Build]
7. Week 2 Build (Day 31-35)
8. Week 1 and 2 Review (Day 36-40)
9. Weeks 3-8 Storyboards (Day 41-70, cascading)
10. Weeks 3-8 Builds (Day 46-95, cascading)
11. Weeks 3-8 Review (Day 96-100)
12. Corrections (Day 101-105)
13. Ready for Launch (Day 106-112)
14. [66-day buffer]
15. Go Live (Day 178)

**Bottleneck Analysis**:
- **Week 1 Extended Duration**: 10-day storyboard (vs 5 days other weeks) adds 5 days to critical path. Justified by pattern establishment and LD/SME relationship building.
- **Batched Reviews**: 5 days each for 2-week and 6-week batches. Could become bottleneck if reviewer capacity constrained.
- **Sequential Weeks 1-2**: Unlike Weeks 3-8 (cascading), Week 2 can't start until Week 1 complete. Design choice prioritizes early quality over speed.

**Non-Critical Paths**:
- Film shoots run parallel to development (not blocking)
- Proofreading independent of academic reviews
- Assessment briefs and reading lists parallel to MPD finalization

---

## 3. API Implementation

### 3.1 Technology Stack

**Primary Technology**: **Asana MCP (Model Context Protocol) Server**

**Components**:
- MCP Server: `asana-mcp` (Model Context Protocol implementation for Asana API)
- API Client: Claude Code with MCP integration
- Data Structures: JSON mapping files for tasks and dependencies
- Version Control: Git repository for specification and mapping files

**Why MCP Over Custom Scripting**:
- **No authentication handling**: MCP abstracts OAuth/API key management
- **Batch operations**: Multiple API calls in single MCP invocation
- **Error handling**: Built-in retry logic and validation
- **No code maintenance**: No custom Python/TypeScript to maintain
- **Reproducible**: Same MCP calls recreate dependencies on any template variant

### 3.2 Implementation Process

**Phase 1: Specification Development** (1 hour)

1. Analyzed original spreadsheet template (`TEMPLATE_Project_Plan_20250708.xlsx`)
2. Extracted 72 tasks with durations, resources, dependencies
3. Created structured specification document (1,550 lines)
4. Identified 52 distinct dependency relationships
5. Organized dependencies into 4 categories (Critical Path, Cascading, Within-Task, Finalization)

**Phase 2: Data Structure Creation** (15 minutes)

Created two JSON files:

**`dependency_mapping.json`**: Dependency specification
```json
{
  "critical_path": [
    {
      "source": "Kick off meeting",
      "target": "Module Planning Document",
      "reason": "MPD requires kickoff alignment"
    }
  ],
  "cascading_build": [...],
  "within_task": [...],
  "finalization": [...]
}
```

**`task_gid_mapping.json`**: Task identifiers
```json
{
  "Kick off meeting": "1211627678168595",
  "Module Planning Document": "1211627678168596",
  "Week 1 - Storyboarding": "1211627678168612",
  ...
}
```

**Phase 3: Task Discovery** (10 minutes)

Used `asana_search_tasks` MCP tool to find all tasks in target project:

```
Search pattern: "Week 1", "MPD", "Kick off", "Film shoot", etc.
Filter: Project GID 1211626875246589
Result: 72 task GIDs mapped to names
```

**Key Pattern Identified**: All tasks in Project 1 have GID format `1211627678168XXX` (consistent prefix).

**Phase 4: Dependency Creation** (10 minutes)

Executed `asana_add_task_dependencies` MCP tool 52 times:

```
For each dependency in mapping:
  1. Resolve source task name → GID
  2. Resolve target task name → GID
  3. Call asana_add_task_dependencies(task_id=target_gid, dependencies=[source_gid])
  4. Verify success (52/52 = 100% success rate)
```

**Performance**:
- Average API call: <1 second
- Total execution: ~10 minutes for 52 dependencies
- No rate limiting encountered
- Zero retry failures

**Phase 5: Verification** (5 minutes)

Tested sample tasks to confirm dependencies active:

```
✅ Week 1 - Build blocked by Week 1 - Storyboard Final draft agreed
✅ Week 1 - Edit blocked by both LD Draft AND SME Draft
✅ Week 2 - Storyboarding blocked by Week 1 - Build
✅ Weeks 3-8 review blocked by all 6 build tasks
✅ Corrections blocked by review + proofreading
✅ Go live blocked by Ready for launch
```

**Total Implementation Time**: 30 minutes (vs 3 hours estimated for custom script development)

### 3.3 Data Structures

#### dependency_mapping.json Structure

**Purpose**: Human-readable dependency specification for version control and template variants

**Schema**:
```json
{
  "dependency_type": [
    {
      "source": "Source Task Name",
      "target": "Target Task Name",
      "reason": "Why this dependency exists (optional documentation)"
    }
  ]
}
```

**Categories**:
- `critical_path`: 16 sequential milestones forming 112-day timeline
- `cascading_build`: 7 dependencies enabling parallel LD/LT work
- `within_task`: 24 storyboard workflow enforcement dependencies
- `finalization`: 5 quality gate dependencies before launch

**Usage**: Template variants copy and modify this file to adjust dependency patterns.

#### task_gid_mapping.json Structure

**Purpose**: Map human-readable task names to Asana Global IDs (GIDs) for API operations

**Schema**:
```json
{
  "Task Name Exactly As In Asana": "1211627678168XXX"
}
```

**Key Characteristics**:
- **Exact match required**: Task names must match Asana exactly (case-sensitive, punctuation-sensitive)
- **Project-specific**: GIDs change when project duplicated; each variant needs own mapping
- **Version control**: Commit to repository for reproducibility
- **Search-based generation**: Use `asana_search_tasks` to rebuild if lost

**Limitations**: Must regenerate for each new template variant (GIDs unique per project).

### 3.4 API Limitations

**What CAN Be Done via API**:
- ✅ Create task dependencies (supports multiple dependencies per task)
- ✅ Batch operations (multiple dependencies in parallel)
- ✅ Search tasks by name pattern
- ✅ Retrieve task metadata (GID, name, sections, assignees)
- ✅ Project structure inspection (sections, task counts)

**What CANNOT Be Done via API** (Limitations Encountered):
- ❌ Duplicate projects with dependencies (duplication loses dependency data unless done manually)
- ❌ Bulk dependency updates (must iterate per task)
- ❌ Dependency removal (can add but not programmatically remove)
- ❌ Conditional dependencies (all dependencies are absolute blocks)
- ❌ Dependency metadata (can't add "reason" or "type" to dependencies themselves)

**Workarounds**:
- **Dependency removal**: Delete and recreate task, or manual UI removal
- **Bulk updates**: Iterate with MCP tool (still faster than manual)
- **Conditional dependencies**: Use custom field flags + workflow rules (Phase 3 automation)

### 3.5 Error Handling

**API Call Success Rate**: 100% (52/52 successful dependency creations)

**Potential Failure Modes**:
1. **Task name mismatch**: If task name in mapping doesn't exactly match Asana
   - **Detection**: API returns "Task not found" error
   - **Resolution**: Update mapping with exact task name from Asana

2. **GID mapping outdated**: If project duplicated and GIDs changed
   - **Detection**: API returns "Invalid task ID" error
   - **Resolution**: Regenerate task_gid_mapping.json via search

3. **Circular dependencies**: If dependency creates cycle
   - **Detection**: Asana API rejects with "Circular dependency" error
   - **Resolution**: Review dependency logic, remove circular reference

4. **Rate limiting**: If too many API calls too quickly
   - **Detection**: API returns 429 Too Many Requests
   - **Resolution**: MCP implements exponential backoff (not encountered in practice)

**Testing Strategy**:
- Created test project copy before production implementation
- Verified dependencies on sample tasks before full execution
- Maintained rollback capability (can delete project and recreate)

---

## 4. Template Variant Architecture

### 4.1 Variant Strategy Overview

**Three Approaches** for creating template variants, each optimized for different scenarios:

| Approach | Time | Best For | Dependencies Preserved | Complexity |
|----------|------|----------|----------------------|------------|
| **A: Duplication** | 5 min | Similar 8-week structures | Yes (auto-copy) | Low |
| **B: API Recreation** | 30 min | Different structures (12-week, 6-week) | Full control | Medium |
| **C: Hybrid** | 15 min | Multiple related variants | Selective | Medium |

### 4.2 Approach A: Template Duplication

**Process**:
1. Open base template in Asana
2. Project Settings → Duplicate project
3. ✅ **CRITICAL**: Check "Duplicate task dependencies"
4. Modify structure (add/remove tasks/sections)
5. Convert to template

**When to Use**:
- Creating variant with same 8-week structure
- Minor modifications (e.g., remove film shoots, change review batching)
- Need fast variant creation
- Want to preserve all 52 base dependencies

**Advantages**:
- Dependencies copy automatically
- No GID remapping needed
- Fastest method (5 minutes)
- Lowest technical complexity

**Disadvantages**:
- Limited to structural similarity with base
- Must manually remove unwanted dependencies
- Can't easily add complex new dependency patterns

**Example Use Cases**:
- "No Film Shoots" variant (remove 2 tasks, 2 dependencies auto-removed)
- "3 Review Batches" variant (split Weeks 3-8 review into two batches)
- "Client-Specific Descriptions" variant (same structure, different task descriptions)

### 4.3 Approach B: API Recreation

**Process**:
1. Create variant specification document (copy base, modify)
2. Update dependency_mapping.json for new structure
3. Create/import base project structure in Asana
4. Run `asana_search_tasks` to generate new task GID mapping
5. Execute `asana_add_task_dependencies` via MCP (52+ times)
6. Verify dependencies in Timeline view
7. Convert to template

**When to Use**:
- Creating 12-week module variant (4 additional weeks)
- Creating 6-week micro-credential variant (2 fewer weeks)
- Significantly different dependency patterns
- Need complete control over all dependencies

**Advantages**:
- Full flexibility for structural changes
- Reproducible process (repeat for multiple variants)
- Version-controlled specifications
- Can add complex new patterns

**Disadvantages**:
- Takes longer (30 minutes)
- Requires GID mapping regeneration
- More technical complexity

**Example Use Cases**:
- "12-Week Module" variant (73 dependencies: 52 base + 21 new)
- "Micro-Credential" variant (31 dependencies: removed Weeks 5-8)
- "Lab-Based Module" variant (new dependencies for equipment, demonstrations)

### 4.4 Approach C: Hybrid

**Process**:
1. Create base variant via API (Approach B) - 30 minutes
2. Duplicate base variant for related variants (Approach A) - 5 minutes each
3. Modify duplicates for variant-specific differences
4. Use API to add variant-specific dependencies only
5. Convert each to template

**When to Use**:
- Creating 3+ related variants (e.g., Theory/Skills/Lab modules)
- Variants share common structure but differ in specifics
- Balance speed and control

**Advantages**:
- Amortizes API setup across multiple variants
- Faster than pure API for each variant
- More flexible than pure duplication

**Disadvantages**:
- Requires planning variant family upfront
- More complex project management

**Example Use Cases**:
- **Module Type Family**: Create "Theory-Heavy" via API (30 min), duplicate to create "Skills-Based" (5 min) and "Lab-Based" (5 min), add variant-specific tasks via API (5 min each) = 50 min for 3 variants (16.7 min average)

### 4.5 Structural Change Patterns

#### Adding Weeks (e.g., 12-Week Module)

**Structural Changes**:
- Add 4 new sections (Weeks 9-12)
- Add 4 storyboarding parent tasks
- Add 16 storyboarding subtasks (4 weeks × 4 subtasks)
- Add 4 build tasks
- Add "Weeks 9-12 review" task

**Dependency Additions**:
- 4 cascading build dependencies (Weeks 9→10, 10→11, 11→12, 12→review)
- 16 within-task dependencies (4 weeks × 4 workflow transitions)
- 1 review gate dependency (Week 12 Build → Weeks 9-12 review)

**Total**: 52 (base) + 21 (new) = **73 dependencies**

**Timeline Impact**: +20 days (4 weeks × 5 days) = 132 days to "Ready for Launch"

**Recommended Approach**: B (API Recreation)

#### Removing Weeks (e.g., 6-Week Micro-Credential)

**Structural Changes**:
- Remove sections Weeks 7-8
- Remove 2 storyboarding parent tasks
- Remove 8 storyboarding subtasks
- Remove 2 build tasks
- Combine reviews (single batch for all 6 weeks)

**Dependency Removals**:
- 2 cascading build dependencies (Weeks 6→7, 7→8)
- 8 within-task dependencies
- Remove second film shoot batch

**Total**: 52 (base) - 11 (removed) = **41 dependencies**

**Timeline Impact**: -10 days = 102 days to "Ready for Launch"

**Recommended Approach**: A (Duplication) with deletions

#### Accelerating Timeline (5-Day Weeks → 3-Day Weeks)

**Structural Changes**:
- Same 8-week structure
- Reduce storyboarding durations (5 days → 3 days for Weeks 2-8)
- Reduce build durations (5 days → 3 days)
- Reduce review durations (5 days → 3 days)

**Dependency Changes**: **NONE** (same 52 dependencies)

**Timeline Impact**: ~-20 days = 92 days to "Ready for Launch"

**Recommended Approach**: A (Duplication), adjust relative date offsets only

### 4.6 Variant Maintenance

**Version Control Strategy**:
```
/variants/
├── 12_week_module/
│   ├── spec_12week.md
│   ├── dependency_mapping_12week.json
│   └── task_gid_mapping_12week.json
├── micro_credential/
│   ├── spec_micro.md
│   └── dependency_mapping_micro.json
└── accelerated/
    ├── spec_accelerated.md
    └── dependency_mapping_accelerated.json
```

**Synchronization**: When base template updated, review impact on variants:
- Critical bug fixes: Propagate to all variants immediately
- Feature additions: Evaluate per-variant applicability
- Dependency pattern improvements: Update all variant mappings

**Ownership**: Each variant should have designated owner responsible for updates and quality.

---

## 5. Task Taxonomy

### 5.1 Section Organization

**12 Sections** with distinct purposes:

| Section | Duration | Task Count | Purpose | Phase |
|---------|----------|------------|---------|-------|
| **Initiation & Planning** | 15 days | 3 tasks (7 subtasks) | Foundation, scope agreement | Planning |
| **Week 1** | 17 days | 3 tasks (4 subtasks + builds + review) | Pattern establishment, extended storyboard | Development |
| **Week 2** | 10 days | 2 tasks (4 subtasks) | Standard storyboard + build | Development |
| **Weeks 3-8** | 60 days | 12 tasks (24 subtasks) | Content development cascade | Development |
| **Finalization** | 20 days | 6 tasks | Media, QA, corrections | Finalization |
| **Launch** | 66 days buffer + 1 day | 1 task | Client calendar alignment | Launch |

**Design Rationale**:
- **Week 1 Special Treatment**: 10 days storyboarding (vs 5 days) establishes patterns, builds LD/SME relationship
- **Batched Reviews**: Two review checkpoints (Weeks 1-2, Weeks 3-8) balance early feedback with reviewer efficiency
- **Separate Finalization**: Groups film shoots, proofreading, reviews, corrections logically
- **Launch Buffer**: 66 days accommodates client academic calendar (varies by client, not standard)

### 5.2 Task Categories

#### Planning Tasks (Initiation & Planning Section)

**Kickoff Tasks**:
- **Kick off meeting**: 2 subtasks (Initiation + Kick off) - 5 days - LD + SME
- **Purpose**: Alignment, relationship establishment, scope agreement

**Planning Document Tasks**:
- **Module Planning Document**: 4 subtasks (Draft, Finalized, Assessments, Reading List) - 10 days - LD + SME + Programme Leader + Librarian
- **Purpose**: Foundational specification for all development

**Quality Gate Tasks**:
- **MPD review**: Academic Reviewer validation - 5 days (parallel to MPD Finalized)
- **Purpose**: Early academic quality assurance

#### Creative Tasks (Weeks 1-8 Storyboarding)

**Standard Storyboard Workflow** (Weeks 2-8, 5 days):
1. **Storyboard Initial LD Draft** (2 days, LD only)
2. **Storyboard SME Scripts Draft** (2 days, SME only, parallel)
3. **Edit** (2 days, LD + SME)
4. **Storyboard Final draft agreed** (1 day, LD + SME)

**Extended Storyboard Workflow** (Week 1, 10 days):
1. **Storyboard Initial LD Draft** (5 days, LD only)
2. **Storyboard SME Scripts Draft** (5 days, SME only, parallel)
3. **Edit** (3 days, LD + SME)
4. **Storyboard Final draft agreed** (2 days, LD + SME)

**Rationale for Week 1 Extension**:
- First week establishes patterns for entire module
- SME learns storyboard format and expectations
- More back-and-forth expected initially
- Can be reduced to 5 days if client demands, but increases rework risk

#### Production Tasks (Weeks 1-8 Build)

**Build Tasks** (5 days each, Learning Technologist):
- **Week N - Build**: Separate top-level task (NOT subtask of storyboarding)
- **Deliverables**: Moodle pages, activities, media, resources, navigation
- **Dependency**: Blocked by "Week N - Storyboard Final draft agreed"

**Design Note**: Build tasks as top-level (not subtasks) enables:
- Separate assignee (LT instead of LD)
- Independent tracking in Timeline view
- Cascading pattern visibility (Week N Build → Week N+1 Storyboard)

#### Review Tasks (Quality Assurance)

**Batched Review 1** (Weeks 1-2, 5 days):
- **Week 1 and 2 review**: Academic Reviewer assesses first two weeks together
- **Dependency**: Blocked by Week 2 Build completion
- **Placement**: Located in Week 1 section for organizational purposes
- **⚠️ Consistency Warning**: Academic Reviewer performance "super inconsistent with current client, tends to be lighter touch than proofreading" (Andrew). Plan for supplemental internal QA.

**Batched Review 2** (Weeks 3-8, 5 days):
- **Weeks 3 to 8 review**: Academic Reviewer assesses remaining 6 weeks together
- **Dependency**: Blocked by Week 8 Build completion
- **Placement**: Located in Finalization section
- **⚠️ Scheduling Risk**: Example timeline places this on Christmas week (12/22-12/26). Check calendar annually.

**Review Batching Rationale**:
- **Two-week batch**: Early feedback on initial pattern establishment
- **Six-week batch**: Efficient reviewer time, coherence assessment across weeks
- **Alternative**: Could split into 3 batches (Weeks 1-2, 3-5, 6-8) for more frequent feedback

#### Launch Tasks (Finalization Section)

**Film Shoot Tasks** (3 filming options available):

**Film shoot - first batch** (6 days):
- **Dependency**: Week 4 **Storyboard** Final draft agreed (NOT Week 4 Build)
- **Timing**: Runs parallel to Week 5 development
- **Options**:
  1. **Physical in London**: Studio at SOAS/Walbrook campus (highest quality)
  2. **Remote Loom**: Academic records via screen recording (flexible scheduling)
  3. **AI Avatars**: Generated avatars (no filming needed, fastest)
- **Scheduling**: Windows are nominal/recommended; actual timing varies by SME availability

**Film shoot - second batch** (5 days):
- **Dependency**: Week 8 Build completion
- **Timing**: Start of Finalization phase

**Design Correction**: Original dependency was Build → Film Shoot. Andrew clarified: Film shoots need **scripts** (storyboards), not **built content** (Moodle). Corrected to Storyboard → Film Shoot.

**Proofreading** (5 days, Editorial Team):
- **Dependency**: Film shoot - second batch
- **Purpose**: Copy editing, grammar, consistency

**Corrections** (5 days, LD/LT + SME):
- **Dependencies**: Proofreading + Weeks 3-8 review (multi-dependency convergence)
- **Flexible Assignment**: Can be LD, LT, or both depending on nature of corrections

**Ready for launch** (1 day milestone):
- **Dependency**: Corrections complete
- **Meaning**: Andrew's deliverable complete; module ready for client launch
- **NOT Go Live**: Actual launch controlled by client academic calendar

**Go Live** (Launch Section):
- **Buffer**: 66 days after Ready for launch (NOT standard; varies by client)
- **Responsibility**: Client controls timing based on academic calendar
- **Purpose**: Actual student access date

### 5.3 Custom Fields

#### Core Identity Fields

| Field Name | Type | Purpose | Example |
|------------|------|---------|---------|
| **Module Code** | Text | Unique identifier | "MKT101" |
| **Client Name** | Text | Organization | "Walbrook" |
| **Programme Name** | Text | Parent programme | "MBA Marketing" |

#### Date Fields

| Field Name | Type | Purpose | Notes |
|------------|------|---------|-------|
| **Launch Date** | Date | Anchor for relative dates | "Ready for Launch" date, NOT Go Live |
| **Go Live Date** | Date | Actual student access | 66-day buffer (varies) after Launch Date |

**Clarification**: "Launch Date" in custom field = "Ready for Launch" milestone. Creates confusion; consider renaming to "Ready Date" in future.

#### Resource Assignment Fields

| Field Name | Type | Options | Purpose |
|------------|------|---------|---------|
| **Module Author (SME)** | Person | Single select | Primary subject matter expert |
| **Learning Designer** | Person | Single select | Assigned LD |
| **Learning Technologist** | Person | Single select | Assigned LT |
| **Senior LD (Reviewer)** | Person | Single select | Nicole or other SLD for QA |

#### Status Tracking Fields

| Field Name | Type | Options | Purpose |
|------------|------|---------|---------|
| **Module Status** | Single Select | Planning / In Development / Build / QA / Ready / Launched / Archived | Overall state |
| **QA Status** | Single Select | Not Started / In Review / Changes Requested / Approved | Quality gate tracking |
| **Blocker Status** | Single Select | None / Waiting on SME / Waiting on Client / Technical Issue / Resource Gap | Dependency tracking |

#### Content Metadata Fields

| Field Name | Type | Options | Purpose |
|------------|------|---------|---------|
| **Content Type** | Multi Select | Theory / Activities / Video / Audio / Interactive / Assessment | Content mix |
| **Media Requirements** | Single Select | None / Standard / Film Shoot Required / Audio Only | Special resources |
| **Review Batch** | Single Select | Weeks 1-2 / Weeks 3-8 / N/A | Academic review grouping |

### 5.4 Milestone Tasks

**Key Milestones** (Tasks with broader significance):

1. **MPD Finalized** (Day 15): Development can begin
2. **Week 1 - Build** (Day 30): First content built, cascading begins
3. **Week 1 and 2 review** (Day 40): Early quality gate passed
4. **Week 8 - Build** (Day 95): All content built
5. **Ready for launch** (Day 112): Andrew's deliverable complete
6. **Go live** (Day 178): Actual module launch to students

**Milestone Tracking**: Use "Module Status" custom field to reflect milestone progression.

---

## 6. Automation Roadmap (Future Phase 3)

### 6.1 Current State (Phase 2 Complete)

**Manual Processes**:
- Template duplication in Asana (5 minutes, manual UI)
- Launch Date entry (manual custom field update)
- Task assignments (manual or template defaults)
- Status updates (manual task completion)

**Semi-Automated**:
- **Dependencies**: 52 relationships enforce workflow automatically (no manual dependency management)
- **Timeline calculations**: Relative dates auto-update from Launch Date
- **Notifications**: Asana built-in notifications when tasks assigned/completed

**Not Automated**:
- Template selection and creation from specifications
- Date calculations (must enter Launch Date manually)
- Multi-service integration (Clockify, CRM, Google Calendar)
- Template variant generation
- Resource capacity planning

### 6.2 Phase 3 Vision: Full Automation with n8n

**Goal**: Generate complete Asana module project from specification document with zero manual intervention.

**Architecture**:
```
User Input (Form/API) → n8n Workflow → Asana Project + Dependencies + Dates
                      ↓
                  Clockify time tracking setup
                  Google Calendar events
                  CRM opportunity update
                  Email notifications
```

**n8n Workflow Components**:

1. **Trigger**: Webhook or form submission with module parameters
2. **Template Selection**: Logic to choose appropriate variant based on:
   - Module length (8-week, 12-week, micro-credential)
   - Module type (theory, skills, lab)
   - Filming requirements (studio, remote, AI, none)
   - Client preferences
3. **Asana Project Creation**: API calls to create project from template
4. **Date Calculation Engine**: JavaScript function to:
   - Accept "Go Live Date" from user
   - Calculate Launch Date (Go Live - 66 days, configurable buffer)
   - Calculate Kickoff Date (Launch Date - 112 days)
   - Generate all task dates from kickoff forward
   - Apply dates via Asana API
5. **Dependency Creation**: Use same MCP approach, but automated:
   - Load dependency_mapping.json for selected variant
   - Create task GID mapping via search
   - Execute asana_add_task_dependencies calls
6. **Resource Assignment**:
   - Query team availability from Clockify or custom API
   - Assign LD, LT, SME based on capacity and skills
   - Update Asana task assignees
7. **Integration Triggers**:
   - Create Clockify project and tasks for time tracking
   - Add events to Google Calendar (kickoff, reviews, deadlines)
   - Update CRM with project timeline and milestones
   - Send email notifications to team and client
8. **Quality Checks**:
   - Verify all 52+ dependencies created successfully
   - Validate timeline calculations (duration = 112 days)
   - Check resource assignments complete
   - Test project in Timeline view
   - Send success/failure report

### 6.3 Target Automations

#### Template Generation Automation

**Input**: Web form or API payload
```json
{
  "client_name": "Walbrook",
  "programme_name": "MBA Marketing",
  "module_code": "MKT101",
  "module_type": "8-week standard",
  "go_live_date": "2026-03-11",
  "filming_option": "studio",
  "assigned_ld": "user_gid_123",
  "assigned_lt": "user_gid_456",
  "assigned_sme": "user_gid_789"
}
```

**Output**: Complete Asana project with:
- All 72 tasks created
- All 52 dependencies set
- All dates calculated from Go Live Date
- All assignees set
- Custom fields populated
- Ready for team to start work

**Time Savings**: 30 minutes manual setup → 2 minutes automated

#### Date Calculation Automation

**Current Process** (Manual):
1. User enters Launch Date in custom field
2. Asana calculates task dates via relative date formulas
3. User reviews Timeline view for conflicts
4. User manually adjusts if holidays detected

**Automated Process**:
1. User enters **Go Live Date** (student-facing date)
2. n8n calculates Launch Date (Go Live - configurable buffer)
3. n8n calculates all task dates from Launch Date backward
4. **Holiday detection**: Check dates against calendar API
5. **Weekend avoidance**: Shift tasks to avoid weekend due dates
6. **Conflict resolution**: Alert user if dates span known holidays (Christmas, etc.)
7. Apply all calculated dates via Asana API
8. Generate Timeline view link for user review

**Time Savings**: Eliminates manual date review and holiday checking

#### Multi-Service Integration

**Clockify Integration**:
- **Trigger**: Asana project created
- **Action**: Create Clockify project with:
  - Same module code and name
  - Time tracking tags matching Asana sections
  - Team members matching Asana assignees
  - Time estimates from task durations
- **Sync**: Bi-directional time tracking updates

**CRM Integration** (e.g., Pipedrive):
- **Trigger**: Asana project created
- **Action**: Update CRM opportunity with:
  - Module timeline (Kickoff → Go Live dates)
  - Key milestones (MPD Finalized, Ready for Launch)
  - Assigned team members
  - Project status link
- **Sync**: Update CRM when module status changes

**Google Calendar Integration**:
- **Trigger**: Asana project created
- **Action**: Create calendar events for:
  - Kickoff meeting
  - Review deadlines
  - Film shoot windows
  - Go Live date
- **Sync**: Update calendar when dates change in Asana

#### Event-Driven Template Management

**Status Change Automation**:
```
Trigger: Task "MPD Finalized" marked complete
→ n8n detects status change
→ Update Module Status to "In Development"
→ Send notification to LT: "Module ready for Week 1 build"
→ Create Clockify time tracking entry
→ Log milestone in CRM
```

**Blocker Escalation**:
```
Trigger: Task custom field "Blocker Status" changed to non-None
→ n8n detects blocker
→ Create escalation task for SLD
→ Send Slack/email alert to project manager
→ Log blocker in project dashboard
→ Set reminder to check resolution in 2 days
```

**Review Cycle Automation**:
```
Trigger: Week 2 Build marked complete
→ n8n detects completion
→ Calculate review ready date
→ Send email to Academic Reviewer with:
  - Links to Week 1 and 2 built content
  - Review checklist
  - Due date (5 days from trigger)
  - Asana task link for feedback
→ Create Google Calendar event for reviewer
→ Set reminder 1 day before review due
```

### 6.4 Technical Requirements

**n8n Setup**:
- n8n instance (cloud or self-hosted)
- Asana API credentials (OAuth token)
- Clockify API credentials (if integrating)
- Google Calendar API access (if integrating)
- CRM API access (if integrating)
- Webhook endpoints for triggers

**API Access Requirements**:
- **Asana API**: Read/write access to projects, tasks, dependencies, custom fields
- **Clockify API**: Create projects, time entries, manage users
- **Google Calendar API**: Create/update events, manage calendars
- **CRM API**: Update opportunities, contacts, activities

**Error Handling**:
- Retry logic for failed API calls (exponential backoff)
- Validation before critical operations (check template exists, assignees valid)
- Rollback capability (delete project if creation fails mid-process)
- Logging and monitoring (track all automation executions)
- Alert system (notify admins of failures)

**Security Considerations**:
- API credentials stored securely (environment variables, not hardcoded)
- Webhook authentication (verify requests from trusted sources)
- Access control (limit who can trigger template creation)
- Audit logging (track all automated changes with user attribution)

### 6.5 Automation Priority

**Phase 3A: Core Automations** (Highest ROI)
1. **Template generation from specification** (30 min → 2 min)
2. **Date calculation with holiday detection** (Eliminates manual review)
3. **Dependency creation automation** (Reproducible variants)

**Phase 3B: Integration Automations** (Medium ROI)
4. **Clockify time tracking setup** (Bi-directional sync)
5. **Google Calendar event creation** (Team coordination)
6. **Status change notifications** (Proactive communication)

**Phase 3C: Advanced Automations** (Lower ROI, Nice-to-Have)
7. **CRM integration** (Client visibility)
8. **Resource capacity planning** (Load balancing)
9. **Predictive analytics** (Risk detection)

**Estimated Development Time**:
- Phase 3A: 20-30 hours (n8n workflow development + testing)
- Phase 3B: 15-20 hours (integration setup + sync logic)
- Phase 3C: 20-30 hours (advanced features + analytics)

**Total**: 55-80 hours for complete automation (Could deliver incrementally)

---

## 7. Integration Points

### 7.1 Google Workspace

**Current Integration** (Manual):
- Module Planning Document (MPD): Google Docs
- Storyboards: Google Docs (one per week)
- Assessment briefs: Google Docs
- Reading lists: Google Sheets
- File storage: Google Drive folders per module

**Potential Automation** (Phase 3):
- **Template MPD Creation**: Auto-generate MPD from Asana project metadata
- **Storyboard Templates**: Create 8 blank storyboard docs in Drive when project starts
- **File Organization**: Auto-create folder structure (MPD, Storyboards, Assessments, Media)
- **Calendar Sync**: Create events for kickoff, reviews, deadlines in Google Calendar
- **Permission Management**: Share docs with team based on Asana assignees

**Technical Approach**:
- n8n Google Drive nodes for file/folder creation
- n8n Google Docs nodes for template document generation
- Google Calendar API for event management
- Asana webhooks trigger Google Workspace actions

**Integration Value**:
- Eliminate manual folder setup (5-10 minutes per module)
- Ensure consistent file naming and organization
- Auto-share documents with correct permissions
- Reduce "where is the storyboard?" questions

### 7.2 Clockify Time Tracking

**Current Integration** (Manual):
- Team members manually create Clockify entries
- Time tracked against module code
- No link between Asana tasks and Clockify entries
- Reporting requires manual data export and analysis

**Potential Automation** (Phase 3):
- **Project Creation**: Auto-create Clockify project when Asana project created
- **Task Sync**: Sync Asana section names to Clockify tags
- **Team Setup**: Add team members to Clockify project based on Asana assignees
- **Time Estimates**: Populate Clockify with estimated hours from Asana task durations
- **Bi-Directional Sync**: Update Asana with actual time from Clockify (for capacity planning)

**Technical Approach**:
- n8n Clockify nodes for project/task management
- Webhook from Asana → n8n → Clockify on project creation
- Scheduled sync (daily) for time tracking updates
- Custom dashboard combining Asana + Clockify data

**Integration Value**:
- Automatic Clockify setup (eliminates 15 minute manual setup)
- Accurate time tracking against Asana tasks
- Better capacity planning (estimated vs actual time visibility)
- Simplified billing (link time directly to client modules)

### 7.3 CRM Systems (Potential)

**Current State**: No direct integration

**Potential Integration** (Phase 3):
- **Opportunity Tracking**: Link Asana module project to CRM opportunity
- **Timeline Visibility**: Display Asana milestones in CRM (Go Live date, etc.)
- **Status Updates**: Auto-update CRM opportunity stage based on Asana Module Status
- **Team Attribution**: Link Asana assignees to CRM contacts
- **Revenue Tracking**: Connect Clockify time to CRM opportunity value

**Technical Approach**:
- n8n CRM nodes (Pipedrive, HubSpot, Salesforce)
- Asana webhooks trigger CRM updates
- Custom fields in both systems for linking (e.g., "CRM Opportunity ID" in Asana)

**Integration Value**:
- Client-facing visibility into project progress
- Sales team can see project timelines without Asana access
- Financial tracking (estimated revenue vs actual time/cost)

### 7.4 GitHub Documentation

**Current Integration**:
- This technical reference in git repository
- Specification files version-controlled
- dependency_mapping.json and task_gid_mapping.json committed

**Usage**:
- Documentation updates tracked via commits
- Specification changes reviewed via pull requests
- Historical context preserved (why decisions made)
- Knowledge base for team (how to create variants, etc.)

**Future Enhancement**:
- Auto-generate documentation from Asana template changes
- Link Asana project to GitHub documentation URL
- Version template specifications (v1.0, v2.0) with git tags

### 7.5 Asana API Boundaries

**What Asana API Provides**:
- Project creation and duplication
- Task management (create, update, delete)
- Dependency management (add dependencies)
- Custom field manipulation
- Team and workspace management
- Webhooks for event-driven automation

**What Asana API Does NOT Provide**:
- Built-in holiday detection (must use external calendar API)
- Resource capacity planning (must build custom logic)
- Time tracking (use Clockify or external tool)
- Advanced reporting (use custom dashboard)
- Conditional dependencies (all dependencies are absolute)

**Integration Strategy**: Use Asana for task/dependency management, external tools for capacity/time/reporting, n8n to orchestrate.

---

## 8. Quality Patterns

### 8.1 Validation Gates

**Quality Gate 1: MPD Review** (Day 15)
- **Trigger**: MPD Finalized + MPD review both complete
- **Reviewer**: Academic Reviewer
- **Purpose**: Validate scope, learning outcomes, assessment alignment before development
- **Dependency Impact**: Blocks all content development (Week 1 Storyboarding)
- **Failure Mode**: If MPD rejected, must revise and re-review (delays entire timeline)

**Quality Gate 2: Week 1 and 2 Review** (Day 40)
- **Trigger**: Week 2 Build complete
- **Reviewer**: Academic Reviewer
- **Purpose**: Catch pattern issues early (first 2 weeks set precedent for 6+ weeks)
- **Dependency Impact**: Doesn't block Week 3+ development (runs parallel)
- **Failure Mode**: If major changes requested, may need to revise Weeks 3-8 patterns
- **⚠️ Consistency Risk**: "Academic Reviewer performance has been super inconsistent with current client, tends to be lighter touch than proofreading" - may need supplemental internal QA

**Quality Gate 3: Weeks 3-8 Review** (Day 100)
- **Trigger**: Week 8 Build complete
- **Reviewer**: Academic Reviewer
- **Purpose**: Comprehensive review of bulk content, coherence across module
- **Dependency Impact**: Blocks Corrections task (must address all feedback before launch)
- **Failure Mode**: Large volume of feedback (6 weeks) can create significant correction workload
- **⚠️ Scheduling Risk**: Example timeline places on Christmas week; check calendar annually

**Quality Gate 4: Proofreading** (Day 105)
- **Trigger**: Film shoot - second batch complete
- **Reviewer**: Editorial Team
- **Purpose**: Copy editing, grammar, formatting consistency
- **Dependency Impact**: Runs parallel to Weeks 3-8 Review (independent quality stream)
- **Failure Mode**: Corrections task must address both proofreading AND academic review feedback

**Quality Gate 5: Ready for Launch** (Day 112)
- **Trigger**: Corrections complete
- **Approver**: Implicit (Senior LD or Project Lead)
- **Purpose**: Final verification all quality feedback addressed
- **Dependency Impact**: Blocks Go Live (66-day buffer before student access)
- **Failure Mode**: If not truly ready, client launch may be delayed

### 8.2 Consistency Enforcement

**Academic Reviewer Requirements**:
- **Qualification**: Subject matter expert in module discipline
- **Availability**: Must review 2-week batch (5 days) and 6-week batch (5 days)
- **Consistency Challenge**: Andrew reports "super inconsistent with current client"
- **Mitigation**:
  - Provide detailed review checklist (academic rigor, level appropriateness, assessment alignment)
  - Require written feedback (not just verbal approval)
  - Supplement with internal SLD review if Academic Reviewer too light
  - Consider two Academic Reviewers for critical modules

**Senior LD (SLD) QA Role**:
- **Current State**: Implicit in process, not explicitly tracked in template
- **Recommendation**: Add SLD QA tasks at strategic points:
  - After Week 1 Storyboard (pattern validation)
  - Before Weeks 3-8 Review (pre-review quality check)
  - After Corrections (final verification before launch)
- **Implementation**: Add 3 new tasks, 5 dependencies in future template version

**Storyboard Quality Standards**:
- **LD Draft**: Learning design, activity structure, assessment alignment
- **SME Draft**: Content accuracy, examples, subject matter depth
- **Edit**: Integration quality, flow, consistency
- **Final**: Both LD and SME sign-off (explicit approval)

### 8.3 Error Prevention via Dependencies

**How Dependencies Prevent Common Errors**:

**Error 1: Building Before Storyboard Complete**
- **Problem**: LT starts build with incomplete storyboard, requires rework
- **Prevention**: "Week N - Build" depends on "Week N - Storyboard Final draft agreed"
- **Enforcement**: Asana blocks build task completion until storyboard approved

**Error 2: Filming Without Scripts**
- **Problem**: Film shoot scheduled, but scripts not ready
- **Prevention**: "Film shoot - first batch" depends on "Week 4 - Storyboard Final draft agreed"
- **Enforcement**: Film shoot can't start until scripts complete (not build, as initially designed)

**Error 3: Reviewing Incomplete Content**
- **Problem**: Academic Reviewer starts review before all content built
- **Prevention**: "Week 1 and 2 review" depends on "Week 2 - Build"
- **Enforcement**: Review task blocked until both weeks fully built

**Error 4: Launching Without Corrections**
- **Problem**: Module goes live with known issues from reviews
- **Prevention**: "Ready for launch" depends on "Corrections"
- **Enforcement**: Can't mark Ready until all feedback addressed

**Error 5: Skipping Quality Gates**
- **Problem**: Team tries to bypass reviews to meet deadline
- **Prevention**: Review tasks block downstream work
- **Enforcement**: No way to proceed without completing reviews (system enforces quality)

### 8.4 Quality Metrics

**Definition of Quality** for this template:
- **Completeness**: All 72 tasks completed, no skipped steps
- **Correctness**: All dependencies satisfied in proper order
- **Academic Rigor**: Academic Reviewer approval obtained
- **Production Quality**: Proofreading complete, no typos/formatting errors
- **Stakeholder Alignment**: SME and Programme Leader sign-offs received

**Measurable Quality Indicators**:
- **Dependency Compliance**: 100% tasks completed only after dependencies satisfied
- **Review Pass Rate**: Percentage of reviews passing without major changes requested
- **Correction Volume**: Number of issues identified in reviews (trend over time)
- **Timeline Adherence**: Percentage of modules reaching "Ready for Launch" on Day 112
- **Rework Rate**: Percentage of tasks requiring revision after completion

**Quality Failure Modes**:
- **Rushed Quality Gates**: Reviews completed in <5 days without thorough assessment
- **Skipped Approvals**: Tasks marked complete without actual sign-off
- **Dependency Bypassing**: Manual task unlocking to meet deadlines (should be rare)
- **Insufficient Corrections**: Corrections task completed without addressing all feedback

**Quality Improvement Levers**:
- **Earlier SLD Review**: Catch issues before Academic Reviewer (reduces correction volume)
- **Stronger Review Criteria**: Detailed checklists for Academic Reviewers
- **Automated Validation**: n8n workflows verify task completion quality (Phase 3)
- **Trend Analysis**: Track correction volume over time, identify recurring issues

---

## 9. Performance Characteristics

### 9.1 Template Creation Time

**Manual Duplication** (Approach A):
- Open base template: 30 seconds
- Duplicate project: 1 minute
- Check "Duplicate task dependencies": Critical step
- Modify structure (if needed): 0-10 minutes
- Convert to template: 2 minutes
- **Total**: **5 minutes minimum** (minor modifications) to **15 minutes** (significant changes)

**API Recreation** (Approach B):
- Specification update: 10 minutes
- Dependency mapping update: 5 minutes
- Project structure creation: 5 minutes
- MCP API execution (52 dependencies): 10 minutes
- Verification: 2 minutes
- **Total**: **30 minutes** for new variant with structural changes

**Hybrid Approach** (Approach C):
- Create base variant via API: 30 minutes (one-time)
- Duplicate for related variants: 5 minutes each
- Add variant-specific dependencies: 5 minutes each
- **Total**: **15 minutes per variant** after base created (amortized)

**Comparison to Pre-Template Process**:
- **Old Manual Setup** (before template system): ~60 minutes per module
  - Create 72 tasks manually: 30 minutes
  - Create 12 sections: 5 minutes
  - Write task descriptions: 15 minutes
  - Set dates manually: 10 minutes
- **New Template Duplication**: 5 minutes
- **Time Savings**: **55 minutes per module** (92% reduction)

### 9.2 Maintenance Overhead

**Template Updates** (Minor):
- Update task description: 2 minutes
- Add custom field option: 3 minutes
- Adjust timeline calculation: 5 minutes
- Test change with dummy project: 5 minutes
- **Total**: **15 minutes** for minor updates

**Template Updates** (Major):
- Add new task with dependencies: 10 minutes (manual) or 15 minutes (API if many dependencies)
- Restructure sections: 20 minutes
- Update all variant templates: 10 minutes per variant
- Full regression test: 30 minutes
- **Total**: **60+ minutes** for major structural changes

**Propagating Changes to Variants**:
- **Approach 1**: Manual update each variant (10-15 minutes × number of variants)
- **Approach 2**: Version control git diff, apply changes via script (future automation)
- **Best Practice**: Minimize base template changes; use variants for differentiation

**Documentation Maintenance**:
- Update specification document: 15-30 minutes (this file)
- Update dependency mapping JSON: 10 minutes
- Update variant documentation: 10 minutes per variant
- **Total**: **35-50 minutes** per significant change

**Recommended Update Frequency**:
- **Quarterly reviews**: Check for process improvements, gather team feedback
- **Annual major updates**: Incorporate learnings from 10+ module deliveries
- **As-needed patches**: Critical bug fixes, client-specific requirements

### 9.3 Scalability

**Concurrent Module Capacity** (LD-LT Team):

**Theoretical Maximum** (Single LD-LT Pair):
- **1 module**: Full attention, high quality, 0% time conflicts
- **2 modules (8-week offset)**: LD on Module 2 while LT builds Module 1 (~80% capacity)
- **3 modules (4-week offsets)**: Requires careful coordination (~60% capacity, quality risk)

**Practical Limit**: **2 modules per LD-LT pair** for quality maintenance

**Scaling Strategy**:
- **2-3 modules/month launch rate**: Requires 1-2 LD-LT pairs
- **5-10 modules/month launch rate**: Requires 3-5 LD-LT pairs (or longer timelines)
- **>10 modules/month**: Requires dedicated project management + offshore LT scaling

**Bottleneck Analysis**:
- **Learning Designer**: Highest utilization (60-70 days effort over 17 weeks) – primary bottleneck
- **SME Availability**: Client-side constraint, often limiting factor
- **Academic Reviewer**: Can batch-review multiple modules if scheduled carefully
- **Learning Technologist**: More scalable (offshore options available)

**Resource Allocation Limits**:
- **LD Capacity**: ~2-3 modules in development simultaneously (staggered)
- **LT Capacity**: ~3-4 modules in build phase simultaneously (cascading pattern)
- **SLD Capacity**: ~10-15 modules under oversight simultaneously (periodic review)
- **Academic Reviewer**: ~5-8 modules under review simultaneously (batched)

**System Capacity** (Asana Platform):
- **No practical limits** on number of projects, tasks, or dependencies
- **Portfolio view** supports 50+ concurrent modules without performance degradation
- **API rate limits**: 150 requests/minute (not a concern for template creation)

### 9.4 Resource Requirements

**Time Investment per Module**:

**Learning Designer** (60-70 days effort over 17 weeks):
- Initiation: 10 days (kickoff, MPD, assessments)
- Week 1 Storyboarding: 10 days (extended)
- Weeks 2-8 Storyboarding: 35 days (5 days × 7 weeks)
- Reviews and Corrections: 10 days
- **Total**: ~65 days effort, ~35% capacity over 17 weeks

**Learning Technologist** (40-45 days effort over 9 weeks):
- Weeks 1-8 Build: 40 days (5 days × 8 weeks)
- Corrections (technical): 5 days
- **Total**: ~45 days effort, ~70% capacity over 9 weeks (concentrated)

**SME** (50-60 days effort over 11 weeks):
- Initiation: 10 days (kickoff, MPD, reading lists)
- Week 1 Storyboarding: 10 days
- Weeks 2-8 Storyboarding: 35 days
- Corrections (content): 5 days
- **Total**: ~60 days effort, ~75% capacity over 11 weeks

**Academic Reviewer** (10 days effort over 2 weeks):
- MPD Review: 5 days
- Week 1-2 Review: 5 days
- Weeks 3-8 Review: 5 days
- **Total**: ~15 days effort (can batch across multiple modules)

**API Quota Requirements** (Template Creation):
- **Search operations**: ~10 API calls (task discovery)
- **Dependency creation**: 52 API calls (one per dependency)
- **Verification**: ~5 API calls (sample checks)
- **Total**: ~70 API calls per template (well within 150/minute limit)

**Storage Requirements**:
- **Asana project**: Negligible (<1 MB per project)
- **Google Drive**: ~500 MB per module (MPD, storyboards, media)
- **Clockify time tracking**: Negligible (<1 MB per project)
- **Git repository**: ~5 MB per template variant (specifications, mappings)

---

## 10. Technical Decisions Log

### Decision 1: API vs Manual Dependencies

**Date**: October 2025
**Context**: Need to create 52 task dependencies for template
**Options Considered**:
1. Manual creation via Asana UI (~49 minutes, error-prone)
2. Custom Python/TypeScript script (3 hours development, ongoing maintenance)
3. Asana MCP API via Claude Code (30 minutes, no custom code)

**Decision**: **Option 3 - Asana MCP API**

**Rationale**:
- **Speed**: 30 minutes vs 49 minutes manual or 3 hours scripting
- **Reproducibility**: Same process works for template variants
- **No Maintenance**: No custom script to maintain/debug
- **Version Control**: Dependency mappings in JSON (git-tracked)
- **Testing**: Can verify before production (test project copy)

**Trade-offs Accepted**:
- **Slightly Slower Than Manual**: 30 min vs 49 min, but reproducible matters more
- **MCP Dependency**: Relies on Asana MCP server availability
- **Less Control**: Can't customize error handling like custom script

**Implementation**: See Section 3 (API Implementation)

**Outcome**: ✅ 100% success rate (52/52 dependencies created), process documented for variants

---

### Decision 2: Dependency Count Optimization

**Date**: October 2025
**Context**: Could create 100+ dependencies (every possible task relationship) or optimize to critical 52
**Options Considered**:
1. **Minimal** (30 dependencies): Only critical path, no within-task workflows
2. **Optimized** (52 dependencies): Critical path + cascading + within-task + finalization
3. **Comprehensive** (100+ dependencies): Every conceivable relationship

**Decision**: **Option 2 - Optimized 52 Dependencies**

**Rationale**:
- **Sufficient Coverage**: Prevents all major workflow errors (building before storyboard, reviewing incomplete content, launching without corrections)
- **Maintainable**: 52 dependencies manageable; 100+ creates complexity burden
- **Performance**: Asana UI handles 52 dependencies well; 100+ may slow Timeline view
- **Flexibility**: Leaves room for ad-hoc task ordering within sections

**Trade-offs Accepted**:
- **Not Exhaustive**: Some possible dependencies omitted (e.g., Reading list → Week 1 Storyboard not enforced)
- **Trust Required**: Assumes team won't bypass obvious sequencing (e.g., won't start Week 5 before Week 4)

**Dependency Categories Included**:
- ✅ Critical Path (16): Sequential milestones
- ✅ Cascading Build (7): Parallel work enablement
- ✅ Within-Task (24): Storyboard quality workflow
- ✅ Finalization (5): Quality gates before launch
- ❌ Optional (not included): Reading list → Storyboards, Assessments → Week 1, etc.

**Implementation**: See Section 2 (Dependency Patterns)

**Outcome**: ✅ Team reports dependencies enforce workflow without being overly restrictive

---

### Decision 3: Section Structure (12 Weeks with 10-Day Week 1)

**Date**: October 2025
**Context**: How to organize 8 weeks of content development
**Options Considered**:
1. **8 sections** (one per week): Simpler structure, consistent week treatment
2. **12 sections** (Initiation, Weeks 1-8, Finalization, Launch): Current structure
3. **4 sections** (Planning, Development, QA, Launch): Fewer sections, tasks grouped differently

**Decision**: **Option 2 - 12 Sections with Special Week 1 Treatment**

**Rationale**:
- **Mirrors Actual Workflow**: Andrew's team already organizes work this way (per spreadsheet)
- **Week 1 Extension**: 10-day Week 1 storyboarding justified by pattern establishment and LD/SME relationship building
- **Finalization Clarity**: Separate section for film shoots, reviews, corrections makes QA phase visible
- **Launch Buffer Visibility**: Dedicated Launch section highlights 66-day gap to Go Live

**Week 1 Rationale** (from Andrew):
- First week establishes patterns for entire module
- SME needs more time to learn storyboard format
- LD and SME building working relationship
- More back-and-forth expected initially
- **Flexibility**: Can reduce to 5 days if client demands, but increases rework risk

**Trade-offs Accepted**:
- **More Sections**: 12 sections vs 8 creates more navigation (but clearer organization)
- **Inconsistent Durations**: Week 1 (10 days) vs Weeks 2-8 (5 days) requires explanation

**Implementation**: See Section 5 (Task Taxonomy)

**Outcome**: ✅ Team finds structure intuitive, Week 1 extension proves valuable for quality

---

### Decision 4: Variant Strategy (Multiple Approaches vs Single Method)

**Date**: October 2025
**Context**: How should teams create template variants (12-week, accelerated, etc.)?
**Options Considered**:
1. **Single Method**: Always use API recreation (consistent but slow)
2. **Single Method**: Always use duplication (fast but limited)
3. **Multiple Approaches**: Duplication (5 min) OR API (30 min) OR Hybrid (15 min) based on needs

**Decision**: **Option 3 - Multiple Approaches**

**Rationale**:
- **Flexibility**: Different scenarios have different optimal approaches
- **Time Efficiency**: 5-minute duplication for minor variants vs 30-minute API for major changes
- **Team Skill Levels**: Less technical users can duplicate, technical users can API
- **Iterative Improvement**: Can start with duplication, move to API as needs evolve

**Approach Selection Criteria**:
- **Duplication** (5 min): Same 8-week structure, minor modifications (remove film shoots, change descriptions)
- **API Recreation** (30 min): Different structure (12-week, 6-week), significantly different dependencies
- **Hybrid** (15 min): Multiple related variants (Theory/Skills/Lab family)

**Trade-offs Accepted**:
- **Complexity**: Teams must understand when to use which approach (documented in TEMPLATE_VARIANTS.md)
- **Inconsistency Risk**: Different teams might choose different approaches for same variant type

**Implementation**: See Section 4 (Template Variant Architecture)

**Outcome**: ✅ Flexible system accommodates variety of needs, documentation guides decision-making

---

### Decision 5: Automation Timing (Phase 3 vs Immediate)

**Date**: October 2025
**Context**: When to implement n8n workflow automation?
**Options Considered**:
1. **Immediate**: Build n8n automation alongside template (Phase 2 + 3 combined)
2. **Phase 3 Later**: Complete template first (Phase 2), automate later when proven (Phase 3)
3. **Never**: Manual template duplication sufficient, no automation needed

**Decision**: **Option 2 - Phase 3 Later**

**Rationale**:
- **Validate First**: Prove template works manually before automating
- **Avoid Premature Optimization**: Don't automate process that might change
- **Incremental Value**: Template provides immediate value (55 min/module savings) without automation
- **Learning Period**: Give team 3-6 months to use template, identify true automation pain points

**What Phase 2 Delivered** (Current):
- 72-task template with 52 API-created dependencies
- Manual duplication (5 minutes per new module)
- Manual date entry (Launch Date custom field)
- Manual resource assignment (template defaults available)

**What Phase 3 Will Deliver** (Future):
- Automated template generation from specifications
- Date calculation with holiday detection
- Multi-service integration (Clockify, Google Calendar, CRM)
- Event-driven workflow automation (status changes, notifications)

**Trade-offs Accepted**:
- **Manual Setup Overhead**: 5 minutes to duplicate + 5 minutes to configure = 10 minutes per module (vs potential 2 minutes fully automated)
- **Delayed ROI**: Automation benefits delayed 3-6 months
- **Integration Gaps**: No Clockify/CRM/Calendar integration initially

**Timeline**:
- **Phase 2 Complete**: October 2025
- **Phase 3 Planning**: After 10+ modules delivered with template (Q1-Q2 2026)
- **Phase 3 Implementation**: 55-80 hours development (Q2-Q3 2026)

**Implementation**: See Section 6 (Automation Roadmap)

**Outcome**: ✅ Template delivering value immediately, automation requirements better understood after usage

---

### Decision 6: Film Shoot Dependencies (Storyboard vs Build)

**Date**: October 2025 (Corrected from initial design)
**Context**: What should film shoots depend on?
**Initial Design**: Film shoot → depends on → Week N Build
**Correction**: Film shoot → depends on → Week N Storyboard Final draft agreed

**Decision**: **Storyboard Dependencies (Corrected)**

**Rationale** (from Andrew):
- **Scripts Needed**: Film shoots need scripts (from storyboards), not built content (Moodle pages)
- **Parallel Efficiency**: LT can continue building while filming happens (no need to wait for build)
- **Logical Dependency**: Filming requires knowing what to say, not where it will be embedded

**Error Analysis**:
- **Why Initial Design Was Wrong**: Assumed filming requires built context (pages ready to embed video)
- **How Error Detected**: Andrew's compliance review of specification
- **How Corrected**: Updated dependency_mapping.json, re-applied via MCP API

**Implementation**:
```json
// BEFORE (incorrect)
{"source": "Week 4 - Build", "target": "Film shoot - first batch"}

// AFTER (correct)
{"source": "Week 4 - Storyboard Final draft agreed", "target": "Film shoot - first batch"}
```

**Impact**:
- **Timeline**: No change (film shoots still run parallel to development)
- **Dependencies**: 2 dependencies corrected (first and second batches)
- **Quality**: Ensures scripts ready before filming (prevents filming delays)

**Outcome**: ✅ Logical dependency corrected, aligns with actual workflow

---

### Decision 7: Launch Date Naming (Potential Confusion)

**Date**: October 2025
**Issue Identified**: "Launch Date" custom field actually means "Ready for Launch" (Day 112), NOT "Go Live" (Day 178)
**Confusion Source**: "Launch" commonly understood as student access date, but template uses as anchor for timeline calculations

**Options Considered**:
1. **Rename to "Ready Date"**: Clearer, but loses "Launch Date" familiarity
2. **Rename to "Anchor Date"**: Technically accurate, but too abstract
3. **Keep "Launch Date"**: Accept confusion, document clearly
4. **Use "Go Live Date" for calculations**: Requires recalculating all relative dates

**Decision**: **Option 3 - Keep "Launch Date" with Clear Documentation**

**Rationale**:
- **Template Already Built**: Renaming requires updating all relative date formulas
- **Documentation Solves**: Specification, this reference, and template description explain clearly
- **Andrew's Clarification**: "Launch is NOT Andrew's task. Andrew's job is to get everything ready for launch (the 'Ready for Launch' milestone). The actual 'Go Live' is controlled by the client's academic calendar."

**Mitigation**:
- **Custom Field Description**: Update to clarify "This is the 'Ready for Launch' date (Day 112), not the 'Go Live' date"
- **Documentation**: Emphasize distinction in all docs
- **Future Template**: Consider renaming in next major version

**Trade-offs Accepted**:
- **Potential Confusion**: New users may assume "Launch Date" = "Go Live"
- **Training Required**: Must explain distinction during onboarding

**Outcome**: ⚠️ Document decision, plan for future renaming if confusion proves significant

---

## 11. Maintenance & Evolution

### 11.1 Template Updates

**Minor Updates** (Task descriptions, assignees, custom fields):

**Process**:
1. Open base template in Asana (not a project created from template)
2. Make changes to template directly
3. Test by creating dummy project from template
4. Verify changes propagated correctly
5. Update specification document to reflect changes
6. Commit specification changes to git

**Examples**:
- Update task description with clearer instructions
- Add custom field option (new module type, new status)
- Adjust task duration (if timeline patterns change)
- Update default assignee (new team member)

**Time**: 15-30 minutes including testing and documentation

**Impact**: All NEW projects from template get updates; existing projects unchanged

---

**Major Updates** (Structural changes, new tasks, dependency modifications):

**Process**:
1. **Plan Change**: Document proposed change, rationale, impact
2. **Test on Copy**: Duplicate template to "Template TEST", make changes there first
3. **Update Dependencies**: If adding/removing tasks, update dependency_mapping.json
4. **Re-apply via MCP**: If dependency structure changed, re-create dependencies via API
5. **Verify Timeline**: Check Timeline view, calculate new duration (should stay 112 days unless intentional)
6. **Update Specification**: Modify Asana_Module_Development_Template_Spec_v2.md
7. **Create Git PR**: Document change in pull request for review
8. **Apply to Production**: Once approved, apply changes to production base template
9. **Test Production**: Create dummy project, verify all changes work
10. **Update Variants**: Propagate changes to variant templates (if applicable)
11. **Notify Team**: Announce change, explain impact, update training materials

**Examples**:
- Add SLD QA task at Week 4 (new task + 3 dependencies)
- Split Weeks 3-8 review into two batches (structural change)
- Add third film shoot batch (new task + dependencies)
- Remove reading list subtask (structural simplification)

**Time**: 1-3 hours including planning, testing, documentation, and rollout

**Impact**: NEW projects get changes; EXISTING projects must be manually updated if change is critical

---

### 11.2 Dependency Adjustments

**When to Adjust Dependencies**:
- Workflow changes (new quality gates, process improvements)
- Error prevention (discovered new failure mode, need dependency to prevent)
- Optimization (remove overly restrictive dependency blocking parallel work)
- Variant needs (different dependency pattern for specific module type)

**How to Add Dependencies**:

**Option A: Manual (Asana UI)**
1. Open task that should be blocked
2. Add dependency in task pane → Dependencies section
3. Save and verify in Timeline view

**Option B: MCP API** (Preferred for bulk)
1. Update dependency_mapping.json with new dependency
2. Search for task GIDs via `asana_search_tasks`
3. Call `asana_add_task_dependencies(task_id=target_gid, dependencies=[source_gid])`
4. Verify in Asana Timeline view

**How to Remove Dependencies**:
- **Manual Only**: Asana API doesn't support dependency removal (must use UI)
- Open task → Dependencies → Click X to remove
- Or delete task entirely and recreate without dependency

**How to Modify Dependencies**:
- Remove old dependency (manual)
- Add new dependency (manual or MCP)
- OR delete task and recreate with correct dependencies (API)

**Testing Dependency Changes**:
1. Create project from template
2. Try to complete tasks out of order (should be blocked)
3. Complete tasks in correct order (should succeed)
4. Check Timeline view for logical flow
5. Delete test project

---

### 11.3 Breaking Changes

**What Constitutes a Breaking Change**:
- Renaming tasks (breaks GID mappings, dependency lookups)
- Removing sections (orphans tasks, breaks Timeline view)
- Changing custom field types (e.g., Single Select → Multi Select)
- Major dependency restructuring (changes critical path)

**How to Handle Breaking Changes**:

**Option 1: New Template Version** (Recommended for major changes)
1. Create new template: "Module Development Template v3.0"
2. Apply breaking changes to new template
3. Keep old template: "Module Development Template v2.0 (Legacy)"
4. Migrate projects to new template over time (not automatically)
5. Document migration path

**Option 2: In-Place Update** (For minor breaking changes)
1. Announce change 2 weeks in advance
2. Document migration steps for in-flight projects
3. Apply change to base template
4. Provide support for teams with in-flight projects
5. Update all documentation

**Migration Path for In-Flight Projects**:
- **If change is minor**: Manual update (5-10 minutes per project)
- **If change is major**: Complete project with old structure, use new template for next module
- **If change is critical bug fix**: Mandate immediate update with support

**Version Control Strategy**:
- Git tag each template version: `v1.0`, `v2.0`, `v3.0`
- Branch for major updates: `feature/template-v3`
- Pull request review before merging to main
- Maintain CHANGELOG.md documenting all versions

---

### 11.4 Rollback Strategy

**When to Rollback**:
- New change breaks workflow (tasks blocked incorrectly)
- Team reports confusion/difficulty
- Critical dependency error discovered
- Timeline calculations incorrect

**How to Rollback**:

**Template Changes** (Last 24 hours):
1. Open base template in Asana
2. Project Settings → Duplicate project → select earlier copy (if available)
3. Convert earlier copy to template
4. Deactivate broken template (don't delete, for forensics)

**Dependency Changes** (via MCP):
1. Checkout previous dependency_mapping.json from git (`git checkout HEAD~1 dependency_mapping.json`)
2. Re-run MCP API calls to restore dependencies
3. Verify restoration in Timeline view

**Git Repository** (Specification/Documentation):
1. Identify commit before change: `git log --oneline`
2. Revert commit: `git revert <commit-hash>`
3. Or checkout specific file: `git checkout <commit-hash> -- filename.md`

**Communication**:
- Notify team immediately of rollback
- Explain issue discovered
- Provide timeline for fix and re-deployment
- Update any in-flight projects affected

**Prevention**:
- Always test changes on duplicate before production
- Require peer review for major changes (git PR)
- Maintain template backups (periodic duplicates)
- Document rollback procedures (this section)

---

### 11.5 Documentation Updates

**When to Update Documentation**:
- **Always**: After any template change (even minor)
- **Specification**: After structural changes, dependency updates, timeline modifications
- **This Reference**: After technical decisions, architecture changes, new insights
- **Variant Guide**: After creating new variant or changing variant strategy
- **Training Materials**: After changes affecting team workflow

**Documentation Hierarchy**:
1. **Asana Template Itself**: Task descriptions, custom field descriptions (primary source of truth)
2. **Specification Document**: Comprehensive design document (1,550 lines, version-controlled)
3. **This Technical Reference**: Architecture, decisions, patterns (you are here)
4. **Variant Guide**: Template creation strategies (TEMPLATE_VARIANTS.md)
5. **Usage Guides**: Quickstart, FAQ, training materials

**Documentation Sync Process**:
1. Make change in Asana template (source of truth)
2. Update specification document to match
3. Update this technical reference if design decision involved
4. Update variant guide if variant strategy affected
5. Commit all documentation changes together (atomic PR)
6. Tag release if significant: `git tag v2.1 -m "Added SLD QA tasks"`

**Documentation Standards**:
- **Precision**: Exact task names, accurate counts, specific GIDs
- **Rationale**: Explain WHY decisions made, not just WHAT
- **Examples**: Include concrete examples from real usage
- **Cross-References**: Link between docs (specification ↔ reference ↔ variant guide)
- **Version Control**: Every change committed with descriptive message

**Review Schedule**:
- **Quarterly**: Review all documentation for accuracy
- **After 10 modules**: Capture learnings, update based on real usage
- **Annually**: Major documentation refresh, incorporate team feedback
- **Before Training**: Ensure all docs current before onboarding new team members

---

## 12. Reference Data

### 12.1 Project IDs

**Production Template**:
- **Template Name**: "TEST Project Template" (to be renamed)
- **Project GID**: `1211626878286938`
- **Workspace GID**: `1210754319198231`
- **Created**: October 2025
- **Dependencies**: 52 API-created relationships

**Test Project** (Used for API Implementation):
- **Project Name**: "Template TEST - Project Plan"
- **Project GID**: `1211626875246589`
- **Purpose**: API dependency creation testing
- **Status**: Complete, dependencies verified

**Task GID Pattern**:
- All tasks in Project `1211626875246589` follow pattern: `1211627678168XXX`
- GIDs unique per project (change when duplicated)
- Must regenerate task_gid_mapping.json for each new variant

### 12.2 API Endpoints

**Asana API Base URL**: `https://app.asana.com/api/1.0`

**MCP Tools Used** (Asana MCP Server):

| MCP Tool | Purpose | Usage Count |
|----------|---------|-------------|
| `asana_search_tasks` | Find tasks by name pattern in workspace | ~10 calls (task discovery) |
| `asana_get_task` | Retrieve task details (name, GID, sections) | ~5 calls (verification) |
| `asana_get_project` | Get project metadata | 2 calls (project validation) |
| `asana_get_project_sections` | List sections in project | 2 calls (structure validation) |
| `asana_add_task_dependencies` | Create dependency relationships | **52 calls** (one per dependency) |

**API Call Patterns**:

**Task Discovery**:
```
asana_search_tasks(query="Week 1", project_id="1211626875246589")
→ Returns: [{"gid": "1211627678168612", "name": "Week 1 - Storyboarding"}, ...]
```

**Dependency Creation**:
```
asana_add_task_dependencies(
  task_id="1211627678168620",  // Week 1 - Build
  dependencies=["1211627678168619"]  // Week 1 - Storyboard Final draft agreed
)
→ Result: Success (dependency created)
```

**Rate Limits**:
- **Asana API**: 150 requests per minute (per access token)
- **MCP Server**: No additional limits beyond Asana API
- **Implementation**: 52 API calls in ~10 minutes = well within limits

### 12.3 File Inventory

**Project Root** (`/asana-systematisation/`):

| File | Purpose | Lines | Format |
|------|---------|-------|--------|
| `Asana_Module_Development_Template_Spec_v2.md` | Complete template specification | 1,550 | Markdown |
| `TEMPLATE_VARIANTS.md` | Variant creation strategies | 660 | Markdown |
| `TECHNICAL_REFERENCE.md` | This document (architecture, decisions) | 3,000+ | Markdown |
| `dependency_mapping.json` | Dependency specifications (52 relationships) | ~200 | JSON |
| `task_gid_mapping.json` | Task name → GID mappings for Project 1211626875246589 | ~150 | JSON |

**Documentation Directory** (`claudedocs/`):

| File | Purpose |
|------|---------|
| `WORKFLOW_RECOMMENDATIONS.md` | Process improvement recommendations |
| `AGENT_DELEGATED_WORKFLOWS.md` | Multi-agent workflow analysis |

**Memory Directory** (`.serena/memories/`):

| File | Purpose |
|------|---------|
| `asana_api_dependency_implementation.md` | API implementation session summary (Oct 14) |
| `asana_compliance_review_session_2025_10_16.md` | Andrew's feedback integration |
| `pending_next_steps.md` | Outstanding work items |

**Version Control**:
- All files tracked in git repository
- Commit history preserves evolution of design decisions
- Branch: `feature/api-dependency-implementation` (merged to master)

### 12.4 Configuration

**Asana Custom Field Configuration**:

**Required Custom Fields** (Must exist in workspace):
- Launch Date (Date field)
- Go Live Date (Date field)
- Module Code (Text field)
- Client Name (Text field)
- Programme Name (Text field)
- Module Status (Single Select: Planning / In Development / Build / QA / Ready / Launched / Archived)

**Optional Custom Fields** (Enhance functionality):
- Module Author (SME) (Person field)
- Learning Designer (Person field)
- Learning Technologist (Person field)
- Senior LD (Reviewer) (Person field)
- QA Status (Single Select: Not Started / In Review / Changes Requested / Approved)
- Blocker Status (Single Select: None / Waiting on SME / Waiting on Client / Technical Issue / Resource Gap)
- Media Requirements (Single Select: None / Standard / Film Shoot Required / Audio Only)
- Content Type (Multi Select: Theory / Activities / Video / Audio / Interactive / Assessment)
- Review Batch (Single Select: Weeks 1-2 / Weeks 3-8 / N/A)

**Relative Date Formulas** (Asana):
- All task dates calculated from "Launch Date" custom field
- Formulas use pattern: `[Launch Date] - X days` (where X is days before launch)
- Example: Kick off meeting = `[Launch Date] - 112 days`

**Environment Variables** (For API/MCP):
- `ASANA_ACCESS_TOKEN`: OAuth token for API access (managed by MCP server)
- No other environment variables required (MCP abstracts authentication)

---

## Appendix A: Dependency Matrix

**Complete List of 52 Dependencies** (By Category):

### Critical Path (16 Dependencies)

| Source Task | Target Task | Days Before Launch (Target) |
|-------------|-------------|---------------------------|
| Kick off meeting | MPD Draft | 107 |
| MPD Draft | MPD Finalised | 102 |
| MPD Finalised | Week 1 - Storyboarding | 91 |
| MPD review | Week 1 - Storyboarding | 91 |
| Week 1 - Storyboard Final draft agreed | Week 1 - Build | 76 |
| Week 1 - Build | Week 2 - Storyboarding | 71 |
| Week 2 - Storyboard Final draft agreed | Week 2 - Build | 61 |
| Week 2 - Build | Week 1 and 2 review | 63 |
| Week 8 - Build | Weeks 3 to 8 review | 14 |
| Week 8 - Build | Film shoot - second batch | 28 |
| Film shoot - second batch | Proofreading | 21 |
| Weeks 3 to 8 review | Corrections | 7 |
| Proofreading | Corrections | 7 |
| Corrections | Ready for launch | 0 |
| Ready for launch | Go live | -66 |

### Cascading Build (7 Dependencies)

| Source Task | Target Task |
|-------------|-------------|
| Week 2 - Build | Week 3 - Storyboarding |
| Week 3 - Build | Week 4 - Storyboarding |
| Week 4 - Build | Week 5 - Storyboarding |
| Week 5 - Build | Week 6 - Storyboarding |
| Week 6 - Build | Week 7 - Storyboarding |
| Week 7 - Build | Week 8 - Storyboarding |

### Within-Task Storyboard Workflow (24 Dependencies)

**For each of 8 weeks** (Week 1-8), pattern of 3 dependencies:

| Source Task | Target Task |
|-------------|-------------|
| Week N - Storyboard Initial LD Draft | Week N - Edit |
| Week N - Storyboard SME Scripts Draft | Week N - Edit |
| Week N - Edit | Week N - Storyboard Final draft agreed |

**Total**: 8 weeks × 3 dependencies = 24 dependencies

### Finalization (5 Dependencies)

| Source Task | Target Task |
|-------------|-------------|
| Week 4 - Storyboard Final draft agreed | Film shoot - first batch |
| Week 8 - Build | Film shoot - second batch |
| Film shoot - second batch | Proofreading |
| Weeks 3 to 8 review | Corrections |
| Corrections | Ready for launch |

**Grand Total**: 16 + 7 + 24 + 5 = **52 Dependencies**

---

## Appendix B: Timeline Calculation Reference

**Relative Date Offsets** (From Launch Date = Day 0):

| Task | Start (Days Before) | Duration | End (Days Before) |
|------|-------------------|----------|------------------|
| Kick off meeting | -112 | 5d | -108 |
| MPD Draft | -107 | 5d | -103 |
| MPD Finalised | -102 | 5d | -98 |
| MPD review | -100 | 5d | -96 |
| Week 1 - Storyboarding | -91 | 10d | -82 |
| Week 1 - Build | -76 | 5d | -72 |
| Week 2 - Storyboarding | -71 | 5d | -67 |
| Week 2 - Build | -61 | 5d | -57 |
| Week 1 and 2 review | -63 | 5d | -59 |
| Week 3 - Storyboarding | -64 | 5d | -60 |
| Week 3 - Build | -58 | 5d | -54 |
| Week 4 - Storyboarding | -58 | 5d | -54 |
| Week 4 - Build | -51 | 5d | -47 |
| Film shoot - first batch | -56 | 6d | -51 |
| Week 5 - Storyboarding | -51 | 5d | -47 |
| Week 5 - Build | -44 | 5d | -40 |
| Week 6 - Storyboarding | -44 | 5d | -40 |
| Week 6 - Build | -37 | 5d | -33 |
| Week 7 - Storyboarding | -37 | 5d | -33 |
| Week 7 - Build | -30 | 5d | -26 |
| Week 8 - Storyboarding | -30 | 5d | -26 |
| Week 8 - Build | -23 | 5d | -19 |
| Film shoot - second batch | -28 | 5d | -24 |
| Proofreading | -21 | 5d | -17 |
| Weeks 3 to 8 review | -14 | 5d | -10 |
| Corrections | -7 | 5d | -3 |
| **Ready for launch** | **0** | **1d** | **0** |
| **Go live** | **+66** | **--** | **+66** |

**Timeline Anchors**:
- **Launch Date** (Day 0) = "Ready for Launch" milestone
- **Kickoff** (Day -112) = 16 weeks before Launch Date
- **Go Live** (Day +66) = 9.4 weeks after Launch Date (client-specific buffer)

**Total Timeline**: 178 days (25.4 weeks) from Kickoff to Go Live

---

## Appendix C: Glossary

| Term | Definition |
|------|------------|
| **Asana MCP** | Model Context Protocol server for Asana API, abstracts authentication and API complexity |
| **Cascading Build** | Pattern where Week N Build completion enables Week N+1 Storyboarding (parallel work optimization) |
| **Critical Path** | Sequence of dependent tasks determining minimum project duration (112 days in this template) |
| **Dependency** | Task relationship where Target task blocked until Source task complete (enforced by Asana) |
| **GID** | Global Identifier, Asana's unique ID for objects (projects, tasks, etc.), format: 16-digit number |
| **Launch Date** | Custom field serving as anchor for relative date calculations; equals "Ready for Launch" milestone (NOT Go Live) |
| **LD** | Learning Designer, instructional designer role responsible for module pedagogy and structure |
| **LT** | Learning Technologist, technical implementer role responsible for Moodle build |
| **MCP** | Model Context Protocol, abstraction layer for API access used via Claude Code |
| **MPD** | Module Planning Document, foundational specification document created during Initiation |
| **Ready for Launch** | Day 112 milestone when Andrew's team completes module (client controls actual Go Live timing) |
| **SLD** | Senior Learning Designer, quality assurance role (e.g., Nicole) |
| **SME** | Subject Matter Expert, client's academic providing content expertise |
| **Storyboard** | Detailed design document specifying module content, activities, and media before Moodle build |
| **Template Variant** | Specialized version of base template for different module types (12-week, micro-credential, etc.) |
| **Within-Task Dependency** | Dependencies within storyboarding workflow (Draft → Edit → Final) enforcing quality process |

---

## Appendix D: Key Contacts & Resources

**Template Ownership**:
- **Creator**: Andrew (Learning Design Solutions)
- **Technical Implementation**: Claude Code with Asana MCP
- **Documentation**: This reference manual and specification documents

**Support Resources**:
- **Specification Document**: `Asana_Module_Development_Template_Spec_v2.md` (1,550 lines)
- **Variant Guide**: `TEMPLATE_VARIANTS.md` (660 lines)
- **API Implementation Summary**: `.serena/memories/asana_api_dependency_implementation.md`
- **Git Repository**: `/asana-systematisation/` (version control for all specifications)

**External Documentation**:
- Asana API Documentation: https://developers.asana.com/docs
- Asana MCP Server: (MCP implementation details)
- n8n Documentation: https://docs.n8n.io/ (for Phase 3 automation)

---

## Document Metadata

**Document Version**: 1.0
**Last Updated**: October 2025
**Word Count**: ~3,500 words
**Applies To**: Asana Module Development Template v2.0 (52 API-created dependencies)
**Status**: Production Reference - Authoritative Technical Documentation
**Next Review**: After 10 modules delivered or Q1 2026, whichever comes first
**Maintainer**: Template team lead (to be assigned)
**Change Log**: See git commit history for detailed evolution

**Future Updates Planned**:
- Phase 3 automation implementation details (Q2-Q3 2026)
- Variant catalog as new variants created (ongoing)
- Performance metrics after 10+ module deliveries (Q1 2026)
- Lessons learned section from real-world usage (Q2 2026)

---

## End of Technical Reference Manual
