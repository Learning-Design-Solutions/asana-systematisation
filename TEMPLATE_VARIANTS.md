# Template Variants Guide - Creating Specialized Module Templates

## Introduction

The base **Asana Module Development Template** is designed for standard 8-week modules with a 17-18 week development timeline. However, Learning Design Solutions may need specialized variants for different module types, client requirements, or delivery models.

This guide shows you how to create template variants efficiently, leveraging the investment already made in the base template's 52 dependency relationships.

### When to Create Variants

**Use the base template when**:
- Standard 8-week module structure
- Typical 17-18 week development timeline
- Standard review process (batched Weeks 1-2, then Weeks 3-8)
- Normal filming requirements (two batches)

**Create a variant when**:
- **Different module length**: 12-week modules, 6-week modules, micro-credentials
- **Different timeline**: Accelerated (5-day weeks), extended (with additional review cycles)
- **Different structure**: Skills-based modules, lab-based content, pure theory
- **Different filming**: No film shoots, continuous filming, pre-recorded content integration
- **Client-specific**: Repeated patterns for specific client relationships

### Why Create Variants Instead of Modifying Base Template

**Benefits of variants**:
- Preserve base template for standard modules
- Optimize for specific use cases
- Reduce setup time for common variations
- Maintain consistency within variant category
- Enable comparative analysis across variant types

**When NOT to create variants**:
- One-off modifications for single module (modify individual project)
- Testing new approaches (use project copy, not variant template)
- Minor differences in assignees or descriptions (handle in base template)

---

## Strategy 1: Duplicate Template (Fastest - 5 minutes per variant)

**Best for**: Similar 8-week structures with minor variations
**Time**: 5 minutes per variant
**Complexity**: Low
**Preserves**: All 52 dependencies automatically

### When to Use This Strategy

**Ideal scenarios**:
- 8-week module with different filming approach (e.g., no film shoots variant)
- Same structure but different review batching (e.g., 3 review batches instead of 2)
- Client-specific customization (e.g., Walbrook-specific task descriptions)
- Different resource allocation patterns (e.g., offshore LT variant)

**Not suitable for**:
- Significantly different module lengths (12-week, 6-week)
- Completely different workflow structures
- Different number of phases or sections

### Process Steps

**Step 1: Duplicate Base Template Project**
1. Open the base Asana Module Development Template
2. Project Settings → Duplicate project
3. Name: `[Variant Name] Module Template`
   Example: `12-Week Module Template`
4. **CRITICAL**: Check "Duplicate task dependencies"
5. Create project

**Step 2: Modify Structure**
1. Add/remove sections as needed
2. Add/remove tasks within sections
3. Modify task descriptions for variant-specific guidance
4. Update custom field options if needed

**Step 3: Adjust Dependencies**
1. Dependencies from base template copy automatically
2. Add dependencies for new tasks (manual or MCP)
3. Remove dependencies for deleted tasks (automatic when task deleted)
4. Test dependency chain in Timeline view

**Step 4: Update Timeline Calculations**
1. Adjust relative date offsets if timeline changes
2. Test with sample Launch Date
3. Verify cascading build pattern still works
4. Check for holiday conflicts

**Step 5: Convert to Template**
1. Project Settings → Convert to Template
2. Add template description
3. Set template category
4. Test duplication with dummy project

### Example: No Film Shoots Variant

**Modifications needed**:
- Delete "Film shoot - first batch" task
- Delete "Film shoot - second batch" task
- Remove "Media Requirements" custom field option
- Update task descriptions removing filming references
- Adjust Timeline: Remove 11 days from timeline (6 + 5 days)

**Time**: 5 minutes to duplicate, delete 2 tasks, update descriptions, and convert to template

**Dependencies**: Automatically adjust when film shoot tasks deleted

---

## Strategy 2: Repeat API Process (Comprehensive - 30 minutes per variant)

**Best for**: Significantly different structures (12-week modules, different phases)
**Time**: 30 minutes per variant
**Complexity**: Medium
**Control**: Complete control over all dependencies

### When to Use This Strategy

**Ideal scenarios**:
- 12-week modules (4 additional weeks of content)
- 6-week modules (2 fewer weeks of content)
- Completely different phase structures
- Different dependency patterns (e.g., no cascading builds)
- Experimental workflow approaches

**Not suitable for**:
- Minor variations on 8-week structure (use Strategy 1)
- One-time custom projects (modify individual project)

### Process Steps

**Step 1: Create Variant Specification**
1. Copy `Asana_Module_Development_Template_Spec_v2.md`
2. Rename: `[Variant_Name]_Template_Spec.md`
3. Modify sections, tasks, durations for variant
4. Document new dependency relationships
5. Calculate new relative date offsets

**Step 2: Update Dependency Mapping**
1. Copy `dependency_mapping.json`
2. Rename: `dependency_mapping_[variant].json`
3. Update task names for variant structure
4. Add/remove dependencies as needed
5. Organize by type (Critical Path, Cascading, Within-Task, Finalization)

**Example for 12-week module**:
```json
{
  "critical_path": [
    {"source": "Kick off meeting", "target": "MPD Draft"},
    {"source": "MPD review", "target": "Week 1 - Storyboarding"},
    {"source": "Week 12 - Build", "target": "Weeks 9-12 review"}
  ],
  "cascading_build": [
    {"source": "Week 9 - Build", "target": "Week 10 - Storyboarding"},
    {"source": "Week 10 - Build", "target": "Week 11 - Storyboarding"},
    {"source": "Week 11 - Build", "target": "Week 12 - Storyboarding"}
  ]
}
```

**Step 3: Create Base Project Structure**
Option A: Import from CSV (if you have CSV template)
Option B: Duplicate base template and modify
Option C: Create manually in Asana

**Step 4: Execute MCP API Calls**
Use same approach as original implementation:

```
1. Search for tasks in new project
2. Build task name → GID mapping
3. Apply dependencies using asana_add_task_dependencies
4. Verify dependencies created
5. Save task_gid_mapping_[variant].json
```

**Step 5: Set Relative Dates**
1. Calculate new relative date offsets
2. Apply to all tasks
3. Test with sample Launch Date
4. Verify timeline duration matches specification

**Step 6: Convert to Template**
1. Test thoroughly with dummy project
2. Project Settings → Convert to Template
3. Document variant-specific setup instructions

### Example: 12-Week Module Variant

**New structure requirements**:
- 4 additional week sections (Weeks 9-12)
- 12 additional storyboarding tasks
- 12 additional build tasks
- Additional review batch (Weeks 9-12)
- Extended timeline (+4 weeks)

**Dependency additions needed**:
- 4 new cascading build dependencies (Weeks 9-12)
- 16 new within-task dependencies (4 weeks × 4 subtasks)
- 1 new review dependency (Weeks 9-12 review)

**Total dependencies**: 52 (base) + 21 (new) = 73 dependencies

**Time breakdown**:
- Specification update: 10 minutes
- Dependency mapping update: 5 minutes
- Project structure creation: 5 minutes
- MCP API execution: 8 minutes
- Verification: 2 minutes
- **Total**: 30 minutes

---

## Strategy 3: Hybrid Approach (Efficient - 15 minutes per variant)

**Best for**: Multiple variants with shared patterns
**Time**: 15 minutes per variant
**Complexity**: Medium
**Flexibility**: Balance between speed and control

### When to Use This Strategy

**Ideal scenarios**:
- Creating 3+ variants that share base structure
- Variants with common patterns but different specifics
- Need for both speed and structural control
- Incremental variant development

**Example use cases**:
- Standard 8-week, Accelerated 8-week, Extended 8-week (same weeks, different durations)
- Theory-heavy, Skills-heavy, Lab-based (same structure, different task emphasis)
- Client A, Client B, Client C variants (same process, different descriptions)

### Process Steps

**Step 1: Create Base Variant via API** (Strategy 2)
1. Use full API process for first variant
2. Document all structural changes
3. Save dependency mapping for variant family
4. Convert to template

**Step 2: Duplicate and Modify for Subsequent Variants** (Strategy 1)
1. Duplicate the base variant
2. Modify task descriptions for specific variant
3. Add/remove specific tasks as needed
4. Dependencies copy automatically

**Step 3: API for Variant-Specific Additions**
1. For new tasks unique to this variant
2. Use MCP to add specific dependencies
3. Update variant-specific task mappings
4. Verify in Timeline view

### Example: Module Type Variants

**Scenario**: Create 3 variants for different content types
- Theory-Heavy Module
- Skills-Based Module
- Lab-Based Module

**Shared structure** (use as base):
- Same 8-week structure
- Same initiation and planning
- Same review process
- Same finalization

**Variant-specific differences**:
- Task descriptions emphasize different deliverables
- Different media requirements
- Different assessment types
- Different filming approaches

**Process**:
1. Create "Theory-Heavy Module Template" via API (30 min)
2. Duplicate to create "Skills-Based Module Template" (5 min)
3. Modify task descriptions for skills focus (5 min)
4. Add skills-specific tasks (practice sessions, labs) (5 min)
5. API to add new dependencies for new tasks (5 min)
6. Repeat for "Lab-Based Module Template" (15 min)

**Total time**: 30 + 15 + 15 = 60 minutes for 3 variants
**Time per variant**: 20 minutes average

---

## Common Variant Types

### 12-Week Module Variant

**Structural changes**:
- Add Weeks 9-12 sections (4 new sections)
- Add Week 9-12 storyboarding tasks (4 tasks × 4 subtasks = 16 new subtasks)
- Add Week 9-12 build tasks (4 new tasks)
- Add "Weeks 9-12 review" task in Finalization
- Possible third film shoot batch

**Dependency additions**:
- 4 cascading build dependencies (Weeks 9-12)
- 16 within-task dependencies (storyboarding workflow)
- 1 review dependency (Weeks 9-12 → Corrections)

**Timeline adjustment**:
- Add 20 days to development phase (4 weeks × 5 days)
- Adjust relative date offsets for all downstream tasks
- New total: 132 days to "Ready for Launch" (vs 112 days)

**Recommended strategy**: Strategy 2 (API process)

### Accelerated Module (5-Day Weeks)

**Structural changes**:
- Same 8-week structure
- Reduce all storyboarding from 5 days to 3 days (Weeks 2-8)
- Reduce all builds from 5 days to 3 days
- Reduce reviews from 5 days to 3 days each

**No dependency changes**: Same 52 dependencies

**Timeline adjustment**:
- Reduce ~20 days from total timeline
- New total: ~92 days to "Ready for Launch"

**Recommended strategy**: Strategy 1 (duplicate template)

### Micro-Credential (4-Week Module)

**Structural changes**:
- Remove Weeks 5-8 sections (4 sections)
- Remove film shoot - second batch
- Single review batch (all weeks together)
- Condensed finalization

**Dependency removals**:
- Remove cascading build for Weeks 5-8 (4 dependencies)
- Remove within-task for Weeks 5-8 (16 dependencies)
- Remove Weeks 3-8 review dependency

**Timeline adjustment**:
- Remove 20 days from development phase
- New total: ~92 days to "Ready for Launch"

**Recommended strategy**: Strategy 1 (duplicate template) or Strategy 2 if creating multiple micro-credential variants

---

## Structural Changes to Consider

### Section Modifications

**Adding sections**:
- Additional weeks (Weeks 9-12 for longer modules)
- Specialized phases (Mid-module review, Client feedback cycle)
- Quality gates (Additional QA checkpoints)

**Removing sections**:
- Weeks 6-8 for shorter modules
- Film shoots for theory-only modules
- Specific review batches if combining

**Renaming sections**:
- Client-specific terminology
- Different content organization (Modules instead of Weeks)
- Phase-based instead of time-based

### Task Additions/Removals

**Common additions**:
- Additional review cycles (mid-module, pre-launch)
- Specialized media tasks (podcast recording, infographic creation)
- Client approval gates (Programme Leader sign-off points)
- Integration tasks (LMS migration, third-party tool setup)

**Common removals**:
- Film shoots (for text-based modules)
- Certain review batches (combining or eliminating)
- Reading list tasks (for non-academic modules)
- Assessment tasks (for non-credit modules)

### Dependency Adjustments

**When adding dependencies**:
- New quality gates must block downstream work
- Client approvals should block next phase
- Media creation should block builds that embed media
- External integrations should block go-live

**When removing dependencies**:
- Ensure workflow still enforced
- Don't create opportunities for out-of-order work
- Maintain quality gate coverage
- Preserve critical path integrity

**When modifying dependencies**:
- Document WHY the change improves workflow
- Test with project copy first
- Verify cascading build pattern preserved (if applicable)
- Check Timeline view for logic errors

### Custom Field Updates

**Variant-specific fields to add**:
- Module Type (Theory/Skills/Lab/Hybrid)
- Filming Approach (Studio/Loom/AI/None)
- Review Intensity (Standard/Enhanced/Light)
- Client Category (Enterprise/Standard/Basic)

**Fields to remove**:
- Media Requirements (if no filming in variant)
- Review Batch (if different batching approach)
- Offshore Location (if all UK-based variant)

**Fields to modify**:
- Module Status options (variant-specific phases)
- QA Status levels (variant-specific quality gates)
- Phase options (different phase names)

---

## Technical Notes

### Dependency Mapping JSON Format

All variant dependency mappings should follow this structure for consistency:

```json
{
  "variant_metadata": {
    "name": "12-Week Module Variant",
    "created": "2025-10-20",
    "based_on": "Base 8-Week Template v2.0",
    "total_dependencies": 73,
    "module_length": "12 weeks",
    "development_timeline": "132 days"
  },
  "critical_path": [
    {"source": "Task A", "target": "Task B", "reason": "Sequential workflow"}
  ],
  "cascading_build": [
    {"source": "Week N - Build", "target": "Week N+1 - Storyboarding"}
  ],
  "within_task": [
    {"source": "Subtask 1", "target": "Subtask 2"}
  ],
  "finalization": [
    {"source": "Final QA", "target": "Ready for Launch"}
  ]
}
```

### GID Patterns for Tracking

When creating variants, document GID patterns for traceability:

**Base template GIDs**: 1211627678168XXX
**Variant 1 GIDs**: (will be different when created)
**Variant 2 GIDs**: (will be different when created)

**Tracking approach**:
- Create `task_gid_mapping_[variant].json` for each variant
- Store in version control
- Reference when updating variants
- Use for bulk operations

### Version Control Strategy

**Recommended structure**:
```
/asana-systematisation/
├── base_template/
│   ├── Asana_Module_Development_Template_Spec_v2.md
│   ├── dependency_mapping.json
│   └── task_gid_mapping.json
├── variants/
│   ├── 12_week_module/
│   │   ├── spec_12week.md
│   │   ├── dependency_mapping_12week.json
│   │   └── task_gid_mapping_12week.json
│   ├── accelerated_module/
│   │   ├── spec_accelerated.md
│   │   └── dependency_mapping_accelerated.json
│   └── micro_credential/
│       ├── spec_micro.md
│       └── dependency_mapping_micro.json
└── documentation/
    ├── QUICKSTART.md
    ├── FAQ.md
    └── TEMPLATE_VARIANTS.md (this file)
```

**Benefits**:
- Clear organization by variant
- Easy comparison across variants
- Version history for each variant
- Reusable specifications

### Naming Conventions

**Template names**:
- Pattern: `[Type] Module Template - [Variant]`
- Examples:
  - "8-Week Module Template - Standard"
  - "12-Week Module Template - Extended"
  - "8-Week Module Template - No Film Shoots"
  - "4-Week Module Template - Micro-Credential"

**Project names** (when using templates):
- Pattern: `[Client] - [Programme] - [Module Code]`
- Example: "Walbrook - MBA Marketing - MKT101"

**Custom field naming**:
- Be consistent with base template where possible
- Prefix variant-specific fields: "[Variant] Field Name"
- Document any deviations from base template

---

## Variant Management Best Practices

### Before Creating a Variant

**Answer these questions**:
1. Will this variant be used 3+ times?
2. Are the structural differences significant?
3. Can't this be handled with base template customization?
4. Do we have specification for the variant structure?
5. Who will maintain this variant over time?

**If NO to questions 1-2**: Don't create variant, modify individual projects instead
**If YES to questions 1-4**: Proceed with variant creation

### During Variant Creation

**Documentation checklist**:
- [ ] Variant specification document created
- [ ] Dependency mapping JSON updated
- [ ] Structural changes documented
- [ ] Timeline calculations verified
- [ ] Task GID mapping saved
- [ ] Test project created from variant
- [ ] Variant-specific setup guide written

**Testing checklist**:
- [ ] Create dummy project from variant template
- [ ] Set sample Launch Date
- [ ] Verify all dates calculate correctly
- [ ] Test dependency enforcement (try completing out of order)
- [ ] Check Timeline view for logical flow
- [ ] Complete one full workflow simulation
- [ ] Delete test project after validation

### After Variant Creation

**Maintenance plan**:
- Assign variant owner (responsible for updates)
- Document update frequency (quarterly? annually?)
- Link to base template evolution (sync major changes)
- Track usage (how many projects created from variant)

**Knowledge transfer**:
- Train team on variant-specific differences
- Create variant-specific quick start guide
- Document common gotchas unique to variant
- Add variant to template selection decision tree

---

## Variant Selection Decision Tree

When starting a new module, choose the appropriate template:

```
New Module → What's the module length?
├─ 8 weeks → Standard structure?
│  ├─ Yes → Filming required?
│  │  ├─ Yes → Base Template (Standard 8-Week)
│  │  └─ No → No Film Shoots Variant
│  └─ No (accelerated) → Accelerated Module Variant
├─ 12 weeks → Extended Module Variant (12-Week)
├─ 4-6 weeks → Micro-Credential Variant
└─ Other → Create custom or use Strategy 2
```

---

## Example Variant Documentation

### Template Variant: No Film Shoots

**Use case**: Theory-heavy modules without video content

**Structural differences from base**:
- Removed: Film shoot - first batch (6 days)
- Removed: Film shoot - second batch (5 days)
- Removed: "Media Requirements" custom field
- Modified: Task descriptions removing filming references

**Timeline impact**:
- Reduced by 11 days (from film shoot removal)
- New total: 101 days to "Ready for Launch"

**Dependencies**:
- Removed 2 dependencies (film shoot dependencies)
- Maintained all 50 other dependencies

**Created using**: Strategy 1 (Duplicate Template)
**Creation time**: 5 minutes
**Maintained by**: Andrew
**Usage count**: 3 projects (as of Oct 2025)

**Setup instructions**:
1. Duplicate "No Film Shoots Module Template"
2. Set Launch Date (auto-calculates to 101 days back)
3. Assign team (no Digital Learning Team needed)
4. Document alternate media approach in project description
5. Proceed with standard workflow

---

## Summary of Strategies

| Strategy | Time | Best For | Complexity | Dependencies |
|----------|------|----------|------------|--------------|
| **1: Duplicate** | 5 min | Minor variations | Low | Copy automatically |
| **2: API Process** | 30 min | Major structural changes | Medium | Full control via MCP |
| **3: Hybrid** | 15 min | Multiple related variants | Medium | Mix of both |

**Recommendation for most teams**: Start with Strategy 1 for your first few variants. Once you understand the process and limitations, move to Strategy 2 or 3 for more complex needs.

---

## Resources and References

**Base Template Files**:
- `Asana_Module_Development_Template_Spec_v2.md` - Complete specification (1550 lines)
- `dependency_mapping.json` - All 52 base dependency definitions
- `task_gid_mapping.json` - Task name to GID mapping for base template

**API Implementation Guide**:
- `.serena/memories/asana_api_dependency_implementation.md` - Session summary from Oct 2025
- Documents MCP tool usage for dependency creation
- Time analysis and process documentation

**Related Documentation**:
- `QUICKSTART.md` - Getting started with base template
- `FAQ.md` - Common questions organized by category
- `API_Implementation_Summary.md` - Technical API process details

**Support**:
- Template owner: Andrew
- Technical support: Senior LD (Nicole)
- Process questions: Project team leads

---

## Document Version

**Version**: 1.0
**Last Updated**: October 2025
**Applies to**: Base Template v2.0 (with 52 API-created dependencies)
**Status**: Production guidance for variant creation

**Future updates planned**:
- Variant catalog as more variants created
- Decision tree expansion based on real-world variant usage
- Time estimates refinement based on actual variant creation experience
