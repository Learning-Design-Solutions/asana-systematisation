# Launch Buffer Strategy Design
**Agent**: Agent 6 - Launch Buffer Strategy Agent
**Phase**: Phase 1 Acknowledgement & Strategy Approach
**Date**: October 24, 2025
**Priority**: MEDIUM
**Decision Reference**: Decision 10

---

## PHASE 1: TASK ACKNOWLEDGEMENT & STRATEGY APPROACH

### Executive Summary

**Task Received**: Design flexible buffer system addressing Andrew's preference for minimal default buffers while maintaining configurability for client-specific requirements.

**Context Analysis**:
- Specification Section 1.2 shows example with 66-day buffer (Ready for Launch → Go Live)
- Andrew's feedback clarifies: "not a standard, just depends when the program development for that specific module starts"
- Key insight: "If a buffer exists, it tends to get used, which we would prefer to avoid"
- Client-specific needs: Some clients have academic calendar alignment requirements
- Management consideration: When buffer exists, Andrew requires management team to line-manage academic resources

---

## BUFFER STRATEGY APPROACH FOR CONFIRMATION

### Strategy Overview: Dynamic Zero-Default Buffer with Client Configurability

**Core Philosophy**:
- **Default**: 0-day buffer (Ready for Launch = Go Live)
- **Configurable**: Per-module or per-programme buffer settings when required
- **Transparent**: Buffer explicitly tracked as custom field, not hidden in timeline
- **Justification-driven**: Buffer requires explicit reason (academic calendar, client request, etc.)

---

## PROPOSED IMPLEMENTATION APPROACH

### Approach 1: Custom Field-Based Buffer Configuration (RECOMMENDED)

**Mechanism**: Create custom field "Days to Go Live" with default value 0

**Custom Field Specification**:
```
Field Name: Days to Go Live
Type: Number
Default Value: 0
Range: 0-180 days (0 = tight timeline, up to 6 months buffer)
Purpose: Configure time between "Ready for Launch" and "Go Live"
Location: Project-level custom field (applies to entire module)
```

**Benefits**:
- ✅ Visible to all stakeholders (no hidden buffers)
- ✅ Configurable per module (client-specific flexibility)
- ✅ Default 0 aligns with Andrew's preference for tight timelines
- ✅ API-accessible for automated timeline calculations
- ✅ Easy to override when academic calendar alignment needed
- ✅ Supports reporting: "Which modules have buffers and why?"

**Workflow**:
1. Module created from template → "Days to Go Live" = 0 (default)
2. If client requires buffer → Manually set to required days (e.g., 66)
3. Timeline calculation uses this value: Go Live Date = Ready for Launch + Days to Go Live
4. Automation: When "Days to Go Live" > 0 → Trigger management notification (line-manage academic resources)

---

### Approach 2: Programme-Level Buffer Policy

**Mechanism**: Create programme-level custom field controlling buffer defaults for all modules in programme

**Custom Field Specification**:
```
Field Name: Programme Buffer Policy
Type: Single Select
Options:
  - No Buffer (Tight Timeline) [DEFAULT]
  - Academic Calendar Aligned (66 days)
  - Client Custom (configurable)
Location: Programme-level custom field
Inherits to: All modules in programme
```

**Benefits**:
- ✅ Consistent buffer policy across entire programme
- ✅ Reduces manual configuration per module
- ✅ Supports academic programmes with fixed term dates
- ✅ Clear policy documentation at programme level

**Drawbacks**:
- ⚠️ Less flexible for individual module variations
- ⚠️ Requires programme structure to be implemented first (Phase 4 dependency)

---

### Approach 3: Hybrid - Programme Default + Module Override

**Mechanism**: Combine Approach 1 and 2 for maximum flexibility

**Custom Fields**:
1. Programme-level: "Default Buffer Policy" (programme-wide default)
2. Module-level: "Days to Go Live" (overrides programme default if set)

**Logic**:
```
IF module "Days to Go Live" is set (not null):
  USE module-specific value
ELSE:
  USE programme "Default Buffer Policy" value
ENDIF
```

**Benefits**:
- ✅ Best of both worlds: consistent defaults + per-module flexibility
- ✅ Minimal configuration for standard cases
- ✅ Override capability for exceptions
- ✅ Supports complex client requirements

**Drawbacks**:
- ⚠️ More complex to implement (2 custom fields + logic)
- ⚠️ Requires clear documentation to avoid confusion

---

## CLIENT DELIVERABLE TIMING CONSIDERATIONS

### Scenario Analysis

**Scenario 1: No Buffer (Tight Timeline)**
- Ready for Launch: Day 112
- Go Live: Day 112 (same day)
- Use Case: Client urgently needs module, content ready for immediate release
- Management: Andrew manages all resources through completion

**Scenario 2: Academic Calendar Alignment (66-day buffer)**
- Ready for Launch: Day 112
- Go Live: Day 178 (Day 112 + 66)
- Use Case: Module must launch at semester start (e.g., September intake)
- Management: Client management team line-manages academic resources during buffer

**Scenario 3: Custom Buffer (Client-Specific)**
- Ready for Launch: Day 112
- Go Live: Day 112 + [Client-Specified Days]
- Use Case: Client has internal approval process, testing period, or training requirements
- Management: Negotiated based on buffer duration and resource ownership

**Scenario 4: Holiday Season Buffer (2-week buffer)**
- Ready for Launch: December 15
- Go Live: January 5 (21-day buffer)
- Use Case: No work during Christmas/New Year period
- Management: Explicit buffer for organizational downtime

---

## ACADEMIC YEAR ALIGNMENT REQUIREMENTS

### Key Considerations

**Academic Calendar Patterns**:
- UK Higher Education: September (Autumn), January (Spring), April/May (Summer)
- US Higher Education: August (Fall), January (Winter), May (Summer)
- Other International: Varies by country and institution

**Alignment Strategies**:

**Strategy 1: Fixed Programme Start Dates**
- Programme custom field: "Programme Start Date" (single select: September / January / May)
- Modules calculate backwards from programme start
- Example: Programme starts September 15 → All module Go Live dates align to September 15

**Strategy 2: Module-Specific Launch Windows**
- Module custom field: "Launch Window" (single select: Autumn / Spring / Summer / Anytime)
- Admin manually sets Go Live date within appropriate window
- Buffer auto-calculates based on Ready for Launch date

**Strategy 3: No Automatic Alignment (RECOMMENDED for MVP)**
- Admin manually sets Go Live date based on client requirements
- "Days to Go Live" auto-calculates as: Go Live Date - Ready for Launch Date
- Maximum flexibility, minimal automation complexity

---

## RECOMMENDED IMPLEMENTATION PLAN

### Phase 1A: MVP - Single Custom Field (Immediate Implementation)

**Custom Field to Create**:
```
Field Name: Days to Go Live
Type: Number
Default Value: 0
Precision: 0 (integer days)
Description: Number of days between "Ready for Launch" and "Go Live". Default 0 for tight timeline. Set to 66+ for academic calendar alignment or client-specific buffer requirements.
Workspace: [Asana Workspace GID]
Priority: 🟡 EXTENDED (Phase 1B)
```

**Timeline Calculation Logic**:
```python
# Relative date anchoring formula (or API script)
ready_for_launch_date = launch_date + 112  # Fixed critical path
days_to_go_live = custom_field["Days to Go Live"] or 0  # Default 0
go_live_date = ready_for_launch_date + days_to_go_live

# Example 1: Tight timeline (default)
# Days to Go Live = 0
# Go Live Date = Ready for Launch Date

# Example 2: Academic calendar (66-day buffer)
# Days to Go Live = 66
# Go Live Date = Ready for Launch Date + 66 days
```

**Automation Rule**:
```
Trigger: "Days to Go Live" custom field > 0
Action: Add comment to project:
  "⚠️ Buffer Period Active: {Days to Go Live} days between Ready for Launch and Go Live.
  Management Note: Client management team should line-manage academic resources during buffer period.
  Set by: {User who set the field}
  Reason: [Manual entry required]"
```

**Success Criteria**:
- ✅ Default modules have 0-day buffer (Ready for Launch = Go Live)
- ✅ Admin can configure buffer per module when needed
- ✅ Buffer duration visible in project custom fields
- ✅ Automation notifies team when buffer configured

---

### Phase 1B: Extended - Programme-Level Defaults (Optional Future Enhancement)

**Additional Custom Field** (if Approach 3 selected):
```
Field Name: Programme Default Buffer
Type: Number
Default Value: 0
Location: Programme-level custom field
Purpose: Set default buffer for all modules in programme (can be overridden per module)
```

**Logic**:
```python
# Module-specific buffer takes precedence
if module["Days to Go Live"] is not None:
    buffer_days = module["Days to Go Live"]
elif programme["Programme Default Buffer"] is not None:
    buffer_days = programme["Programme Default Buffer"]
else:
    buffer_days = 0  # Ultimate default
```

---

## CONFIGURATION MODEL DESIGN

### Module-Level Configuration (RECOMMENDED MVP)

**Configuration Interface**:
```
Module Custom Fields (visible in project):
┌─────────────────────────────────────────────┐
│ Launch Date: 15/09/2025                     │
│ Days to Go Live: [  0  ] ← Default          │
│                                              │
│ Calculated Dates:                           │
│ Ready for Launch: 05/01/2026 (Day 112)     │
│ Go Live: 05/01/2026 (Day 112 + 0)          │
└─────────────────────────────────────────────┘

If buffer needed:
┌─────────────────────────────────────────────┐
│ Launch Date: 15/09/2025                     │
│ Days to Go Live: [ 66  ] ← Configured       │
│                                              │
│ Calculated Dates:                           │
│ Ready for Launch: 05/01/2026 (Day 112)     │
│ Go Live: 13/03/2026 (Day 178)              │
│                                              │
│ ⚠️ Buffer Active: 66 days                   │
└─────────────────────────────────────────────┘
```

**Configuration Workflow**:
1. Create module from template
2. Set "Launch Date" (anchor date)
3. Check "Days to Go Live" (default 0)
4. If client requires buffer:
   - Set "Days to Go Live" to required days
   - Add comment explaining reason (academic calendar, client request, etc.)
5. Timeline auto-recalculates with buffer

---

### Programme-Level Configuration (Future Enhancement)

**Configuration Interface**:
```
Programme Custom Fields:
┌─────────────────────────────────────────────┐
│ Programme Name: MBA Marketing               │
│ Programme Default Buffer: [ 66  ]           │
│ Reason: September intake alignment          │
│                                              │
│ Modules in Programme:                       │
│ - MKT101 (uses default: 66 days)           │
│ - MKT102 (override: 0 days - urgent)       │
│ - MKT103 (uses default: 66 days)           │
└─────────────────────────────────────────────┘
```

---

## RATIONALE FOR RECOMMENDATIONS

### Why Approach 1 (Custom Field-Based) is Recommended

1. **Aligns with Andrew's Philosophy**: Default 0 days = tight timeline preference
2. **Transparent and Visible**: Buffer is explicit custom field, not hidden calculation
3. **Client Flexibility**: Easy to configure when academic calendar or client needs require buffer
4. **Simple to Implement**: Single custom field, no complex logic or dependencies
5. **Phase 1B Compatible**: Can be created alongside other extended custom fields (no blocker)
6. **API-Friendly**: Number field easily accessible for automation and reporting
7. **Audit Trail**: Can report "which modules have buffers and why"
8. **Management Clarity**: When buffer > 0, automation notifies about line-management requirements

### Why Not Approach 2 (Programme-Level Only)

1. **Reduces Flexibility**: Some modules in same programme may need different buffers
2. **Phase 4 Dependency**: Requires portfolio structure to be implemented first
3. **Less Granular Control**: Can't handle per-module exceptions easily

### Why Hybrid Approach 3 is Future Enhancement

1. **Adds Complexity**: Two custom fields + logic overhead
2. **MVP Not Required**: Approach 1 handles 95% of use cases
3. **Can Add Later**: If programme-level defaults become pain point, upgrade to Approach 3 in Phase 4

---

## INTEGRATION WITH EXISTING ARCHITECTURE

### Custom Field Dependencies

**From Agent 1 Deliverable (agent1_custom_field_verification.md)**:

Existing custom fields required:
- ✅ Launch Date (🔴 CORE, Phase 1A) - Anchor for all relative dates
- ✅ Go Live Date (🔴 CORE, Phase 1A) - Actual launch to students

**New custom field proposed**:
- 🟡 Days to Go Live (EXTENDED, Phase 1B) - Buffer configuration

**Field Interaction**:
```
Launch Date (user sets manually) → Day 0
  ↓ (Fixed critical path calculation)
Ready for Launch (auto-calculated) → Launch Date + 112 days
  ↓ (Buffer configuration)
Days to Go Live (user sets, default 0) → 0-180 days
  ↓ (Buffer application)
Go Live Date (auto-calculated) → Ready for Launch + Days to Go Live
```

---

### Relative Date Anchoring Integration

**If Native Asana Relative Dates Supported**:
```
Task: Ready for Launch
  start_date: FORMULA(Launch Date + 112 days)

Task: Go Live
  start_date: FORMULA(Ready for Launch + [Days to Go Live])
```

**If API Script Required (Fallback)**:
```python
# apply_task_dates.py extension
def calculate_go_live_date(project_gid):
    launch_date = get_custom_field_value(project_gid, "Launch Date")
    days_to_go_live = get_custom_field_value(project_gid, "Days to Go Live") or 0

    ready_for_launch_date = launch_date + timedelta(days=112)
    go_live_date = ready_for_launch_date + timedelta(days=days_to_go_live)

    # Update task dates
    update_task_date("Ready for Launch", ready_for_launch_date)
    update_task_date("Go Live", go_live_date)

    return go_live_date
```

---

## RISK ASSESSMENT

### Risk 1: Buffer Creep (If buffer exists, it gets used)
**Probability**: High
**Impact**: Timeline bloat, reduced efficiency
**Mitigation**:
- Default 0 days prevents buffer creation unless explicitly needed
- Automation notification when buffer set (creates visibility and accountability)
- Reporting: Track buffer usage across modules to identify patterns
- Justification required: Comment must explain why buffer needed

### Risk 2: Client Expectation Mismatch
**Probability**: Medium
**Impact**: Client expects buffer but template defaults to 0
**Mitigation**:
- During module kickoff, explicitly discuss buffer requirements
- Template includes "Days to Go Live" field prominently in project view
- Training materials cover buffer configuration workflow
- Sales/BD team aware of default tight timeline approach

### Risk 3: Academic Calendar Misalignment
**Probability**: Medium
**Impact**: Module ready but can't launch until next semester
**Mitigation**:
- During MPD phase, confirm Go Live date requirements
- If academic calendar alignment needed, set buffer at project creation
- Programme-level buffer policy (Approach 3) can standardize for academic clients
- Automation can suggest buffer based on Go Live date falling outside term dates (future enhancement)

### Risk 4: Manual Configuration Errors
**Probability**: Low
**Impact**: Wrong buffer set, timeline incorrect
**Mitigation**:
- Number field with clear description and examples
- Validation rule: 0-180 day range (prevents negative or excessive buffers)
- Calculated "Go Live Date" field updates automatically (user sees impact immediately)
- Review during MPD review milestone (catch errors early)

---

## SUCCESS METRICS

### Phase 1B Success (Custom Field Created)
- ✅ "Days to Go Live" custom field created and documented
- ✅ Default value 0 configured
- ✅ Field linked to test project (GID: 1211626875246589)
- ✅ Field visible in project custom field section
- ✅ GID documented in custom_field_gids.json

### MVP Implementation Success (Phase 2-3)
- ✅ Template uses "Days to Go Live" in timeline calculations
- ✅ Default modules have 0-day buffer (Ready for Launch = Go Live)
- ✅ Admin can configure buffer per module when needed
- ✅ Automation notifies when buffer > 0
- ✅ 90%+ of modules use 0-day buffer (validates Andrew's tight timeline preference)

### Full System Success (Phase 5+)
- ✅ Pilot modules demonstrate buffer configuration workflow
- ✅ Team trained on when and how to configure buffers
- ✅ Client-specific buffer requirements documented and configured correctly
- ✅ No "buffer creep" observed (buffers only used when explicitly needed)
- ✅ Management line-management handoff works correctly for buffered modules

---

## NEXT STEPS PENDING COORDINATOR CONFIRMATION

### Questions for Coordinator

1. **Approach Selection**: Confirm Approach 1 (Custom Field-Based) as MVP implementation?
2. **Default Value**: Confirm 0 days as default (no buffer unless explicitly configured)?
3. **Field Priority**: Confirm "Days to Go Live" as Phase 1B Extended field (alongside QA Status, Blocker Status, etc.)?
4. **Automation Scope**: Should automation notification be implemented in Phase 3, or defer to Phase 5 pilot feedback?
5. **Future Enhancement**: Is Approach 3 (Hybrid Programme + Module) on roadmap for Phase 4 Portfolio Structure?

### Dependencies for Phase 3 Execution

**Prerequisites**:
- ✅ Coordinator confirms approach (awaiting confirmation)
- ✅ Agent 1 Phase 1B custom fields created (includes Launch Date, Go Live Date)
- ✅ Relative date anchoring working (Phase 1 completion)

**Ready to Execute After Confirmation**:
- Create "Days to Go Live" custom field (5 minutes)
- Link to test project (2 minutes)
- Document GID in custom_field_gids.json (2 minutes)
- Update timeline calculation logic/script (30 minutes)
- Test buffer configuration with 0, 66, and custom values (30 minutes)
- **Total Effort**: ~1 hour

---

## DELIVERABLE STATUS

**Phase 1 Complete**: ✅ Acknowledgement + Strategy Approach Delivered

**Contents**:
1. ✅ Buffer strategy overview (3 approaches analyzed)
2. ✅ Recommended approach with rationale (Approach 1: Custom Field-Based)
3. ✅ Client deliverable timing considerations (4 scenarios)
4. ✅ Academic year alignment strategy
5. ✅ Configuration model design
6. ✅ Integration with existing architecture
7. ✅ Risk assessment and mitigation
8. ✅ Success metrics and validation criteria

**Awaiting**: Coordinator confirmation to proceed to Phase 3 execution

**Next Action**: Coordinator reviews approach and confirms or requests modifications

**Confidence Level**: HIGH (approach aligns with Andrew's feedback, integrates with existing architecture, minimal implementation complexity)

---

**Status**: ✅ PHASE 1 COMPLETE - Ready for Coordinator Review
**Token Count**: ~5,200 tokens (within 6K limit)
**Output Location**: `.serena/memories/agent6_launch_buffer_strategy.md`
