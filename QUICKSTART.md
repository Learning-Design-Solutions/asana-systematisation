# Asana Module Development Template - Quick Start Guide

## What This Template Does

The **Asana Module Development Template** systematizes the creation of 8-week online learning modules for Learning Design Solutions. It manages the complete 17-18 week development workflow from kickoff to "Ready for Launch," coordinating work between Learning Designers (LD), Learning Technologists (LT), Subject Matter Experts (SME), and Academic Reviewers through 52 carefully orchestrated task dependencies.

**Who uses it**: Learning Designers creating new module projects
**When to use it**: At the start of every new module development engagement

## Quick Start: Creating Your Module in 7 Steps

### Step 1: Duplicate the Template
1. Open the Asana Module Development Template project
2. Click **Project Settings** → **Duplicate project**
3. Name it: `[Client Name] - [Programme Name] - [Module Code]`
   Example: `Walbrook - MBA Marketing - MKT101`
4. Select: **Duplicate task dependencies** (critical!)
5. Click **Create Project**

### Step 2: Set the Launch Date (Your Timeline Anchor)
1. Open project **Custom Fields**
2. Find **Launch Date** field
3. Enter your target "Ready for Launch" date
4. All 72 task dates will auto-calculate backward from this anchor

**Important**: "Launch Date" means "Ready for Launch" (when Andrew delivers), NOT "Go Live" (when students access). There's typically a 66-day buffer between these, but this varies based on academic calendar requirements.

### Step 3: Assign Your Team
Set these custom fields at project level:
- **Learning Designer**: Your name
- **Learning Technologist**: Assigned LT
- **Module Author (SME)**: Client's subject matter expert
- **Senior LD (Reviewer)**: Nicole or assigned reviewer
- **Client Name**: Client organization
- **Programme Name**: Parent programme

### Step 4: Make Your Filming Decision
Decide which filming approach to use (affects Film Shoot tasks):

**Option 1 - Physical London Studio**
Best for: SME based in/visiting London
Location: SOAS or Walbrook campus studio
Quality: Highest production value

**Option 2 - Remote Loom Recording**
Best for: Remote SMEs, flexible schedules
Tool: Loom or similar screen recording
Quality: Professional but lower overhead

**Option 3 - AI Avatars**
Best for: No SME filming availability
Speed: Fastest turnaround
Quality: Consistent, no filming required

Document your choice in the Film Shoot task descriptions.

### Step 5: Review Week 1 Timeline
Week 1 gets **10 days** for storyboarding (vs 5 days for Weeks 2-8).

**Why?** Week 1 establishes:
- Patterns and processes for entire module
- SME understanding of storyboard format
- LD-SME working relationship
- Communication patterns

**Flexibility**: If client needs faster delivery, Andrew may reduce to 5 days, but this increases rework risk.

### Step 6: Start With Kickoff
Begin work with the **Kick off meeting** task:
1. Schedule initiation meeting with SME
2. Complete both kickoff subtasks
3. This unblocks the Module Planning Document (MPD)
4. All development depends on MPD completion

### Step 7: Monitor Dependencies
The template includes 52 dependencies that enforce workflow:
- **Week storyboards** must complete before builds start
- **Builds cascade**: Week 2 build enables Week 3 storyboard
- **Reviews are batched**: Weeks 1-2 together, then Weeks 3-8
- **Film shoots** depend on storyboards, NOT builds

Use Timeline view to see the complete Gantt chart.

## Key Decisions to Make Upfront

### Filming Approach (Critical)
Choose from three options documented in Step 4. This affects:
- Film Shoot task scheduling
- SME availability requirements
- Production timeline and budget

### Academic Reviewer Expectations
**Warning from Andrew**: Academic Reviewer performance "has been super inconsistent with current client, tends to be lighter touch than proofreading."

**What to do**:
- Manage expectations accordingly
- Consider allocating supplemental internal QA
- Don't assume thorough academic review coverage
- Budget for additional proofreading if needed

### Launch Buffer Duration
The 66-day buffer between "Ready for Launch" and "Go Live" is **NOT standard**.

**Actual buffer depends on**:
- Academic calendar alignment
- Client-specific launch windows
- Programme scheduling decisions
- When module development starts

**Your responsibility**: Deliver "Ready for Launch" on time. Client controls actual "Go Live" date.

## Common Pitfalls to Avoid

### Don't Skip Dependencies
All 52 dependencies exist for workflow enforcement:
- You cannot build before storyboard approval
- Reviews are blocked until all prerequisite builds complete
- Corrections depend on both reviews and proofreading
- Violating this creates rework and delays

### Week 1 Sets Module Patterns
The 10-day Week 1 storyboarding period establishes quality patterns for Weeks 2-8:
- Invest time in Week 1 setup
- Establish clear SME communication
- Define storyboard standards early
- Week 1 shortcuts compound through 8 weeks

### Launch Buffer Variability
Don't assume the 66-day buffer shown in examples is standard:
- Ask client about academic calendar requirements
- Understand programme launch timing
- Buffer can be shorter or longer based on context
- Plan your "Ready for Launch" delivery, not "Go Live"

### Film Shoot Timing Flexibility
Film shoot windows (Week 4 and Week 8) are recommended, not mandatory:
- Actual timing depends on SME availability
- Coordinate with Digital Learning Team
- Book studio space early (if Option 1)
- Film shoots depend on storyboards, not builds

## Where to Get Help

### Detailed Documentation
- **FAQ.md**: Common questions organized by category
- **TEMPLATE_VARIANTS.md**: Creating specialized template versions
- **Specification (v2.0)**: Complete 1550-line technical reference

### Contact Points
- **Template questions**: Andrew
- **Asana technical issues**: Senior LD (Nicole)
- **Process clarifications**: Project team leads

### Template Status
- **52 dependencies**: Successfully created via API
- **Timeline**: 17-18 weeks to "Ready for Launch"
- **Compliance**: Reviewed and approved by Andrew (Oct 2025)
- **Production ready**: Yes, convert to template and use

---

**Pro Tip**: Use Asana's Timeline view to visualize the entire module waterfall. The cascading build pattern shows Week N storyboarding happening in parallel with Week N-1 building, creating an efficient pipeline.

**Next Steps**: Read FAQ.md for answers to specific questions, or dive into TEMPLATE_VARIANTS.md if you need to create a specialized version (12-week modules, accelerated timelines, etc.).
