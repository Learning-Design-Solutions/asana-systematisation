# Asana Module Development Template - Complete Tutorial Guide

**Welcome!** This guide transforms you from template beginner to confident power user through hands-on learning and progressive skill building.

**Who this is for**: Team members who need to master the template beyond the quick start basics.

**What you'll learn**: How to create, manage, and optimize module projects using the systematized Asana workflow.

**Time investment**: 45-60 minutes to read through; lifetime of improved project management.

---

## Table of Contents

1. [Understanding the Template](#chapter-1-understanding-the-template)
2. [Creating Your First Module](#chapter-2-creating-your-first-module)
3. [Critical Decision Points](#chapter-3-critical-decision-points)
4. [Managing Dependencies](#chapter-4-managing-dependencies)
5. [Week 1 Deep Dive](#chapter-5-week-1-deep-dive)
6. [Launch Process](#chapter-6-launch-process)
7. [Template Variants](#chapter-7-template-variants)
8. [Troubleshooting and Tips](#chapter-8-troubleshooting--tips)

---

## Chapter 1: Understanding the Template

### The Problem This Solves

Before this template, module development involved:
- Manual task creation (60+ minutes per module)
- Forgotten dependencies creating workflow chaos
- Timeline calculations done by hand (error-prone)
- Inconsistent quality gates across projects
- Lost handoffs between team members

**The chaos**: Builds starting before storyboards approved. Reviews happening before content ready. Launch dates missed because dependencies weren't clear.

### How 52 Dependencies Create Automatic Project Management

The template includes **52 carefully orchestrated dependency relationships** that enforce workflow automatically:

**Critical Path Dependencies** (16 total):
- Kickoff → MPD → Week storyboards → Builds → Reviews → Corrections → Launch
- You literally cannot complete tasks out of order
- Asana blocks you from marking tasks complete if prerequisites aren't done

**Cascading Build Dependencies** (7 total):
- Week N Build enables Week N+1 Storyboarding
- Creates efficient pipeline: LD works on Week 3 while LT builds Week 2
- Prevents resource conflicts between LD and LT

**Within-Task Dependencies** (24 total):
- LD Draft + SME Draft (parallel) → Edit → Final Draft Agreed
- Enforces proper storyboarding workflow within each week
- Cannot finalize before both drafts complete

**Finalization Dependencies** (5 total):
- Film shoots → Proofreading
- Reviews → Corrections → Ready for Launch → Go Live
- Ensures quality gates aren't bypassed

**Visual metaphor**: Think of dependencies as guardrails on a mountain road. You can drive efficiently, but you can't accidentally drive off a cliff.

### The 12-Week Structure Explained

The template manages **12 distinct sections** over 17-18 weeks:

**Initiation & Planning** (15 days):
- Kickoff meeting
- Module Planning Document (MPD)
- MPD review
- Sets foundation for everything that follows

**Week 1** (17 days - special extended timeline):
- 10 days storyboarding (vs 5 days for other weeks)
- 5 days building
- 2 days review prep
- **Why extended?** Establishes patterns for entire module

**Weeks 2-8** (10 days each, cascading):
- 5 days storyboarding per week
- 5 days building per week
- Efficient parallel work between LD and LT

**Finalization** (20 days):
- Film shoots (two batches)
- Proofreading
- Academic review
- Corrections
- Ready for Launch milestone

**Launch** (Variable buffer, typically 66 days):
- Gap between "Ready for Launch" (Andrew's deliverable) and "Go Live" (client timing)
- **NOT a standard 66 days** - varies by academic calendar

### Key Roles in the Template

**Learning Design Solutions Team**:
- **Learning Designer (LD)**: Storyboarding, instructional design, editing
- **Learning Technologist (LT)**: Moodle build, technical implementation
- **Senior Learning Designer (Nicole)**: QA review, quality assurance

**Client Team**:
- **SME (Subject Matter Expert)**: Content creation, script development
- **Academic Reviewer**: Quality assurance (with variability warning - see Chapter 3)
- **Programme Leader**: Assessment approval
- **Digital Learning Team**: Video production
- **Editorial Team**: Proofreading

**Role coordination**: Template automatically assigns tasks based on custom field settings, ensuring everyone knows their responsibilities.

---

## Chapter 2: Creating Your First Module

### Step-by-Step Walkthrough

**Scenario**: You're creating a new module "MKT101 - Marketing Fundamentals" for Walbrook's MBA programme, launching March 11, 2026.

#### Step 1: Open the Base Template

Location: Asana workspace → Templates → "Asana Module Development Template"

**What you'll see**:
- 12 sections (Initiation through Launch)
- 72 tasks and subtasks
- Empty custom fields waiting for your data
- Timeline view showing theoretical Gantt chart

**Screenshot description**: Timeline view shows cascading pattern with Week 1-8 storyboards and builds overlapping in a waterfall pattern.

#### Step 2: Duplicate the Template

Click **Project Actions** (⋮) → **Duplicate project**

**Critical duplication settings**:
- ✅ **Tasks**: Yes (copies all 72 tasks)
- ✅ **Task dependencies**: YES - THIS IS CRITICAL (copies all 52 dependencies)
- ✅ **Task descriptions**: Yes (copies guidance in each task)
- ❌ **Dates**: No (you'll set these via Launch Date)
- ❌ **Assignees**: No (you'll assign via custom fields)

**Name your project**: `Walbrook - MBA Marketing - MKT101`

Pattern: `[Client Name] - [Programme Name] - [Module Code]`

Click **Create Project**.

**Time checkpoint**: 2 minutes elapsed.

#### Step 3: Set the Launch Date (Your Timeline Anchor)

This is the most critical step because ALL dates calculate from this anchor.

Navigate to project **Custom Fields** (top right).

Find **Launch Date** field.

**Important clarification**: "Launch Date" in the template means **"Ready for Launch"** (when Andrew delivers the completed module), NOT "Go Live" (when students access it).

For our scenario:
- Client wants students to access on March 11, 2026
- Academic calendar requires 66-day buffer before go-live
- Therefore, "Ready for Launch" must be: January 5, 2026

Enter: **01/05/2026**

**Watch the magic**: All 72 task dates auto-calculate backward:
- Kickoff meeting: September 15, 2025 (112 days before launch)
- Week 1 storyboard: October 6-17, 2025
- Week 8 build: December 8-13, 2025
- Corrections: December 29, 2025 - January 2, 2026

**Screenshot description**: Timeline view after setting Launch Date shows all tasks with calculated dates creating complete project schedule.

**Time checkpoint**: 5 minutes elapsed.

#### Step 4: Understanding How Dependencies Cascade Through Your Timeline

Switch to **Timeline** view (if not already there).

Notice the **cascading pattern**:

Week 1 (October 6-25):
- Storyboard: Oct 6-17 (10 days)
- Build: Oct 20-25 (5 days)
- Dependency: Build cannot start until "Storyboard Final draft agreed" completes

Week 2 (October 20 - November 1):
- Storyboard: Oct 20-24 (5 days) **← parallel with Week 1 Build**
- Build: Oct 27 - Nov 1 (5 days)
- Dependency: Week 2 Storyboard depends on Week 1 Build

**The efficiency insight**: While LT builds Week 1, LD is already storyboarding Week 2. This cascading pattern saves ~7 weeks compared to sequential workflow.

**Test the enforcement**:
1. Try to mark "Week 1 - Build" complete before "Week 1 - Storyboard Final draft agreed" is done
2. Asana will show warning: "This task is blocked by incomplete dependencies"
3. This is the safety system in action

**Time checkpoint**: 8 minutes elapsed.

#### Step 5: Assign Your Team

Set these **project-level custom fields**:

- **Learning Designer**: Your name
- **Learning Technologist**: Assigned LT (e.g., "Raj Kumar")
- **Module Author (SME)**: Client contact (e.g., "Dr. Sarah Johnson")
- **Senior LD (Reviewer)**: Nicole
- **Client Name**: Walbrook
- **Programme Name**: MBA Marketing
- **Module Code**: MKT101

**Why project-level?** These assignments propagate to relevant tasks automatically:
- All "Storyboard Initial LD Draft" subtasks → Your name
- All "Build" tasks → Raj Kumar
- All "Storyboard SME Scripts Draft" subtasks → Dr. Sarah Johnson

**Screenshot description**: Custom Fields panel showing all fields filled with example team names.

**Time checkpoint**: 10 minutes elapsed.

#### Step 6: Make Your Critical Decisions

Before starting work, decide on three critical workflow aspects:

**Decision 1: Filming Approach** (see Chapter 3 for detailed decision tree)

For MKT101 scenario:
- Dr. Johnson is based in Manchester (cannot travel to London)
- Module includes talking-head lecture content
- Budget is moderate

**Decision**: Remote Loom Recording (Option 2)

Document in Film Shoot task descriptions:
"Filming approach: Remote Loom. Dr. Johnson will record from Manchester using Loom. LT will provide Loom training and recording guidelines."

**Decision 2: Academic Review Expectations** (critical warning from Andrew)

Academic Reviewer performance has been "super inconsistent, tends to be lighter touch than proofreading."

For MKT101 scenario:
**Decision**: Add supplemental internal QA
- Nicole will review Weeks 1-2 alongside Academic Reviewer
- Budget 3 extra days for internal QA in timeline
- Document in "Week 1 and 2 review" task description

**Decision 3: Launch Buffer**

The 66-day buffer is NOT standard. For MKT101:
- Client confirmed: MBA cohort starts March 11, 2026
- Buffer needed: 66 days from Ready for Launch (standard in this case)
- No academic calendar conflicts

**Decision**: Maintain 66-day buffer, Go Live = March 11, 2026

Document in "Go live" task description:
"Go Live Date: March 11, 2026 (MBA cohort start). Buffer: 66 days from Ready for Launch. Client responsible for final launch timing."

**Time checkpoint**: 15 minutes elapsed. Your module is now configured and ready to start.

### Common Mistakes to Avoid

**Mistake 1: Starting work before setting Launch Date**

Symptom: Team members ask "When does this task start?"
Impact: Manual date calculations, coordination chaos
Fix: Always set Launch Date in Step 3 before assigning work

**Mistake 2: Not checking "Duplicate task dependencies"**

Symptom: Tasks can be completed out of order, no workflow enforcement
Impact: Builds start before storyboards, reviews before content ready
Fix: If you forgot, delete project and start over (faster than manually recreating 52 dependencies)

**Mistake 3: Treating "Launch Date" as "Go Live Date"**

Symptom: Timeline calculations off by 66 days
Impact: Missed deadlines, team confusion about milestone ownership
Fix: Remember: Launch Date = Ready for Launch (Andrew's deliverable), NOT Go Live (client timing)

**Mistake 4: Skipping filming decision**

Symptom: Film Shoot tasks arrive with no plan, SME unprepared
Impact: Rushed filming decisions, scheduling conflicts, budget surprises
Fix: Make filming decision in Step 6, document in task descriptions

---

## Chapter 3: Critical Decision Points

### Filming Decision Tree

This is arguably the most impactful decision you'll make for your module. It affects timeline, budget, production quality, and SME coordination.

#### Decision Point 1: SME Location and Availability

**If SME is based in London OR can travel to London:**
→ Proceed to Decision Point 2

**If SME is remote and cannot travel:**
→ Skip to Option 2 (Remote Loom) or Option 3 (AI Avatars)

#### Decision Point 2: Production Quality Requirements

**If high production value is critical:**
- High-profile programme
- Marketing/recruitment emphasis on course quality
- Demonstration-heavy content (equipment, lab procedures)
- Client has reputation for production excellence

→ Choose **Option 1: Physical Presence in London Studio**

**If professional quality is sufficient:**
- Standard academic module
- Talking-head lectures
- Interview-style content
- Theory-heavy module

→ Consider **Option 2: Remote Loom Recording**

#### Option 1: Physical Presence in London Studio

**Best for**:
- SME based in/visiting London
- High production value requirements
- Demonstration-heavy content
- First module with new client (relationship building)

**Logistics**:
- **Location**: Studio at SOAS or Walbrook campus
- **Booking**: Coordinate with Digital Learning Team 4+ weeks in advance
- **Duration**: First batch: 6 days, Second batch: 5 days
- **SME time**: 2 full days filming per batch (plus travel)
- **Support**: Direct support from Digital Learning Team

**Timeline dependencies**:
- First batch: After Week 4 storyboard completion (scripts ready)
- Second batch: After Week 8 storyboard completion
- Windows are nominal - actual timing flexible based on SME/studio availability

**Budget considerations**:
- Studio rental
- Digital Learning Team time
- SME travel/accommodation (if traveling to London)
- Equipment (usually included in studio rental)

**Quality output**:
- Highest production value
- Professional lighting and sound
- Multiple camera angles possible
- Studio backdrop consistency

**Example scenario**: Walbrook MBA programme wants high-quality marketing content. Dr. Johnson will travel to London for 2-day film shoot. Budget approved for travel expenses. Digital Learning Team books SOAS studio for November 10-15.

#### Option 2: Remote Loom Recording

**Best for**:
- Remote SMEs
- Quick turnarounds
- Standard academic content
- Budget-conscious projects
- SMEs comfortable with self-recording

**Logistics**:
- **Tool**: Loom or similar screen recording software
- **Training**: LT provides Loom training to SME (1-hour session)
- **Duration**: SME records on their own schedule
- **Support**: LT provides recording guidelines, reviews test recordings
- **Flexibility**: SME can re-record segments as needed

**Timeline dependencies**:
- Same as Option 1 (after storyboard completion)
- More flexible scheduling (no studio booking)
- Can record in smaller batches over several days

**Budget considerations**:
- Loom subscription (if not already available)
- LT time for training and quality review
- Significantly lower than studio option
- No travel costs

**Quality output**:
- Professional but not studio-grade
- Maintains personal presence
- Good lighting/sound achievable with home setup
- Consistent if SME has dedicated recording space

**SME requirements**:
- Basic technical comfort
- Quiet recording space
- Decent webcam and microphone
- Stable internet connection
- Willingness to self-direct

**Example scenario**: Dr. Johnson based in Manchester, comfortable with technology. LT provides Loom training October 30. Dr. Johnson records Week 1-4 content November 10-12 from home office. LT reviews and approves recordings November 13.

#### Option 3: AI Avatars

**Best for**:
- No SME filming availability
- Consistent visual branding across modules
- Experimental/innovative programmes
- Theory-heavy content (less performance/demonstration)
- Fastest turnaround needs

**Logistics**:
- **Technology**: AI avatar generation service
- **Input**: Scripts from storyboards
- **SME involvement**: Script review/approval only (no filming)
- **Production time**: 2-3 days per batch
- **Customization**: Avatar appearance, voice, pacing

**Timeline dependencies**:
- Same script dependencies (after storyboard completion)
- Faster production (no filming coordination)
- May need extra time for SME comfort with approach

**Budget considerations**:
- AI avatar service subscription/fees
- Variable by provider and video minutes
- No travel or studio costs
- May require upfront investment in avatar creation

**Quality output**:
- Consistent visual presentation
- Controllable pacing and emphasis
- No filming artifacts (background noise, lighting changes)
- May lack authentic personal presence

**Client acceptance considerations**:
- Novel approach - some clients enthusiastic, others skeptical
- Consider programme culture and student expectations
- Test with pilot content before committing to full module
- May need stakeholder buy-in

**Example scenario**: Walbrook wants to experiment with AI avatars for cost efficiency. Dr. Johnson approves scripts but doesn't want to film. Avatar created using AI service, videos produced in 3 days. Client reviews pilot video before approving approach for full module.

### Decision Matrix

| Factor | Option 1: Studio | Option 2: Loom | Option 3: AI |
|--------|-----------------|----------------|--------------|
| SME Location | London-based or traveling | Remote | Any |
| Production Quality | Highest | Professional | Consistent |
| Timeline | 11 days (6+5) | Flexible | Fastest (2-3 days) |
| Budget | Highest | Medium | Medium-Low |
| SME Time | 4 days (2+2) | 2-3 days | 0 days filming |
| Technical Requirements | Studio booking | Loom setup | AI service |
| Best For | High-profile, demos | Standard content | Theory-heavy |

### Launch Buffer Management

**The Critical Truth**: The 66-day buffer you see in template examples is **NOT a standard**. This is one of the most important clarifications from Andrew.

#### What Determines Your Buffer

**Academic Calendar Constraints**:
- Semester/term start dates
- Programme cohort timing
- Pre-registration periods
- Academic year boundaries

**Example**: MBA programme starts first Monday of March. Launch must align regardless of when development completes.

**Holiday Periods**:
- Christmas shutdown
- Summer break
- Reading weeks
- National holidays

**Example**: Ready for Launch December 20, but university closed until January 6. Effective buffer extends by 17 days.

**Pre-Registration Timing**:
- Student enrollment windows
- Marketing campaign schedules
- Programme approval processes
- Quality review periods

**Example**: Students register in January for March start. Module must be ready for preview by mid-December. Buffer compresses to 45 days.

#### Buffer Variability Examples

**Scenario 1: Compressed Buffer (30 days)**
- Module ready January 5
- Urgent programme launch February 4
- Reason: Replacement module for withdrawn content
- Risk: Less time for final reviews, stakeholder previews

**Scenario 2: Standard Buffer (66 days)**
- Module ready January 5
- Programme starts March 11
- Reason: Normal academic calendar alignment
- Risk: Low, adequate time for final preparations

**Scenario 3: Extended Buffer (120 days)**
- Module ready January 5
- Programme starts May 5
- Reason: Academic year boundary (September vs January start)
- Risk: Content may need refresh if delayed too long

#### Planning Your Buffer

**Step 1**: Confirm programme launch timing with client Programme Leader
- When does the cohort actually start?
- Is this date fixed or flexible?
- What approval processes happen between Ready for Launch and Go Live?

**Step 2**: Work backward from Go Live to calculate Ready for Launch
- Programme starts: March 11, 2026
- Need 2 weeks pre-launch review: February 25, 2026
- Need 4 weeks student enrollment: January 28, 2026
- **Ready for Launch target**: January 28, 2026

**Step 3**: Set Launch Date (Ready for Launch) in template
- Enter January 28, 2026 as Launch Date
- Template calculates Kickoff: September 8, 2025
- Buffer to Go Live: 43 days (not 66)

**Step 4**: Document buffer rationale in Go Live task
"Go Live: March 11, 2026 (MBA cohort start). Buffer: 43 days from Ready for Launch (January 28). Compressed to accommodate enrollment and preview period. Client responsible for final launch timing."

### Reviewer Allocation Strategy

**The Academic Review Challenge**: Per Andrew's warning, "Academic Reviewer performance has been super inconsistent with current client, tends to be lighter touch than proofreading."

#### When Academic Review Alone May Be Sufficient

**Green light indicators**:
- Low-stakes module (elective, not core)
- Well-established content domain
- Experienced SME with strong track record
- Previous modules with same Academic Reviewer showed thoroughness
- Time/budget constraints prevent supplemental QA

**Decision**: Rely on Academic Review only, but monitor closely

#### When to Add Supplemental QA

**Red flag indicators**:
- High-profile module (core programme, first module students encounter)
- New content domain or experimental pedagogy
- Inexperienced SME or first collaboration
- Previous Academic Reviewer feedback was superficial
- Compliance requirements (accreditation, professional standards)

**Supplemental QA Options**:

**Option A: Senior LD (Nicole) Review**
- When: Alongside Academic Review or as backup
- Focus: Instructional design quality, learning alignment
- Time: 5 days (parallel to Academic Review)
- Cost: Internal resource allocation

**Option B: Additional Proofreading Pass**
- When: After Academic Review if concerns identified
- Focus: Language quality, consistency, clarity
- Time: 5 days (extends timeline)
- Cost: Editorial Team budget

**Option C: Peer LD Review**
- When: Internal quality check before Academic Review
- Focus: Storyboard quality, activity design
- Time: 3 days (adds to timeline)
- Cost: Internal resource sharing

**Option D: Client Programme Leader Spot Check**
- When: High-stakes modules needing stakeholder confidence
- Focus: Strategic alignment, programme coherence
- Time: 2 days (spot check, not comprehensive)
- Cost: Client time allocation

#### Batched Review Strategy

The template batches reviews: Weeks 1-2 together, then Weeks 3-8 together.

**Why this batching?**

**Early Feedback (Weeks 1-2)**:
- Establishes quality expectations
- Catches pattern issues before they compound
- Smaller batch = faster turnaround
- Allows course correction for Weeks 3-8

**Comprehensive Review (Weeks 3-8)**:
- Assesses full module consistency
- Evaluates progression and coherence
- Batching reduces Academic Reviewer context-switching
- More efficient than 6 separate reviews

**Alternative: Three-Batch Approach**

Some teams prefer: Weeks 1-2, Weeks 3-5, Weeks 6-8

**Advantages**:
- More frequent feedback
- Smaller batches easier to review thoroughly
- Catches issues earlier in Weeks 3-8

**Disadvantages**:
- Adds 5 days to timeline (third review batch)
- More Academic Reviewer coordination
- Increases context-switching overhead

**When to use three batches**:
- First module with new client (relationship building)
- Complex or experimental content
- Academic Reviewer preference for smaller batches
- Timeline can accommodate extra review cycle

---

## Chapter 4: Managing Dependencies

### How Task Dependencies Work in the Template

Think of dependencies as a **network of relationships** between tasks that enforce proper sequencing.

**What a dependency means**:
- Task A depends on Task B = Task A is **blocked** until Task B completes
- Asana enforces this automatically
- You cannot mark Task A complete while Task B is incomplete
- Timeline view shows these relationships with connecting lines

**Example dependency in action**:

```
Week 1 - Storyboard Final draft agreed
          ↓ (blocks)
Week 1 - Build
```

**What happens**:
1. You complete "Storyboard Final draft agreed" on October 17
2. "Week 1 - Build" becomes available (no longer blocked)
3. LT sees notification: "Week 1 - Build is now ready to start"
4. LT completes build October 20-25
5. "Week 2 - Storyboarding" becomes unblocked (depends on Week 1 Build)

**Enforcement mechanism**:
- Try to complete "Week 1 - Build" on October 16 (before storyboard done)
- Asana shows: "This task is blocked by incomplete dependencies"
- Cannot mark complete until blocker resolves

### Understanding the Storyboard → Build Relationship

**Common misconception**: Film shoots depend on builds (they need the Moodle content)

**Correction from Andrew**: Film shoots depend on **storyboards**, NOT builds

**Why this matters**:

**Storyboards contain**:
- Scripts for video content
- Learning objectives
- Activity instructions
- Content structure

**Builds contain**:
- Moodle implementation
- Configured activities
- Embedded media
- Navigation structure

**For filming, you need**: Scripts and content plans (from storyboards)
**For filming, you DON'T need**: Moodle builds (technical implementation)

**Correct dependency chain**:
```
Week 4 - Storyboard Final draft agreed
          ↓ (blocks)
Film shoot - first batch
```

**Incorrect dependency**:
```
Week 4 - Build  ← WRONG
          ↓
Film shoot - first batch
```

**Impact of correction**:
- Film shoots can start 1 week earlier (storyboard done before build)
- Reduces timeline by up to 2 weeks
- LT can build while filming happens (parallel work)

### What Happens When Tasks Are Delayed

**Scenario**: SME unavailable during Week 3. Storyboard delayed by 3 days.

**Cascade effect**:

```
Week 3 - Storyboard (delayed +3 days)
    ↓
Week 3 - Build (delayed +3 days, blocked by storyboard)
    ↓
Week 4 - Storyboard (delayed +3 days, depends on Week 3 Build)
    ↓
Week 4 - Build (delayed +3 days)
    ↓
... continues through Week 8
    ↓
Weeks 3-8 review (delayed +3 days)
    ↓
Corrections (delayed +3 days)
    ↓
Ready for Launch (delayed +3 days)
```

**Impact**: Single 3-day delay in Week 3 delays final launch by 3 days.

**Mitigation strategies**:

**Option 1: Compress later weeks**
- Reduce Week 4-8 storyboarding from 5 days to 4 days each
- Requires LD+SME overtime or reduced quality
- Risk: Pattern shortcuts, rework later

**Option 2: Accept delay, communicate early**
- Notify stakeholders of 3-day launch delay
- Adjust Launch Date in template (all dates recalculate)
- Maintain quality, adjust expectations
- Best if Go Live buffer accommodates

**Option 3: Parallel recovery**
- Overlap Week 4 storyboard with Week 3 build (compress cascade)
- Requires extra LD capacity
- Risk: Week 4 quality suffers from reduced focus

### Manual Dependency Adjustments

**When to adjust dependencies**:

**Scenario 1: Client requests different review batching**
- Client wants three review batches instead of two
- Add new "Weeks 3-5 review" task
- Manually add dependency: Week 5 Build → Weeks 3-5 review

**How to add dependency in Asana**:
1. Open task "Weeks 3-5 review"
2. Click "Add dependencies" in task details
3. Search for "Week 5 - Build"
4. Select "This task is waiting on Week 5 - Build"
5. Save

**Scenario 2: Additional QA checkpoint needed**
- Add "Mid-module Quality Check" after Week 4
- Create dependency: Week 4 Build → Mid-module Quality Check
- Create dependency: Mid-module Quality Check → Week 5 Storyboarding

**Scenario 3: Film shoot timing change**
- SME only available after Week 6, not Week 4
- Delete dependency: Week 4 Storyboard → Film shoot - first batch
- Add dependency: Week 6 Storyboard → Film shoot - first batch

**How to delete dependency in Asana**:
1. Open task with dependency
2. Find dependency in task details
3. Click X next to dependency name
4. Confirm deletion

**Impact of manual changes**:
- Timeline view updates immediately
- Downstream tasks may shift dates
- Other dependencies remain intact
- Document changes in project description for future reference

### Visualizing Dependencies in Timeline View

**Timeline view benefits**:
- See entire project schedule at a glance
- Dependency lines show task relationships
- Critical path highlighted (tasks that affect launch date)
- Identify bottlenecks and parallel work opportunities

**How to use Timeline view effectively**:

**View 1: Full project timeline**
- Zoom out to see all 12 sections
- Identify overall pacing and milestones
- Check for holiday conflicts
- Verify launch date alignment

**View 2: Week-by-week focus**
- Zoom in to current week
- See LD vs LT parallel work
- Monitor dependency completion
- Track handoffs between team members

**View 3: Critical path only**
- Filter to show only tasks on critical path
- Focus on tasks that affect launch date
- Prioritize work that cannot be delayed
- Identify recovery opportunities

**Dependency line colors** (Asana visual cues):
- Gray line: Normal dependency
- Red line: Blocking dependency with incomplete predecessor
- Green line: Completed dependency chain

---

## Chapter 5: Week 1 Deep Dive

### Why Week 1 is 10 Days (Not 5 Like Other Weeks)

Week 1 is **special** and deserves the extra investment. Here's why from Andrew's clarification:

**Pattern Establishment**:
- Week 1 sets the template for Weeks 2-8
- Quality patterns (good or bad) compound through remaining weeks
- Shortcuts in Week 1 create 7x the rework (repeated through 7 more weeks)

**SME Learning Curve**:
- First exposure to storyboard format and expectations
- Understanding instructional design terminology
- Learning collaboration tools and workflow
- More questions and back-and-forth expected

**Relationship Building**:
- LD and SME establishing working relationship
- Communication patterns and preferences
- Understanding each other's work styles
- Building trust for efficient collaboration

**Quality Foundation**:
- First week demonstrates module quality level
- Academic Reviewer sees Week 1 first - sets their expectations
- Students encounter Week 1 first - creates first impression
- More time = higher quality foundation

### The Extended Timeline Breakdown

**Week 1 storyboarding: 10 days total**

**Days 1-5: Parallel drafting**
- **LD Draft** (5 days): Learning Designer creates initial storyboard structure
  - Learning activities
  - Assessment design
  - Navigation and pacing
  - Instructional scaffolding

- **SME Draft** (5 days, parallel): SME develops content
  - Subject matter expertise
  - Examples and case studies
  - Scripts for video content
  - Supplementary resources

**Why 5 days each?** (vs 2 days in Weeks 2-8)
- SME needs time to understand storyboard format
- LD needs time to establish module patterns
- First week more iterative - expect multiple drafts

**Days 6-8: Editing** (3 days)
- LD and SME integrate their drafts
- Refine learning design
- Adjust scripts and activities
- Resolve content gaps or overlaps

**Why 3 days?** (vs 2 days in Weeks 2-8)
- More substantial integration needed
- Pattern decisions affect all subsequent weeks
- Quality investment pays off in Weeks 2-8

**Days 9-10: Finalization** (2 days)
- Final review and sign-off
- Confirm storyboard ready for build
- Document build notes for LT
- Quality checkpoint before proceeding

**Why 2 days?** (vs 1 day in Weeks 2-8)
- Extra review time for pattern validation
- Ensure quality foundation established

**Total: 10 days** (vs 5 days for Weeks 2-8)

### The Upfront Preparation Phase

**What happens in those extra 5 days**:

**For the Learning Designer**:
- Experimenting with activity types
- Refining navigation structure
- Establishing assessment patterns
- Creating reusable templates for Weeks 2-8

**For the SME**:
- Understanding learning outcomes translation
- Practicing script writing
- Gathering supplementary resources
- Building confidence with storyboard format

**For the partnership**:
- Calibrating feedback styles
- Establishing communication rhythm
- Clarifying roles and responsibilities
- Building collaborative momentum

**Return on investment**:
- Weeks 2-8 storyboarding becomes faster (5 days instead of 10)
- Less rework needed in later weeks
- Smoother LD-SME collaboration
- Higher overall module quality

### Module Specification and Planning Tasks

**Before Week 1 storyboarding begins**, the Initiation & Planning section establishes module foundation.

**Kick off meeting (5 days)**:
- **Initiation meeting held** (subtask): Initial conversation between LD and SME
  - Introduce team members
  - Discuss module vision and goals
  - Establish communication preferences
  - Set expectations for collaboration

- **Kick off meeting held** (subtask): Formal project kickoff
  - Review timeline and milestones
  - Confirm resource availability
  - Discuss filming approach
  - Align on quality standards

**Module Planning Document (MPD) (10 days)**:
- **MPD Draft** (5 days, subtask): Initial planning document creation
  - Learning outcomes
  - Module structure (8 weeks)
  - Assessment strategy
  - Resource requirements

- **MPD Finalised** (5 days, subtask): Refinement and approval
  - Incorporate stakeholder feedback
  - Finalize learning outcomes
  - Lock module structure
  - Sign-off from Programme Leader

- **Assessment briefs drafted** (5 days, subtask, parallel): Assessment design
  - Detailed assessment briefs
  - Rubrics and marking criteria
  - Alignment with learning outcomes
  - Programme Leader approval

- **Reading list revised** (5 days, subtask, parallel): Resource planning
  - Update reading list
  - Check library access
  - Librarian validation
  - Copyright clearance

**MPD review (5 days, parallel with finalization)**:
- Academic Reviewer validates MPD
- Ensures academic rigor
- Confirms alignment with programme standards
- May identify issues requiring MPD revision

**Critical dependency**:
Week 1 storyboarding **cannot start** until both:
- MPD Finalised completes
- MPD review completes

**Why both?** MPD provides the blueprint for storyboarding. Academic Reviewer input ensures storyboards align with validated plan.

### Setting Up for Success in Remaining Weeks

**Week 1 deliverables that enable Weeks 2-8**:

**1. Storyboard Template**
- Reusable structure for consistent formatting
- Standard sections (introduction, content, activities, summary)
- Navigation patterns
- Activity templates

**Example**: Week 1 establishes 5-part structure:
- Introduction (learning objectives)
- Content Part A (theory + examples)
- Activity 1 (application)
- Content Part B (advanced concepts)
- Summary (reflection + next week preview)

Weeks 2-8 follow this same structure = faster storyboarding.

**2. SME Confidence**
- Comfort with storyboard format
- Understanding of LD terminology
- Practiced script writing
- Established revision process

**Example**: SME initially confused by "formative assessment" terminology. Week 1 clarifies this means "low-stakes practice activities." SME confidently uses term in Weeks 2-8 storyboards.

**3. Communication Patterns**
- Preferred communication channels (email vs Asana comments)
- Feedback turnaround expectations
- Meeting frequency and format
- Escalation path for blockers

**Example**: Week 1 reveals SME prefers video calls for complex discussions, Asana comments for minor edits. LD adjusts Weeks 2-8 workflow accordingly.

**4. Quality Standards**
- Example activities demonstrating expected rigor
- Script length and pacing
- Interactivity balance
- Resource integration approach

**Example**: Week 1 activity uses case study with 3-part analysis. Academic Reviewer praises depth. LD and SME replicate this pattern in Weeks 2-8 activities.

**Efficiency gains in Weeks 2-8**:
- Storyboarding time reduces from 10 days to 5 days
- Less revision needed (patterns established)
- Faster turnaround (confidence built)
- Smoother collaboration (communication calibrated)

**Total time investment**:
- Week 1: 10 days storyboarding
- Weeks 2-8: 7 × 5 days = 35 days storyboarding
- **Total**: 45 days storyboarding

**Alternative (without Week 1 investment)**:
- Week 1: 5 days storyboarding (rushed)
- Weeks 2-8: 7 × 7 days = 49 days (more rework)
- **Total**: 54 days storyboarding

**Time saved by investing in Week 1**: 9 days

---

## Chapter 6: Launch Process

### "Ready for Launch" vs "Go Live"

This distinction is **critical** and often misunderstood. Let's clarify with absolute precision.

**Ready for Launch (Day 112, Andrew's Deliverable)**:

**What it means**:
- Module is 100% complete from LDS perspective
- All content built in Moodle
- All QA reviews completed and corrections applied
- All media embedded and functional
- Proofreading complete
- Module tested and ready for student access

**Who's responsible**: Andrew and Learning Design Solutions team

**What happens at this milestone**:
- Andrew delivers completed module to client
- Client receives access to fully-built Moodle course
- Documentation provided (build notes, media credits, etc.)
- Handoff meeting conducted
- LDS work complete

**Status in Asana**: "Ready for launch" task marked complete

**Go Live (Variable, Client-Controlled)**:

**What it means**:
- Students gain access to module in learning platform
- Module appears in student course lists
- Enrollment opens or activates
- Learning journey begins for cohort

**Who's responsible**: Client (Walbrook, SOAS, etc.) based on their academic calendar

**What happens at this milestone**:
- Client activates module visibility
- Students enrolled in course
- Support systems activated (forums, help desk)
- Client-side preparations complete (faculty briefings, TA training)

**Status in Asana**: "Go live" task marked complete (informational only for LDS)

**The Buffer Between These Milestones**:

**Why a buffer exists**:
- Academic calendar alignment (semester/term starts)
- Student enrollment and registration periods
- Quality assurance and stakeholder previews
- Faculty preparation and training
- Marketing and recruitment windows
- Client internal approval processes

**Why buffer varies** (NOT always 66 days):
- Different academic calendars (semester vs trimester vs year-round)
- Programme-specific launch timing
- Cohort start dates vary by programme
- Holiday periods affect available launch windows

**Example buffers**:
- 30 days: Urgent replacement module mid-semester
- 66 days: Standard new programme launch
- 120 days: Academic year boundary (ready December, launch April)

**Your planning responsibility**:
- Confirm Go Live date with client Programme Leader during kickoff
- Work backward to calculate Ready for Launch date
- Set Launch Date in template = Ready for Launch
- Document Go Live in task description
- Track buffer duration for expectation management

### Final Review and Approval Workflow

**The final 20 days** (Finalization section) orchestrate multiple quality gates in sequence.

**Film shoot - second batch** (5 days, starts Day 58 before launch):
- Depends on: Week 8 - Storyboard Final draft agreed
- Video content for Weeks 5-8
- Raw footage delivered
- Editing and captions complete

**Proofreading** (5 days, starts Day 21 before launch):
- Depends on: Film shoot - second batch complete
- Editorial Team reviews all content
- Language quality, consistency, clarity
- Spelling, grammar, style guide compliance
- Accessibility language review

**Weeks 3 to 8 review** (5 days, starts Day 14 before launch):
- Depends on: Week 8 - Build complete
- Academic Reviewer assesses Weeks 3-8 together
- Batched review for efficiency
- Academic rigor, consistency, progression
- Programme standard alignment

**Warning**: This often falls on Christmas week (12/22-12/26 in example timeline). Confirm Academic Reviewer availability or adjust timeline.

**Corrections** (5 days, starts Day 7 before launch):
- Depends on: BOTH Proofreading AND Weeks 3-8 review complete
- Addresses feedback from both quality gates
- LD/LT makes required changes
- SME involved if content revisions needed
- Final quality verification

**Ready for launch** (1 day, Day 0):
- Depends on: Corrections complete
- Formal handoff milestone
- Andrew delivers to client
- Documentation provided
- LDS work complete

**Parallel workflows during Finalization**:

```
Timeline:
Day 58: Film shoot - second batch starts
Day 54: Film shoot complete
Day 21: Proofreading starts
Day 16: Proofreading complete
Day 14: Weeks 3-8 review starts (parallel timing, different dependency)
Day 10: Weeks 3-8 review complete
Day 7:  Corrections starts (waits for BOTH proofreading AND review)
Day 2:  Corrections complete
Day 0:  Ready for launch
```

**Critical coordination**: Corrections task depends on **both** proofreading and review completing. If either is delayed, corrections wait for both.

### Post-Launch Monitoring

**After Go Live, what happens?**

**Learning Design Solutions responsibilities** (varies by contract):
- **Weeks 1-2**: Monitor student activity and forum questions
- **Support Level 1**: Respond to technical issues (broken links, access problems)
- **Support Level 2**: LD available for content clarification questions
- **Analytics review**: Mid-module check-in on engagement metrics
- **End-of-module debrief**: Discuss what worked, what to improve

**Client responsibilities**:
- Student enrollment and access management
- Faculty/TA briefings and support
- Academic integrity monitoring
- Grade book and assessment management
- Student support services

**Handoff documentation** (provided at Ready for Launch):
- Module build notes
- Media credits and sources
- Known issues or limitations
- Recommendations for future iterations
- Contact information for ongoing support

**Continuous improvement cycle**:
- Student feedback collection
- Analytics analysis (completion rates, activity engagement)
- Faculty/TA observations
- Identify enhancement opportunities
- Feed insights into next module or next cohort iteration

---

## Chapter 7: Template Variants

### When to Create Specialized Variants

**Use the base 8-week template when**:
- Standard module structure (8 weeks of content)
- Typical 17-18 week development timeline
- Standard review process (batched Weeks 1-2, then Weeks 3-8)
- Normal filming requirements (two batches or equivalent)

**Create a variant when you have**:
- **3+ modules** with same structural pattern
- **Significant** structural differences (not just task description changes)
- **Repeatable** pattern worth systematizing
- **Team capacity** to maintain multiple templates

**Don't create variant if**:
- One-off module with unique requirements (modify individual project)
- Minor differences (different assignees, descriptions) (handle in base template)
- Unsure if pattern will repeat (test with project copy first)
- No capacity to maintain multiple templates (stick with base, customize per project)

### Duplication vs API-Based Variant Creation

**Method 1: Template Duplication (5 minutes per variant)**

**Best for**:
- Similar 8-week structure with minor variations
- Same dependency patterns (52 dependencies copy automatically)
- Different task descriptions or resources
- Quick creation needed

**Process**:
1. Duplicate base template project
2. Modify task descriptions for variant-specific guidance
3. Add/remove specific tasks as needed
4. Dependencies copy automatically, adjust manually if needed
5. Convert modified project to template

**Example**: Creating "No Film Shoots" variant
- Duplicate base template
- Delete two film shoot tasks (dependencies auto-adjust)
- Update task descriptions removing filming references
- Reduce timeline by 11 days
- Convert to template
- **Time**: 5 minutes

**Method 2: API-Based Creation (30 minutes per variant)**

**Best for**:
- Significantly different structures (12-week modules, different phases)
- Different dependency patterns
- Need complete control over all relationships
- Creating foundation for multiple related variants

**Process**:
1. Create variant specification document
2. Update dependency mapping JSON for variant structure
3. Build project structure (import from CSV or duplicate+modify)
4. Execute MCP API calls to create dependencies
5. Set relative dates and verify timeline
6. Convert to template

**Example**: Creating "12-Week Module" variant
- Add Weeks 9-12 sections (4 new sections)
- Add 28 new tasks (storyboarding + builds)
- Update dependency_mapping.json with 21 new dependencies
- Execute MCP API calls for 73 total dependencies
- Verify cascading pattern extends through Week 12
- **Time**: 30 minutes

**Method 3: Hybrid Approach (15 minutes per variant)**

**Best for**:
- Creating variant family (3+ related variants)
- Shared base structure with variant-specific additions
- Balance between speed and control

**Process**:
1. Create first variant via API (comprehensive, 30 min)
2. Duplicate first variant for subsequent variants (5 min each)
3. Use API for variant-specific additions only (5 min)
4. Total time for 3 variants: 30 + 15 + 15 = 60 min (20 min avg)

**Example**: Creating content type variants (Theory-Heavy, Skills-Based, Lab-Based)
- Create Theory-Heavy via API (30 min)
- Duplicate to Skills-Based, add skills-specific tasks via API (15 min)
- Duplicate to Lab-Based, add lab-specific tasks via API (15 min)

### Maintaining Multiple Template Versions

**Template inventory management**:

**Base template**:
- Name: "Asana Module Development Template - Standard 8-Week"
- Owner: Andrew
- Usage: Default for most modules
- Maintenance: Quarterly review, update as process evolves

**Variant templates**:
- Name pattern: "[Type] Module Template - [Variant]"
- Examples:
  - "12-Week Module Template - Extended"
  - "8-Week Module Template - No Film Shoots"
  - "4-Week Module Template - Micro-Credential"
- Owner: Designated per variant
- Usage: Specific use cases documented
- Maintenance: Sync with base template updates

**Documentation requirements** (per variant):
- Variant specification document
- Dependency mapping JSON
- Setup instructions (variant-specific)
- Decision criteria (when to use this variant)
- Maintenance log (changes over time)

**Version control strategy**:
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
│   │   └── setup_instructions_12week.md
│   ├── no_film_shoots/
│   │   ├── spec_no_film.md
│   │   └── setup_instructions_no_film.md
│   └── micro_credential/
│       ├── spec_micro.md
│       └── dependency_mapping_micro.json
```

**Template evolution workflow**:

**When base template changes**:
1. Document change in base template specification
2. Assess impact on each variant
3. Update affected variants (duplication or API)
4. Test variant changes with dummy projects
5. Communicate changes to team
6. Update variant documentation

**Example**: Base template adds "Mid-module Check-in" task after Week 4
- Impact assessment: All variants need this task
- Update: Add task to each variant template
- Dependency: Add dependency (Week 4 Build → Mid-module Check-in → Week 5 Storyboard)
- Testing: Create dummy project from each variant, verify new task flows correctly
- Communication: Email team about new mid-module checkpoint in all templates

**Quarterly maintenance cycle**:
- **Month 1**: Review base template usage and feedback
- **Month 2**: Update base template based on learnings
- **Month 3**: Propagate changes to variants, test, deploy

---

## Chapter 8: Troubleshooting & Tips

### Common Issues and Solutions

**Issue 1: Tasks Won't Mark Complete (Dependency Blocked)**

**Symptom**: You try to mark a task complete, but Asana shows "This task is blocked by incomplete dependencies"

**Diagnosis**:
1. Click on the blocked task
2. Check Dependencies section in task details
3. Identify which prerequisite task(s) are incomplete

**Solution**:
- Complete prerequisite task(s) first
- If prerequisite is incorrectly blocking, remove dependency (see Chapter 4)
- If you need to bypass (emergency only), contact Senior LD for guidance

**Prevention**: Review Timeline view regularly to see upcoming dependencies and complete tasks in proper sequence.

**Issue 2: Dates Don't Match Expected Timeline**

**Symptom**: Task dates seem wrong, or timeline is shorter/longer than 17-18 weeks

**Diagnosis**:
1. Check Launch Date custom field at project level
2. Verify it's set to "Ready for Launch" date (not Go Live date)
3. Check if someone modified task dates manually (overriding relative dates)

**Solution**:
- Correct Launch Date if wrong
- All dates will recalculate automatically
- If manual dates were set, remove manual dates to revert to auto-calculation
- Project Settings → Dates → Reset to template defaults

**Prevention**: Set Launch Date correctly at project creation. Communicate changes if Launch Date must adjust mid-project.

**Issue 3: Team Members Not Receiving Notifications**

**Symptom**: LD or LT doesn't know when their task is ready to start

**Diagnosis**:
1. Check if team member is assigned to task
2. Verify Asana notification settings
3. Confirm project-level custom fields populated (auto-assignment)

**Solution**:
- Assign team members manually to tasks if auto-assignment failed
- Ask team members to check Asana notification preferences
- Use Asana's "Add followers" feature to ensure key people notified

**Prevention**: Set project-level custom fields (Learning Designer, Learning Technologist, etc.) at project creation. These auto-populate task assignments.

**Issue 4: Film Shoot Dependencies Incorrect**

**Symptom**: Film shoots blocked by builds instead of storyboards

**Diagnosis**: Template created before Andrew's clarification (Oct 2025)

**Solution**:
1. Open "Film shoot - first batch" task
2. Remove dependency on "Week 4 - Build"
3. Add dependency on "Week 4 - Storyboard Final draft agreed"
4. Repeat for "Film shoot - second batch" (Week 8 Storyboard)

**Prevention**: Use template version 2.0 or later (dependencies corrected). If using older template, apply this fix.

**Issue 5: Academic Review Falls on Holiday Week**

**Symptom**: Weeks 3-8 review scheduled during Christmas, Thanksgiving, summer break, etc.

**Diagnosis**: Timeline calculation doesn't account for holiday periods

**Solution**:
- Identify holiday conflict when setting Launch Date
- Option A: Shift Launch Date to avoid holiday in review period
- Option B: Coordinate with Academic Reviewer for early/late review window
- Option C: Add holiday buffer to timeline (extend development phase)

**Prevention**: When setting Launch Date, check where Weeks 3-8 review falls (typically 14 days before Ready for Launch). Adjust if conflicts with known holidays.

**Issue 6: SME Availability Conflicts**

**Symptom**: SME unavailable during scheduled storyboarding weeks

**Diagnosis**: SME commitments not checked during project setup

**Solution**:
- Identify SME availability gaps during kickoff meeting
- Adjust Launch Date to accommodate SME schedule
- Or: Plan storyboarding weeks to skip SME unavailable periods
- Communicate timeline adjustment to all stakeholders

**Prevention**: Confirm SME availability for all 8 storyboarding weeks during kickoff. Block SME calendar time.

### When to Modify vs Follow the Template

**Follow the template strictly when**:
- First time using template (learn the workflow)
- Standard 8-week module with normal timeline
- No special client requirements
- Team is new to systematized workflow

**Modify the template when**:
- Client has specific approval gates not in template
- Integration with client systems (requires additional tasks)
- Compliance requirements (additional QA checkpoints)
- **After** experiencing full workflow once (you understand implications)

**Modifications that are usually safe**:
- Adding custom fields for project tracking
- Adding supplemental QA tasks (doesn't remove existing quality gates)
- Adjusting task descriptions for client terminology
- Adding client-specific sections (e.g., "Integration Testing")

**Modifications that are risky**:
- Removing dependencies (breaks workflow enforcement)
- Removing review tasks (compromises quality)
- Shortening Week 1 from 10 days (increases rework risk)
- Changing cascading build pattern (creates resource conflicts)

**Before modifying**:
1. Understand WHY the current structure exists
2. Document your proposed change and rationale
3. Discuss with Andrew or Senior LD
4. Test on project copy, not production project
5. Monitor for unintended consequences

### Escalation Path When Blocked

**Level 1: Self-Resolution (try first, 15 minutes)**
- Review task dependencies in Timeline view
- Check FAQ.md and this tutorial for guidance
- Search Asana help docs for technical questions
- Review project description for project-specific notes

**Level 2: Team Lead (same-day response)**
- **For workflow questions**: Contact Senior LD (Nicole)
  - Examples: "Should we add extra review?", "How to handle this scenario?"
- **For SME coordination**: Contact assigned LD
  - Examples: "SME not responding", "Storyboard feedback unclear"
- **For technical Asana issues**: Contact Senior LD
  - Examples: "Can't mark task complete", "Dependencies not working"

**Level 3: Template Owner (1-2 day response)**
- **For template structure questions**: Contact Andrew
  - Examples: "Should we create a variant?", "Is this dependency correct?"
- **For strategic decisions**: Contact Andrew or Account Manager
  - Examples: "Client wants major timeline change", "Different module structure needed"

**Emergency escalation** (same-day response needed):
- **Blocker affecting launch date**: Immediate escalation to Senior LD and Andrew
- **Client relationship at risk**: Immediate escalation to Account Manager and Andrew
- **Technical failure**: Immediate escalation to Senior LD
- **Resource conflict**: Immediate escalation to Senior LD for reallocation

**How to escalate effectively**:
1. Document the issue clearly (screenshots help)
2. Describe what you've tried already
3. State impact (e.g., "Blocks Week 3 storyboard, affects launch date")
4. Propose potential solutions
5. Request specific help needed

**Example escalation message**:
"Week 2 Build task blocked by incomplete dependency on Week 1 Build, but Week 1 Build is marked complete. Timeline view shows dependency line still red. Tried: refreshing browser, checking task completion. Impact: LT cannot start Week 2 Build (due today), Week 3 at risk. Request: Technical support to resolve Asana dependency issue. Attached screenshot."

### Tips from Experienced Template Users

**Tip 1: Set Up Email Digests**
Configure Asana to send daily digest of:
- Tasks due today
- Tasks completed yesterday
- Tasks coming due in next 3 days

**Why**: Keeps team aligned without constant Asana checking. Morning digest = daily prioritization.

**Tip 2: Use Asana Mobile for Status Updates**
Learning Technologists report: Updating task progress from mobile during builds is faster than desktop.

**Why**: Mark subtasks complete immediately as you finish them. Triggers next task notifications faster.

**Tip 3: Comment on Handoff Tasks**
When completing a task that hands off to another team member, add comment:
"Storyboard complete and ready for build. Build notes: [specific guidance for LT]. Files in [location]."

**Why**: Reduces back-and-forth questions. Handoff includes context, not just task completion.

**Tip 4: Review Timeline View Weekly**
Every Monday, open Timeline view and:
- Confirm tasks on track for this week
- Identify potential bottlenecks next week
- Check dependency chains for upcoming work

**Why**: Proactive bottleneck identification. Adjust before delays cascade.

**Tip 5: Document Filming Approach Early**
During Week 1, confirm and document filming approach in Film Shoot task descriptions. Include:
- Chosen option (Studio/Loom/AI)
- SME availability confirmed for film dates
- Equipment or software requirements
- Contact person for Digital Learning Team coordination

**Why**: Prevents last-minute scrambling when Film Shoot tasks arrive. Everyone knows the plan.

**Tip 6: Batch Asana Updates**
Instead of marking tasks complete one-by-one throughout the day, batch updates:
- Mark multiple subtasks complete at once (morning and end of day)
- Add all day's comments in one Asana session

**Why**: Reduces notification noise for team. More focused work time, less Asana context-switching.

**Tip 7: Use Custom Fields for Tracking**
Add project-specific custom fields for tracking:
- "Risk Level" (Low/Medium/High) for early warning
- "Client Satisfaction" (track SME engagement)
- "Innovation Level" (experiment tracking)

**Why**: Surface insights for project retrospectives. Data-driven improvement.

**Tip 8: Celebrate Milestones**
When completing major milestones (MPD Finalised, Week 4 Review, Ready for Launch):
- Add celebratory comment in Asana task
- Tag team members who contributed
- Share with broader team (email or Slack)

**Why**: Maintains team morale through long 17-week projects. Recognition matters.

**Tip 9: Keep Dummy Test Project**
Create a "TEST - Module Practice" project from template. Use it to:
- Practice workflow before real module
- Test dependency changes before applying to production
- Train new team members

**Why**: Safe experimentation environment. Learn without affecting real client work.

**Tip 10: Screenshot Critical Moments**
Capture screenshots of:
- Completed review feedback
- Client approval emails
- Milestone completions
- Quality gate sign-offs

Attach screenshots to relevant Asana tasks.

**Why**: Documentation for future reference. Proof of approval. Audit trail.

---

## Conclusion: Your Journey from Beginner to Power User

**What you've learned**:

**Chapter 1**: The template solves workflow chaos through 52 automated dependencies creating reliable project management.

**Chapter 2**: Creating a module in 6 steps (10 minutes setup) with timeline auto-calculation from Launch Date anchor.

**Chapter 3**: Three filming options (Studio/Loom/AI), variable launch buffers (not always 66 days), supplemental QA strategies.

**Chapter 4**: Dependency management, cascading builds, film shoot → storyboard relationship, Timeline view mastery.

**Chapter 5**: Week 1's 10-day investment (vs 5 days for other weeks) establishes patterns that accelerate Weeks 2-8.

**Chapter 6**: "Ready for Launch" (Andrew's deliverable) vs "Go Live" (client timing), final review workflow, post-launch monitoring.

**Chapter 7**: When to create variants (3+ modules with same pattern), duplication vs API approaches, variant maintenance.

**Chapter 8**: Common issues (dependencies, dates, notifications), escalation path, tips from experienced users.

**Your next steps**:

**Immediate**: Create your first module from the template
- Apply the 6-step process from Chapter 2
- Make the three critical decisions from Chapter 3
- Monitor dependencies as you work (Chapter 4)

**Short-term**: Experience full workflow once
- Complete at least one full module (all 17-18 weeks)
- Apply tips from Chapter 8 as you discover them
- Document what works for your work style

**Medium-term**: Optimize your practice
- Identify variant needs if patterns emerge (Chapter 7)
- Share learnings with team
- Contribute improvements to base template

**Long-term**: Become template advocate
- Train new team members
- Refine processes based on experience
- Help evolve template for future needs

**Resources for continuing education**:
- **FAQ.md**: Quick answers to specific questions
- **TEMPLATE_VARIANTS.md**: Deep dive on creating specialized versions
- **Specification v2.0**: Complete technical reference (1550 lines)
- **Team leads**: Andrew (template), Nicole (process), your LD colleagues (practical tips)

**Remember**: This template represents 18 months of Learning Design Solutions experience systematized into repeatable workflow. You're building on proven patterns, not starting from scratch.

**Welcome to systematized module development. Your future self (and your team) will thank you for investing time to learn this workflow properly.**

---

## Document Metadata

**Version**: 1.0
**Created**: October 2025
**Tutorial Length**: ~2800 words
**Reading Time**: 45-60 minutes
**Applies To**: Asana Module Development Template v2.0 (52 API-created dependencies)
**Status**: Complete tutorial for team member training

**Related Documentation**:
- **QUICKSTART.md**: 7-step setup for first-time users (10 min read)
- **FAQ.md**: Common questions organized by category (reference)
- **TEMPLATE_VARIANTS.md**: Creating specialized template versions (30 min read)
- **Specification v2.0**: Complete technical reference (comprehensive)

**Feedback**: Share tutorial feedback with Andrew for continuous improvement.
