# Asana Module Development Template - Frequently Asked Questions

## Template Usage

### Q: How do I create a new module from this template?
**A**: Follow these steps:
1. Open the Asana Module Development Template project
2. Click **Project Settings** → **Duplicate project**
3. Name it: `[Client Name] - [Programme Name] - [Module Code]`
4. **CRITICAL**: Check **Duplicate task dependencies** - this copies all 52 dependency relationships
5. Set the **Launch Date** custom field - all task dates auto-calculate from this
6. Assign team members to project-level custom fields
7. Start with the Kick off meeting task

**Time required**: Less than 10 minutes to set up a new module project.

### Q: What's the difference between "Ready for Launch" and "Go Live"?
**A**: These are two distinct milestones with different ownership:

**Ready for Launch** (Day 112):
- Andrew's deliverable and responsibility
- Module is complete, QA'd, and ready for student access
- All content built, reviewed, corrected, and proofread
- This is what the "Launch Date" custom field refers to

**Go Live** (Variable, typically +66 days):
- Client's decision and responsibility
- Actual date students access the module
- Controlled by academic calendar and programme scheduling
- Buffer varies - NOT always 66 days
- Depends on when programme development starts

**Key point**: Andrew delivers "Ready for Launch" on schedule. Client determines "Go Live" timing.

### Q: Can I modify the template structure for my module?
**A**: You can, but be careful:

**Safe modifications**:
- Adjust task assignees
- Update task descriptions with module-specific notes
- Add custom fields for project tracking
- Extend the launch buffer period

**Risky modifications**:
- Changing the 52 dependency relationships
- Removing review tasks or quality gates
- Shortening Week 1 from 10 days to 5 days (increases rework risk)
- Removing or reorganizing sections

**Recommendation**: Use the template as-is for your first module. After experiencing the full workflow, you'll better understand which modifications are safe and beneficial.

### Q: What happens if I change the Launch Date after starting work?
**A**: All task dates auto-recalculate:
- Asana's relative date feature recalculates all 72 task dates
- Dependencies remain intact
- Team members receive notifications about date changes
- Timeline view updates to show new schedule

**Best practice**: Set Launch Date accurately at project creation. Changes mid-project can disrupt team coordination.

---

## Filming Decisions

### Q: What filming options are available?
**A**: Three distinct options based on SME location and project needs:

**Option 1 - Physical Presence in London Studio**
- **When**: SME is physically in London or can travel to campus
- **Where**: Studio at SOAS or Walbrook campus
- **Quality**: Highest production value
- **Support**: Direct support from Digital Learning Team
- **Best for**: High-profile modules, demonstration-heavy content

**Option 2 - Remote Loom Recording**
- **When**: SME cannot come to campus or prefers remote recording
- **Tool**: Loom or similar screen recording software
- **Quality**: Professional but lower production overhead
- **Schedule**: More flexible, SME records on their own time
- **Best for**: Standard modules, interview/talking head content

**Option 3 - AI Avatars**
- **When**: No SME filming availability or preference for consistency
- **Tech**: AI-generated avatars for video content
- **Speed**: Fastest turnaround time
- **Consistency**: Uniform visual presentation across all videos
- **Best for**: Text-heavy content, consistent branding needs

**Decision timing**: Make this choice during project setup and document in Film Shoot task descriptions.

### Q: When should filming happen?
**A**: The template shows two recommended windows, but actual timing is flexible:

**Film Shoot - First Batch**: Nominally during Week 5 development (after Week 4 storyboard)
**Film Shoot - Second Batch**: Nominally at start of Finalization (after Week 8 storyboard)

**Key points**:
- Windows are recommendations to the client, not rigid deadlines
- Actual timing depends on SME availability and project needs
- Film shoots depend on **storyboard completion**, not build completion
- Coordinate with Digital Learning Team for studio booking (Option 1)

**Flexibility note from Andrew**: "These windows are nominal and recommended to the client - actual timing may vary based on SME availability and project needs."

### Q: What are the dependencies for film shoots?
**A**: **IMPORTANT CORRECTION**: Film shoots depend on **storyboards**, NOT builds.

**Correct dependency chain**:
- Film Shoot - First Batch depends on → Week 4 - Storyboard Final draft agreed
- Film Shoot - Second Batch depends on → Week 8 - Storyboard Final draft agreed

**Why storyboards, not builds?**
Filming requires completed scripts and content plans from storyboards. Moodle builds (technical implementation) are not needed for filming.

**Common error**: Assuming film shoots wait for builds. This creates unnecessary delays.

---

## Review Process

### Q: What should I expect from the Academic Reviewer?
**A**: **CRITICAL WARNING from Andrew**: "Academic Reviewer performance has been super inconsistent with current client, tends to be lighter touch than proofreading."

**What this means**:
- Review depth varies significantly
- May be less thorough than you expect
- Often lighter touch than professional proofreading
- Consistency is not guaranteed

**Recommended actions**:
1. Manage your expectations accordingly
2. Consider allocating supplemental internal QA resources
3. Budget for additional proofreading if needed
4. Don't assume comprehensive academic review coverage
5. Build in backup quality checks

**Impact on timeline**: You may need additional correction time if internal QA identifies issues Academic Reviewer missed.

### Q: Do I need supplemental QA beyond Academic Review?
**A**: **Yes, Andrew recommends this** given Academic Reviewer inconsistency.

**Options for supplemental QA**:
- Senior LD (Nicole) review at key milestones
- Internal peer review between LDs
- Additional proofreading pass (Editorial Team)
- Client Programme Leader spot-checks
- Learning Technologist content review during build

**When to add QA**:
- High-profile modules or programmes
- First module with new client (relationship building)
- Content with compliance requirements
- Modules with Academic Reviewer history of light touch

**Budget impact**: Plan 5-10 additional days for supplemental QA in your timeline.

### Q: Why are reviews batched (Weeks 1-2, then Weeks 3-8)?
**A**: Batched reviews improve efficiency and maintain consistency:

**Weeks 1-2 Review** (5 days for 2 weeks):
- Early feedback on module patterns and quality standards
- Establishes Academic Reviewer expectations
- Allows course correction before developing Weeks 3-8
- Smaller batch = faster turnaround

**Weeks 3-8 Review** (5 days for 6 weeks):
- Comprehensive review of remaining content
- Assesses consistency across full module
- Evaluates progression and module coherence
- Batching reduces Academic Reviewer context-switching

**Alternative approaches**: You could request 3 batches (Weeks 1-2, 3-5, 6-8), but this extends timeline and increases Academic Reviewer coordination overhead.

**Timing consideration**: The Weeks 3-8 review may fall during holidays (e.g., Christmas week in example timeline). Check Academic Reviewer availability when setting Launch Date.

---

## Week 1 Timing

### Q: Why does Week 1 get 10 days instead of 5?
**A**: Week 1 establishes critical patterns for the entire module. According to Andrew:

**What Week 1 establishes**:
- Patterns and processes for entire module development
- SME understanding of storyboard format and expectations
- LD-SME working relationship and communication patterns
- Quality standards and review cycles
- More back-and-forth expected in initial week

**Extended timeline breakdown**:
- Storyboard Initial LD Draft: 5 days (vs 2 days in Weeks 2-8)
- Storyboard SME Scripts Draft: 5 days (vs 2 days in Weeks 2-8)
- Edit: 3 days (vs 2 days in Weeks 2-8)
- Final Draft Agreed: 2 days (vs 1 day in Weeks 2-8)

**Investment rationale**: Time invested in Week 1 reduces rework in Weeks 2-8. Poor Week 1 patterns compound across the module.

### Q: Can Week 1 be shortened to 5 days?
**A**: **Maybe, but risky.** From Andrew's clarification:

**Andrew's flexibility**: "If the client truly wants to trim time, Andrew may be willing to reduce Week 1 to one week (5 days) instead of the standard 10 days."

**Risk factors**:
- Increases probability of rework in Weeks 2-8
- Less time for SME to learn storyboard format
- Rushed LD-SME relationship building
- Quality pattern shortcuts compound through module
- May require additional correction time later

**When to consider**:
- Client has aggressive timeline requirements
- SME has prior storyboarding experience with LDS
- LD and SME have existing working relationship
- Client accepts rework risk

**Recommendation**: Keep the 10-day Week 1 unless client explicitly requests compression and accepts documented risks.

---

## Launch Buffer

### Q: Is the 66-day buffer between "Ready for Launch" and "Go Live" standard?
**A**: **No, this is NOT standard.** This is a critical clarification from Andrew.

**The 66-day buffer in examples is an artifact, not a rule.**

**What determines actual buffer**:
- When programme development starts for the specific module
- Academic calendar alignment requirements
- Client-specific launch windows
- Programme scheduling decisions
- Variable lead times based on institutional requirements

**Buffer can be**:
- Shorter than 66 days (e.g., accelerated launches)
- Longer than 66 days (e.g., academic year boundaries)
- Different for each module in same programme

**Your responsibility**: Deliver "Ready for Launch" on your committed date. Client handles "Go Live" timing.

### Q: What factors affect buffer duration?
**A**: Multiple factors outside Andrew's control determine the buffer:

**Academic Calendar Factors**:
- Semester start dates
- Term boundaries
- Exam periods
- Holiday breaks

**Programme Factors**:
- Module sequencing in programme curriculum
- Prerequisite module completion
- Cohort start dates
- Programme marketing timelines

**Institutional Factors**:
- Approval processes
- Quality review periods
- Accreditation requirements
- Client internal readiness

**Coordination Factors**:
- Student enrollment periods
- Faculty availability
- LMS migration schedules
- Support staff readiness

**Planning impact**: Don't assume 66-day buffer. Confirm actual buffer with client Programme Leader during kickoff.

---

## Dependencies

### Q: How do dependencies work in this template?
**A**: The template has 52 carefully orchestrated dependencies across four categories:

**1. Critical Path Dependencies** (16 dependencies):
Sequential workflow enforcement from kickoff through launch
- Kickoff → MPD → Week storyboards → Builds → Reviews → Corrections → Launch
- Cannot skip steps or work out of order

**2. Cascading Build Dependencies** (7 dependencies):
Enable parallel work between LD and LT
- Week N Build enables Week N+1 Storyboarding
- LD works on Week 3 storyboard while LT builds Week 2
- Creates efficient pipeline without resource conflicts

**3. Within-Task Dependencies** (24 dependencies):
Control workflow within each week's storyboarding
- LD Draft + SME Draft (parallel) → Edit → Final Draft Agreed
- Cannot edit before both drafts complete
- Cannot finalize before editing complete

**4. Finalization Dependencies** (5 dependencies):
Coordinate final quality checks
- Film shoots → Proofreading
- Reviews → Corrections
- Corrections → Ready for Launch → Go Live

**How they help**:
- Prevent out-of-order work
- Enforce quality gates
- Coordinate handoffs between team members
- Visualize workflow in Timeline view
- Auto-block tasks until prerequisites complete

### Q: Can I modify dependencies?
**A**: Yes, but understand the implications:

**Safe to modify**:
- Add new dependencies for project-specific requirements
- Extend dependency chains for additional review steps
- Add parallel work streams for specialized content

**Risky to modify**:
- Removing critical path dependencies (breaks workflow)
- Changing cascading build pattern (creates resource conflicts)
- Bypassing review dependencies (compromises quality)
- Altering within-task storyboarding dependencies (enables incomplete work)

**How to modify safely**:
1. Understand WHY the dependency exists
2. Document your modification rationale
3. Test on project copy first
4. Communicate changes to team
5. Monitor for workflow issues

**Recommendation**: Complete at least one module with dependencies as-designed before modifying. Real-world experience reveals which dependencies are essential vs. optional.

### Q: What's the cascading build pattern?
**A**: Cascading builds enable parallel LD and LT work to optimize timeline:

**Pattern**:
- Week 1: LD+SME storyboard Week 1 (10 days) | LT waiting
- Week 2: LD+SME storyboard Week 2 (5 days) | LT builds Week 1 (5 days) **← parallel work**
- Week 3: LD+SME storyboard Week 3 (5 days) | LT builds Week 2 (5 days) **← parallel work**
- Week 4-9: Pattern continues through Week 8

**Dependencies that enable this**:
- Week N - Build depends on → Week N - Storyboard Final draft agreed
- Week N+1 - Storyboard depends on → Week N - Build (allowing overlap)

**Benefits**:
- LD and LT work in parallel (not sequential)
- Reduces total timeline by ~7 weeks
- Minimizes resource conflicts
- Maintains quality (storyboard approved before build)

**Visualization**: In Timeline view, you'll see storyboard bars overlapping with build bars in a cascading pattern.

---

## Getting Help

### Q: Where can I find more detailed information?
**A**: Documentation is organized by detail level:

**Quick Reference** (this document):
- Common questions organized by category
- Quick answers with context
- Suitable for day-to-day template use

**QUICKSTART.md**:
- 7-step setup process
- Key decisions to make upfront
- Common pitfalls to avoid
- Perfect for first-time template users

**TEMPLATE_VARIANTS.md**:
- Creating specialized template versions
- 12-week module variants
- Different module types
- For advanced users creating multiple templates

**Specification v2.0** (1550 lines):
- Complete technical reference
- Full dependency documentation
- All custom field definitions
- For understanding template architecture

### Q: What if I encounter issues with the template?
**A**: Escalation path:

**Template Structure Issues**:
→ Contact: Andrew (template owner)
→ Examples: Missing dependencies, incorrect durations, structural problems

**Asana Technical Issues**:
→ Contact: Senior LD (Nicole)
→ Examples: Custom field problems, automation failures, permission issues

**Process Clarifications**:
→ Contact: Project team leads
→ Examples: Workflow questions, role responsibilities, handoff procedures

**Client-Specific Adaptations**:
→ Contact: Account manager or Andrew
→ Examples: Timeline variations, special requirements, custom deliverables

### Q: How do I report bugs or suggest improvements?
**A**: Template improvement process:

**Found a bug**:
1. Document the issue with screenshots
2. Note which project and task(s) affected
3. Report to Andrew with reproduction steps
4. Mark as urgent if blocking workflow

**Have an improvement idea**:
1. Use the template for at least one complete module first
2. Document your suggestion with rationale
3. Include success metrics if applicable
4. Discuss with Andrew or team leads

**Template evolution**: This template was refined through real-world use with Walbrook and other clients. Your feedback improves it for everyone.

---

## Template Metadata

**Template Version**: 2.0
**Last Updated**: October 2025
**Dependencies**: 52 API-created relationships
**Timeline**: 17-18 weeks to "Ready for Launch"
**Compliance**: Reviewed and approved by Andrew
**Status**: Production-ready

**Files in this documentation suite**:
- `QUICKSTART.md` - 7-step setup guide for first-time users
- `FAQ.md` - This document, organized Q&A by category
- `TEMPLATE_VARIANTS.md` - Guide for creating specialized versions
- `Asana_Module_Development_Template_Spec_v2.md` - Complete technical specification (1550 lines)
