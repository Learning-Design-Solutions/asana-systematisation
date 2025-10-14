# CSV Import Analysis and Recommended Fixes

**Date**: 2025-10-13
**Analyst**: Claude
**Purpose**: Analyze two test CSV imports and provide solutions for identified issues

---

## Executive Summary

Two test imports of the Module Development Template CSV were performed with different results:

| Import Method | Sections | Tasks | Subtasks | Due Dates | Start Dates | Dependencies | Issues |
|--------------|----------|-------|----------|-----------|-------------|--------------|--------|
| **Direct Import** (Project 1211626875246589) | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | ❌ No | ❌ No | Empty placeholder tasks |
| **AI-Assisted** (Project 1211626878286938) | ✅ Yes | ✅ Yes | ❌ No | ✅ Yes | ✅ Yes | ❌ No | Lost subtask relationships |

**Key Finding**: **Neither import method successfully handled dependencies**, which is a critical limitation of Asana's CSV import system.

---

## Detailed Analysis

### Project 1: Direct CSV Import (with pre-existing fields)
**URL**: https://app.asana.com/1/1210754319198231/project/1211626875246589/list/1211627018102262

#### What Worked ✅
1. **Sections**: All 12 sections created correctly (Instructions, Initiation & Planning, Weeks 1-8, Finalization, Launch)
2. **Parent Tasks**: All 26 top-level tasks created (e.g., "Kick off meeting", "Week 1 - Storyboarding", "Week 1 - Build")
3. **Subtasks**: All 37 subtasks created with correct parent relationships
   - Example: "Week 1 - Storyboard Initial LD Draft" is correctly nested under "Week 1 - Storyboarding"
4. **Due Dates**: All tasks have correct due dates
   - Example: "Kick off meeting" → 2025-09-19
   - Example: "Go live" → 2026-03-11
5. **Task Notes**: All descriptions preserved correctly

#### What Failed ❌
1. **Start Dates**: All `start_on` fields are `null`
   - CSV had "Start Date" column populated
   - Asana did not map this during import
   - **Impact**: Timeline Gantt chart shows tasks as points, not bars

2. **Dependencies**: All `dependencies` and `dependents` arrays are empty
   - CSV had "Blocked By (Dependencies)" and "Blocking (Dependencies)" columns
   - Asana CSV import **does not support dependency import**
   - **Impact**: No workflow constraints, tasks can be completed out of order

3. **Empty Placeholder Tasks**: Several tasks with name="" and notes="—" were created
   - Example: Task 1211627678168623 in Week 3 section
   - Example: Task 1211627678168655 in Week 7 section
   - These appear to be CSV parsing artifacts
   - **Impact**: Clutter in project, confusing for users

### Project 2: AI-Assisted Import (without pre-existing fields)
**URL**: https://app.asana.com/1/1210754319198231/project/1211626878286938/board/1211627584395286

#### What Worked ✅
1. **Sections**: All 12 sections created correctly
2. **Top-Level Tasks**: All major tasks created (though some that should be subtasks are top-level)
3. **Due Dates**: All tasks have correct due dates
4. **Start Dates**: Most tasks have start dates populated
   - Example: "Go live" → start_on: 2026-03-11, due_on: 2026-03-11
   - Example: "Corrections" → start_on: 2025-12-29, due_on: 2026-01-02
5. **Task Notes**: All descriptions preserved

#### What Failed ❌
1. **Subtasks**: Parent-child relationships were lost
   - All tasks show `"parent":null`
   - Tasks that should be subtasks (e.g., "Week 1 - Storyboard Initial LD Draft") appear as top-level tasks in their sections
   - **Impact**: Flat task structure, harder to navigate, can't collapse week storyboarding tasks

2. **Dependencies**: All `dependencies` and `dependents` arrays are empty
   - Same as Project 1 - AI assistant also couldn't create dependencies via API
   - **Impact**: No workflow constraints

3. **Inconsistent Start Dates**: Some tasks have start dates, some don't
   - Instruction task: `"start_on":null`
   - Most other tasks have start dates matching or preceding due dates

---

## Root Cause Analysis

### Issue 1: Dependencies Not Imported

**Root Cause**: Asana's CSV import system **does not support** importing task dependencies through "Blocked By" and "Blocking" columns.

**Evidence**:
- Both imports (manual and AI) resulted in zero dependencies
- Asana's CSV import documentation confirms this limitation
- Dependencies must be created via:
  - Asana UI (manual clicking)
  - Asana API (programmatic creation)
  - Asana templates (copying from existing template project)

**Why This Is Critical**:
- Without dependencies, the template loses its **workflow enforcement**
- Users can complete tasks out of order (e.g., build Week 1 before storyboard is approved)
- The cascading build pattern (Week N build while Week N+1 storyboards) is not enforced
- Academic reviews won't wait for builds to complete

### Issue 2: Start Dates Not Imported (Direct Import)

**Root Cause**: Column name mismatch or Asana import parser limitation

**Evidence**:
- CSV column named "Start Date"
- Asana expects "Start Date" but may require exact formatting
- AI-assisted import DID map start dates, suggesting it's a parser/mapping issue

**Possible Causes**:
1. Date format mismatch (Asana expects YYYY-MM-DD, CSV had this but parser failed)
2. Column header spacing or character encoding issue
3. Import wizard didn't recognize "Start Date" column during manual import

### Issue 3: Subtasks Lost (AI-Assisted Import)

**Root Cause**: AI parsing interpreted "Parent task" column as task name instead of relationship indicator

**Evidence**:
- CSV column "Parent task" had values like "Week 1 - Storyboarding"
- AI created tasks named "Week 1 - Storyboard Initial LD Draft" but didn't link them as subtasks
- All tasks show `"parent":null`

**Why AI Failed**:
- AI treated "Parent task" as descriptive text, not a relationship field
- Without explicit instruction to create parent-child relationships, AI created flat structure
- AI cannot access task GIDs to reference parents (those only exist after creation)

### Issue 4: Empty Placeholder Tasks (Direct Import)

**Root Cause**: CSV had empty rows or section separator rows that were imported as tasks

**Evidence**:
- Tasks with name="" and notes="—" appear between section tasks
- These seem to be CSV formatting rows or accidental blank rows

**Location Pattern**:
- Appear at the end of some sections (Week 2, Week 3, Week 4, Week 5, Week 6, Week 7, Week 8, Initiation, Finalization, Launch)
- Suggests there were blank rows in CSV between section groups

---

## Recommended Solutions

### Solution 1: Create Template Project with Manual Dependencies ⭐ RECOMMENDED

**Approach**: Use the better import (Project 1) as base, then manually complete it as an Asana Template

**Steps**:

1. **Start with Project 1** (Direct Import - has subtasks)
   - Already has correct task hierarchy
   - Already has correct due dates
   - Only missing start dates and dependencies

2. **Add Start Dates Manually**:
   - Switch to Timeline view
   - Click each task bar
   - Add start date from the original CSV or specification
   - ~65 tasks × 10 seconds each = ~11 minutes

3. **Add Dependencies Manually**:
   - Follow dependency chain from specification v2.0
   - Use Asana UI: click task → Dependencies tab → Add "Blocked by" tasks
   - Critical dependencies (~40 relationships):
     - Kick off meeting → MPD Draft
     - MPD Finalised → Week 1 Storyboarding
     - Week N Final draft → Week N Build
     - Week N Build → Week N+1 Storyboarding (cascading)
     - Batched reviews → Corrections
   - **Time estimate**: ~30 minutes for all dependencies

4. **Delete Empty Placeholder Tasks**:
   - Search for tasks with name=""
   - Delete manually (~10 tasks)
   - **Time estimate**: 2 minutes

5. **Convert to Template**:
   - Project Settings → Convert to Template
   - Set as "Module Development Template"
   - All future modules duplicated from this

**Total Time**: ~45 minutes of manual work

**Advantages**:
- ✅ One-time setup effort
- ✅ Future modules inherit all dependencies automatically
- ✅ Subtask structure preserved
- ✅ Can be duplicated infinitely with all relationships intact
- ✅ Relative date anchoring works (when Asana implements it fully)

**Disadvantages**:
- ❌ Manual dependency creation required (one time)
- ❌ Start dates must be manually added or adjusted per module

### Solution 2: Hybrid Import + API Script

**Approach**: Import CSV for structure, then use Asana API to add dependencies programmatically

**Steps**:

1. **Use Project 1 as base** (has subtasks)

2. **Write Python/Node.js script** using Asana API:
   ```python
   # Pseudo-code
   tasks = get_all_tasks(project_id)

   # Map task names to GIDs
   task_map = {task['name']: task['gid'] for task in tasks}

   # Read dependency rules from specification
   dependencies = load_dependency_rules()

   # Create dependencies via API
   for dep in dependencies:
       source_gid = task_map[dep['source']]
       target_gid = task_map[dep['target']]
       asana.add_dependency(source_gid, target_gid)
   ```

3. **Define dependency rules** in structured format:
   ```yaml
   dependencies:
     - source: "Kick off meeting"
       blocks: ["MPD Draft"]
     - source: "MPD Finalised"
       blocks: ["Week 1 - Storyboarding"]
     - source: "Week 1 - Storyboard Final draft agreed"
       blocks: ["Week 1 - Build"]
     # ... continue for all 40+ dependencies
   ```

4. **Run script** against Project 1

5. **Convert to template**

**Total Time**: ~2-3 hours (script development + testing)

**Advantages**:
- ✅ Programmatically repeatable
- ✅ Can be version-controlled
- ✅ Useful if template needs frequent updates
- ✅ Can batch-add start dates too

**Disadvantages**:
- ❌ Requires development skills
- ❌ Asana API authentication setup
- ❌ Overkill for one-time template creation
- ❌ Still requires manual work for future updates

### Solution 3: Use Asana API to Build Template from Scratch

**Approach**: Programmatically create entire template using Asana API

**Steps**:

1. Write comprehensive script that:
   - Creates project
   - Creates all sections
   - Creates all tasks with dates, assignees, custom fields
   - Creates all subtasks
   - Creates all dependencies
   - Sets up automations

2. Run script to generate template project

3. Convert to template

**Total Time**: ~8-10 hours (full script development + testing)

**Advantages**:
- ✅ Fully automated and reproducible
- ✅ Can regenerate template at any time
- ✅ Version-controlled source of truth
- ✅ Useful if template changes frequently

**Disadvantages**:
- ❌ Significant development effort
- ❌ Overkill for stable template
- ❌ Requires Asana API expertise
- ❌ Maintenance burden if Asana API changes

---

## Recommended Path Forward ⭐

**Use Solution 1: Manual Completion of Project 1**

**Rationale**:
1. **Fastest path to working template** (~45 minutes vs hours)
2. **Leverages existing work** (CSV import already 90% complete)
3. **One-time effort** (once template is created, all future modules inherit dependencies)
4. **Low technical risk** (no scripts to maintain)
5. **Template duplication is native Asana feature** (very reliable)

**Specific Action Plan**:

### Phase 1: Clean Up Project 1 (10 minutes)

1. Open Project 1211626875246589
2. Delete empty placeholder tasks (search for name="")
3. Verify all sections and tasks are present

### Phase 2: Add Start Dates (15 minutes)

Switch to Timeline view and add start dates for:

| Task Type | Start Date Calculation | Count |
|-----------|----------------------|-------|
| Kick off meeting | Due date - 4 days | 1 |
| Initiation tasks | Due date - duration | 4 |
| Week storyboarding tasks | Due date - 10 days (Week 1) or 5 days (Weeks 2-8) | 8 |
| Storyboard subtasks | Staggered within parent duration | 32 |
| Build tasks | Due date - 5 days | 8 |
| Review tasks | Due date - 5 days | 3 |
| Finalization tasks | Due date - duration | 5 |
| Go live | Same as due date | 1 |

**Shortcut**: Can bulk-adjust by selecting multiple tasks in same section and setting same start date offset

### Phase 3: Add Dependencies (20 minutes)

Follow this dependency creation sequence (grouped by priority):

**Critical Path Dependencies** (Must have - 15 dependencies):
```
1. Kick off meeting → MPD Draft
2. MPD Draft → MPD Finalised
3. MPD Finalised → Week 1 - Storyboarding
4. MPD review → Week 1 - Storyboarding (parallel with MPD Finalised)
5. Week 1 - Storyboard Final draft agreed → Week 1 - Build
6. Week 2 - Storyboard Final draft agreed → Week 2 - Build
7. Week 3 - Storyboard Final draft agreed → Week 3 - Build
8. Week 4 - Storyboard Final draft agreed → Week 4 - Build
9. Week 5 - Storyboard Final draft agreed → Week 5 - Build
10. Week 6 - Storyboard Final draft agreed → Week 6 - Build
11. Week 7 - Storyboard Final draft agreed → Week 7 - Build
12. Week 8 - Storyboard Final draft agreed → Week 8 - Build
13. Week 2 - Build → Week 1 and 2 review
14. Week 8 - Build → Weeks 3 to 8 review
15. Corrections → Ready for launch → Go live
```

**Cascading Build Dependencies** (Parallel work enablement - 7 dependencies):
```
16. Week 1 - Build → Week 2 - Storyboarding (Week 2 can start while Week 1 builds)
17. Week 2 - Build → Week 3 - Storyboarding
18. Week 3 - Build → Week 4 - Storyboarding
19. Week 4 - Build → Week 5 - Storyboarding
20. Week 5 - Build → Week 6 - Storyboarding
21. Week 6 - Build → Week 7 - Storyboarding
22. Week 7 - Build → Week 8 - Storyboarding
```

**Within-Task Dependencies** (Subtask flow - 16 dependencies):
```
For Week 1:
23. Week 1 - Storyboard Initial LD Draft → Week 1 - Edit
24. Week 1 - Storyboard SME Scripts Draft → Week 1 - Edit
25. Week 1 - Edit → Week 1 - Storyboard Final draft agreed

For Weeks 2-8 (same pattern × 7 weeks):
26-40. [LD Draft + SME Draft] → Edit → Final draft agreed
```

**Finalization Dependencies** (5 dependencies):
```
41. Week 8 - Build → Film shoot - second batch
42. Week 4 - Build → Film shoot - first batch
43. Film shoot - second batch → Proofreading
44. Weeks 3 to 8 review → Corrections
45. Proofreading → Corrections (parallel with review)
```

**Total**: 45 dependency relationships

### Phase 4: Convert to Template (2 minutes)

1. Project Settings → Convert to Template
2. Name: "Module Development Template"
3. Description: "17-18 week module development workflow with 8 weeks of content creation, batched reviews, and cascading builds"
4. Save

### Phase 5: Test Template (10 minutes)

1. Create new project from template: "TEST Module XYZ"
2. Verify all sections, tasks, subtasks copied
3. Verify all dependencies copied
4. Try to complete "Week 1 - Build" before "Week 1 - Storyboard" (should warn/block)
5. Check Timeline view shows correct Gantt chart with start/due dates
6. Delete test project

**Total Time**: ~57 minutes

---

## Alternative: Fix Project 2 (AI-Assisted Import)

If you prefer to fix the AI-assisted import instead (has start dates but lost subtasks):

**Steps**:

1. **Manually recreate subtask relationships** (~30 minutes):
   - For each week section:
     - Find "Week N - Storyboarding" task
     - Find its 4 component tasks (LD Draft, SME Draft, Edit, Final draft)
     - Convert component tasks to subtasks by dragging them onto parent in List view
   - Repeat for Initiation section (MPD parent task with 4 subtasks)

2. **Add dependencies** (same as Solution 1 Phase 3)

3. **Convert to template**

**Total Time**: ~50 minutes (similar to Solution 1)

**Trade-off**: You'd preserve start dates but need to manually recreate all subtask relationships

---

## Quick Comparison of Paths

| Approach | Time | Technical Skill | Repeatability | Future Maintenance |
|----------|------|-----------------|---------------|-------------------|
| **Fix Project 1** | **~57 min** | **Low** | **High (template)** | **None** |
| Fix Project 2 | ~50 min | Low | High (template) | None |
| API Script | ~3 hours | Medium-High | Very High | Low-Medium |
| Full API Build | ~10 hours | High | Very High | Medium |

---

## Immediate Next Steps

**Recommendation**: Proceed with **Solution 1 - Fix Project 1**

1. **Andrew decision**: Confirm approach (manual completion of Project 1)
2. **Schedule 1-hour session** to complete manual work
3. **Follow Phase 1-5 sequence** above
4. **Test thoroughly** with real module before Tuesday meeting
5. **Prepare demo** showing:
   - Template structure
   - Dependency enforcement
   - Timeline view
   - Duplication process
   - Custom field usage

**For Tuesday Meeting**:
- Show completed template in Timeline view
- Demonstrate creating new module from template
- Show dependency blocking behavior
- Walk through resource allocation in Workload view
- Discuss automation rules to add post-template creation

---

## Long-Term Considerations

### Option 1: Keep Template Stable
- **Effort**: None ongoing
- **Updates**: Manual if needed (rare)
- **Best for**: Stable workflow that won't change often

### Option 2: Invest in API Automation
- **Effort**: 10 hours upfront + occasional updates
- **Updates**: Regenerate template from script
- **Best for**: Frequently changing workflow or multiple template variants

**Recommendation**: Start with manual template (Option 1), only invest in API automation if:
- Template needs frequent significant updates
- Creating multiple template variants for different module types
- Integrating with other systems (Clockify, CRM, etc.)

---

## Risk Assessment

### Risks of Manual Approach (Solution 1)

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Missed dependency | Medium | Medium | Use specification checklist, test thoroughly |
| Wrong start dates | Low | Low | Copy from CSV/specification, verify in Timeline |
| Template duplication issues | Low | High | Test before rolling out, Asana feature is stable |
| Future template changes | Low | Low | Changes are infrequent, manual update acceptable |

### Risks of Automated Approach (Solutions 2-3)

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| API authentication issues | Medium | High | Use personal access token, test thoroughly |
| Script bugs | High | High | Extensive testing, manual verification |
| Asana API changes | Medium | Medium | Monitor Asana API changelog, update script |
| Over-engineering | High | Medium | Only automate if truly needed |

---

## Conclusion

**Recommended Path**: **Manual completion of Project 1 (Direct CSV Import)**

**Rationale**:
- ✅ Fastest time to working template (~1 hour)
- ✅ Lowest technical risk
- ✅ Leverages Asana's native template system (very stable)
- ✅ No ongoing maintenance burden
- ✅ Ready for Tuesday demo

**Success Criteria**:
- [ ] All 65+ tasks have start and due dates
- [ ] All 45 dependency relationships created
- [ ] All subtask relationships preserved
- [ ] Template duplication creates identical structure
- [ ] Dependencies enforce workflow sequence
- [ ] Timeline view shows accurate Gantt chart
- [ ] No empty placeholder tasks remain

**Estimated Completion**: Within 1 hour focused session

**Ready for**: Tuesday meeting demo and production use

