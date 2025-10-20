# Asana Module Development Template - Compliance Review Session
**Date**: 2025-10-16
**Reviewer**: Andrew (via Google Doc feedback)
**Session Type**: Remote specification review and local sync

## Executive Summary

Completed comprehensive review of Asana Module Development Template specification against Andrew's authoritative feedback integrated into the remote Google Doc. All 12 identified clarifications have been incorporated into the local specification file, and key learnings documented for Asana template implementation.

## Key Clarifications from Andrew

### 1. Launch Buffer Variability (Section 1.2)
**Finding**: The 10-week (66-day) buffer between "Ready for Launch" and "Go Live" is **NOT a standard**.
**Clarification**: Buffer duration depends on when program development starts for each specific module.
**Factors**:
- Academic calendar alignment requirements
- Client-specific launch windows  
- Variable lead times based on programme scheduling
**Impact**: Template must accommodate flexible buffer periods, not assume 66-day standard.

### 2. Week 1 Extended Duration Rationale (Section 1.3)
**Finding**: Week 1 gets 10 days for storyboarding vs. 5 days for Weeks 2-8.
**Rationale Confirmed**:
- First week establishes patterns and processes for entire module
- SME needs more time to understand storyboard format and expectations
- LD and SME building working relationship and communication patterns
- More back-and-forth expected in initial week
**Flexibility Option**: Andrew may be willing to reduce Week 1 to 5 days if client truly wants to trim time, though this increases risk of rework.
**Impact**: Template should default to 10-day Week 1, with flexibility note.

### 3. Film Shoot Options (Section 5.6)
**Critical Finding**: Three distinct filming approaches available, not just physical studio shoots.

**Option 1 - Physical Presence in London**:
- Academic physically present in London (Andrew can come into campus)
- Film in studio at SOAS or Walbrook's campus
- Highest production quality
- Professional studio environment
- Direct support from Digital Learning Team

**Option 2 - Remote Loom Recording**:
- Academic can't come into campus
- Record themselves using Loom or similar screen recording software
- More flexible scheduling
- Lower production overhead
- Still maintains personal presence

**Option 3 - AI Avatars**:
- Use AI-generated avatars for video content
- No Academic filming required
- Consistent visual presentation
- Fastest turnaround time

**Scheduling Flexibility**: Film shoot windows are nominal and recommended to client - actual timing may vary based on SME availability and project needs.

**Impact**: Task descriptions must document all three options and emphasize flexibility.

### 4. Launch Responsibility Clarification (Section 4.4)
**Finding**: Confusion about "Go Live" responsibility.
**Clarification**: Launch is NOT Andrew's task. Andrew's job is to get everything ready for launch (the "Ready for Launch" milestone). The actual "Go Live" is controlled by the client's academic calendar and programme scheduling.
**Impact**: Template must clearly separate "Ready for Launch" (Andrew's deliverable) from "Go Live" (client timing decision).

### 5. Film Shoot Dependency Correction (Section 6.2)
**Error Found**: Film shoots were shown as depending on "Week 4 - Build" completion.
**Correction**: Film shoots depend on **Storyboard** completion, not Build completion.
**Logic**: Film shoots need completed scripts/storyboards (content), not completed builds (Moodle implementation).
**Impact**: Dependency chain must be corrected in Asana template.

### 6. Academic Reviewer Consistency Warning (Section 5.5)
**Critical Warning from Andrew**: Academic Reviewer performance "has been super inconsistent with current client, tends to be lighter touch than proofreading".
**Recommendation**: Manage expectations accordingly and may need to allocate additional internal QA resources.
**Impact**: 
- Task descriptions must include this warning
- Template should flag potential need for supplemental QA
- Both review batches (Weeks 1-2 and Weeks 3-8) need this note

## Application to Asana Template

### High Priority Updates Required

1. **Film Shoot Task Descriptions** (Tasks: 1211627678168672, 1211627678168673)
   - Current: Basic description without filming options
   - Required: Add all three filming options with details
   - Add scheduling flexibility note
   - Status: **NOT YET APPLIED**

2. **Film Shoot Dependencies** (Task: 1211627678168672)
   - Current: Blocked by "Week 4 - Build"
   - Required: Change to "Week 4 - Storyboard Final draft agreed"
   - Status: **NOT YET APPLIED**

3. **Academic Review Task Descriptions**
   - Add consistency warning to both review tasks
   - Include expectation management guidance
   - Status: **NOT YET APPLIED**

4. **Launch Task Description**
   - Add responsibility clarification
   - Distinguish "Ready for Launch" (Andrew) from "Go Live" (client)
   - Status: **NOT YET APPLIED**

5. **Project-Level Custom Field Documentation**
   - Update "Launch Date" field description to clarify buffer variability
   - Status: **NOT YET APPLIED**

6. **Week 1 Task Descriptions**
   - Add rationale for 10-day duration
   - Include flexibility option note
   - Status: **NOT YET APPLIED**

### Implementation Approach

**Phase 1**: Critical Corrections
- Fix film shoot dependencies (Storyboard → Film Shoot, not Build → Film Shoot)
- Update film shoot task descriptions with three options
- Add Academic Reviewer consistency warnings

**Phase 2**: Clarifications and Context
- Update launch task with responsibility clarification
- Add Week 1 rationale to storyboarding tasks
- Update custom field descriptions

**Phase 3**: Documentation and Training
- Create template usage guide with Andrew's clarifications
- Document filming options decision tree
- Include Academic Reviewer management strategies

## Questions Still Pending

From Section 11 of specification, several questions remain unanswered and should be discussed with Andrew:

- Christmas week scheduling conflicts (Q2)
- Go Live day-of-week preferences (Q3)
- Storyboard draft timing realism (Q5)
- SLD QA tracking (Q6)
- Review batching optimization (Q7, Q8)
- Resource allocation details (Q11-Q13)
- Automation priorities (Q14-Q16)
- Portfolio structure (Q17-Q19)
- Integration requirements (Q20-Q22)

## Success Metrics

**Specification Sync**: ✅ COMPLETE - All 12 identified clarifications incorporated into local specification file.

**Asana Template Updates**: ⏳ IN PROGRESS
- Film shoot descriptions: Pending
- Dependency corrections: Pending
- Review warnings: Pending
- Launch clarification: Pending
- Week 1 rationale: Pending

**Documentation**: ⏳ IN PROGRESS
- Memory file created: ✅
- Implementation guide: Pending

## Next Actions

1. Update Film Shoot task descriptions (both first and second batch)
2. Correct Film Shoot dependency (Week 4 Build → Week 4 Storyboard)
3. Add Academic Reviewer consistency warnings to both review tasks
4. Update Launch task description with responsibility clarification
5. Create supplemental implementation guide document
6. Schedule follow-up meeting with Andrew for remaining Section 11 questions

## File References

- **Local Specification**: `Asana_Module_Development_Template_Spec_v2.md` (1550 lines, fully updated)
- **Remote Source**: Google Doc ID `1rbNNtT2Pk8PdHZKSVFnFAZMEjs1i_7kOLxEqK5WOPiU`
- **Asana Template**: Project ID `1211626878286938` ("TEST Project Template")
- **Key Tasks**:
  - Film shoot first batch: `1211627678168672`
  - Film shoot second batch: `1211627678168673`

## Document Control

| Version | Date | Author | Status |
|---------|------|--------|--------|
| 1.0 | 2025-10-16 | Claude | Active - Awaiting Asana template application |
