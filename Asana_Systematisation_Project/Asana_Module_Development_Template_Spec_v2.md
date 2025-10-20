# Asana Module Development Template Specification v2.0

**Document Version**: 2.0 (Revised based on actual spreadsheet template)
**Last Updated**: 2025-10-13
**Purpose**: Definitive technical specification for implementing the Asana Module Development Template based on actual TEMPLATE_Project_Plan_20250708.xlsx structure
**Supersedes**: Asana_Module_Development_Template_Spec.md (v1.0)

---

## Executive Summary

This specification defines the complete Asana template structure for Learning Design Solutions' 17-18 week module development process, based on analysis of the actual spreadsheet template used with clients like Walbrook.

**Key Findings from Actual Template Analysis:**
- **Actual Duration**: 17-18 weeks from kickoff to "Ready for Launch" (not 16 weeks as initially documented)
- **Full Cycle**: 26 weeks (178 days) including 10-week buffer to "Go Live"
- **Week 1 Special Treatment**: 10 days for storyboarding (vs 5 days for weeks 2-8)
- **Batched Reviews**: Academic reviews in two batches (Weeks 1-2, then Weeks 3-8)
- **Build Tasks**: Separate top-level tasks, not subtasks of week groups
- **Film Shoots**: Two integrated phases (after Week 4 and after Week 8)

---

## Table of Contents

1. [Timeline Architecture](#timeline-architecture)
2. [Asana Hierarchy Structure](#asana-hierarchy-structure)
3. [Custom Fields](#custom-fields)
4. [Section Breakdown](#section-breakdown)
5. [Task Specifications](#task-specifications)
6. [Dependency Chains](#dependency-chains)
7. [Relative Date Anchoring](#relative-date-anchoring)
8. [Resource Allocation](#resource-allocation)
9. [Automation Rules](#automation-rules)
10. [Template Implementation Plan](#template-implementation-plan)
11. [Questions for Andrew](#questions-for-andrew)

---

## 1. Timeline Architecture

### 1.1 Overall Duration

```
KICKOFF → READY FOR LAUNCH: 112 days (16 weeks)
READY FOR LAUNCH → GO LIVE: 66 days (10 weeks buffer)
TOTAL CYCLE: 178 days (≈26 weeks)
```

### 1.2 Phase Breakdown

| Phase | Duration | Days | Weeks | Key Milestone |
|-------|----------|------|-------|---------------|
| Initiation & Planning | 15 days | 15 | 2-3 weeks | MPD Finalized |
| Week 1 Development | 10 days | 10 | 2 weeks | Storyboards completed |
| Week 1 Build | 5 days | 5 | 1 week | Week 1 built |
| Weeks 2-8 Development | 35 days | 35 | 7 weeks | All storyboards done |
| Weeks 2-8 Build | 35 days | 35 | 7 weeks | All content built |
| Finalization | 20 days | 20 | 4 weeks | Ready for Launch |
| **Launch Buffer** | **66 days** | **66** | **~10 weeks** | **Go Live** |

**Critical Note**: The 10-week buffer between "Ready for Launch" and "Go Live" is **not a standard** - it depends on when the program development for that specific module starts. This buffer accommodates:
- Academic calendar alignment requirements
- Client-specific launch windows
- Variable lead times based on programme scheduling

### 1.3 Week 1 Special Structure

Week 1 receives extended time allocation compared to weeks 2-8:

| Activity | Week 1 Duration | Weeks 2-8 Duration | Difference |
|----------|----------------|-------------------|------------|
| Storyboard LD Draft | 5 days | 2 days | +3 days |
| Storyboard SME Scripts | 5 days | 2 days | +3 days |
| Edit | 3 days | 2 days | +1 day |
| Final Draft Agreed | 2 days | 1 day | +1 day |
| **Total Storyboarding** | **10 days** | **5 days** | **+5 days** |

**Rationale** (confirmed with Andrew):
- First week establishes patterns and processes for the entire module
- SME needs more time to understand storyboard format and expectations
- LD and SME building working relationship and communication patterns
- More back-and-forth expected in initial week
- **Flexibility Note**: If the client truly wants to trim time, Andrew may be willing to reduce Week 1 to one week (5 days) instead of the standard 10 days, though this increases risk of rework

---

## 2. Asana Hierarchy Structure

### 2.1 Portfolio → Project → Section → Task → Subtask

```
📁 PORTFOLIO: [Client Name] Programmes
├── 📋 PROJECT: [Programme Name]
│   ├── 📑 SECTION: Initiation & Planning
│   │   ├── ☑️ TASK: Kick off meeting
│   │   │   └── ☐ Subtask: Initiation meeting held
│   │   │   └── ☐ Subtask: Kick off meeting held
│   │   ├── ☑️ TASK: Module Planning Document
│   │   │   └── ☐ Subtask: MPD Draft
│   │   │   └── ☐ Subtask: MPD Finalised
│   │   │   └── ☐ Subtask: Assessment briefs drafted
│   │   │   └── ☐ Subtask: Reading list revised
│   │   └── ☑️ TASK: MPD review
│   ├── 📑 SECTION: Week 1
│   │   ├── ☑️ TASK: Week 1 - Storyboarding
│   │   │   └── ☐ Subtask: Storyboard Initial LD Draft
│   │   │   └── ☐ Subtask: Storyboard SME Scripts Draft
│   │   │   └── ☐ Subtask: Edit
│   │   │   └── ☐ Subtask: Storyboard Final draft agreed
│   │   ├── ☑️ TASK: Week 1 - Build
│   │   └── ☑️ TASK: Week 1 and 2 review
│   ├── 📑 SECTION: Week 2
│   │   ├── ☑️ TASK: Week 2 - Storyboarding
│   │   │   └── ☐ Subtask: Storyboard Initial LD Draft
│   │   │   └── ☐ Subtask: Storyboard SME Scripts Draft
│   │   │   └── ☐ Subtask: Edit
│   │   │   └── ☐ Subtask: Storyboard Final draft agreed
│   │   └── ☑️ TASK: Week 2 - Build
│   ├── 📑 SECTION: Week 3-8
│   │   └── [Similar structure for weeks 3-8]
│   ├── 📑 SECTION: Finalization
│   │   ├── ☑️ TASK: Film shoot - first batch
│   │   ├── ☑️ TASK: Film shoot - second batch
│   │   ├── ☑️ TASK: Proofreading
│   │   ├── ☑️ TASK: Weeks 3 to 8 review
│   │   ├── ☑️ TASK: Corrections
│   │   └── ☑️ TASK: Ready for launch
│   └── 📑 SECTION: Launch
│       └── ☑️ TASK: Go live
```

### 2.2 Structural Key Findings

1. **Build Tasks Are NOT Subtasks**: Each "Week X - Build" is a separate top-level task in the section, not a subtask of "Week X - Storyboarding"
2. **Batched Reviews Are Separate Tasks**: Reviews appear as their own tasks in Week 1 and Finalization sections
3. **Film Shoots Are Top-Level Tasks**: Integrated into timeline but not subtasks of any week
4. **Launch Section Separate**: "Go live" gets its own section to emphasize the 10-week buffer

---

## 3. Custom Fields

### 3.1 Core Tracking Fields

| Field Name | Type | Options/Format | Purpose |
|------------|------|----------------|---------|
| **Module Code** | Text | e.g., "MKT101" | Unique identifier for module |
| **Client Name** | Text | e.g., "Walbrook" | Client organization |
| **Programme Name** | Text | e.g., "MBA Marketing" | Parent programme |
| **Launch Date** | Date | DD/MM/YYYY | Anchor for all relative dates |
| **Go Live Date** | Date | DD/MM/YYYY | Actual launch to students |
| **Module Author (SME)** | Person | Single select | Primary SME contact |
| **Learning Designer** | Person | Single select | Assigned LD |
| **Learning Technologist** | Person | Single select | Assigned LT |
| **Senior LD (Reviewer)** | Person | Single select | Nicole or other SLD |

### 3.2 Status & Progress Fields

| Field Name | Type | Options | Purpose |
|------------|------|---------|---------|
| **Module Status** | Single Select | Planning / In Development / Build / QA / Ready / Launched / Archived | Overall module state |
| **Content Type** | Multi Select | Theory / Activities / Video / Audio / Interactive / Assessment | Content mix tracking |
| **Week Number** | Number | 1-8 | For week-based tasks |
| **Phase** | Single Select | Initiation / Development / Build / Finalization / Launch | Workflow phase |

### 3.3 Resource Allocation Fields

| Field Name | Type | Options/Format | Purpose |
|------------|------|----------------|---------|
| **LDS Resource** | Text | Learning Designer / Learning Technologist / LD/LT / blank | LDS team member role |
| **Client Resource** | Text | SME / Programme Leader / Academic Reviewer / Librarian / Digital Learning Team / Editorial Team | Client team member role |
| **Offshore Location** | Single Select | UK / India / South Africa | For resource planning |
| **Estimated Hours** | Number | Decimal | For capacity planning |

### 3.4 Quality & Dependencies Fields

| Field Name | Type | Options | Purpose |
|------------|------|---------|---------|
| **QA Status** | Single Select | Not Started / In Review / Changes Requested / Approved | Quality gate tracking |
| **Blocker Status** | Single Select | None / Waiting on SME / Waiting on Client / Technical Issue / Resource Gap | Dependency tracking |
| **Media Requirements** | Single Select | None / Standard / Film Shoot Required / Audio Only | Special resource needs |
| **Review Batch** | Single Select | Weeks 1-2 / Weeks 3-8 / N/A | Academic review grouping |

---

## 4. Section Breakdown

### 4.1 Section: Initiation & Planning

**Duration**: 15 days (09/15/2025 - 10/03/2025 in example)
**Purpose**: Establish project foundation, agree scope, finalize planning document

#### Tasks in This Section:

1. **Kick off meeting** (5 days total)
   - Subtask: Initiation meeting held (5 days) - LD + SME
   - Subtask: Kick off meeting held (5 days) - LD + SME

2. **Module Planning Document** (10 days total, starts after kickoff)
   - Subtask: MPD Draft (5 days) - LD + SME
   - Subtask: MPD Finalised (5 days) - LD + SME
   - Subtask: Assessment briefs drafted and passed to Programme Leader (5 days) - LD + SME + Programme Leader
   - Subtask: Reading list revised (if required) (5 days) - LD + SME + Librarian

3. **MPD review** (5 days, overlaps with MPD finalization)
   - Academic Reviewer only
   - Runs in parallel with final MPD tasks

**Dependencies**:
- Module Planning Document tasks depend on Kick off meeting completion
- All subsequent phases depend on MPD review approval

---

### 4.2 Sections: Weeks 1-8 (Content Development)

Each week section follows a similar pattern, with **Week 1 being special** (10 days vs 5 days).

#### Week 1 Section (Special Extended Timeline)

**Duration**: 17 days total (storyboarding 10 days + build 5 days + 2 days for review start)

**Tasks**:

1. **Week 1 - Storyboarding** (10 days: 10/06/2025 - 10/17/2025)
   - Subtask: Storyboard Initial LD Draft (5 days) - LD only
   - Subtask: Storyboard SME Scripts Draft (5 days) - SME only (parallel with LD draft)
   - Subtask: Edit (3 days) - LD + SME
   - Subtask: Storyboard Final draft agreed (2 days) - LD + SME

2. **Week 1 - Build** (5 days: 10/20/2025 - 10/25/2025)
   - Learning Technologist only
   - **Note**: This is a separate top-level task, NOT a subtask

3. **Week 1 and 2 review** (5 days: 11/03/2025 - 11/08/2025)
   - Academic Reviewer only
   - Covers both Week 1 and Week 2 together (batched review)
   - **Note**: This task appears in Week 1 section but doesn't start until Week 2 build is complete

**Dependencies**:
- Week 1 Build depends on Week 1 Storyboard Final draft agreed
- Week 1 and 2 review depends on Week 2 Build completion

#### Weeks 2-8 Sections (Standard 5-day Pattern)

**Duration per week**: 10 days total (storyboarding 5 days + build 5 days)

**Tasks** (repeated for each week 2-8):

1. **Week [N] - Storyboarding** (5 days)
   - Subtask: Storyboard Initial LD Draft (2 days) - LD only
   - Subtask: Storyboard SME Scripts Draft (2 days) - SME only (parallel)
   - Subtask: Edit (2 days) - LD + SME
   - Subtask: Storyboard Final draft agreed (1 day) - LD + SME

2. **Week [N] - Build** (5 days, starts 1 week after storyboard starts)
   - Learning Technologist only
   - **Note**: Separate top-level task

**Special Notes**:
- Week 2 includes the batched review with Week 1 (appears in Week 1 section)
- Weeks 3-8 have a single batched review that appears in Finalization section
- Film shoot - first batch (6 days: 11/10/2025 - 11/15/2025) runs during Week 5 development
- Film shoot - second batch (5 days: 12/08/2025 - 12/12/2025) runs during Week 8 build

---

### 4.3 Section: Finalization

**Duration**: 20 days (12/08/2025 - 01/02/2026 in example)
**Purpose**: Complete final QA, corrections, and prepare for launch

#### Tasks in This Section:

1. **Film shoot - first batch** (6 days: 11/10/2025 - 11/15/2025)
   - Digital Learning Team
   - **Note**: Technically overlaps with Week 5 development, but grouped here for organization

2. **Film shoot - second batch** (5 days: 12/08/2025 - 12/13/2025)
   - Digital Learning Team
   - Starts at beginning of Finalization phase

3. **Proofreading** (5 days: 12/15/2025 - 12/19/2025)
   - Editorial Team
   - Starts after film shoot - second batch

4. **Weeks 3 to 8 review** (5 days: 12/22/2025 - 12/26/2025)
   - Academic Reviewer
   - Batched review of Weeks 3-8
   - **Note**: Falls on Christmas week! (Potential issue to address)

5. **Corrections** (5 days: 12/29/2025 - 01/02/2026)
   - Learning Designer/Technologist + SME
   - Addresses issues from Weeks 3-8 review

6. **Ready for launch** (1 day: 01/05/2026)
   - Milestone marker
   - No specific resource assigned

**Dependencies**:
- Film shoot - second batch depends on Week 8 Build completion
- Proofreading depends on Film shoot - second batch
- Weeks 3 to 8 review depends on Week 8 Build completion
- Corrections depends on Weeks 3 to 8 review
- Ready for launch depends on Corrections completion

---

### 4.4 Section: Launch

**Duration**: 1 day for milestone + 66 days buffer
**Purpose**: Mark actual launch date to students

#### Task in This Section:

1. **Go live** (Launch date: 03/11/2026)
   - No specific resource assigned
   - 66-day gap from "Ready for launch" (01/05/2026)
   - **Responsibility Clarification** (from Andrew): Launch is not Andrew's task. Andrew's job is to get everything ready for launch (the "Ready for Launch" milestone). The actual "Go Live" is controlled by the client's academic calendar and programme scheduling.

---

## 5. Task Specifications

### 5.1 Task Template Structure

Each task in Asana should include:

```
Task Name: [From template]
Assignee: [Derived from LDS Resource or Client Resource field]
Due Date: [Calculated from Launch Date using relative dates]
Custom Fields:
  - Phase: [Section it belongs to]
  - Week Number: [If applicable]
  - LDS Resource: [From template]
  - Client Resource: [From template]
  - Module Status: [Inherited from project]
  - QA Status: Not Started
  - Blocker Status: None
Dependencies: [Based on dependency chain analysis]
Description: [Task-specific guidance]
```

### 5.2 Subtask Template Structure

```
Subtask Name: [From template]
Assignee: [Based on resource allocation]
Duration: [From template]
Description: [Specific deliverables and expectations]
```

### 5.3 Week Storyboarding Task Pattern

#### Week 1 Storyboarding Task (Extended)

**Task**: Week 1 - Storyboarding
**Duration**: 10 days
**Start**: Launch Date - 156 days
**Finish**: Launch Date - 147 days
**Assignees**: Learning Designer + SME

**Subtasks**:

1. **Storyboard Initial LD Draft** (5 days)
   - Assignee: Learning Designer
   - Start: Same as parent task
   - Description: Create initial storyboard structure, learning activities, assessments. Establish week pattern and navigation.

2. **Storyboard SME Scripts Draft** (5 days - parallel)
   - Assignee: SME
   - Start: Same as parent task
   - Description: Develop subject matter content, examples, case studies. Write scripts for any video/audio content.

3. **Edit** (3 days)
   - Assignee: Learning Designer + SME
   - Start: Launch Date - 144 days
   - Depends on: Storyboard Initial LD Draft AND Storyboard SME Scripts Draft
   - Description: Integrate LD structure with SME content. Refine learning design. Adjust scripts and activities.

4. **Storyboard Final draft agreed** (2 days)
   - Assignee: Learning Designer + SME
   - Start: Launch Date - 141 days
   - Depends on: Edit
   - Description: Final review and sign-off. Confirm storyboard ready for build. Document any build notes for LT.

#### Weeks 2-8 Storyboarding Task (Standard)

**Task**: Week [N] - Storyboarding
**Duration**: 5 days
**Assignees**: Learning Designer + SME

**Subtasks**:

1. **Storyboard Initial LD Draft** (2 days)
   - Assignee: Learning Designer

2. **Storyboard SME Scripts Draft** (2 days - parallel)
   - Assignee: SME

3. **Edit** (2 days)
   - Assignee: Learning Designer + SME
   - Depends on: Both drafts

4. **Storyboard Final draft agreed** (1 day)
   - Assignee: Learning Designer + SME
   - Depends on: Edit

### 5.4 Build Task Pattern

**Task**: Week [N] - Build
**Duration**: 5 days
**Assignee**: Learning Technologist
**Depends on**: Week [N] - Storyboard Final draft agreed
**Start**: 1 week after corresponding storyboard starts

**Description Template**:
```
Build Week [N] content in Moodle based on approved storyboard.

Key deliverables:
- All pages created with correct navigation
- Activities configured (forums, quizzes, assignments, etc.)
- Media embedded (videos, audio, images)
- Resources uploaded (PDFs, downloads, links)
- Basic accessibility checks completed
- Week ready for LD/SME review

Build notes from storyboard: [Link to Week N storyboard task]
```

### 5.5 Review Task Pattern

#### Batched Review: Weeks 1-2

**Task**: Week 1 and 2 review
**Duration**: 5 days
**Start**: Launch Date - 130 days (11/03/2025 in example)
**Assignee**: Academic Reviewer
**Depends on**: Week 2 - Build
**Section**: Week 1 (for organizational purposes)

**Description**:
```
Academic review of Weeks 1-2 content together.

Review criteria:
- Academic rigor and accuracy
- Appropriate level for target audience
- Assessment alignment with learning outcomes
- Reading list currency and relevance
- Compliance with academic standards

Output: Review feedback document with required changes

⚠️ CONSISTENCY NOTE (from Andrew): Academic Reviewer performance "has been super inconsistent with current client, tends to be lighter touch than proofreading". Manage expectations accordingly and may need to allocate additional internal QA resources.
```

#### Batched Review: Weeks 3-8

**Task**: Weeks 3 to 8 review
**Duration**: 5 days
**Start**: Launch Date - 20 days (12/22/2025 in example - Christmas week!)
**Assignee**: Academic Reviewer
**Depends on**: Week 8 - Build
**Section**: Finalization

**Description**:
```
Academic review of Weeks 3-8 content together.

Review criteria:
- Academic rigor and accuracy
- Consistency with Weeks 1-2
- Progression of difficulty across weeks
- Assessment load balance
- Module coherence and flow

Output: Review feedback document with required changes

⚠️ CONSISTENCY NOTE (from Andrew): Academic Reviewer performance "has been super inconsistent with current client, tends to be lighter touch than proofreading". Manage expectations accordingly and may need to allocate additional internal QA resources.

⚠️ SCHEDULING NOTE: This review falls on Christmas week (12/22-12/26). Confirm with Academic Reviewer availability or adjust timeline.
```

### 5.6 Film Shoot Tasks

#### Film Shoot - First Batch

**Task**: Film shoot - first batch
**Duration**: 6 days
**Start**: Launch Date - 116 days (11/10/2025 in example)
**Finish**: Launch Date - 111 days (11/15/2025)
**Assignee**: Digital Learning Team
**Depends on**: Week 4 - Build (runs in parallel with Week 5 development)
**Section**: Finalization (for organizational purposes, though timing overlaps with Week 5)

**Custom Fields**:
- Media Requirements: Film Shoot Required
- Phase: Build

**Description**:
```
Film first batch of video content for module.

**Film Shoot Options** (confirmed with Andrew):

**1st Option - Physical Presence in London**:
If the Academic is physically present in London (Andrew can come into campus), they will film in the studio at SOAS or Walbrook's campus.
- Highest production quality
- Professional studio environment
- Direct support from Digital Learning Team

**2nd Option - Remote Loom Recording**:
If Academic can't come into campus, they will record themselves using Loom or similar screen recording software.
- Academic records from their own location
- More flexible scheduling
- Lower production overhead
- Still maintains personal presence

**3rd Option - AI Avatars**:
Use AI-generated avatars for video content.
- No Academic filming required
- Consistent visual presentation
- Fastest turnaround time

**Scheduling Flexibility**: These windows are nominal and recommended to the client - actual timing may vary based on SME availability and project needs.

**Planning requirements**:
- Confirm SME availability and preferred filming option
- Book studio/location (if Option 1)
- Prepare scripts and prompts (from Weeks 1-4 storyboards)
- Arrange equipment and crew (if Option 1)

**Deliverables**:
- Raw footage for Weeks 1-4 content
- Edited videos ready for embedding
- Captions/transcripts prepared

**Coordination**: Work with LT to embed videos as they're completed
```

#### Film Shoot - Second Batch

**Task**: Film shoot - second batch
**Duration**: 5 days
**Start**: Launch Date - 58 days (12/08/2025 in example)
**Finish**: Launch Date - 54 days (12/12/2025)
**Assignee**: Digital Learning Team
**Depends on**: Week 8 - Build
**Section**: Finalization

**Description**:
```
Film second batch of video content for module.

**Film Shoot Options** (confirmed with Andrew):

**1st Option - Physical Presence in London**:
If the Academic is physically present in London (Andrew can come into campus), they will film in the studio at SOAS or Walbrook's campus.
- Highest production quality
- Professional studio environment
- Direct support from Digital Learning Team

**2nd Option - Remote Loom Recording**:
If Academic can't come into campus, they will record themselves using Loom or similar screen recording software.
- Academic records from their own location
- More flexible scheduling
- Lower production overhead
- Still maintains personal presence

**3rd Option - AI Avatars**:
Use AI-generated avatars for video content.
- No Academic filming required
- Consistent visual presentation
- Fastest turnaround time

**Scheduling Flexibility**: These windows are nominal and recommended to the client - actual timing may vary based on SME availability and project needs.

**Planning requirements**:
- Confirm SME availability and preferred filming option
- Book studio/location (if Option 1)
- Prepare scripts and prompts (from Weeks 5-8 storyboards)
- Arrange equipment and crew (if Option 1)

**Deliverables**:
- Raw footage for Weeks 5-8 content
- Edited videos ready for embedding
- Captions/transcripts prepared

**Coordination**: Work with LT to embed videos as they're completed
```

**Question for Andrew**: Are film shoots standard for all modules, or only certain content types? Should this be controlled by "Media Requirements" custom field?

---

## 6. Dependency Chains

### 6.1 Critical Path Analysis

The critical path through the template runs:

```
Kick off meeting (5d)
  ↓
MPD Draft (5d)
  ↓
MPD Finalised (5d) [parallel with MPD review]
  ↓
Week 1 Storyboard (10d)
  ↓
Week 1 Build (5d)
  ↓
Week 2 Storyboard (5d)
  ↓
Week 2 Build (5d)
  ↓
Week 1 and 2 review (5d)
  ↓
Week 3-8 Storyboards (5d each, can overlap)
  ↓
Week 3-8 Builds (5d each, cascade after storyboards)
  ↓
Weeks 3 to 8 review (5d)
  ↓
Corrections (5d)
  ↓
Ready for launch (1d)
  ↓
[66-day buffer]
  ↓
Go live
```

**Total Critical Path Duration**: 112 days (16 weeks) to Ready for Launch

### 6.2 Dependency Definitions for Asana

#### Initiation Dependencies

```
"Kick off meeting" → Must complete before:
  - MPD Draft

"MPD Draft" → Must complete before:
  - MPD Finalised
  - Assessment briefs drafted
  - Reading list revised

"MPD Finalised" → Must complete before:
  - Week 1 Storyboard

"MPD review" → Must complete before:
  - Week 1 Storyboard
  [Note: MPD review runs parallel to MPD Finalised, so both must complete]
```

#### Week 1 Dependencies

```
"Week 1 - Storyboard Initial LD Draft" + "Week 1 - Storyboard SME Scripts Draft" → Both must complete before:
  - Week 1 - Edit

"Week 1 - Edit" → Must complete before:
  - Week 1 - Storyboard Final draft agreed

"Week 1 - Storyboard Final draft agreed" → Must complete before:
  - Week 1 - Build

"Week 1 - Build" → Must complete before:
  - Week 2 - Storyboard (can start in parallel)
  - Week 1 and 2 review (must wait for Week 2 Build too)
```

#### Weeks 2-8 Dependencies (Pattern)

For each week N (2-8):

```
"Week N - Storyboard Initial LD Draft" + "Week N - Storyboard SME Scripts Draft" → Both must complete before:
  - Week N - Edit

"Week N - Edit" → Must complete before:
  - Week N - Storyboard Final draft agreed

"Week N - Storyboard Final draft agreed" → Must complete before:
  - Week N - Build

"Week N - Build" → Must complete before:
  - Week N+1 - Storyboard (if applicable)
```

**Cascading Build Pattern**:
- Week 2 Build can start once Week 1 Build is underway (1 week offset)
- Week 3 Build can start once Week 2 Build is underway
- And so on through Week 8

#### Review Dependencies

```
"Week 2 - Build" → Must complete before:
  - Week 1 and 2 review

"Week 8 - Build" → Must complete before:
  - Film shoot - second batch
  - Weeks 3 to 8 review

"Week 4 - Storyboard Final draft agreed" → Must complete before:
  - Film shoot - first batch (depends on Storyboard completion, not Build completion)
```

#### Finalization Dependencies

```
"Film shoot - second batch" → Must complete before:
  - Proofreading

"Weeks 3 to 8 review" → Must complete before:
  - Corrections

"Corrections" → Must complete before:
  - Ready for launch

"Ready for launch" → Must complete before:
  - Go live
  [Note: 66-day gap, no blocker tasks in between]
```

### 6.3 Parallel Work Streams

The template allows significant parallel work:

```
PARALLEL STREAM 1: Weeks 2-8 Storyboarding
└─ Weeks can be storyboarded in parallel if LD capacity allows
   (though typically sequential with 1-week offsets)

PARALLEL STREAM 2: Weeks 2-8 Building
└─ Builds cascade with 1-week offsets
   Week 2 Build (starts) → Week 3 Build (starts) → etc.

PARALLEL STREAM 3: Reviews
└─ MPD review runs parallel to MPD Finalised
└─ Film shoots run parallel to ongoing development

SEQUENTIAL REQUIRED: Within each week
└─ Draft → Edit → Final → Build must be sequential
```

---

## 7. Relative Date Anchoring

### 7.1 Anchor Point: Launch Date

All dates in the template are calculated backward from the **Launch Date** (which becomes "Ready for launch" in the template).

**Example Timeline** (from spreadsheet):
- **Ready for launch**: 01/05/2026 (Monday)
- **Kickoff date**: 09/15/2025 (Monday)
- **Days between**: 112 days (16 weeks)

**Full Cycle** (including Go Live):
- **Go live**: 03/11/2026 (Wednesday - note: NOT a Monday!)
- **Days from Ready to Go Live**: 66 days (~10 weeks)
- **Total project duration**: 178 days (≈26 weeks)

### 7.2 Relative Date Calculation Formula

For Asana's relative date feature:

```
Task Start Date = Launch Date - [Days Before Launch]
Task Due Date = Launch Date - [Days Before Launch] + [Task Duration] - 1
```

**Example: Week 1 Storyboard**
```
Launch Date: 01/05/2026
Days Before Launch: 91 days (from 01/05/2026 back to 10/06/2025)
Duration: 10 days

Start Date = 01/05/2026 - 91 days = 10/06/2025
Due Date = 10/06/2025 + 10 days - 1 = 10/17/2025
```

### 7.3 Complete Relative Date Table

| Task / Milestone | Days Before Launch | Start Date (Example) | Duration | End Date (Example) |
|------------------|-------------------|---------------------|----------|-------------------|
| Kick off meeting | 112 | 09/15/2025 | 5d | 09/19/2025 |
| MPD Draft | 107 | 09/22/2025 | 5d | 09/26/2025 |
| MPD Finalised | 102 | 09/29/2025 | 5d | 10/03/2025 |
| MPD review | 100 | 10/06/2025 | 5d | 10/11/2025 |
| Week 1 Storyboard | 91 | 10/06/2025 | 10d | 10/17/2025 |
| Week 1 Build | 76 | 10/20/2025 | 5d | 10/25/2025 |
| Week 2 Storyboard | 71 | 10/20/2025 | 5d | 10/24/2025 |
| Week 2 Build | 61 | 10/27/2025 | 5d | 11/01/2025 |
| Week 1 and 2 review | 63 | 11/03/2025 | 5d | 11/08/2025 |
| Week 3 Storyboard | 64 | 10/27/2025 | 5d | 10/31/2025 |
| Week 3 Build | 58 | 11/03/2025 | 5d | 11/08/2025 |
| Week 4 Storyboard | 58 | 11/03/2025 | 5d | 11/07/2025 |
| Week 4 Build | 51 | 11/10/2025 | 5d | 11/15/2025 |
| Film shoot - first batch | 56 | 11/10/2025 | 6d | 11/15/2025 |
| Week 5 Storyboard | 51 | 11/10/2025 | 5d | 11/14/2025 |
| Week 5 Build | 44 | 11/17/2025 | 5d | 11/22/2025 |
| Week 6 Storyboard | 44 | 11/17/2025 | 5d | 11/21/2025 |
| Week 6 Build | 37 | 11/24/2025 | 5d | 11/29/2025 |
| Week 7 Storyboard | 37 | 11/24/2025 | 5d | 11/28/2025 |
| Week 7 Build | 30 | 12/01/2025 | 5d | 12/06/2025 |
| Week 8 Storyboard | 30 | 12/01/2025 | 5d | 12/05/2025 |
| Week 8 Build | 23 | 12/08/2025 | 5d | 12/13/2025 |
| Film shoot - second batch | 28 | 12/08/2025 | 5d | 12/12/2025 |
| Proofreading | 21 | 12/15/2025 | 5d | 12/19/2025 |
| Weeks 3 to 8 review | 14 | 12/22/2025 | 5d | 12/26/2025 |
| Corrections | 7 | 12/29/2025 | 5d | 01/02/2026 |
| **Ready for launch** | **0** | **01/05/2026** | **1d** | **01/05/2026** |
| **Go live** | **-66** | **03/11/2026** | **--** | **03/11/2026** |

**Note**: "Days Before Launch" is negative for "Go live" because it occurs AFTER the anchor point.

### 7.4 Asana Implementation

Asana Premium's relative date feature should be configured:

1. **Project Template Custom Field**: "Launch Date" (Date field)
2. **All task dates set relative to "Launch Date"**
3. **When creating new module from template**:
   - User enters only the Launch Date
   - All other dates auto-calculate

**Configuration Example**:
```
Task: Kick off meeting
Start Date: [Launch Date] - 112 days
Due Date: [Launch Date] - 108 days

Task: Week 1 Storyboard
Start Date: [Launch Date] - 91 days
Due Date: [Launch Date] - 82 days
```

---

## 8. Resource Allocation

### 8.1 Resource Types & Roles

#### LDS Internal Resources

| Role | Abbreviation | Primary Responsibilities | Typical Allocation |
|------|--------------|-------------------------|-------------------|
| **Learning Designer** | LD | Storyboarding, instructional design, editing | Full module lifecycle |
| **Learning Technologist** | LT | Moodle build, technical implementation | Build phases |
| **Senior Learning Designer** | SLD | QA review, quality assurance | Review checkpoints |
| **Learning Designer/Technologist** | LD/LT | Corrections, flexible assignments | Finalization phase |

#### Client/External Resources

| Role | Abbreviation | Primary Responsibilities | Engagement Points |
|------|--------------|-------------------------|-------------------|
| **SME / Module Author** | SME | Subject matter expertise, content creation | Initiation + Weeks 1-8 |
| **Academic Reviewer** | AR | Academic quality assurance | Two review batches |
| **Programme Leader** | PL | Programme-level oversight | Initiation (assessments) |
| **Librarian** | Lib | Reading list validation | Initiation |
| **Digital Learning Team** | DLT | Video production, media creation | Film shoots |
| **Editorial Team** | ET | Proofreading, copy editing | Finalization |

### 8.2 Resource Allocation by Phase

#### Initiation & Planning (15 days)

| Task | LD | LT | SLD | SME | AR | PL | Lib | DLT | ET |
|------|----|----|-----|-----|----|----|-----|-----|----|
| Kick off meeting | ✓ |  |  | ✓ |  |  |  |  |  |
| MPD Draft | ✓ |  |  | ✓ |  |  |  |  |  |
| MPD Finalised | ✓ |  |  | ✓ |  |  |  |  |  |
| Assessment briefs | ✓ |  |  | ✓ |  | ✓ |  |  |  |
| Reading list | ✓ |  |  | ✓ |  |  | ✓ |  |  |
| MPD review |  |  |  |  | ✓ |  |  |  |  |

**Peak Concurrent**: LD + SME + AR (during MPD finalization + review overlap)

#### Week 1 Development (10 days storyboarding + 5 days build)

| Task | LD | LT | SME |
|------|----|----| ----|
| Storyboard LD Draft | ✓ |  |  |
| Storyboard SME Draft |  |  | ✓ |
| Edit | ✓ |  | ✓ |
| Final draft agreed | ✓ |  | ✓ |
| Build |  | ✓ |  |

**Peak Concurrent**: LD + SME (during editing)
**Sequential**: LT starts after LD/SME complete

#### Weeks 2-8 Development (5 days storyboarding + 5 days build per week)

| Task | LD | LT | SME |
|------|----|----| ----|
| Storyboard LD Draft | ✓ |  |  |
| Storyboard SME Draft |  |  | ✓ |
| Edit | ✓ |  | ✓ |
| Final draft agreed | ✓ |  | ✓ |
| Build (cascading) |  | ✓ |  |

**Cascading Pattern**:
- LD + SME work on Week N storyboard (5 days)
- LT works on Week N-1 build (5 days, parallel)
- Creates efficient pipeline with minimal resource conflicts

**Example Cascade**:
```
Week 2: LD+SME on W2 storyboard | LT on W1 build
Week 3: LD+SME on W3 storyboard | LT on W2 build
Week 4: LD+SME on W4 storyboard | LT on W3 build
...
Week 9: [no storyboarding] | LT on W8 build
```

#### Reviews

| Review | AR | Notes |
|--------|----| ------|
| Week 1 and 2 review | ✓ | 5 days for both weeks together |
| Weeks 3 to 8 review | ✓ | 5 days for 6 weeks together (12/22-12/26 - Christmas!) |

**Question for Andrew**: Does Nicole (SLD) also review, or just the external Academic Reviewer? If Nicole reviews, when/how is this tracked?

#### Finalization (20 days)

| Task | LD | LT | LD/LT | SME | AR | DLT | ET |
|------|----|----| ------|-----|----|-----|----|
| Film shoot - first batch |  |  |  |  |  | ✓ |  |
| Film shoot - second batch |  |  |  |  |  | ✓ |  |
| Proofreading |  |  |  |  |  |  | ✓ |
| Weeks 3-8 review |  |  |  |  | ✓ |  |  |
| Corrections |  |  | ✓ | ✓ |  |  |  |

**Flexible Assignment**: Corrections can be handled by LD, LT, or both depending on the nature of required changes (content vs technical).

### 8.3 Resource Capacity Planning

#### Total Effort Estimation (Per Module)

**Internal LDS Resources**:
- Learning Designer: ~60-70 days of effort (spread across 17 weeks)
- Learning Technologist: ~40-45 days of effort (concentrated in 8-week build period)
- Senior Learning Designer: ~10-15 days of effort (QA and oversight)

**External Client Resources**:
- SME: ~50-60 days of effort (initiation + 8 weeks storyboarding + corrections)
- Academic Reviewer: ~10 days of effort (2 review batches)
- Programme Leader: ~2-3 days (initiation only)
- Librarian: ~2-3 days (initiation only)
- Digital Learning Team: ~11 days (two film shoot batches)
- Editorial Team: ~5 days (proofreading)

#### Concurrent Module Capacity

With cascading build pattern, a single LD-LT pair can theoretically manage:
- **1 module at a time comfortably**: Full attention, high quality
- **2 modules with 8-week offset**: LD starts Module 2 while LT builds Module 1 weeks
- **3+ modules**: Requires multiple LD-LT teams or accepting longer timelines

**Bottleneck Analysis**:
- **Learning Designer**: Highest utilization (60-70 days)
- **SME Availability**: Often the constraining factor (client-side resource)
- **Academic Reviewer**: Can batch-review multiple modules if scheduled carefully

### 8.4 Offshore Allocation Considerations

**UK-Based Resources**:
- Client-facing roles (LD, SME interactions)
- Academic reviews (typically UK-based reviewers)

**Offshore Resources** (India, South Africa):
- Learning Technologists (Moodle builds)
- Media creation (if supported)
- Proofreading / editorial (if quality standards met)

**Custom Field Usage**:
- "Offshore Location" field indicates resource location
- Timeline view can filter by location for capacity planning
- Useful for understanding timezone considerations

---

## 9. Automation Rules

Asana Premium automation rules can improve workflow efficiency and reduce manual updates.

### 9.1 Status Update Rules

#### Rule: Auto-Progress Task Status

**Trigger**: All subtasks marked complete
**Action**: Change task custom field "QA Status" to "In Review"

**Example**: When all Week 1 storyboard subtasks complete → Set "Week 1 - Storyboarding" QA Status to "In Review"

#### Rule: Module Status Propagation

**Trigger**: Section "Initiation & Planning" complete
**Action**: Update project custom field "Module Status" to "In Development"

**Trigger**: Section "Finalization" complete
**Action**: Update project custom field "Module Status" to "Ready"

**Trigger**: Task "Go live" marked complete
**Action**: Update project custom field "Module Status" to "Launched"

### 9.2 Notification Rules

#### Rule: Notify Next Resource

**Trigger**: Task "Week N - Storyboard Final draft agreed" marked complete
**Action**:
- Notify Learning Technologist assigned to "Week N - Build"
- Add comment: "Storyboard approved and ready for build. See build notes in description."

#### Rule: Review Ready Notifications

**Trigger**: Task "Week 2 - Build" marked complete
**Action**:
- Notify Academic Reviewer assigned to "Week 1 and 2 review"
- Add comment: "Weeks 1-2 are built and ready for academic review."

**Trigger**: Task "Week 8 - Build" marked complete
**Action**:
- Notify Academic Reviewer assigned to "Weeks 3 to 8 review"
- Add comment: "Weeks 3-8 are built and ready for academic review."

#### Rule: Blocker Escalation

**Trigger**: Custom field "Blocker Status" changed to anything except "None"
**Action**:
- Notify Senior Learning Designer (Nicole)
- Add project to "Blockers & Issues" portfolio
- Change task color to red

### 9.3 Dependency Management Rules

#### Rule: Auto-Create Dependencies

**Trigger**: New section "Week N" created from template
**Action**: Automatically link dependencies:
- Week N Storyboard → depends on → Week N-1 Build (if N > 1)
- Week N Storyboard → depends on → Week N-1 Storyboard Final draft agreed
- Week N Build → depends on → Week N Storyboard Final draft agreed

*Note: This may require custom Asana API integration or zapier/make.com workflow*

#### Rule: Dependency Conflict Warning

**Trigger**: Task moved with incomplete dependencies
**Action**:
- Add comment: "⚠️ Warning: This task has incomplete dependencies and may not be ready to start"
- Notify task assignee

### 9.4 Resource Allocation Rules

#### Rule: Assign Default Resources by Task Type

**Trigger**: Task name contains "Storyboard Initial LD Draft"
**Action**: Auto-assign to Learning Designer from project custom field

**Trigger**: Task name contains "Build"
**Action**: Auto-assign to Learning Technologist from project custom field

**Trigger**: Task name contains "review" (lowercase)
**Action**: Auto-assign to Academic Reviewer from project custom field

#### Rule: Capacity Warning

**Trigger**: Person assigned to >3 tasks with same due date
**Action**:
- Notify Senior Learning Designer
- Add comment to each task: "⚠️ Resource potentially over-allocated on this date"

*Note: May require custom reporting integration*

### 9.5 Quality Gate Rules

#### Rule: QA Approval Required

**Trigger**: Task marked complete with "QA Status" = "Changes Requested"
**Action**:
- Reopen task
- Add comment: "Cannot complete - QA changes requested. Please address feedback first."
- Notify task assignee

#### Rule: Academic Review Rejection Workflow

**Trigger**: Task "Week 1 and 2 review" custom field "QA Status" → "Changes Requested"
**Action**:
- Create new task: "Address Week 1-2 Review Feedback"
- Assign to Learning Designer + SME
- Link as dependency to "Corrections" task
- Notify assignees with review feedback

### 9.6 Timeline Management Rules

#### Rule: Launch Date Changed

**Trigger**: Project custom field "Launch Date" modified
**Action**:
- Notify all project members
- Add project comment: "🔄 Launch date changed. All task dates have been recalculated."
- Trigger relative date recalculation (built-in Asana feature)

#### Rule: Overdue Task Escalation

**Trigger**: Task becomes overdue
**Action**:
- Notify task assignee (immediate)
- After 1 day overdue: Notify Senior Learning Designer
- After 3 days overdue: Add to "At Risk Modules" portfolio
- Change task priority to "High"

---

## 10. Template Implementation Plan

### 10.1 Implementation Phases

#### Phase 1: Template Structure Creation (Week 1)

**Tasks**:
1. Create new Asana project: "MODULE DEVELOPMENT TEMPLATE"
2. Set up all custom fields (Section 3)
3. Create sections (Initiation, Week 1-8, Finalization, Launch)
4. Create all top-level tasks in each section
5. Create all subtasks under each task
6. Add task descriptions with deliverable expectations

**Validation**:
- All 72+ tasks/subtasks from spreadsheet represented
- Week 1 has 10-day storyboard duration
- Weeks 2-8 have 5-day storyboard duration
- Build tasks are separate top-level tasks, not subtasks
- Film shoots and reviews in correct sections

#### Phase 2: Dependencies & Timeline (Week 1-2)

**Tasks**:
1. Set up all task dependencies (Section 6)
2. Configure relative dates anchored to "Launch Date" (Section 7)
3. Test relative date calculations with sample launch date
4. Validate critical path duration = 112 days
5. Verify 66-day buffer from Ready to Go Live

**Validation**:
- Enter test launch date (e.g., 01/05/2026)
- Verify kickoff calculates to 09/15/2025 (112 days prior)
- Verify go live calculates to 03/11/2026 (66 days after)
- Check all task start/end dates match spreadsheet example
- Test changing launch date recalculates entire timeline

#### Phase 3: Resource & Automation (Week 2)

**Tasks**:
1. Add default resource assignments to tasks
2. Create automation rules (Section 9)
3. Set up notification workflows
4. Configure quality gate automations
5. Test automation triggers with dummy tasks

**Validation**:
- Complete test task → verify next resource notified
- Change blocker status → verify SLD notified
- Mark section complete → verify module status updates
- Test QA approval workflow

#### Phase 4: Testing & Validation (Week 2-3)

**Tasks**:
1. Create test module from template: "TEST Module XYZ"
2. Walk through entire workflow:
   - Complete initiation tasks
   - Complete Week 1 storyboard
   - Complete Week 1 build
   - Trigger review notifications
   - Test correction workflow
3. Validate timeline view shows correct Gantt chart
4. Test resource allocation workload view
5. Identify and fix any issues

**Validation Checklist**:
- [ ] Dependencies work correctly (can't complete out of order)
- [ ] Relative dates calculate properly
- [ ] Notifications trigger at correct times
- [ ] Resource assignments clear and accurate
- [ ] Timeline view shows 17-week development + 10-week buffer
- [ ] Custom fields populate and filter correctly

#### Phase 5: Documentation (Week 3)

**Tasks**:
1. Create template usage guide
2. Document duplication process
3. Create resource allocation guide
4. Write troubleshooting FAQ
5. Prepare demo presentation for Tuesday meeting

**Deliverables**:
- "How to Use the Module Development Template.md"
- "Module Development Workflow Guide.md"
- Video walkthrough (optional but recommended)
- Tuesday meeting demo deck

#### Phase 6: Portfolio Integration (Week 3-4)

**Tasks**:
1. Create Portfolio structure for client-level organization
2. Link module template to portfolio workflows
3. Configure portfolio-level timeline view (master waterfall)
4. Set up portfolio-level reporting
5. Test portfolio with multiple mock modules

**Portfolio Structure**:
```
📁 PORTFOLIO: [Client Name] Programmes
├── 📋 PROJECT: [Programme Name]
│   ├── Module 1 (from template)
│   ├── Module 2 (from template)
│   └── Module 3 (from template)
└── 📊 Portfolio Dashboard
    ├── Timeline View (Master Waterfall)
    ├── Resource Allocation View
    └── Status Report
```

### 10.2 Rollout Strategy

#### Pilot Phase (1 module)

**Select pilot module**:
- Ideal: Module starting in 4-6 weeks (time to prepare)
- Moderate complexity (not simplest, not most complex)
- Engaged SME with good availability
- Standard 8-week content structure

**Pilot Goals**:
- Validate template workflow in real production use
- Identify any gaps or needed adjustments
- Train LD/LT team on new Asana workflow
- Gather feedback from team and client

#### Expansion Phase (2-3 modules)

**After successful pilot**:
- Roll out to 2-3 additional modules
- Include variety (different clients, complexity levels)
- Continue gathering feedback and refining
- Begin training all team members

#### Full Adoption Phase (All new modules)

**Once template proven**:
- All new modules use Asana template
- Migrate any in-flight modules (if beneficial)
- Establish template as standard workflow
- Regular review and iteration

### 10.3 Training Plan

#### LD Team Training (2 hours)

**Topics**:
1. Asana basics (if needed)
2. Module template walkthrough
3. How to create module from template
4. Storyboard task workflow
5. Updating task status and custom fields
6. Working with dependencies
7. Communicating with SME via Asana
8. Escalation process for blockers

#### LT Team Training (1.5 hours)

**Topics**:
1. Build task workflow
2. Receiving storyboard handoff
3. Updating build progress
4. Flagging technical issues
5. Coordinating with LD on corrections
6. Using Asana mobile for status updates

#### SLD Training (1 hour)

**Topics**:
1. Template overview and philosophy
2. Portfolio-level views
3. Monitoring multiple modules
4. Identifying at-risk modules
5. Resource allocation and capacity planning
6. Running reports

#### SME/Client Training (30 min)

**Topics**:
1. Accessing Asana (guest account)
2. Understanding their tasks
3. Receiving notifications
4. Commenting and feedback
5. Uploading files
6. Where to get help

---

## 11. Questions for Andrew

Before finalizing template implementation, clarify the following with Andrew:

### 11.1 Timeline Questions

1. ~~**10-Week Launch Buffer**: Why is there a 66-day gap between "Ready for Launch" and "Go Live"?~~ **[ANSWERED - See Section 1.2]**
   - ~~Is this standard for all modules?~~
   - ~~Related to academic year calendar?~~
   - ~~Buffer for client final review?~~
   - ~~Should this be configurable per module?~~

2. **Christmas Week Reviews**: The Weeks 3-8 review falls on 12/22-12/26 (Christmas week) in the example timeline.
   - Is this typical scheduling or an artifact of the example dates?
   - How do we typically handle reviews falling on holidays?
   - Should we build in holiday detection/warnings?

3. **Go Live Date Day of Week**: In the example, "Go Live" is Wednesday (03/11/2026), not Monday like most other milestones.
   - Is this intentional (mid-week launch preference)?
   - Or should Go Live always calculate to a Monday?

### 11.2 Week 1 Structure Questions

4. ~~**Week 1 Extended Duration**: Week 1 gets 10 days for storyboarding (vs 5 days for weeks 2-8).~~ **[ANSWERED - See Section 1.3]**
   - ~~Is this pattern universal for all modules?~~
   - ~~What's the rationale? (relationship building, pattern setting, etc.)~~
   - ~~Should this ever be adjusted for certain module types?~~
   - ~~**Answer**: Extended Week 1 establishes patterns for entire module, allows SME to learn format, builds LD-SME relationship. Andrew may reduce to 5 days if client requires, but this increases rework risk.~~

5. **Storyboard Drafts Timing**: In Week 1, LD and SME drafts are 5 days each (parallel). In Weeks 2-8, they're 2 days each (parallel).
   - Are these realistic durations?
   - Should they ever be adjusted based on module complexity?

### 11.3 Review Process Questions

6. **SLD QA Tasks**: Where/how is Nicole's (Senior LD) QA review tracked?
   - Is this separate from Academic Reviewer tasks?
   - When does SLD review happen (ongoing? at milestones?)?
   - Should there be explicit SLD QA tasks in the template?

7. **Review Batching Logic**: Weeks 1-2 reviewed together (2 weeks), then Weeks 3-8 reviewed together (6 weeks).
   - Why this specific batching?
   - Could it be 3 batches instead (Weeks 1-2, 3-5, 6-8)?
   - Is the 6-week batch ever problematic (too much content to review at once)?

8. **Review Turnaround**: Both review tasks are 5 days duration.
   - Is 5 days realistic for 6 weeks of content (Weeks 3-8 review)?
   - What happens if reviewer needs more time?
   - Should this be flagged as a potential bottleneck?

### 11.4 Film Shoot Questions

9. ~~**Film Shoot Applicability**: Are film shoots standard for all modules?~~ **[ANSWERED - See Section 5.6]**
   - ~~Or only certain content types (e.g., skills-based, lab demonstrations)?~~
   - ~~Should "Film shoot" tasks be controlled by "Media Requirements" custom field?~~
   - ~~What determines first batch vs second batch content split?~~
   - ~~**Answer**: Three filming options available (Physical in London studio, Remote Loom recording, AI Avatars). Choice depends on SME location and project needs.~~

10. ~~**Film Shoot Scheduling**: First batch (6 days) runs during Week 5 development, second batch (5 days) at start of finalization.~~ **[ANSWERED - See Section 5.6]**
    - ~~Is this timing based on SME availability?~~
    - ~~Content readiness?~~
    - ~~Studio booking constraints?~~
    - ~~Should this be more flexible per module?~~
    - ~~**Answer**: Windows are nominal and recommended to client. Actual timing varies based on SME availability and project needs - scheduling is flexible.~~

### 11.5 Resource Allocation Questions

11. **LD/LT Flexibility**: In "Corrections" task, resource is listed as "Learning Designer/Technologist".
    - How is this decision made (content changes vs technical fixes)?
    - Should both always be involved?
    - Is this typical of other tasks as well?

12. **Offshore Allocation**: Which roles are typically offshore (India/South Africa) vs UK-based?
    - Learning Technologists?
    - Editorial Team?
    - Any LD roles?
    - Does this impact timeline (timezone considerations)?

13. **Concurrent Module Capacity**: How many modules can a single LD-LT pair handle concurrently?
    - Is the cascading build pattern (LD on Week N while LT builds Week N-1) the typical workflow?
    - What's the practical limit before quality suffers?

### 11.6 Custom Fields & Automation Questions

14. **Time Tracking**: Should Asana time tracking be used, or continue with Clockify?
    - If Asana, which tasks need time tracking?
    - How granular (task level? subtask level?)?
    - Is this for billing or just capacity planning?

15. **Must-Have Automations**: Which automation rules are highest priority?
    - Notifications to next resource?
    - Status auto-updates?
    - Blocker escalations?
    - Should we start simple and iterate?

16. **Custom Field Priorities**: Which custom fields are essential vs nice-to-have?
    - Review and confirm the custom field list in Section 3
    - Are there additional fields needed?
    - Are any listed fields unnecessary?

### 11.7 Portfolio & Reporting Questions

17. **Portfolio Structure**: How should client projects be organized?
    - One portfolio per client?
    - Portfolios by programme or by module?
    - How to handle multi-year client relationships?

18. **Reporting Needs**: What reports/views are most critical?
    - Master waterfall timeline (all modules)?
    - Resource allocation by person?
    - Status dashboard (on track / at risk / delayed)?
    - Financial/billing reports?

19. **Client Visibility**: What should clients see in Asana?
    - Guest access to their module only?
    - Can they see other modules in their programme?
    - Portfolio-level visibility for programme leaders?
    - What permissions (view only? comment? edit their tasks?)?

### 11.8 Integration & Migration Questions

20. **Existing Modules**: How to handle modules currently in progress?
    - Migrate to new Asana template mid-flight?
    - Complete current workflow and start fresh with next module?
    - Parallel run (old + new) for transition period?

21. **Other System Integrations**: Are there other systems that need to integrate?
    - Clockify (time tracking)?
    - Accounting/billing system?
    - CRM (Pipedrive?)?
    - Google Drive (document storage)?

22. **Workflow Variations**: Do all modules follow this exact pattern?
    - Are there shorter/longer module types?
    - Modules without film shoots?
    - Modules with different review requirements?
    - Should we create template variations, or one flexible template?

---

## 12. Next Steps

### 12.1 Immediate Actions (Before Building Template)

1. **Schedule Meeting with Andrew**: Review Section 11 questions
2. **Finalize Timeline Parameters**: Confirm 17-18 week structure, buffer duration
3. **Confirm Resource Model**: Clarify LD/LT/SLD roles and offshore allocation
4. **Decide on Custom Fields**: Lock down essential vs optional fields
5. **Prioritize Automations**: Identify must-have vs nice-to-have rules

### 12.2 Template Build (After Clarifications)

1. **Create Template in Asana**: Following Phase 1 implementation plan
2. **Configure Dependencies**: Set up all task relationships
3. **Set Up Relative Dates**: Anchor to Launch Date field
4. **Add Default Resources**: Assign roles to tasks
5. **Create Automation Rules**: Start with high-priority notifications
6. **Test Thoroughly**: Use test module to validate entire workflow

### 12.3 Documentation & Training (Parallel to Build)

1. **Write Usage Guide**: How to create module from template
2. **Create Training Materials**: For LD, LT, SLD, SME roles
3. **Prepare Demo**: For Tuesday meeting presentation
4. **Document Decision Log**: Capture rationale for template choices

### 12.4 Pilot & Iterate (After Template Ready)

1. **Select Pilot Module**: Choose appropriate first real-world test
2. **Monitor Closely**: Daily check-ins during pilot
3. **Gather Feedback**: From all participants (team + client)
4. **Iterate Template**: Refine based on learnings
5. **Expand Gradually**: Roll out to additional modules with confidence

---

## 13. Success Criteria

The Module Development Template will be considered successful when:

### 13.1 Efficiency Metrics

- [ ] Time to create new module project: <10 minutes (down from ~60 minutes manual setup)
- [ ] Timeline visibility: All stakeholders can see full module schedule at a glance
- [ ] Dependency management: No missed handoffs between LD → LT or storyboard → build
- [ ] Resource conflicts: Identified proactively via workload view, not reactively via missed deadlines

### 13.2 Quality Metrics

- [ ] QA consistency: All modules go through same quality gates
- [ ] Review completeness: No weeks skipped in academic review process
- [ ] Documentation: All storyboards and build notes properly linked and accessible
- [ ] Client satisfaction: SME feedback on visibility and collaboration improves

### 13.3 Adoption Metrics

- [ ] Team adoption: All LDs and LTs using template for new modules within 1 month
- [ ] Client adoption: SME engagement in Asana (commenting, task completion) within 2 weeks of module start
- [ ] Template usage: 100% of new modules created from template (not manual setup)
- [ ] Training completion: All team members trained on template workflow

### 13.4 Business Metrics

- [ ] Delivery reliability: Modules hit "Ready for Launch" date ≥90% of the time
- [ ] Capacity predictability: Resource allocation accurate enough for 4-6 week pipeline forecasting
- [ ] Client communication: Reduced time spent on status update emails/meetings
- [ ] Scalability: System supports 10+ concurrent modules without breaking down

---

## Appendix A: Spreadsheet-to-Asana Mapping

### Full Task List with Asana Structure

| Row | Task Name (from CSV) | Asana Section | Asana Task | Asana Subtask | Duration | Resource LDS | Resource Client |
|-----|---------------------|---------------|------------|---------------|----------|--------------|-----------------|
| 6 | Kick off meeting | Initiation & Planning | Kick off meeting | (parent) | 5d | | |
| 7 | Initiation meeting held | Initiation & Planning | Kick off meeting | Initiation meeting held | 5d | Learning Designer | SME |
| 8 | Kick off meeting held | Initiation & Planning | Kick off meeting | Kick off meeting held | 5d | Learning Designer | SME |
| 9 | Module Planning Document | Initiation & Planning | Module Planning Document | (parent) | 10d | | |
| 10 | MPD Draft | Initiation & Planning | Module Planning Document | MPD Draft | 5d | Learning Designer | SME |
| 11 | MPD Finalised | Initiation & Planning | Module Planning Document | MPD Finalised | 5d | Learning Designer | SME |
| 12 | Assessment briefs... | Initiation & Planning | Module Planning Document | Assessment briefs... | 5d | Learning Designer | SME, Programme Leader |
| 13 | Reading list revised | Initiation & Planning | Module Planning Document | Reading list revised | 5d | Learning Designer | SME, Librarian |
| 14 | MPD review | Initiation & Planning | MPD review | (task) | 5d | | Academic Reviewer |
| 15 | Week 1 | Week 1 | Week 1 - Storyboarding | (parent) | 10d | | |
| 16 | Week 1 - Storyboard Initial LD Draft | Week 1 | Week 1 - Storyboarding | Storyboard Initial LD Draft | 5d | Learning Designer | |
| 17 | Week 1 - Storyboard SME Scripts Draft | Week 1 | Week 1 - Storyboarding | Storyboard SME Scripts Draft | 5d | | SME |
| 18 | Week 1 - Edit | Week 1 | Week 1 - Storyboarding | Edit | 3d | Learning Designer | SME |
| 19 | Week 1 - Storyboard Final draft agreed | Week 1 | Week 1 - Storyboarding | Final draft agreed | 2d | Learning Designer | SME |
| 20 | Week 1 - Build | Week 1 | Week 1 - Build | (task) | 5d | Learning Technologist | |
| 21 | Week 2 | Week 2 | Week 2 - Storyboarding | (parent) | 5d | | |
| 22 | Week 2 - Storyboard Initial LD Draft | Week 2 | Week 2 - Storyboarding | Storyboard Initial LD Draft | 2d | Learning Designer | |
| 23 | Week 2 - Storyboard SME Scripts Draft | Week 2 | Week 2 - Storyboarding | Storyboard SME Scripts Draft | 2d | | SME |
| 24 | Week 2 - Edit | Week 2 | Week 2 - Storyboarding | Edit | 2d | Learning Designer | SME |
| 25 | Week 2 - Storyboard Final draft agreed | Week 2 | Week 2 - Storyboarding | Final draft agreed | 1d | Learning Designer | SME |
| 26 | Week 2 - Build | Week 2 | Week 2 - Build | (task) | 5d | Learning Technologist | |
| 27 | Week 1 and 2 review | Week 1 | Week 1 and 2 review | (task) | 5d | | Academic Reviewer |

[Pattern continues for Weeks 3-8...]

| 40 | Film shoot - first batch | Finalization | Film shoot - first batch | (task) | 6d | | Digital Learning Team |
| 66 | Film shoot - second batch | Finalization | Film shoot - second batch | (task) | 5d | | Digital Learning Team |
| 67 | Proofreading | Finalization | Proofreading | (task) | 5d | | Editorial Team |
| 68 | Weeks 3 to 8 review | Finalization | Weeks 3 to 8 review | (task) | 5d | | Academic Reviewer |
| 69-70 | Corrections | Finalization | Corrections | (task) | 5d | Learning Designer/Technologist | SME |
| 71 | Ready for launch | Finalization | Ready for launch | (task) | 1d | | |
| 72 | Go live | Launch | Go live | (task) | -- | | |

---

## Appendix B: Glossary

| Term | Definition |
|------|------------|
| **Academic Reviewer** | External subject matter expert who validates academic quality and rigor of module content |
| **Build** | Process of implementing storyboarded content in the Moodle LMS by Learning Technologist |
| **Client Project** | Business engagement with a client (e.g., Walbrook partnership), distinct from Asana "project" |
| **Digital Learning Team** | Client's or third-party team responsible for video production and media creation |
| **Editorial Team** | Professional proofreaders/copy editors who review final content for language quality |
| **Go Live Date** | Date when module actually launches to students (66 days after Ready for Launch) |
| **Launch Date** | Anchor date for all relative date calculations; equivalent to "Ready for Launch" milestone |
| **LD** | Learning Designer - instructional designer responsible for module structure and pedagogy |
| **LT** | Learning Technologist - technical implementer who builds module in Moodle |
| **Module** | Individual learning unit, typically 10 credits, comprising 8 weeks of content |
| **Module Author** | See SME - subject matter expert who creates content |
| **MPD** | Module Planning Document - foundational document defining module scope, outcomes, and structure |
| **Programme** | Collection of modules leading to a qualification (e.g., MBA Marketing) |
| **Programme Leader** | Client role overseeing entire programme, involved in assessment design approval |
| **Ready for Launch** | Milestone when module is complete, QA'd, and ready for student access (but not yet launched) |
| **SLD** | Senior Learning Designer - experienced LD providing quality assurance and oversight (e.g., Nicole) |
| **SME** | Subject Matter Expert - client's academic expert who provides content expertise |
| **Storyboard** | Detailed design document specifying all module content, activities, and media before build |

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-10-09 | Claude | Initial specification based on documentation review |
| **2.0** | **2025-10-13** | **Claude** | **Complete revision based on actual spreadsheet template analysis. Updated timeline to 17-18 weeks, added Week 1 extended duration, batched reviews, separate build tasks, film shoots, 10-week buffer. Added comprehensive questions for Andrew.** |

---

**Status**: DRAFT - Requires Andrew's review and clarification of questions in Section 11 before implementation
**Next Action**: Schedule review meeting to address Section 11 questions
**Target Implementation Date**: TBD after clarifications
**Tuesday Meeting Demo**: To be prepared after template finalized
