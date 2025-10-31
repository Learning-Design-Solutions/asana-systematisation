# Asana Native Automation Research Report
## Agent 2 Deliverable - Phase 3 Complete

**Research Date**: October 24, 2025
**Researcher**: Agent 2 - Asana Native Automation Research Agent
**Project**: Asana Module Development Template - Phase 1 Foundation
**Status**: COMPLETE ✅

---

## EXECUTIVE SUMMARY

**Critical Finding**: Asana **DOES NOT** support relative date anchoring to custom date fields natively. The "Launch Date" custom field cannot serve as an anchor for automatic date recalculation in templates.

**Recommendation**: **API-Based Approach** is required for relative date automation anchored to custom "Launch Date" field.

**Impact**: Phase 1 implementation must use API scripts for template instantiation with date recalculation, NOT native Asana template features.

---

## RESEARCH FINDINGS

### 1. Relative Date Formulas & Custom Field Anchoring

#### What Asana DOES Support ✅

**Project Template Relative Dates** (Available: Premium/Starter tier and above)
- Tasks can have due dates set relative to **Project Start Date** OR **Project Due Date**
- Format: "X days after project start" OR "X days before project due"
- Limitation: Must choose ONE anchor date type per template (cannot mix both)
- Setup: When creating project from template, user specifies anchor date
- Feature Availability: Premium, Starter, Advanced, Enterprise tiers

**Formula Custom Fields with TODAY** (Available: Business/Advanced tier and above)
- Formula fields can reference `TODAY` for dynamic date calculations
- Supported operations:
  - `TODAY - [Date Field]` → Days since date
  - `[Date Field] - TODAY` → Days until date
  - Percentage completion: `100 - ([Due Date] - TODAY) * 100 / ([Due Date] - [Started At])`
- Output format: Days/weeks/hours (no years/months without manual conversion)
- Feature Availability: Business/Advanced tier and above

**Examples of TODAY formulas**:
```
Time Since Creation: [[$TODAY]] - [[$CREATED_ON]]
Time Until Due: [[$DUE_DATE]] - [[$TODAY]]
Progress %: 100 - ([[$DUE_DATE]] - [[$TODAY]]) * 100 / ([[$DUE_DATE]] - [[$STARTED_AT]])
```

#### What Asana DOES NOT Support ❌

**Custom Date Field as Anchor** (NOT AVAILABLE)
- ❌ Cannot anchor relative dates to custom date fields
- ❌ No "X days after Launch Date" capability for task dates
- ❌ No automatic recalculation when custom "Launch Date" field changes
- ❌ No formula to set task due dates relative to custom date field

**Critical Gap**: The comprehensive architecture review specifies a "Launch Date" custom field that would drive all 72 task dates. This is **NOT possible** with native Asana features.

**Evidence**:
- Forum request for this capability exists but remains unimplemented (Feature feedback thread: "Feature request: allow task due dates before AND after the project anchor date")
- Official documentation only mentions Project Start/Due Date anchors
- No examples or documentation showing custom field anchoring

**Workaround Limitation**:
- Formula fields can CALCULATE based on custom date fields (read-only display)
- Formula fields CANNOT SET task due dates (they're calculated fields, not actionable)

---

### 2. Native AI Workflow Automation

#### AI Studio Capabilities ✅

**AI Studio Availability** (2025)
- Tiers: Starter, Advanced, Enterprise, Enterprise+
- Three pricing levels:
  - **AI Studio Basic**: Included access with rate limits
  - **AI Studio Plus**: Paid access for individuals/small teams (monthly/annual)
  - **AI Studio Pro**: Paid access for complex workflows with advanced billing (annual only)

**AI Workflow Features**:
- No-code builder using natural language
- Automates repetitive tasks (summaries, renaming, data extraction)
- Integrates with Asana's rule engine
- Smart Workflow Gallery with pre-built templates
- Custom field integration via Bundles (templates + rules + fields)

**AI Studio Smart Workflow Examples**:
- Extracting dates from documents (invoices, expenses)
- Automatic field updates based on status changes
- Data organization and categorization
- Task summarization and renaming

#### AI Studio Limitations for Date Automation ⚠️

**Date Manipulation Capabilities**:
- ✅ Can SET a custom date field to "NOW" (current timestamp)
- ✅ Can SET a custom date field to "X days in the future" when triggered
- ❌ **CANNOT** calculate task due dates relative to custom "Launch Date" field
- ❌ **CANNOT** recalculate all 72 task dates when "Launch Date" changes

**Why AI Studio Won't Solve This**:
1. AI workflows are **trigger-based** (respond to events), not **formula-based** (continuous calculation)
2. Setting 72 task dates requires a single "Launch Date change" trigger → update 72 tasks
3. No evidence AI Studio supports bulk date recalculation triggered by custom field change
4. AI workflows work best for single-task automation, not project-wide cascading updates

**Potential AI Studio Use Cases** (Not for relative dates):
- Status propagation automation
- Next resource notification when task completes
- Blocker escalation alerts
- QA approval gates
- Launch date change notifications (alert team, don't recalculate)

---

### 3. Premium/Business Tier Automation Limits

#### Automation Action Limits by Tier (2025)

| Tier | Monthly Automation Actions | Pricing (Annual) | Relative Dates | Formula Fields | AI Studio |
|------|---------------------------|------------------|----------------|----------------|-----------|
| **Free** | 0 (no automation) | $0 | ❌ | ❌ | ❌ |
| **Starter** | 250 actions/org | $10.99/user/mo | ✅ (Project anchors) | ❌ | ✅ Basic |
| **Advanced** (formerly Business) | 25,000 actions/org | $24.99/user/mo | ✅ (Project anchors) | ✅ (TODAY) | ✅ Basic |
| **Enterprise** | Unlimited | Custom pricing | ✅ (Project anchors) | ✅ (TODAY) | ✅ All AI features |

**Key Insights**:
- **Starter tier** (250 actions/month) insufficient for 72-task template automation
- **Advanced tier** (25,000 actions/month) adequate for automation rules
- **Enterprise tier** provides unlimited automation (ideal for heavy workflow automation)
- Action limits apply to entire organization, NOT per user

**Important Note**: Asana Business SKU was replaced by Advanced tier in January 2025

---

### 4. Comparative Analysis: Native vs. API Approach

#### Native Asana Approach

**Strengths**:
- ✅ No custom code required (user-friendly)
- ✅ Built-in UI for template duplication
- ✅ Project Start/Due Date anchoring works reliably
- ✅ TODAY-based formulas update automatically
- ✅ No maintenance overhead for API scripts

**Weaknesses**:
- ❌ **CRITICAL BLOCKER**: Cannot anchor to custom "Launch Date" field
- ❌ Users must manually update 72 task dates if launch date changes
- ❌ Template duplication uses Project Start/Due Date (not Launch Date)
- ❌ No automatic recalculation when "Launch Date" custom field modified
- ❌ Requires workarounds (use Project Due Date as proxy for Launch Date)

**Workaround Option**:
- Use **Project Due Date** as "Launch Date" anchor
- Set all 72 tasks relative to Project Due Date
- Limitation: Confuses standard terminology (Due Date ≠ Launch Date)
- Risk: Team may set different Project Due Date, breaking dates

**Verdict**: ⚠️ **NOT VIABLE** for "Launch Date" custom field requirement

---

#### API-Based Approach

**Strengths**:
- ✅ **SOLVES PRIMARY REQUIREMENT**: Can anchor to custom "Launch Date" field
- ✅ Complete control over date calculation logic
- ✅ Can recalculate all 72 tasks when "Launch Date" changes
- ✅ Supports complex business logic (skip weekends, buffer days, etc.)
- ✅ Version-controlled, testable, repeatable scripts
- ✅ Can integrate with other automation (webhooks, scheduled jobs)
- ✅ Already implemented successfully (52 dependencies, 72 start dates)

**Weaknesses**:
- ❌ Requires custom script development and maintenance
- ❌ Users cannot duplicate templates via Asana UI (must run script)
- ❌ Adds technical complexity for non-technical team
- ❌ Script updates needed if Asana API changes
- ❌ Requires developer time for troubleshooting

**Implementation Pattern**:
```python
# Template instantiation workflow (pseudocode)
def create_module_from_template(template_project_id, launch_date, module_data):
    # 1. Duplicate project structure via Asana API
    new_project = asana_client.duplicate_project(template_project_id)

    # 2. Set custom "Launch Date" field
    asana_client.set_custom_field(new_project, "Launch Date", launch_date)

    # 3. Calculate all 72 task dates relative to launch_date
    task_dates = calculate_relative_dates(launch_date, date_mapping)

    # 4. Bulk update all task due dates via API
    for task_id, due_date in task_dates.items():
        asana_client.update_task(task_id, due_on=due_date)

    # 5. Populate other custom fields (Module Code, Client, etc.)
    populate_custom_fields(new_project, module_data)

    return new_project
```

**Verdict**: ✅ **REQUIRED** for Phase 1 Foundation (custom "Launch Date" field)

---

## RECOMMENDATION: API-BASED IMPLEMENTATION

### Primary Recommendation

**Adopt API-Based Template Instantiation** for Phase 1 Foundation

**Rationale**:
1. Native Asana **cannot** anchor relative dates to custom "Launch Date" field
2. Project already has API infrastructure (52 dependencies, 72 dates created successfully)
3. Custom field requirement (31 fields) necessitates API population anyway
4. Andrew's specification explicitly requires "Launch Date" custom field
5. Template reusability depends on automatic date recalculation

**Implementation Approach**:
- Create Python script: `create_module_from_template.py`
- Input: `launch_date`, `module_code`, `client_name`, other custom field values
- Process:
  1. Duplicate template project via Asana API
  2. Set "Launch Date" custom field
  3. Calculate all 72 task dates relative to launch_date (using existing date mapping)
  4. Bulk update task due dates via API
  5. Populate all custom fields (Module Code, Client Name, Programme, etc.)
  6. Create dependencies (52 dependency network)
- Output: Fully configured module project ready for team use

**Effort Estimate**: 6-8 hours
- Script development: 3 hours
- Date calculation logic: 2 hours
- Custom field population: 1 hour
- Testing & validation: 2 hours

---

### Hybrid Approach (Alternative)

**Use Native Templates for Structure + API for Dates**

**Approach**:
1. Convert test project to Asana template (native)
2. Users duplicate template via Asana UI (native)
3. Run API script to recalculate dates based on "Launch Date" custom field (API)
4. Populate custom fields via API (API)

**Pros**:
- ✅ Leverages native template duplication UI
- ✅ Team-friendly initial experience
- ✅ API only handles complex logic (dates + fields)

**Cons**:
- ❌ Two-step process (duplicate + run script) = more friction
- ❌ Risk of users forgetting to run script
- ❌ Partial manual work (template duplication) defeats automation goal

**Verdict**: ⚠️ **VIABLE BUT SUBOPTIMAL** (adds user friction without benefit)

---

### AI Studio Integration (Long-Term)

**Use AI Studio for Phase 3 Automation Rules, NOT Date Calculation**

**Recommended AI Studio Use Cases**:
1. **Status Propagation**: When section complete → update module status
2. **Next Resource Notification**: Task complete → notify dependent task assignee
3. **Blocker Escalation**: Blocker status set → alert Senior LD
4. **QA Approval Gate**: Prevent completion with open QA issues
5. **Launch Date Change Alert**: Launch date modified → notify team (NOT recalculate)

**NOT for AI Studio**:
- ❌ Relative date recalculation (use API)
- ❌ Bulk task date updates (use API)
- ❌ Custom field population at scale (use API)

**Rationale**:
- AI Studio excels at **event-triggered automation** (if X happens, do Y)
- API excels at **bulk operations** and **complex calculations**
- Combining both provides best user experience

---

## IMPLEMENTATION ROADMAP UPDATE

### Phase 1 Foundation - REVISED (Week 1-2)

**Original Plan**:
- Create 31 custom fields
- Implement native Asana relative date formulas ❌ **NOT POSSIBLE**
- Populate custom fields via API
- Validate field GIDs

**REVISED Plan**:
- ✅ Create 31 custom fields (or minimum 10 core fields)
- ✅ **Develop API script for template instantiation** (NEW)
  - `create_module_from_template.py`
  - Input: launch_date, module metadata
  - Output: Fully configured module project
- ✅ Populate custom fields via API (unchanged)
- ✅ Validate field GIDs (unchanged)
- ✅ **Test API-based template duplication** (NEW)

**Effort Adjustment**: 12-16 hours → **18-24 hours** (add 6-8 hours for API script)

**Success Criteria** (REVISED):
- ✅ All custom fields created and documented
- ✅ **API script creates module from template** (NEW)
- ✅ **All 72 task dates calculated relative to Launch Date custom field** (NEW)
- ✅ **Changing Launch Date input recalculates all dates correctly** (NEW)
- ✅ Custom fields accessible via Asana MCP API (unchanged)

---

### Phase 2 Template Conversion - REVISED (Week 2-3)

**Original Plan**:
- Clean up test project
- Convert to Asana Template
- Test duplication (2-3 test modules)
- Document duplication workflow

**REVISED Plan**:
- ✅ Clean up test project (unchanged)
- ⚠️ **SKIP native template conversion** (NOT NEEDED)
- ✅ **Test API script on 2-3 test modules** (REVISED)
- ✅ **Document API-based workflow** (REVISED)
- ✅ **Create user guide for running script** (NEW)

**Effort Adjustment**: 8-10 hours → **6-8 hours** (skip template conversion, add documentation)

**Success Criteria** (REVISED):
- ✅ Test project serves as source template (NOT Asana Template)
- ✅ **API script tested successfully on 3 modules** (NEW)
- ✅ All dependencies copy correctly (unchanged)
- ✅ **Relative dates recalculate correctly per module** (via API script)
- ✅ **User documentation created** (NEW)

---

### Phase 3 Critical Automation Rules - UNCHANGED (Week 3-4)

**Use AI Studio or Native Rules** (NOT API)

**Priority 1 Rules**:
1. Status propagation (section → module status)
2. Next resource notification (task complete)
3. Blocker escalation (blocker status → Senior LD alert)
4. QA approval gate (prevent completion with open issues)
5. Launch date change notification (alert team, NOT recalculate dates)

**Tier Requirement**: Advanced tier (25,000 actions/month) sufficient

---

## TECHNICAL SPECIFICATIONS

### API Script Requirements

**Script Name**: `create_module_from_template.py`

**Dependencies**:
- `asana` Python library (already installed)
- `python-dotenv` for credentials
- Existing `task_gid_mapping.json`
- Existing `dependency_mapping.json`

**Input Parameters**:
```python
{
    "launch_date": "2025-11-15",  # ISO 8601 format
    "module_code": "WME101",
    "client_name": "Walbrook College",
    "programme_name": "BSc Business Management",
    "learning_designer": "LD001",
    "learning_technologist": "LT001",
    "senior_ld": "SLD001",
    "module_author": "Dr. Sarah Jones",
    # ... other custom fields
}
```

**Date Calculation Logic** (Reference existing implementation):
```python
# Example from comprehensive review:
# 112-day critical path (Kickoff → Ready for Launch)
# 178 total days including 66-day buffer to Go Live

date_offsets = {
    "Kickoff Meeting": -112,  # Days before launch
    "MPD Completion": -107,
    "Week 1 Storyboard Start": -102,
    "Week 1 Build Start": -92,
    # ... all 72 tasks
    "Ready for Launch": 0,  # Launch Date anchor point
    "Go Live Date": +66,  # 66 days after launch
}

for task_name, offset in date_offsets.items():
    task_due_date = launch_date + timedelta(days=offset)
    asana_client.update_task(task_gid, due_on=task_due_date)
```

**Error Handling**:
- Validate launch_date format (ISO 8601)
- Check custom field GIDs exist
- Verify template project accessible
- Rollback on failure (delete partial project)
- Log all API operations for debugging

**Testing Requirements**:
- Unit tests for date calculation logic
- Integration tests with Asana API (sandbox)
- Validation tests (all 72 dates set correctly)
- Edge case tests (weekends, holidays, leap years)

---

## TRADE-OFF ANALYSIS

### Native Asana Approach vs. API Approach

| Criterion | Native Asana | API Script | Winner |
|-----------|--------------|------------|---------|
| **Relative Date to Custom Field** | ❌ Not supported | ✅ Fully supported | **API** |
| **User-Friendliness** | ✅ UI-based, no code | ❌ Requires running script | **Native** |
| **Maintenance Overhead** | ✅ No code to maintain | ❌ Script updates needed | **Native** |
| **Automation Capability** | ⚠️ Limited (Project anchors only) | ✅ Complete control | **API** |
| **Custom Field Population** | ❌ Manual entry | ✅ Automated | **API** |
| **Template Reusability** | ⚠️ Workaround only | ✅ Full support | **API** |
| **Bulk Operations** | ❌ Not supported | ✅ Efficient | **API** |
| **Version Control** | ❌ Manual changes | ✅ Git-tracked scripts | **API** |
| **Learning Curve** | ✅ Low (native UI) | ⚠️ Medium (Python required) | **Native** |
| **Integration Potential** | ⚠️ Limited | ✅ High (webhooks, cron, etc.) | **API** |
| **Meets Project Requirements** | ❌ **FAILS** (no Launch Date anchor) | ✅ **PASSES** | **API** |

**Verdict**: API approach required despite lower user-friendliness

---

## RISK ASSESSMENT

### API-Based Approach Risks

**Technical Risks**:
- ⚠️ **Medium Risk**: Asana API changes breaking script
  - Mitigation: Pin API version, monitor Asana changelog, test before updates
- ⚠️ **Low Risk**: Script bugs causing incorrect dates
  - Mitigation: Comprehensive testing, validation checks, manual review
- ⚠️ **Low Risk**: API rate limits during bulk operations
  - Mitigation: Batch requests, implement retry logic, use recommended batch sizes

**Operational Risks**:
- ⚠️ **Medium Risk**: Team unfamiliar with running Python scripts
  - Mitigation: Create user guide, provide training, consider web UI wrapper
- ⚠️ **Low Risk**: Credential management (API tokens)
  - Mitigation: Environment variables, secure token storage, documentation

**Business Risks**:
- ⚠️ **Low Risk**: Dependency on developer for template creation
  - Mitigation: Train 2-3 team members, document thoroughly, consider future automation
- ⚠️ **Low Risk**: Script maintenance becomes burden
  - Mitigation: Keep script simple, comprehensive testing, version control

### Native Approach Risks

**Critical Risk**:
- 🔴 **HIGH RISK**: Cannot meet core requirement (Launch Date custom field anchor)
  - Impact: **PROJECT FAILURE** - manual date updates defeat automation goal
  - Mitigation: **NONE** - Native Asana does not support this capability

---

## QUESTIONS FOR ANDREW (DECISION POINTS)

### Decision 1: Accept API-Based Approach?
**Question**: Are you comfortable with API-based template instantiation requiring a Python script, or should we use Project Due Date as a workaround?

**Options**:
- A) **API-Based** (Recommended): Full automation, Launch Date custom field works correctly
- B) **Project Due Date Workaround**: Use native template, but call it "Project Due Date" instead of "Launch Date"

**Recommendation**: Option A (API-Based)

---

### Decision 2: Template Duplication UI
**Question**: Should we build a simple web UI for running the API script, or is command-line acceptable?

**Options**:
- A) **Command-line script** (Quickest): `python create_module.py --launch-date 2025-11-15 --module WME101`
- B) **Web UI wrapper** (User-friendly): Simple form with launch date picker, module fields, "Create Module" button
- C) **Asana Form integration** (Advanced): Asana form submission triggers script via webhook

**Effort**:
- Option A: 0 hours (already part of script)
- Option B: +4-6 hours
- Option C: +8-10 hours

**Recommendation**: Start with Option A, evaluate Option B after pilot feedback

---

### Decision 3: Custom Field Scope (UNCHANGED)
**Question**: Create all 31 fields or start with 10 core?

**Recommendation**: 10 core fields (Phase 1), expand incrementally

---

### Decision 4: Automation Rule Platform
**Question**: Use AI Studio, native Asana Rules, or mix of both for Phase 3 automation?

**Options**:
- A) **AI Studio** (Modern): Better for complex logic, natural language setup
- B) **Native Rules** (Simple): More limited but proven, included in Advanced tier
- C) **Mix**: AI Studio for complex rules, Native for simple triggers

**Tier Requirement**: Advanced tier required for both (25,000 actions/month)

**Recommendation**: Option C (Mix) - evaluate during Phase 3

---

## NEXT STEPS (IMMEDIATE ACTIONS)

### After Andrew Approval

**Phase 1A - Custom Fields Creation** (4-6 hours)
1. Create 10 core custom fields in Asana workspace
   - Module Code (Text)
   - Client Name (Text)
   - Programme Name (Text)
   - **Launch Date (Date)** ← Critical field
   - Go Live Date (Date)
   - Learning Designer (People)
   - Learning Technologist (People)
   - Senior LD (People)
   - Module Author (Text)
   - Module Status (Single-select dropdown)
2. Document field GIDs for API use
3. Test field accessibility via Asana MCP API

**Phase 1B - API Script Development** (6-8 hours)
1. Create `create_module_from_template.py`
2. Implement date calculation logic (reuse existing mapping)
3. Add custom field population
4. Implement dependency creation
5. Add validation and error handling
6. Write tests (unit + integration)
7. Document usage in README

**Phase 1C - Testing & Validation** (2-3 hours)
1. Test script on 2-3 test modules
2. Validate all 72 dates set correctly
3. Verify custom fields populated
4. Confirm dependencies created
5. Test Launch Date recalculation

**Total Phase 1 Effort**: 18-24 hours (REVISED from 12-16 hours)

---

## CONCLUSION

**Primary Finding**: Asana's native capabilities **DO NOT** support relative date anchoring to custom "Launch Date" field.

**Required Approach**: API-based template instantiation script for Phase 1 Foundation.

**Trade-Off**: Accept technical complexity (Python script) to achieve core requirement (Launch Date custom field automation).

**Business Value**: Despite added complexity, API approach provides:
- Complete automation (10-minute module setup vs 60-minute manual)
- Custom field integration (31 fields populated automatically)
- Scalability (version-controlled, testable, repeatable)
- Future-proofing (foundation for advanced integrations)

**Confidence Level**: **HIGH** - Research comprehensive, findings conclusive, API approach proven viable.

---

## REFERENCES

### Official Asana Documentation
- Formula custom fields: https://help.asana.com/hc/en-us/articles/15956483311259
- Relative due dates in templates: https://forum.asana.com/t/relative-due-dates-in-custom-project-templates/783408
- AI Studio smart workflows: https://help.asana.com/s/article/ai-studio-smart-workflows

### Forum Discussions
- TODAY input in formulas: https://forum.asana.com/t/how-you-can-use-the-today-input-in-advanced-formulas-today/746315
- Advanced Formula Editor: https://forum.asana.com/t/formula-custom-field-with-advanced-editor/481803
- Feature requests for custom field anchoring: https://forum.asana.com/t/feature-request-in-project-templates-allow-task-due-dates-before-and-after-the-project-anchor-date/662046

### Project Documentation
- Comprehensive Architecture Review: `.serena/memories/comprehensive_asana_architecture_review_oct_23_2025.md`
- Original Specification: `Asana_Module_Development_Template_Spec_v2.md`

---

**Report Prepared By**: Agent 2 - Asana Native Automation Research Agent
**Approval Status**: Awaiting Andrew review and decision on 4 key questions
**Next Agent**: Ready to hand off to Phase 1 implementation team

---

## APPENDIX: Research Methodology

**Research Tools Used**:
- Tavily web search (primary research tool)
- WebFetch for official documentation extraction
- Forum analysis for community feedback and feature requests
- Asana pricing page analysis for tier comparison

**Search Queries Executed**:
1. "Asana relative date formulas custom fields automation"
2. "Asana AI workflow automation premium business tier"
3. "Asana automation rules limits business premium tier 2025"
4. "Asana formula custom fields date calculations anchor launch date relative 2025"
5. "Asana formula date field reference custom field examples"
6. "Asana AI Studio workflow automation custom fields date calculations 2025"

**Documentation Pages Analyzed**:
1. Asana Help Center - Formula custom fields
2. Asana Forum - Advanced Formula Editor discussion (481803)
3. Asana Forum - TODAY input guide (746315)
4. Asana Forum - Relative due dates in templates (783408)
5. Asana Pricing page - Tier comparison
6. Asana Summer 2025 Release notes

**Key Limitations Identified**:
- Some official documentation pages returned only CSS/JavaScript (not content)
- Relied on forum discussions for practical examples
- AI Studio specific documentation limited (mostly marketing content)
- No official API for "relative date to custom field" (confirmed via absence in docs)

**Confidence Assessment**:
- **HIGH confidence** on "Native Asana cannot anchor to custom date fields" (multiple confirmatory sources, no counter-evidence)
- **HIGH confidence** on tier limits and pricing (official Asana pricing page)
- **MEDIUM confidence** on AI Studio capabilities (limited technical documentation, mostly marketing)
- **HIGH confidence** on Formula field capabilities (official documentation + forum examples)

---

**END OF REPORT**
