# Module Development Template CSV Import Instructions

**File**: `Module_Development_Template_IMPORT.csv`
**Created**: 2025-10-13
**Purpose**: Ready-to-import Asana CSV file for complete Module Development Template

---

## Overview

This CSV file contains the complete Module Development Template structure with:
- **72+ tasks and subtasks** mapped from the original spreadsheet template
- **11 sections**: Initiation & Planning, Weeks 1-8, Finalization, Launch
- **Complete dependency chains** ensuring proper workflow sequencing
- **Calculated dates** based on Launch Date: 2026-01-05 (example timeline)
- **All custom fields** populated with realistic values
- **Estimated time** in hours for all tasks (native Asana time tracking)
- **Resource assignments** with placeholder emails (update with actual team)

---

## What's Included

### Task Structure

| Section | Tasks | Subtasks | Key Features |
|---------|-------|----------|---------------|
| **Instructions** | 1 | 0 | Template usage guide |
| **Initiation & Planning** | 3 | 5 | Kickoff, MPD development, review |
| **Week 1** | 2 | 4 | Extended 10-day storyboarding + build + review |
| **Weeks 2-8** | 14 | 28 | Standard 5-day storyboarding + cascading builds |
| **Finalization** | 5 | 0 | Film shoots, proofreading, reviews, corrections |
| **Launch** | 1 | 0 | Go live milestone |
| **Total** | **26 tasks** | **37 subtasks** | **63 work items** |

### Dependencies Configured

All critical dependencies are pre-configured using task names:

**Initiation Chain:**
```
Kick off meeting → MPD Draft → MPD Finalised → Week 1 Storyboarding
                                              ↗ MPD review →
```

**Week 1 (Extended):**
```
LD Draft (5d) ╮
              ├→ Edit (3d) → Final draft (2d) → Build (5d) → Week 1-2 Review
SME Draft (5d) ╯                                              (after Week 2 Build)
```

**Weeks 2-8 (Standard pattern):**
```
LD Draft (2d) ╮
              ├→ Edit (2d) → Final draft (1d) → Build (5d)
SME Draft (2d) ╯
```

**Cascading Builds:**
- Week N Build can start while Week N+1 storyboarding happens
- Creates efficient resource pipeline (LD+SME on new week while LT builds previous week)

**Finalization Chain:**
```
Week 8 Build → Film shoot 2 → Proofreading → Corrections → Ready for Launch → Go Live
            → Weeks 3-8 review →
```

### Custom Fields Populated

All custom fields that you've created in Asana are included in the CSV:

| Field Category | Fields | Sample Values |
|---------------|--------|---------------|
| **Project Metadata** | Module Code, Client Name, Programme Name | (blank - fill when creating real module) |
| **Key Dates** | Launch Date, Go Live Date | 2026-01-05, 2026-03-11 |
| **People** | Module Author, Learning Designer, LT, Senior LD Reviewer | Placeholder emails (replace with actual) |
| **Status Tracking** | Module Status, QA Status, Blocker Status | Planning, Not Started, None |
| **Content** | Content Type, Week Number, Phase | (varies by task) |
| **Resources** | LDS Resource, Client Resource, Offshore Location | LD/LT/SLD, SME/AR/PL, UK |
| **Time** | Estimated time (hours) | 8-48 hours per task |
| **Special** | Media Requirements, Review Batch | Standard/Film Shoot Required, Weeks 1-2/3-8 |

### Dates Calculated

All dates calculated from **Launch Date: 2026-01-05** (Monday):

| Milestone | Date | Days Before Launch |
|-----------|------|-------------------|
| Kickoff | 2025-09-15 | -112 days |
| MPD Draft | 2025-09-22 | -105 days |
| Week 1 Storyboard | 2025-10-06 | -91 days |
| Week 1 Build | 2025-10-20 | -76 days |
| Week 8 Build | 2025-12-13 | -23 days |
| Corrections complete | 2026-01-02 | -3 days |
| **Ready for Launch** | **2026-01-05** | **0 days** |
| **Go Live** | **2026-03-11** | **+66 days** |

Total timeline: **178 days** (26 weeks) from kickoff to go live.

### Estimated Time Summary

Total effort per role (approximate):

| Role | Estimated Hours | Key Activities |
|------|----------------|----------------|
| **Learning Designer** | 440 hours | Storyboarding, editing, corrections (8 weeks × 40h + planning + finalization) |
| **Learning Technologist** | 360 hours | Building 8 weeks in Moodle (8 × 40h + setup + go live) |
| **SME** | 360 hours | Content creation, scripts (8 weeks × 40h + planning) |
| **Academic Reviewer** | 44 hours | Two batched reviews (20h + 24h) |
| **Digital Learning Team** | 88 hours | Two film shoot batches (48h + 40h) |
| **Editorial Team** | 40 hours | Proofreading finalization |
| **Senior LD Reviewer** | 8 hours | Final sign-off |
| **Programme Leader** | 8 hours | Assessment approval (initiation) |
| **Librarian** | 16 hours | Reading list review (initiation) |

**Total Project Effort**: ~1,364 hours across all roles

---

## How to Use This CSV

### Before Import

1. **Review the CSV** in spreadsheet software (Excel, Google Sheets)
2. **Update placeholder emails** to match your Asana team members:
   - `ld@example.com` → Actual Learning Designer email
   - `lt@example.com` → Actual Learning Technologist email
   - `sme@example.com` → Actual SME/Module Author email
   - `reviewer@example.com` → Actual Academic Reviewer email
   - `sld@example.com` → Actual Senior LD email
   - `media@example.com` → Actual Digital Learning Team email
   - `editor@example.com` → Actual Editorial Team email

3. **Verify custom fields exist** in your Asana workspace:
   - Module Code, Client Name, Programme Name (text)
   - Launch Date, Go Live Date (date)
   - Module Author, Learning Designer, Learning Technologist, Senior LD Reviewer (person)
   - Module Status, QA Status, Blocker Status, Media Requirements, Review Batch (single select)
   - Content Type (multi select)
   - Week Number (number)
   - Phase (single select)
   - LDS Resource, Client Resource (text)
   - Offshore Location (single select)
   - Estimated time (native Asana field - should already exist)

### Import Process

1. **Create new Asana project** or use existing one
2. **Import CSV**:
   - Click project dropdown → "Import" → "CSV"
   - Upload `Module_Development_Template_IMPORT.csv`
   - Map columns to Asana fields (should auto-detect)
   - Confirm import

3. **Asana will automatically**:
   - Create all sections
   - Create all tasks and subtasks
   - Set up all dependencies
   - Assign resources
   - Populate custom fields
   - Set start and due dates

### After Import

1. **Switch to Timeline View** to see Gantt chart
2. **Verify dependencies** are showing correctly
3. **Check resource assignments** in Workload view
4. **Update any flexible elements**:
   - Film shoot tasks (if not needed, delete or mark N/A)
   - Holiday date conflicts (e.g., Christmas week review)
   - 10-week buffer (adjust Go Live date if needed)

5. **Save as Template**:
   - Once satisfied, convert project to Asana template
   - Future modules can be created from this template
   - Only need to update Launch Date and custom fields

---

## Flexible Elements (Noted in Task Descriptions)

These elements are documented as flexible based on your guidance:

### Timing Flexibility

1. **10-Week Buffer**: Go Live is 66 days after Ready for Launch
   - **Purpose**: Academic calendar alignment, client approval time
   - **Adjust**: Change "Go live" due date to match client's term start

2. **Week 1 Extended Time**: 10 days vs 5 days for other weeks
   - **Purpose**: Pattern establishment, LD-SME relationship building
   - **Adjust**: Can standardize to 5 days if team is experienced

3. **Holiday Scheduling**: Weeks 3-8 review falls on Christmas week (Dec 22-26)
   - **Warning**: Note in task description
   - **Adjust**: Shift timeline to avoid holidays for specific modules

4. **Film Shoots**: Two batches integrated into timeline
   - **Purpose**: Video content creation for media-rich modules
   - **Adjust**: Delete or mark N/A if module doesn't require film shoots
   - **Control**: "Media Requirements" custom field can indicate if needed

### Review Batching

- **Weeks 1-2**: Reviewed together (5 days for 2 weeks)
- **Weeks 3-8**: Reviewed together (5 days for 6 weeks)
- **Flexible**: Can adjust batching based on Academic Reviewer availability and preferences

### Resource Allocation

- **LD vs LT**: "Corrections" task shows "Learning Designer" but may need LT for technical fixes
  - Assign both if corrections span content and technical issues

- **Offshore**: "Offshore Location" field defaults to UK
  - Update for roles based offshore (India/South Africa)
  - Helps with capacity planning and timezone considerations

---

## Custom Field Reference

### Module Status Options
- Planning
- In Development
- Build
- QA
- Ready
- Launched
- Archived

### Phase Options
- Initiation
- Development
- Build
- Finalization
- Launch

### QA Status Options
- Not Started
- In Review
- Changes Requested
- Approved

### Blocker Status Options
- None
- Waiting on SME
- Waiting on Client
- Technical Issue
- Resource Gap

### Media Requirements Options
- None
- Standard
- Film Shoot Required
- Audio Only

### Review Batch Options
- Weeks 1-2
- Weeks 3-8
- N/A

### Offshore Location Options
- UK
- India
- South Africa

---

## Testing Recommendations

### After Import, Test:

1. **Timeline View**:
   - All tasks show in correct sequence
   - Dependencies display as arrows
   - Critical path highlights correctly
   - Dates span Sep 2025 - Mar 2026

2. **Dependency Flow**:
   - Try to complete Week 2 Build before Week 1 Build (should warn/block)
   - Complete Kick off meeting → see MPD Draft unblock
   - Verify cascading build pattern works

3. **Workload View**:
   - Filter by Learning Designer → see storyboarding tasks
   - Filter by Learning Technologist → see build tasks cascading
   - Check for any over-allocation warnings

4. **Custom Fields**:
   - Filter by Phase: Development → see Weeks 1-8 storyboarding
   - Filter by Review Batch: Weeks 1-2 → see Week 1-2 review task
   - Sort by Week Number → verify 1-8 ordering

5. **Time Tracking**:
   - Click on any task → "Estimated time" should show hours
   - Start timer on a task → verify time tracking works
   - Generate time report → verify estimated vs actual tracking

---

## Next Steps After Import

1. **Create a Template**: Convert the imported project to an Asana template
2. **Test Creation**: Create a test module from the template
3. **Update Launch Date**: Enter a new Launch Date custom field value
4. **Verify Recalculation**: Check if all dates adjust (may need manual adjustment or Asana automation)
5. **Set Up Automation**: Configure automation rules for notifications and status updates
6. **Train Team**: Walk through the template with LD, LT, and SLD
7. **Pilot**: Use template for first real module and gather feedback
8. **Iterate**: Refine based on pilot experience

---

## Troubleshooting

### Common Issues

**Dependencies Don't Import**:
- Asana may require exact task name matches (case-sensitive)
- Verify "Blocked By" and "Blocking" columns use exact task names from "Name" column
- Re-import if needed after fixing task name mismatches

**Custom Fields Don't Populate**:
- Custom fields must exist in workspace BEFORE import
- Field names in CSV must exactly match Asana custom field names
- Check field types match (text, date, single select, etc.)

**Subtasks Don't Nest**:
- "Parent task" column must exactly match parent task name
- Subtasks must come AFTER parent task in CSV
- If subtasks appear as top-level tasks, re-import with corrected parent names

**Dates Look Wrong**:
- Dates are in YYYY-MM-DD format (ISO 8601)
- Check your Asana date format preferences match
- Weekend days are included in calculations (not just business days)

**Assignees Don't Show**:
- Email addresses in CSV must match Asana user emails exactly
- Users must have access to the project
- For guests (like SME), invite them to project first before import

---

## Support & Feedback

For questions or issues with the template:
1. Review the **Asana_Module_Development_Template_Spec_v2.0.md** for detailed specifications
2. Check the **Template_Analysis_-_Actual_Structure.md** for original spreadsheet mapping
3. Consult Andrew for business logic questions (timing, resource allocation, process)
4. Contact Asana support for import technical issues

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-10-13 | Initial CSV generated from template specification v2.0 |

---

**Status**: Ready for Andrew's review and feedback
**Next Action**: Import into Asana test workspace for validation
**Tuesday Meeting**: Can demo imported template if approved
