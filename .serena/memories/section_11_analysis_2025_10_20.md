# Section 11 Questions Analysis - October 20, 2025

## Analysis Overview
Systematically cross-referenced all 22 Section 11 questions against three sources:
1. Remote Google Doc: "Learning Design Solutions Workflows" (8 workflows)
2. October 14, 2025 transcript (specification review meeting)
3. October 16, 2025 transcript (course demonstration and workflow)

## Questions Status Summary

### ✅ ANSWERED (8 questions)

**Q1: 10-Week Launch Buffer**
- **Answer**: Oct 14 transcript discusses "10-week buffer variability"
- **Source**: October 14 transcript
- **Status**: Fully answered

**Q4: Week 1 Extended Duration**
- **Answer**: Oct 14 covered "Week 1 extended duration rationale"
- **Source**: October 14 transcript
- **Status**: Fully answered

**Q7: Review Batching Logic & Holiday Detection**
- **Answer**: Oct 14 discussed "Holiday detection (Christmas + academic out-of-office)"
- **Source**: October 14 transcript
- **Status**: Fully answered

**Q9: Film Shoot Applicability**
- **Answer**: Oct 14 mentioned "Critical dependency clarifications (film shoot depends on storyboard, not build)"
- **Source**: October 14 transcript
- **Status**: Partially answered (dependency clear, but not applicability across all modules)

**Q12: Offshore Allocation**
- **Answer**: "UK vs offshore allocation based on budget"
- **Source**: Remote Doc Workflow 5 (Team & Resource Management)
- **Status**: Partially answered (principle stated, but specific role allocation not detailed)

**Q17: Portfolio Structure**
- **Answer**: "Aspiration: Portfolio-level dashboard showing all modules and milestones"
- **Source**: Remote Doc Workflow 3 (Programme Management)
- **Status**: Aspiration stated, actual structure is design task

**Q18: Reporting Needs**
- **Answer**: "Weekly reporting from LDs into master spreadsheet" + "Weekly reporting spreadsheet in client's shared drive"
- **Source**: Remote Doc Workflows 3 & 6
- **Status**: Current practice documented, critical reports to be determined during design

**Q22: Workflow Variations**
- **Answer**: 8 different workflows documented (not all modules follow exact pattern)
- **Source**: Remote Doc (all 8 workflows)
- **Status**: Implicitly answered - yes there are variations

### ⚠️ LIKELY ANSWERED (3 questions - need transcript extraction)

**Q6: SLD QA Tasks**
- **Indicator**: Oct 16 covered "Quality assurance processes"
- **Source**: October 16 transcript
- **Status**: Likely answered, needs extraction

**Q10: Film Shoot Scheduling**
- **Indicator**: Oct 16 covered "Video production options (on-campus, self-recorded, AI avatars)"
- **Source**: October 16 transcript
- **Status**: Likely answered, needs extraction

**Q15: Must-Have Automations**
- **Indicator**: Oct 16 covered "Workflow automation requirements"
- **Source**: October 16 transcript
- **Status**: Likely answered, needs extraction

### ❌ NOT FOUND / DESIGN DECISIONS (11 questions)

**Q2: Academic Calendar Alignment**
- **Status**: Not explicitly addressed
- **Nature**: May be design decision based on client needs

**Q3: Go Live Date Day of Week**
- **Status**: Not found
- **Nature**: Design decision (should we force Monday Go Live?)

**Q5: Storyboard Drafts Timing**
- **Status**: Not found
- **Nature**: Validation needed on realistic durations

**Q8: Review Turnaround**
- **Status**: Not found
- **Nature**: Validation question (is 5 days realistic for 6 weeks of content?)

**Q11: LD/LT Flexibility**
- **Status**: Roles documented but decision logic not detailed
- **Nature**: Process design decision

**Q13: Concurrent Module Capacity**
- **Status**: "20+ concurrent modules" mentioned at programme level, not pair capacity
- **Nature**: Resource planning decision

**Q14: Time Tracking Tool**
- **Status**: Gap mentioned but no tool decision
- **Nature**: Tool selection decision (Asana vs Clockify)

**Q16: Custom Field Priorities**
- **Status**: 22 fields proposed but no priority ranking
- **Nature**: Design decision during implementation

**Q19: Client Visibility**
- **Status**: Not addressed
- **Nature**: Design decision (permissions and views)

**Q20: Existing Modules Handling**
- **Status**: Not addressed
- **Nature**: Migration strategy decision

**Q21: System Integrations**
- **Status**: Gaps identified (Clockify, profitability tracking) but no integration solution
- **Nature**: Technical implementation decision

## Key Insights

### 1. Distinction Between Answered vs Design Decisions
Many "unanswered" questions are actually decisions to be made during implementation:
- Q16, Q17, Q19: Structure and visibility design
- Q14, Q21: Tool selection and integration
- Q3, Q11: Process design decisions

### 2. Current Spec Scope
The current Asana specification v2.0 only covers **Workflow 4** (single module development within a program).

**Missing scope includes:**
- Programme-level management (multiple modules per program)
- Module interconnection and tracking
- Business development pipeline (Workflow 1)
- Client onboarding processes (Workflow 2)
- Resource allocation across programs (Workflow 5)
- Financial tracking (Workflow 7)
- Closeout procedures (Workflow 8)

### 3. Architecture Design Requirements
From 8 workflows analysis, need to design:
- **Hierarchy expansion**: Portfolio → Programme → Project (Module) → Section → Task/Subtask
- **Workflow 1 integration**: Lead → Contact → Proposal → Negotiation → Closed pipeline
- **Workflow 2 integration**: Onboarding checklist with RACI, questionnaires, playbooks
- **Workflow 3 integration**: Programme dashboard with module tracking
- **Workflow 5 integration**: Resource utilization and availability tracker
- **Workflow 6 integration**: Issue log and resolution tracking
- **Workflow 7 integration**: Project-level profitability tracking
- **Workflow 8 integration**: Closeout checklist and feedback tracker

### 4. API Implementation Priorities
Based on analysis, critical API needs:
1. Native task start dates (not dependent on predecessor completion)
2. Relative date anchoring to Launch Date
3. Role assignment automation
4. Dependency chain configuration
5. Custom field population
6. Portfolio/Programme hierarchy creation

## Next Steps

1. ✅ Section 11 analysis - COMPLETED
2. 🔄 Document findings - IN PROGRESS
3. ⏳ Audit current Asana test project implementation - NEXT
4. ⏳ Design full multi-program architecture integrating 8 workflows
5. ⏳ Plan API implementation strategy

## Recommendations

### For Questions Requiring Andrew's Input
The following genuinely need Andrew's clarification:
- Q2: Academic calendar alignment requirements
- Q3: Go Live day preference
- Q5: Storyboard timing validation
- Q8: Review turnaround realism
- Q13: Pair capacity expectations
- Q14: Time tracking tool preference
- Q16: Custom field priority ranking
- Q19: Client visibility preferences
- Q20: Migration strategy for existing modules

### For Design Decisions During Implementation
These will be resolved through architecture design:
- Q11: LD/LT decision process
- Q17: Portfolio structure (we're designing this)
- Q21: System integration approach
