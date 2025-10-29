# Agent Task Assignments - October 24, 2025

## Context
Based on 10 project decisions from Andrew, creating 6 specialized agent assignments for Asana systematisation project.

---

## AGENT 1: Custom Field Verification Agent
**Priority**: HIGH (IMMEDIATE)
**Decision Reference**: Decision 1

**Task**: Verify custom field implementation status

**Instructions**:
1. Review Asana_Module_Development_Template_Spec_v2.md Section 3 (31 custom fields specified)
2. Check Asana workspace for existing custom fields via API
3. Document: What exists, what's missing, field GIDs for API use
4. Compare against comprehensive_asana_architecture_review (states "31 fields specified, 0 created")

**Expected Deliverables**:
- Acknowledgement of task received
- Proposed verification approach for confirmation
- Final report: Custom field gap analysis with field GIDs and creation requirements

**Output Location**: `.serena/memories/agent1_custom_field_verification.md`

**Key Constraints**:
- Use Asana MCP tools for workspace inspection
- Reference specification Section 3.1-3.4
- Stay within 8K token output limit

---

## AGENT 2: Asana Native Automation Research Agent
**Priority**: HIGH (IMMEDIATE)
**Decision Reference**: Decision 2

**Task**: Research Asana native workflow automation for relative date implementation

**Instructions**:
1. Use Context7 MCP to research Asana documentation on:
   - Relative date formulas/anchoring capabilities
   - Native AI workflow automation features
   - Premium/Business tier automation limits
2. Evaluate feasibility of native solution vs. API-based approach
3. Provide recommendation with trade-offs

**Expected Deliverables**:
- Acknowledgement of task received
- Research plan for confirmation
- Final report: Native automation capabilities assessment with implementation recommendation

**Output Location**: `.serena/memories/agent2_asana_automation_research.md`

**Key Constraints**:
- Use Context7 for official Asana documentation
- Focus on relative date anchoring to custom "Launch Date" field
- Compare native vs. API-based script approach
- Stay within 10K token output limit

---

## AGENT 3: Flexible Portfolio Structure Design Agent
**Priority**: MEDIUM
**Decision Reference**: Decision 6

**Task**: Design flexible programme structure for client-specific scope

**Instructions**:
1. Review TRACK_1_PORTFOLIO_DASHBOARD_ARCHITECTURE.md (45-page design)
2. Design configurable portfolio/programme hierarchy supporting:
   - Client-specific programme scope variability
   - 1-20 modules per programme
   - Multiple programmes per client
   - Flexible custom field configuration
3. Address Phase 2 requirements from Track 1

**Expected Deliverables**:
- Acknowledgement of task received
- Design approach for confirmation
- Final design: Flexible portfolio architecture with configuration guidelines

**Output Location**: `.serena/memories/agent3_flexible_portfolio_design.md`

**Key Constraints**:
- Build on existing Track 1 Phase 1 architecture
- Ensure programme scope configurable per client
- Stay within 12K token output limit

---

## AGENT 4: Critical Automation Rules Design Agent
**Priority**: MEDIUM
**Decision Reference**: Decisions 3, 7

**Task**: Design 5 critical automation rules (simple first, expand during pilot)

**Instructions**:
1. Review specification Section 9 (15 automation rules specified)
2. Select 5 most critical rules for pilot phase:
   - Status propagation
   - Next resource notification
   - Blocker escalation
   - QA approval gate
   - Launch date change notification
3. Design simple implementation, plan complexity expansion path
4. Consider Nicole's pilot module (mid-late November)

**Expected Deliverables**:
- Acknowledgement of task received
- Rule prioritization plan for confirmation
- Final design: 5 critical automation rules with expansion roadmap

**Output Location**: `.serena/memories/agent4_critical_automation_rules.md`

**Key Constraints**:
- Start simple, avoid complexity
- Plan for pilot feedback iteration
- Stay within 8K token output limit

---

## AGENT 5: Pilot Project Planning Agent
**Priority**: MEDIUM
**Decision Reference**: Decision 5

**Task**: Plan pilot module for Nicole (mid-late November kickoff)

**Instructions**:
1. Review comprehensive_asana_architecture_review.md Phase 5 (pilot requirements)
2. Create pilot-specific plan:
   - Timeline: Mid-late November start
   - Success criteria for pilot validation
   - Monitoring approach during pilot
   - Feedback collection strategy
3. Define template validation requirements

**Expected Deliverables**:
- Acknowledgement of task received
- Pilot planning approach for confirmation
- Final plan: Nicole pilot module plan with success criteria

**Output Location**: `.serena/memories/agent5_pilot_project_plan.md`

**Key Constraints**:
- Align with Nicole's November timeline
- Focus on template validation objectives
- Stay within 8K token output limit

---

## AGENT 6: Launch Buffer Strategy Agent
**Priority**: MEDIUM
**Decision Reference**: Decision 10

**Task**: Design flexible buffer system (minimal default, configurable)

**Instructions**:
1. Review specification Section 1.2 (66-day buffer context)
2. Design buffer strategy addressing:
   - Minimal default buffer (Andrew prefers tight timelines)
   - Configurable per module/programme for flexibility
   - Client deliverable timing management
   - Academic year alignment when required
3. Create custom field design for buffer configuration

**Expected Deliverables**:
- Acknowledgement of task received
- Buffer strategy approach for confirmation
- Final strategy: Flexible buffer system design with configuration model

**Output Location**: `.serena/memories/agent6_launch_buffer_strategy.md`

**Key Constraints**:
- Default to minimal buffer
- Support flexibility for client-specific requirements
- Stay within 6K token output limit

---

## Agent Execution Standards

**All agents must**:
1. Use sequential thinking (`--think` flag) for complex analysis
2. Deliver in 3 phases:
   - Phase 1: Acknowledgement + proposed plan
   - Phase 2: Confirmation from coordinator
   - Phase 3: Final deliverable
3. Write outputs to `.serena/memories/` (avoid project file pollution)
4. Stay within specified token output limits
5. Reference loaded project context from memories

**Priority Execution Order**:
1. Agent 1 + Agent 2 (parallel - both HIGH priority)
2. Agent 3 + Agent 4 (parallel - both MEDIUM priority)
3. Agent 5 + Agent 6 (parallel - both MEDIUM priority)

**Total Estimated Effort**: 24-30 hours across all agents
**Timeline**: 1-2 weeks for completion

---

## Decision Summary Reference

1. **Custom Fields**: Verify existing (Agent 1)
2. **Relative Dates**: Research native Asana automation (Agent 2)
3. **Automation Scope**: Critical rules first, expand based on feedback (Agent 4)
4. **Template Conversion**: Deferred until project requirements scoped
5. **Pilot Module**: Nicole, mid-late November (Agent 5)
6. **Portfolio Structure**: Flexible, client-specific (Agent 3)
7. **Automation Complexity**: Start simple, add during pilot (Agent 4)
8. **Film Shoot**: Recommendation accepted (no agent needed)
9. **Academic Reviewer**: Recommendation accepted (no agent needed)
10. **Launch Buffer**: Minimal default, flexible (Agent 6)

**Decisions 8 & 9**: No agent assignment required - recommendations already accepted.
