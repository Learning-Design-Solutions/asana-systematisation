# Comprehensive Asana Architecture Design
## Learning Design Solutions - Full Business Operations Integration

**Version**: 1.0
**Date**: October 20, 2025
**Status**: Design Specification
**Scope**: Integration of all 8 workflows into unified Asana architecture

---

## Executive Summary

This document presents the comprehensive architecture design for Learning Design Solutions' complete business operations in Asana, expanding from the current single-workflow implementation (Workflow 4: Module Development) to a fully integrated system covering all 8 business workflows.

**Current State**: Module development template (72 tasks, 52 dependencies) covering only Workflow 4
**Target State**: Complete business operations system with portfolio/programme/project hierarchy

**Key Architecture Decisions**:
- **Hierarchy**: Portfolio → Programme → Project (Module) → Section → Task → Subtask
- **Scope Expansion**: From 1 workflow → 8 integrated workflows
- **Structure**: Maintain current module template as project-level component
- **Integration**: Wrap existing template within programme and portfolio structures

---

## Table of Contents

1. [Architecture Overview](#1-architecture-overview)
2. [Hierarchy Design](#2-hierarchy-design)
3. [Workflow Integration](#3-workflow-integration)
4. [Custom Fields System](#4-custom-fields-system)
5. [Automation Strategy](#5-automation-strategy)
6. [API Implementation Plan](#6-api-implementation-plan)
7. [Migration Strategy](#7-migration-strategy)
8. [Reporting & Views](#8-reporting--views)
9. [Technical Specifications](#9-technical-specifications)
10. [Implementation Roadmap](#10-implementation-roadmap)

---

## 1. Architecture Overview

### 1.1 Current vs Target Architecture

**Current Implementation** (as of Oct 14, 2025):
```
Project: Module Development Template
├── 12 Sections (Initiation → Launch)
├── 72 Tasks (including subtasks)
└── 52 Dependencies (API-created)
```

**Target Architecture**:
```
Portfolio: LDS Operations
├── Programme: [Client A] - [Programme Name]
│   ├── Project: Business Development (Workflow 1)
│   ├── Project: Client Onboarding (Workflow 2)
│   ├── Project: Programme Oversight (Workflow 3)
│   ├── Project: Module 1 Development (Workflow 4) ← CURRENT TEMPLATE
│   ├── Project: Module 2 Development (Workflow 4)
│   ├── Project: Module N Development (Workflow 4)
│   ├── Project: Team & Resources (Workflow 5)
│   ├── Project: Client Management (Workflow 6)
│   ├── Project: Finance & Operations (Workflow 7)
│   └── Project: Closeout (Workflow 8)
├── Programme: [Client B] - [Programme Name]
│   └── [Same project structure]
└── Programme: [Client C] - [Programme Name]
    └── [Same project structure]
```

### 1.2 Design Principles

**Principle 1: Preserve Current Investment**
- Maintain existing module development template (72 tasks, 52 dependencies)
- Wrap with programme/portfolio structure rather than rebuild
- Current template becomes repeatable component within programmes

**Principle 2: Gradual Expansion**
- Implement workflows incrementally (not all at once)
- Start with critical workflows (3, 4, 6) before supporting workflows
- Validate each workflow before expanding

**Principle 3: Portfolio-First Thinking**
- Design hierarchy from top-down (portfolio → programme → project)
- Ensure programme-level tracking and oversight built in
- Enable cross-programme reporting and resource management

**Principle 4: API-Driven Automation**
- Continue API-based approach for reproducibility
- Automate template creation for new programmes
- Implement relative date anchoring via API

**Principle 5: Flexible Structure**
- Not all programmes need all 8 workflows
- Allow programme-specific customization
- Support different module development patterns

---

## 2. Hierarchy Design

### 2.1 Portfolio Level

**Purpose**: Top-level container for all LDS business operations

**Structure**:
```
Portfolio: "LDS Operations"
├── Description: "Learning Design Solutions - All Client Programmes and Projects"
├── Owner: Andrew (PM role)
├── Visibility: Team members only
└── Purpose: Cross-programme reporting and resource visibility
```

**Alternative: Multiple Portfolios** (if needed for scale):
```
Portfolio: "LDS - Client Programmes"
Portfolio: "LDS - Business Development"
Portfolio: "LDS - Internal Operations"
```

**Recommendation**: Start with single portfolio, split later if >20 programmes

### 2.2 Programme Level

**Purpose**: Client-specific programme containing multiple modules and supporting projects

**Naming Convention**: `[Client Name] - [Programme Name]`

**Examples**:
- "Walbrook University - MBA Programme Refresh"
- "Healthcare Academy - Clinical Skills Development"
- "Finance Institute - Professional Certification Series"

**Programme Structure**:
```
Programme: [Client] - [Programme Name]
├── Custom Fields (Programme-level):
│   ├── Client Name
│   ├── Programme Start Date
│   ├── Programme Status (Planning, Active, Delivery, Closeout)
│   ├── Total Modules (count)
│   ├── Module Status Summary (e.g., "3 Active, 2 Planning, 1 Complete")
│   ├── Programme Budget
│   ├── Programme Owner (Andrew as PM)
│   └── Health Status (Green/Amber/Red)
│
├── Projects (vary by programme phase):
│   ├── Business Development (Workflow 1) - if prospecting
│   ├── Client Onboarding (Workflow 2) - at programme start
│   ├── Programme Oversight (Workflow 3) - always present
│   ├── Module Development x N (Workflow 4) - core work
│   ├── Team & Resources (Workflow 5) - always present
│   ├── Client Management (Workflow 6) - always present
│   ├── Finance & Operations (Workflow 7) - always present
│   └── Closeout (Workflow 8) - at programme end
│
└── Programme-Level Tasks (not in projects):
    ├── Strategic milestones
    ├── Cross-module dependencies
    └── Programme-wide deliverables
```

### 2.3 Project Level

**Purpose**: Specific workflow execution within a programme

**Project Types** (corresponding to 8 workflows):

1. **Business Development Project** (Workflow 1)
   - Lead tracking and pipeline management
   - Proposal development
   - Contract negotiation

2. **Client Onboarding Project** (Workflow 2)
   - RACI model creation
   - Questionnaire completion
   - Playbook setup

3. **Programme Oversight Project** (Workflow 3)
   - Weekly reporting consolidation
   - Cross-module dependency tracking
   - Milestone monitoring

4. **Module Development Projects** (Workflow 4) ← CURRENT TEMPLATE
   - Multiple instances per programme
   - Each follows 16-week template structure
   - Named: "[Programme] - Module [N]: [Module Title]"

5. **Team & Resources Project** (Workflow 5)
   - Subcontractor availability tracking
   - Work allocation across modules
   - Quality monitoring

6. **Client Management Project** (Workflow 6)
   - Weekly reporting to client
   - Issue log and escalation
   - Stakeholder communication

7. **Finance & Operations Project** (Workflow 7)
   - Budget tracking
   - Invoice milestones
   - Profit First allocations

8. **Closeout Project** (Workflow 8)
   - Project completion checklist
   - Feedback collection
   - Relationship maintenance

### 2.4 Section → Task → Subtask Levels

**These levels remain as currently implemented in module development template**

Current structure (Workflow 4):
```
Project: Module Development
├── Section: Initiation & Planning
│   ├── Task: Kick off meeting
│   ├── Task: Module Planning Document
│   │   ├── Subtask: MPD Draft
│   │   ├── Subtask: MPD Finalised
│   │   └── Subtask: MPD review
│
├── Sections: Week 1-8 (each has similar structure)
│   └── Task: Week N - Storyboarding
│       ├── Subtask: LD Draft
│       ├── Subtask: SME Scripts Draft
│       ├── Subtask: Edit
│       ├── Subtask: Final draft agreed
│       └── Task: Week N - Build (top-level task)
│
└── Sections: Finalization, Launch
    └── [Current task structure maintained]
```

---

## 3. Workflow Integration

### 3.1 Workflow Priority & Phasing

**Critical Workflows** (implement first):
- Workflow 3: Programme Oversight ← HIGHEST PRIORITY (enables multi-module tracking)
- Workflow 4: Module Development ← ALREADY IMPLEMENTED
- Workflow 6: Client Management ← HIGH PRIORITY (ongoing client interaction)

**Supporting Workflows** (implement second):
- Workflow 2: Client Onboarding (run once per programme)
- Workflow 5: Team & Resources (ongoing resource management)
- Workflow 7: Finance & Operations (ongoing financial tracking)

**Optional Workflows** (implement later):
- Workflow 1: Business Development (separate from programme execution)
- Workflow 8: Closeout (run once at programme end)

### 3.2 Workflow 1: Business Development / Sales Pipeline

**Purpose**: Track opportunities from lead to contract

**Implementation Approach**: Lightweight CRM-style project

**Structure**:
```
Project: Business Development
├── Section: Leads (New Opportunities)
│   └── Tasks: Individual leads (name, organization, contact info)
├── Section: Contact Made
│   └── Tasks: Qualified opportunities
├── Section: Proposal Development
│   └── Tasks: Active proposals (linked to proposal documents)
├── Section: Negotiation
│   └── Tasks: In negotiation (pricing, terms, timeline)
├── Section: Closed Won
│   └── Tasks: Signed contracts → Trigger programme creation
└── Section: Closed Lost
    └── Tasks: Declined or abandoned opportunities
```

**Custom Fields**:
- Lead Source
- Organization
- Contact Name/Email
- Estimated Value
- Probability (%)
- Expected Close Date
- Proposal Submitted (Y/N)
- Status (Lead/Contact/Proposal/Negotiation/Closed)

**Integration Points**:
- Closed Won → Creates new Programme with Client Onboarding project
- Links to Programme once created

### 3.3 Workflow 2: Client Onboarding / Initiation

**Purpose**: Systematize programme setup after contract signing

**Implementation Approach**: Checklist-style project (run once per programme)

**Structure**:
```
Project: Client Onboarding
├── Section: Setup
│   ├── Task: Create programme structure in Asana
│   ├── Task: Set up shared drive folder
│   ├── Task: Create weekly reporting spreadsheet
│   └── Task: Schedule kickoff meeting
├── Section: Discovery
│   ├── Task: Complete client questionnaire
│   ├── Task: Interview key stakeholders
│   ├── Task: Document brand guidelines
│   └── Task: Review existing materials
├── Section: RACI & Roles
│   ├── Task: Create RACI matrix
│   ├── Task: Define decision-making authority
│   ├── Task: Identify SME availability
│   └── Task: Confirm team allocation
├── Section: Playbook Creation
│   ├── Task: Document communication protocols
│   ├── Task: Set up meeting cadence
│   ├── Task: Define escalation procedures
│   └── Task: Create issue management process
└── Section: Handoff
    ├── Task: Brief operational team
    ├── Task: Transition to programme oversight
    └── Task: Mark onboarding complete
```

**Custom Fields**:
- Onboarding Status (Not Started / In Progress / Complete)
- Assigned Owner
- Due Date
- Client Stakeholder (who to follow up with)

**Integration Points**:
- Links to Business Development opportunity (if came from pipeline)
- Creates Programme Oversight project upon completion
- Populates programme-level custom fields

### 3.4 Workflow 3: Programme Oversight (Global Management)

**Purpose**: Master tracking view across all modules within a programme

**Implementation Approach**: Dashboard-style project with automated aggregation

**Structure**:
```
Project: Programme Oversight
├── Section: Programme Planning
│   ├── Task: Define module sequence and dependencies
│   ├── Task: Set launch dates for all modules
│   ├── Task: Allocate LD/LT pairs to modules
│   └── Task: Create programme timeline
├── Section: Module Tracking
│   ├── Task: Module 1 - [Title] (status tracker)
│   ├── Task: Module 2 - [Title] (status tracker)
│   └── Task: Module N - [Title] (status tracker)
│       └── Linked to actual Module Development project
├── Section: Milestones & Dependencies
│   ├── Task: Programme kickoff
│   ├── Task: First module launch
│   ├── Task: Mid-programme review
│   ├── Task: Final module completion
│   └── Task: Programme closeout
├── Section: Weekly Reporting
│   ├── Task: Week 1 consolidated report
│   ├── Task: Week 2 consolidated report
│   └── [Recurring weekly tasks]
├── Section: Issues & Risks
│   ├── Task: Cross-module dependency issues
│   ├── Task: Resource conflicts
│   ├── Task: Timeline risks
│   └── Task: Budget variances
└── Section: Meetings & Reviews
    ├── Task: Weekly programme review (recurring)
    ├── Task: Client steering committee meetings
    └── Task: Phase gate reviews
```

**Custom Fields** (Programme Oversight specific):
- Module Phase (Planning / Storyboarding / Build / Review / Launch)
- Module Health (Green / Amber / Red)
- Days to Launch
- LD Assigned
- LT Assigned
- Blockers (Y/N)
- Client Visibility (Public / Internal Only)

**Automation Requirements**:
- Auto-create module tracker task when new module project added
- Auto-update module status based on module project progress
- Flag blockers when module dependencies at risk
- Generate weekly report task with summary data

**Integration Points**:
- Links to all Module Development projects in programme
- Pulls status data from module projects
- Feeds data to Client Management weekly reports

### 3.5 Workflow 4: Module Development (Current Template)

**Status**: ✅ IMPLEMENTED (72 tasks, 52 dependencies)

**Integration Changes Needed**:
1. Add programme-level linking
2. Implement role assignment via custom fields
3. Add native start dates (currently missing)
4. Enable relative date anchoring to Launch Date

**Custom Field Additions**:
- Programme Name (link to parent programme)
- Module Number (1, 2, 3, etc.)
- LD Assigned
- LT Assigned
- SLD Assigned (Nicole)
- Launch Date Anchor
- Module Status (per phase)
- Health Status
- Client-Facing Deliverable (Y/N)

**No Structural Changes**: Maintain current 12-section, 72-task, 52-dependency structure

### 3.6 Workflow 5: Team & Resource Management

**Purpose**: Track subcontractor availability and allocation across programmes

**Implementation Approach**: Resource calendar project with capacity tracking

**Structure**:
```
Project: Team & Resources
├── Section: Team Directory
│   ├── Task: [LD Name 1] - Profile & Availability
│   ├── Task: [LD Name 2] - Profile & Availability
│   ├── Task: [LT Name 1] - Profile & Availability
│   └── [One task per team member]
├── Section: Current Allocations
│   ├── Task: [LD Name] - Module A (dates, utilization %)
│   ├── Task: [LD Name] - Module B (dates, utilization %)
│   └── [Links to actual module projects]
├── Section: Availability Calendar
│   ├── Task: [Month] LD Capacity
│   ├── Task: [Month] LT Capacity
│   └── Task: [Month] Offshore Capacity
├── Section: Quality Monitoring
│   ├── Task: Review QA metrics for UK team
│   ├── Task: Review QA metrics for offshore team
│   └── Task: Address quality issues
└── Section: Recruiting & Onboarding
    ├── Task: Active recruitment needs
    ├── Task: New subcontractor onboarding
    └── Task: Team training requirements
```

**Custom Fields** (Resource Management):
- Resource Name
- Role Type (LD / LT / SLD / Offshore)
- Location (UK / Offshore / Hybrid)
- Availability Status (Available / Partially Allocated / Fully Allocated / Unavailable)
- Current Utilization % (0-100%)
- Modules Assigned (count)
- Performance Rating (for quality tracking)

**Integration Points**:
- Pulls allocation data from all Module Development projects
- Feeds resource availability to Programme Oversight
- Links to Finance project for cost tracking

### 3.7 Workflow 6: Ongoing Client Management

**Purpose**: Centralize client communication, reporting, and issue resolution

**Implementation Approach**: Communication hub with issue tracking

**Structure**:
```
Project: Client Management
├── Section: Weekly Reporting
│   ├── Task: Week 1 Report [Auto-generated]
│   ├── Task: Week 2 Report [Auto-generated]
│   └── [Recurring weekly tasks]
│       └── Pulls data from Programme Oversight
├── Section: Meeting Schedule
│   ├── Task: Weekly sync with operational stakeholder
│   ├── Task: Monthly steering committee
│   └── Task: Quarterly programme review
├── Section: Issue Log
│   ├── Task: Issue #1 - [Description]
│   ├── Task: Issue #2 - [Description]
│   └── [One task per issue, status tracked]
├── Section: Escalations
│   ├── Task: Escalation to sponsor required
│   └── Task: Critical decisions pending
├── Section: Stakeholder Management
│   ├── Task: Sponsor engagement
│   ├── Task: Operational stakeholder coordination
│   └── Task: SME relationships
└── Section: Client Feedback
    ├── Task: Mid-programme feedback collection
    └── Task: End-of-module feedback
```

**Custom Fields** (Client Management):
- Issue Type (Technical / Timeline / Resource / Scope / Budget)
- Severity (Low / Medium / High / Critical)
- Escalation Required (Y/N)
- Stakeholder (who needs to be informed)
- Resolution Status (Open / In Progress / Resolved / Closed)
- Days Open

**Automation Requirements**:
- Auto-create weekly report task
- Pull module status from Programme Oversight
- Auto-flag overdue issues
- Escalation notification when critical

**Integration Points**:
- Pulls status data from Programme Oversight
- Links to Module Development projects for issue details
- Feeds data to Finance for client invoicing milestones

### 3.8 Workflow 7: Finance & Operations

**Purpose**: Track project profitability, invoicing, and financial allocations

**Implementation Approach**: Financial dashboard with invoice tracking

**Structure**:
```
Project: Finance & Operations
├── Section: Programme Budget
│   ├── Task: Initial budget estimate
│   ├── Task: Budget breakdown by module
│   ├── Task: Profit First allocation plan
│   └── Task: Budget variance tracking
├── Section: Deliverable Tracking
│   ├── Task: Module 1 deliverables → Invoice milestone
│   ├── Task: Module 2 deliverables → Invoice milestone
│   └── [Links to module projects]
├── Section: Invoicing
│   ├── Task: Invoice #1 - [Description] (amount, date, status)
│   ├── Task: Invoice #2 - [Description]
│   └── [One task per invoice]
├── Section: Cost Tracking
│   ├── Task: LD costs (day rates × days)
│   ├── Task: LT costs (day rates × days)
│   ├── Task: SLD costs (Nicole QA)
│   ├── Task: Offshore costs
│   └── Task: Other expenses
├── Section: Profitability
│   ├── Task: Programme revenue
│   ├── Task: Total costs
│   ├── Task: Gross margin
│   └── Task: Profit First allocations
└── Section: Integrations
    ├── Task: Clockify time tracking sync
    └── Task: Accounting system reconciliation
```

**Custom Fields** (Finance):
- Budget Item Type (Revenue / Cost)
- Amount (£)
- Date
- Invoice Status (Draft / Sent / Paid)
- Payment Terms (days)
- Profit First Category (Operating / Owner Pay / Tax / Profit)
- Clockify Time Entry Link

**Integration Points**:
- Links to Module Development projects for deliverable completion
- Links to Team & Resources for cost data
- Links to Client Management for reporting
- Future: API integration with Clockify and accounting system

### 3.9 Workflow 8: Closeout & Follow-up

**Purpose**: Structured programme completion and relationship maintenance

**Implementation Approach**: Checklist project (run once at programme end)

**Structure**:
```
Project: Closeout
├── Section: Completion Verification
│   ├── Task: Verify all modules launched
│   ├── Task: Confirm all deliverables submitted
│   ├── Task: Review final invoices paid
│   └── Task: Archive programme documentation
├── Section: Feedback Collection
│   ├── Task: Client feedback survey
│   ├── Task: Team retrospective
│   ├── Task: Document lessons learned
│   └── Task: Update playbooks based on insights
├── Section: Relationship Maintenance
│   ├── Task: Schedule 3-month follow-up
│   ├── Task: Schedule 6-month follow-up
│   ├── Task: Add to newsletter distribution
│   └── Task: Track for renewal/expansion opportunities
├── Section: Handoff
│   ├── Task: Transfer ongoing support to operations team
│   ├── Task: Update CRM/contact management
│   └── Task: Mark programme complete
└── Section: Celebration & Recognition
    ├── Task: Team appreciation
    └── Task: Case study development (if appropriate)
```

**Custom Fields** (Closeout):
- Closeout Status (Not Started / In Progress / Complete)
- Client Satisfaction Score
- Lessons Learned Documented (Y/N)
- Follow-up Scheduled (Y/N)

**Integration Points**:
- Links to all projects in programme for completion verification
- Links to Finance for final budget reconciliation
- Creates tasks in Business Development for follow-up opportunities

---

## 4. Custom Fields System

### 4.1 Custom Field Architecture

**Hierarchical Principle**: Custom fields cascade from portfolio → programme → project → task

**Field Inheritance**:
- Portfolio-level fields visible across all programmes
- Programme-level fields visible to all projects within programme
- Project-level fields specific to workflow type
- Task-level fields for granular tracking

### 4.2 Portfolio-Level Custom Fields

*Recommendation*: Minimal at portfolio level (only cross-programme reporting needs)

```yaml
Portfolio Fields:
  - Programme Status: [Planning, Active, Delivery, On Hold, Complete]
  - Programme Owner: [Person - Andrew default]
  - Total Active Modules: [Number]
  - Health Status: [Green, Amber, Red]
```

### 4.3 Programme-Level Custom Fields

**Purpose**: Track overall programme metadata and status

```yaml
Programme Identity:
  - Client Name: [Text]
  - Programme Code: [Text] # e.g., "WAL-MBA-2025"
  - Contract Value: [Currency - £]
  - Contract Start Date: [Date]
  - Expected Completion Date: [Date]

Programme Status:
  - Programme Phase: [Planning, Onboarding, Active Delivery, Closeout, Complete]
  - Health Status: [Green, Amber, Red]
  - Overall % Complete: [Number 0-100]

Module Summary:
  - Total Modules: [Number]
  - Modules Planning: [Number]
  - Modules In Development: [Number]
  - Modules Complete: [Number]
  - Modules at Risk: [Number]

Key Contacts:
  - Primary Sponsor: [Person]
  - Operational Stakeholder: [Person]
  - Programme Owner (Andrew): [Person - locked]

Financial:
  - Budget: [Currency]
  - Actual Costs: [Currency]
  - Variance: [Currency - calculated]
  - Profitability %: [Number]
```

### 4.4 Project-Level Custom Fields (by Workflow)

**Workflow 1: Business Development**
```yaml
Lead Info:
  - Lead Source: [Dropdown: Referral, Network, Outreach, Website, Event]
  - Organization: [Text]
  - Contact Name: [Text]
  - Contact Email: [Email]
  - Contact Phone: [Phone]

Opportunity:
  - Estimated Value: [Currency]
  - Probability %: [Number 0-100]
  - Expected Close Date: [Date]
  - Proposal Submitted: [Checkbox]
  - Last Contact Date: [Date]
  - Next Action: [Text]

Status:
  - Pipeline Stage: [Lead, Contact Made, Proposal, Negotiation, Closed Won, Closed Lost]
  - Lost Reason: [Text - if Closed Lost]
```

**Workflow 2: Client Onboarding**
```yaml
Onboarding:
  - Onboarding Status: [Not Started, Discovery, RACI, Playbook, Complete]
  - Onboarding Owner: [Person]
  - Kickoff Date: [Date]
  - Handoff Date: [Date]
  - Client Questionnaire Complete: [Checkbox]
  - RACI Matrix Complete: [Checkbox]
  - Playbook Created: [Checkbox]
```

**Workflow 3: Programme Oversight**
```yaml
Module Tracking:
  - Module Number: [Number]
  - Module Title: [Text]
  - Module Phase: [Planning, Storyboarding, Build, Review, Launch Prep, Complete]
  - Launch Date: [Date]
  - Days to Launch: [Number - calculated]
  - Health Status: [Green, Amber, Red]
  - LD Assigned: [Person]
  - LT Assigned: [Person]
  - Blockers: [Checkbox]
  - Blocker Description: [Text]

Reporting:
  - Week Number: [Number]
  - Report Status: [Draft, Submitted, Reviewed]
  - Issues This Week: [Number]
  - Escalations: [Checkbox]
```

**Workflow 4: Module Development** ← MOST DETAILED
```yaml
Module Identity:
  - Programme Name: [Text - from parent]
  - Module Number: [Number]
  - Module Title: [Text]
  - Module Code: [Text] # e.g., "MBA-FIN501"
  - Academic Credits: [Number]
  - Week Count: [Number] # Usually 8

Timeline:
  - Kickoff Date: [Date]
  - Launch Date: [Date] # ANCHOR for relative dates
  - Go Live Date: [Date]
  - Actual Launch Date: [Date]
  - Days to Launch: [Number - calculated]
  - Phase: [Initiation, Storyboarding, Build, Review, Finalization, Launch]

Resources:
  - LD Assigned: [Person]
  - LT Assigned: [Person]
  - SLD Assigned: [Person] # Nicole default
  - MA/SME: [Person]
  - Offshore Support: [Checkbox]

Status:
  - Module Status: [Planning, Active, At Risk, Blocked, Complete]
  - Health Status: [Green, Amber, Red]
  - % Complete: [Number 0-100 - calculated from task completion]
  - Blockers: [Text]
  - Priority: [Low, Normal, High, Critical]

Quality:
  - Weeks 1-2 Review Status: [Not Started, In Progress, Complete]
  - Weeks 3-8 Review Status: [Not Started, In Progress, Complete]
  - Proofreading Status: [Not Started, In Progress, Complete]
  - Corrections Status: [Not Started, In Progress, Complete]
  - Ready for Launch: [Checkbox]

Client:
  - Client-Facing Deliverable: [Checkbox]
  - Client Visibility: [Yes - they can see / No - internal only]

Technical:
  - Content Type: [Video-heavy, Text-heavy, Interactive, Mixed]
  - Film Shoot Required: [Yes - Standard, Yes - Extended, No]
  - AI Content Generation: [None, Partial, Heavy]
```

**Workflow 5: Team & Resources**
```yaml
Resource Info:
  - Resource Name: [Person]
  - Role Type: [LD, LT, SLD, Offshore LD, Offshore LT]
  - Location: [UK, Offshore - India, Offshore - Other]
  - Specialization: [Text]

Availability:
  - Availability Status: [Available, Partially Allocated, Fully Allocated, Unavailable]
  - Current Utilization %: [Number 0-100]
  - Available Start Date: [Date]
  - Committed Until: [Date]
  - Modules Assigned: [Number]
  - Max Concurrent Modules: [Number]

Quality:
  - Performance Rating: [1-5 stars]
  - Recent QA Issues: [Number]
  - Client Feedback Score: [Number 1-10]

Financial:
  - Day Rate (£): [Currency]
  - Billing Status: [Employee, Contractor, Subcontractor]
```

**Workflow 6: Client Management**
```yaml
Communication:
  - Meeting Type: [Weekly Sync, Steering Committee, Ad Hoc]
  - Meeting Date: [Date]
  - Attendees: [Multi-person]
  - Follow-up Required: [Checkbox]

Issue Tracking:
  - Issue Type: [Technical, Timeline, Resource, Scope, Budget, Quality]
  - Severity: [Low, Medium, High, Critical]
  - Reported By: [Person]
  - Assigned To: [Person]
  - Status: [Open, In Progress, Resolved, Closed]
  - Days Open: [Number - calculated]
  - Escalation Required: [Checkbox]
  - Stakeholder to Inform: [Person]
  - Resolution Date: [Date]

Reporting:
  - Report Week: [Number]
  - Report Status: [Draft, Sent, Acknowledged]
  - Report Date: [Date]
  - Issues Count: [Number]
  - Risks Count: [Number]
```

**Workflow 7: Finance & Operations**
```yaml
Financial:
  - Budget Item Type: [Revenue, Cost - LD, Cost - LT, Cost - SLD, Cost - Other]
  - Amount (£): [Currency]
  - Date: [Date]
  - Cost Center: [Dropdown: Delivery, Sales, Marketing, Admin, Owner]

Invoicing:
  - Invoice Number: [Text]
  - Invoice Status: [Draft, Sent, Paid, Overdue]
  - Invoice Date: [Date]
  - Due Date: [Date]
  - Payment Received Date: [Date]
  - Days Outstanding: [Number - calculated]
  - Payment Terms: [30 days, 60 days, Net 30, etc.]

Deliverables:
  - Deliverable Name: [Text]
  - Module Link: [Text - link to module project]
  - Completion Date: [Date]
  - Invoice Milestone: [Checkbox]

Profit First:
  - Profit First Category: [Operating, Owner Pay, Tax, Profit]
  - Allocation %: [Number]
  - Account: [Dropdown: aligned with Starling Bank accounts]
```

**Workflow 8: Closeout**
```yaml
Closeout:
  - Closeout Status: [Not Started, In Progress, Complete]
  - All Modules Complete: [Checkbox]
  - All Invoices Paid: [Checkbox]
  - Feedback Collected: [Checkbox]
  - Client Satisfaction Score: [Number 1-10]
  - Lessons Learned Documented: [Checkbox]

Follow-up:
  - 3-Month Follow-up Scheduled: [Date]
  - 6-Month Follow-up Scheduled: [Date]
  - Added to Newsletter: [Checkbox]
  - Renewal Opportunity: [Checkbox]
  - Case Study Developed: [Checkbox]
```

### 4.5 Task-Level Custom Fields

**Principle**: Inherit from project level + add task-specific tracking

**Task-Specific Fields** (examples):
```yaml
Task Execution:
  - Task Owner: [Person]
  - Due Date: [Date]
  - Actual Completion Date: [Date]
  - Est. Hours: [Number]
  - Actual Hours: [Number]
  - Status: [Not Started, In Progress, Blocked, Complete]
  - Priority: [Low, Normal, High, Urgent]

Dependencies:
  - Blocking Tasks: [Number]
  - Blocked By: [Number]
  - Dependency Type: [Sequential, Parallel, Milestone]

Tracking:
  - Time Tracking Link: [Text - link to Clockify]
  - Notes: [Long text]
```

### 4.6 Custom Field Implementation Priority

Based on Section 11 Question 16 and audit findings, prioritize implementation:

**Phase 1: Essential Fields** (Week 1)
```yaml
Must-Have:
  - Programme Name
  - Module Number / Title
  - LD / LT / SLD Assigned
  - Launch Date (anchor)
  - Health Status
  - Phase / Status
  - Client Name
  - Blockers
```

**Phase 2: Operational Fields** (Week 2)
```yaml
Important:
  - Days to Launch (calculated)
  - % Complete
  - Resource Utilization
  - Issue Type / Severity
  - Budget / Actual Costs
  - Invoice Status
```

**Phase 3: Advanced Fields** (Week 3-4)
```yaml
Nice-to-Have:
  - Content Type
  - AI Generation level
  - Performance Ratings
  - Client Satisfaction
  - Profit First categories
  - Follow-up tracking
```

---

## 5. Automation Strategy

### 5.1 Automation Principles

1. **API-First**: Use Asana API for reproducible automation
2. **Gradual Implementation**: Start with highest-value automations
3. **Minimize Manual Work**: Automate repetitive tasks
4. **Maintain Flexibility**: Allow manual overrides when needed
5. **Validate Before Scale**: Test automations on single programme first

### 5.2 Critical Automations (Priority 1)

**1. Programme Creation from Template**
- **Trigger**: Closed Won opportunity in Business Development
- **Action**:
  - Create new programme in portfolio
  - Populate programme-level custom fields from opportunity
  - Create Client Onboarding project
  - Create Programme Oversight project
  - Create Client Management project
  - Create Team & Resources project (if first programme)
  - Create Finance & Operations project
- **API Method**: `asana_create_project`, `asana_update_task` for custom fields
- **Complexity**: Medium
- **Value**: High (saves 30-60 minutes per programme)

**2. Module Development Project Instantiation**
- **Trigger**: New module added to programme
- **Action**:
  - Duplicate module development template
  - Populate custom fields (programme name, module number, etc.)
  - Calculate and set all task start dates relative to Launch Date
  - Create dependencies (52 relationships)
  - Create tracker task in Programme Oversight project
  - Link to Programme Oversight
- **API Method**: `asana_create_project`, `asana_add_task_dependencies`, custom date logic
- **Complexity**: High (requires relative date calculation)
- **Value**: Very High (saves 30-45 minutes per module, critical path)

**3. Relative Date Anchoring to Launch Date**
- **Trigger**: Launch Date set or changed in module project
- **Action**:
  - Calculate all task start dates backward from Launch Date
  - Apply duration rules (Week 1 = 17 days, Weeks 2-8 = 10 days, etc.)
  - Skip holidays (Christmas, academic out-of-office)
  - Update all 72 task start dates
  - Flag if dates conflict with resource availability
- **API Method**: Custom logic + `asana_update_task` for each date
- **Complexity**: High (date arithmetic + holiday logic)
- **Value**: Critical (manual date management is error-prone and time-consuming)

**4. Status Aggregation to Programme Oversight**
- **Trigger**: Task completion or status change in module project
- **Action**:
  - Calculate module % complete from task completion
  - Update module health status based on timeline and blockers
  - Update tracker task in Programme Oversight
  - Calculate "Days to Launch"
  - Flag if module at risk (timeline slippage, blockers)
- **API Method**: `asana_get_task`, calculate, `asana_update_task`
- **Complexity**: Medium
- **Value**: High (enables real-time programme dashboard)

**5. Weekly Report Generation**
- **Trigger**: Every Monday morning (or configurable day)
- **Action**:
  - Create new "Week N Report" task in Client Management
  - Pull module status data from Programme Oversight
  - Pull issue count from Client Management issue log
  - Generate report content (summary of progress, issues, next steps)
  - Notify Andrew (PM) for review
- **API Method**: `asana_create_task`, `asana_get_tasks` for data aggregation
- **Complexity**: Medium
- **Value**: High (saves 15-30 minutes weekly per programme)

### 5.3 Important Automations (Priority 2)

**6. Role Assignment Based on Resource Availability**
- **Trigger**: New module project created OR resource custom field changed
- **Action**:
  - Check Team & Resources project for availability
  - Suggest LD/LT pair with capacity
  - Auto-assign if single option available
  - Update utilization % in Team & Resources
  - Flag conflicts if resource over-allocated
- **Complexity**: High (resource optimization logic)
- **Value**: Medium-High (improves resource utilization)

**7. Issue Escalation Notifications**
- **Trigger**: Issue marked as "Critical" OR Days Open > threshold
- **Action**:
  - Notify Andrew (PM)
  - Update issue status to "Escalation Required"
  - Create task in Programme Oversight "Issues & Risks" section
  - Add to next weekly report
- **Complexity**: Low
- **Value**: Medium (ensures critical issues don't slip)

**8. Invoice Milestone Triggers**
- **Trigger**: Module deliverable marked complete
- **Action**:
  - Check if deliverable is invoice milestone
  - Create invoice task in Finance & Operations
  - Populate invoice details (amount, date, status)
  - Notify Andrew for invoice generation
- **Complexity**: Medium
- **Value**: Medium (improves cash flow management)

**9. Dependency Violation Detection**
- **Trigger**: Task marked complete before dependency satisfied
- **Action**:
  - Flag dependency violation
  - Notify task owner and PM
  - Require confirmation to override
  - Log exception in Programme Oversight
- **Complexity**: Low
- **Value**: Medium (maintains workflow integrity)

**10. Resource Capacity Alerts**
- **Trigger**: Resource utilization > 90% OR trying to assign to fully allocated resource
- **Action**:
  - Alert PM (Andrew)
  - Suggest alternative resources
  - Flag in Team & Resources project
  - Update capacity forecast
- **Complexity**: Medium
- **Value**: Medium (prevents resource conflicts)

### 5.4 Future Automations (Priority 3)

**11. Clockify Time Tracking Integration**
- **Trigger**: Task marked complete
- **Action**: Pull actual hours from Clockify, update task custom field, update Finance cost tracking

**12. Client Feedback Collection**
- **Trigger**: Module launch complete
- **Action**: Create feedback task, send survey link, track responses

**13. Programme Health Score Calculation**
- **Trigger**: Daily or weekly schedule
- **Action**: Calculate aggregate health across all modules, update programme-level status

**14. Profit First Allocation Automation**
- **Trigger**: Invoice payment received
- **Action**: Calculate allocations, create tasks for bank transfers

**15. Template Variant Generation**
- **Trigger**: New template specification provided
- **Action**: Generate complete project structure with dependencies from specification

### 5.5 Asana Built-In Rules (No API Required)

Leverage native Asana automation where possible:

**Examples**:
- Auto-assign task to project owner when created
- Move task to "In Progress" section when assignee set
- Add due date reminder 2 days before task due
- Mark parent task complete when all subtasks complete
- Auto-follow task when assigned
- Send notification when dependency satisfied

### 5.6 API Implementation Patterns

**Pattern 1: Triggered Update**
```python
# Pseudo-code example
def on_module_launch_date_changed(module_project_id, new_launch_date):
    """Update all task dates relative to new launch date"""
    # 1. Get all tasks in module project
    tasks = asana.get_project_tasks(module_project_id)

    # 2. Calculate relative dates
    dates = calculate_relative_dates(new_launch_date)

    # 3. Update each task
    for task in tasks:
        task_name = task['name']
        if task_name in dates:
            asana.update_task(task['gid'], {
                'start_on': dates[task_name]['start'],
                'due_on': dates[task_name]['due']
            })
```

**Pattern 2: Scheduled Aggregation**
```python
# Pseudo-code example
def generate_weekly_report(programme_id):
    """Generate weekly report from programme data"""
    # 1. Get programme oversight project
    oversight_project = asana.get_programme_oversight(programme_id)

    # 2. Get all module status
    modules = asana.get_module_trackers(oversight_project)

    # 3. Get issues from client management
    issues = asana.get_open_issues(programme_id)

    # 4. Generate report content
    report_content = generate_report_template(modules, issues)

    # 5. Create report task
    asana.create_task(
        project=programme.client_management_project,
        name=f"Week {week_number} Report",
        notes=report_content,
        due_date=today
    )
```

**Pattern 3: Template Instantiation**
```python
# Pseudo-code example
def create_module_from_template(programme_id, module_number, launch_date):
    """Create new module project from template"""
    # 1. Duplicate template project
    new_project = asana.duplicate_project(TEMPLATE_PROJECT_ID)

    # 2. Move to correct programme
    asana.add_project_to_portfolio(programme_id, new_project['gid'])

    # 3. Populate custom fields
    asana.update_project_custom_fields(new_project['gid'], {
        'module_number': module_number,
        'launch_date': launch_date,
        # ... other fields
    })

    # 4. Calculate and set all task dates
    set_task_dates_from_launch_date(new_project['gid'], launch_date)

    # 5. Create tracker in Programme Oversight
    create_module_tracker(programme_id, new_project['gid'], module_number)
```

---

## 6. API Implementation Plan

### 6.1 API Requirements Summary

**Current Capability** (via Asana MCP):
- ✅ Task dependency creation
- ✅ Task search and retrieval
- ✅ Project creation and structure
- ✅ Custom field reading
- ⚠️ Limited: Custom field writing, date management, automation triggers

**Additional API Needs**:
- Native task start date setting (not available via CSV import)
- Custom field value setting (write operations)
- Project duplication with custom field population
- Webhook subscriptions for automation triggers
- Batch operations for performance

### 6.2 API Implementation Phases

**Phase 1: Essential Date Management** (Week 1)
```yaml
Goal: Enable relative date anchoring to Launch Date

Tasks:
  1. Implement task start date API calls
     - Use Asana REST API: PUT /tasks/{task_gid}
     - Set start_on and due_on fields
     - Handle date format (YYYY-MM-DD)

  2. Build date calculation engine
     - Input: Launch Date anchor
     - Logic: Backward calculation for all 72 tasks
     - Rules: Week 1 = 17 days, Weeks 2-8 = 10 days, etc.
     - Output: Task-to-date mapping

  3. Implement holiday skip logic
     - Christmas detection (Dec 20 - Jan 6)
     - Academic out-of-office detection (configurable)
     - Weekend skip (if configured)
     - Adjust durations accordingly

  4. Create date update utility
     - Input: Module project GID + Launch Date
     - Action: Update all 72 task dates
     - Validation: Ensure dependencies respected
     - Logging: Track date changes

Deliverables:
  - set_module_dates.py script
  - Holiday configuration file
  - Date calculation logic documented
  - Test suite for date calculations

Success Criteria:
  - Can set all module task dates from Launch Date in <2 minutes
  - Holiday skipping works correctly
  - Dependency sequences maintained
  - Zero manual date entry required
```

**Phase 2: Custom Field Automation** (Week 2)
```yaml
Goal: Populate essential custom fields automatically

Tasks:
  1. Implement custom field write operations
     - Use Asana REST API: PUT /tasks/{task_gid}
     - Set custom_fields object
     - Handle field types (text, number, enum, person)

  2. Build programme-to-module field propagation
     - Read programme-level fields
     - Populate into all module projects
     - Examples: Programme Name, Client Name, PM Owner

  3. Implement role assignment logic
     - Check Team & Resources for availability
     - Auto-populate LD/LT/SLD custom fields
     - Update resource utilization %

  4. Create module metadata automation
     - Auto-generate Module Code
     - Calculate Module Number from programme
     - Set Phase based on Launch Date proximity
     - Initialize Health Status = Green

Deliverables:
  - populate_custom_fields.py script
  - Field mapping configuration
  - Role assignment logic
  - Custom field documentation

Success Criteria:
  - Essential fields auto-populated on module creation
  - Role assignment reduces manual effort by 80%
  - Programme-level fields cascade correctly
  - Field types handled correctly (enum, person, etc.)
```

**Phase 3: Programme Template Instantiation** (Week 3)
```yaml
Goal: Automate full programme creation from Business Development

Tasks:
  1. Implement programme creation automation
     - Input: Closed Won opportunity data
     - Action: Create programme + 8 workflow projects
     - Populate programme-level custom fields
     - Link projects to programme

  2. Build module instantiation from template
     - Duplicate module development template
     - Populate custom fields (module #, launch date, etc.)
     - Set all task dates relative to launch
     - Create 52 dependencies
     - Link to Programme Oversight

  3. Implement Programme Oversight tracker creation
     - Auto-create tracker task for each module
     - Link tracker to module project
     - Set up status aggregation

  4. Create programme setup validation
     - Verify all 8 projects created
     - Verify custom fields populated
     - Verify links between projects
     - Report any errors

Deliverables:
  - create_programme.py script
  - create_module_from_template.py script
  - Programme template configuration
  - Setup validation report

Success Criteria:
  - Full programme created in <5 minutes (vs 2+ hours manual)
  - All 8 workflow projects linked correctly
  - Module projects fully functional (dates, dependencies, fields)
  - Zero post-creation manual fixes required
```

**Phase 4: Status Aggregation & Reporting** (Week 4)
```yaml
Goal: Automate status updates and weekly reporting

Tasks:
  1. Implement status aggregation logic
     - Read module task completion %
     - Calculate module health (Green/Amber/Red)
     - Update Programme Oversight tracker
     - Flag at-risk modules

  2. Build weekly report generation
     - Pull data from Programme Oversight
     - Pull issues from Client Management
     - Generate report content (template-based)
     - Create report task with content

  3. Implement webhook subscriptions
     - Subscribe to task completion events
     - Subscribe to custom field changes
     - Trigger status aggregation on events
     - Handle webhook payload

  4. Create dashboard data preparation
     - Aggregate programme health
     - Calculate resource utilization
     - Prepare financial summaries
     - Export for dashboard visualization

Deliverables:
  - aggregate_status.py script
  - generate_weekly_report.py script
  - Webhook handler service
  - Dashboard data export utility

Success Criteria:
  - Module status auto-updates within 5 minutes of change
  - Weekly report generated in <1 minute
  - Dashboard always shows current data
  - Webhook events handled reliably (>99% success)
```

**Phase 5: Advanced Automations** (Week 5-6)
```yaml
Goal: Implement resource management and notifications

Tasks:
  1. Resource availability tracking
     - Update utilization % on assignment changes
     - Calculate capacity forecasts
     - Alert on over-allocation

  2. Escalation notifications
     - Monitor issue severity and age
     - Trigger notifications on thresholds
     - Create escalation tasks

  3. Invoice milestone automation
     - Detect deliverable completion
     - Create invoice tasks
     - Populate invoice details

  4. Dependency violation detection
     - Monitor dependency satisfaction
     - Flag violations
     - Require confirmation to override

Deliverables:
  - Resource management automation
  - Notification service
  - Invoice automation
  - Dependency monitoring

Success Criteria:
  - Resource conflicts detected and alerted
  - Critical issues never missed
  - Invoices generated within 24h of milestone
  - Dependency violations <1% of completions
```

### 6.3 API Technology Stack

**Recommended Stack**:
```yaml
Language: Python 3.11+
Framework: FastAPI (for webhook handlers)
Asana Client: asana Python SDK (official)
Task Queue: Celery + Redis (for async processing)
Database: PostgreSQL (for state/logging)
Scheduler: APScheduler (for weekly reports, etc.)
Deployment: Docker containers
Monitoring: Logging + Sentry (error tracking)
```

**Alternative Stack** (if team prefers):
```yaml
Language: Node.js/TypeScript
Framework: Express.js
Asana Client: asana Node SDK
Task Queue: Bull + Redis
Database: PostgreSQL or MongoDB
Scheduler: node-cron
Deployment: Docker containers
```

**Rationale for Python**:
- Current implementation uses Python (MCP)
- Asana SDK well-maintained
- Better date manipulation libraries
- Easier for business logic (less verbose than TypeScript)
- Team familiarity (assumed)

### 6.4 API Authentication & Security

**Authentication Method**: OAuth 2.0 with Personal Access Token (PAT)

**Security Requirements**:
```yaml
Token Management:
  - Store PAT in environment variable (never in code)
  - Use separate PAT per environment (dev/staging/prod)
  - Rotate tokens every 90 days
  - Audit token usage

API Rate Limits:
  - Respect Asana rate limit (150 requests/minute)
  - Implement exponential backoff on 429 errors
  - Batch operations where possible
  - Cache frequently-accessed data

Error Handling:
  - Log all API errors with context
  - Retry transient failures (network, rate limit)
  - Alert on persistent failures
  - Maintain idempotency (safe to retry)

Webhook Security:
  - Verify webhook signatures
  - Validate payload structure
  - Reject old/duplicate events
  - Rate limit webhook processing
```

### 6.5 API Cost & Performance Considerations

**Asana API Costs**: Free for current tier (likely Premium or Business)

**Performance Targets**:
```yaml
Operation Performance:
  - Module creation: <5 minutes (vs 30 minutes manual)
  - Date updates: <2 minutes for 72 tasks
  - Status aggregation: <30 seconds per module
  - Weekly report: <1 minute per programme
  - Batch operations: <10 minutes for 10 modules

Scalability Limits:
  - Concurrent programmes: 20+ (no bottleneck expected)
  - Modules per programme: 10+ (tested to 20)
  - API calls per day: ~5000 (well within limits)
  - Webhook events per day: ~500 (manageable)
```

**Optimization Strategies**:
```yaml
Caching:
  - Cache project structures (TTL: 1 hour)
  - Cache custom field definitions (TTL: 1 day)
  - Cache user/team data (TTL: 4 hours)

Batching:
  - Batch task updates (10 tasks per API call)
  - Batch custom field reads
  - Batch dependency creation (already doing this)

Parallelization:
  - Use async/await for independent operations
  - Parallel status aggregation across modules
  - Concurrent webhook processing

Lazy Loading:
  - Load task details only when needed
  - Paginate large result sets
  - Use sparse fieldsets (only request needed fields)
```

---

## 7. Migration Strategy

### 7.1 Migration Philosophy

**Principle**: Build new structure alongside current implementation, migrate incrementally

**Approach**:
- Phase 1: Build portfolio/programme hierarchy (empty)
- Phase 2: Create one pilot programme with all 8 workflows
- Phase 3: Migrate existing module projects into pilot programme
- Phase 4: Create additional programmes as needed
- Phase 5: Deprecate standalone module projects

**Risk Mitigation**:
- Keep current module template functional during migration
- Test all new structures before production use
- Maintain rollback capability
- Document migration steps for team

### 7.2 Migration Phases

**Phase 1: Foundation Setup** (Week 1)
```yaml
Goal: Establish portfolio and first programme

Tasks:
  1. Create "LDS Operations" portfolio in Asana
  2. Create pilot programme: "TEST - Programme Structure"
  3. Create all 8 workflow projects in pilot programme
  4. Configure custom fields at programme level
  5. Document new structure for team

Deliverables:
  - Portfolio created with pilot programme
  - 8 workflow projects (empty templates)
  - Custom field configuration
  - Migration documentation

Validation:
  - Team can access new portfolio
  - Custom fields display correctly
  - Links between projects work
  - No impact on current module projects
```

**Phase 2: Module Template Integration** (Week 2)
```yaml
Goal: Integrate current module template into programme structure

Tasks:
  1. Duplicate current module template into pilot programme
  2. Add programme-level custom fields to template
  3. Update template documentation to reference programme
  4. Test template duplication within programme
  5. Validate dependencies still work

Deliverables:
  - Module template as programme project
  - Updated custom fields
  - Tested duplication workflow
  - Updated documentation

Validation:
  - Template duplicates correctly
  - All 52 dependencies preserved
  - Custom fields populated
  - Dates can be set via API
```

**Phase 3: API Implementation** (Week 3-4)
```yaml
Goal: Implement date management and field automation

Tasks:
  1. Build date calculation and setting logic (Phase 1 from API plan)
  2. Implement custom field automation (Phase 2 from API plan)
  3. Test on pilot programme module
  4. Create programme instantiation script (Phase 3 from API plan)
  5. Document API usage for team

Deliverables:
  - Working date automation
  - Custom field automation
  - Programme creation automation
  - API documentation

Validation:
  - Dates set correctly from Launch Date
  - Custom fields populate automatically
  - New programmes created in <5 minutes
  - Zero manual post-creation fixes
```

**Phase 4: Pilot Programme Population** (Week 5)
```yaml
Goal: Populate pilot programme with real workflow content

Tasks:
  1. Populate Business Development project (if applicable)
  2. Populate Client Onboarding project (with pilot data)
  3. Populate Programme Oversight project (with module trackers)
  4. Create 2-3 test module projects in pilot
  5. Populate Team & Resources project (with current team)
  6. Configure Client Management project
  7. Configure Finance project (with pilot financials)
  8. Configure Closeout project (leave for future)

Deliverables:
  - Fully populated pilot programme
  - Real workflow data (anonymized if needed)
  - Working examples of all integrations
  - Lessons learned document

Validation:
  - All workflow projects functional
  - Data flows between projects correctly
  - Team can navigate structure
  - Reports generate correctly
```

**Phase 5: Production Rollout** (Week 6-8)
```yaml
Goal: Create real client programmes and migrate existing modules

Tasks:
  1. Create first real client programme (highest priority)
  2. Migrate 2-3 existing modules into programme structure
  3. Validate no disruption to ongoing work
  4. Create second client programme
  5. Train team on new structure and workflows
  6. Document best practices and workflows

Deliverables:
  - 2+ real client programmes in production
  - Migrated modules functioning correctly
  - Team training complete
  - Production documentation

Validation:
  - Modules continue operating normally
  - Team using new structure effectively
  - Reports and dashboards working
  - No showstopper issues
```

**Phase 6: Complete Migration** (Week 9-12)
```yaml
Goal: Migrate all remaining modules and deprecate old structure

Tasks:
  1. Migrate all remaining modules to appropriate programmes
  2. Create programmes for all active clients
  3. Archive or delete old standalone projects
  4. Implement advanced automations (Phase 4-5 from API plan)
  5. Launch cross-programme reporting
  6. Conduct retrospective and capture lessons

Deliverables:
  - 100% of modules in programme structure
  - Old structure deprecated
  - Advanced automations running
  - Cross-programme reports available
  - Retrospective document

Validation:
  - No modules outside programme structure
  - All automations functioning
  - Team proficient with new system
  - Client-facing workflows smooth
```

### 7.3 Rollback Plan

**If Critical Issues Arise**:

```yaml
Rollback Triggers:
  - Data loss or corruption
  - System unusable for >4 hours
  - Team cannot complete critical work
  - Client-facing disruption

Rollback Procedure:
  1. Pause all migrations immediately
  2. Document issue thoroughly
  3. Restore access to old module projects
  4. Communicate status to team
  5. Investigate root cause
  6. Fix issue in pilot environment
  7. Re-test before resuming migration

Rollback Safety:
  - Old module projects NOT deleted until migration complete
  - All new structures tested in pilot first
  - Incremental migration allows partial rollback
  - API operations logged for audit trail
```

### 7.4 Team Change Management

**Communication Plan**:
```yaml
Week 0 (Before Migration):
  - Announce coming changes to team
  - Share vision for new structure
  - Explain benefits (better tracking, less manual work)
  - Set expectations for timeline
  - Invite feedback and questions

Week 1-2 (Foundation):
  - Show pilot programme structure
  - Walk through new hierarchy
  - Explain custom fields and their purpose
  - Demonstrate navigation
  - Keep team informed of progress

Week 3-4 (API Implementation):
  - Demo automation features
  - Explain how dates will auto-calculate
  - Show weekly report generation
  - Preview programme dashboard
  - Address concerns about change

Week 5 (Pilot Population):
  - Invite team to explore pilot programme
  - Hands-on session: creating modules
  - Practice navigation and workflows
  - Collect feedback and adjust
  - Build confidence before production

Week 6-8 (Production Rollout):
  - Formal training session
  - Documentation: how-to guides
  - Office hours for questions
  - Monitor usage and provide support
  - Celebrate quick wins

Week 9-12 (Complete Migration):
  - Continued support and refinement
  - Advanced features training
  - Best practices documentation
  - Retrospective: what worked, what didn't
  - Recognition for team adaptation
```

**Training Materials Needed**:
- Quick Start Guide: New programme structure
- Video: Navigating portfolio → programme → projects
- Video: Creating a new module in programme
- Cheat Sheet: Custom field meanings
- FAQ: Common questions about new structure
- Reference: Where to find what (old vs new)

---

## 8. Reporting & Views

### 8.1 Key Reports Required

From Remote Google Doc Workflow 3 and 6:

**1. Programme Dashboard** (Programme Oversight)
```yaml
View: Board grouped by Module Phase
Columns: Planning, Storyboarding, Build, Review, Launch Prep, Complete
Cards: Module tracker tasks
Card Fields: Module number, Health status, Days to launch, LD/LT assigned

Filters:
  - Hide complete modules (optional)
  - Show only at-risk modules
  - Filter by assigned LD/LT

Purpose: At-a-glance programme status for Andrew
Update Frequency: Real-time (as tasks update)
```

**2. Weekly Client Report** (Client Management)
```yaml
Content:
  - Programme overview (modules planned/active/complete)
  - This week's progress (tasks completed per module)
  - Issues encountered (from issue log)
  - Risks identified (timeline, resource, quality)
  - Next week's planned milestones
  - Upcoming decisions needed
  - Overall health status

Format: Text summary in task notes (can export to Google Doc)
Frequency: Weekly (Mondays)
Generation: Automated via API
```

**3. Resource Utilization Dashboard** (Team & Resources)
```yaml
View: List grouped by Resource
Rows: Each team member (LD, LT, SLD)
Fields: Utilization %, Modules assigned, Available start date

Filters:
  - Filter by role type (LD, LT, SLD)
  - Filter by location (UK, Offshore)
  - Show only available resources

Purpose: Resource planning for new modules
Update Frequency: Real-time (as assignments change)
```

**4. Financial Summary** (Finance & Operations)
```yaml
View: List grouped by Budget Item Type
Sections: Revenue, Costs, Invoicing, Profitability
Fields: Amount, Date, Status, Notes

Summary Calculations:
  - Total Revenue
  - Total Costs (broken down by role)
  - Gross Margin £ and %
  - Outstanding Invoices
  - Projected Profitability

Purpose: Programme financial health tracking
Update Frequency: Updated as costs/invoices logged
```

**5. Cross-Programme Portfolio View**
```yaml
View: Portfolio Timeline or Board
Scope: All programmes in portfolio
Grouping: By programme status or client
Fields: Programme name, Active modules, Health status, Next milestone

Filters:
  - Show only active programmes
  - Filter by client
  - Show only at-risk programmes

Purpose: Executive overview for Andrew across all clients
Update Frequency: Real-time
```

### 8.2 Asana Views Configuration

**Custom Views to Create**:

```yaml
Programme Oversight Views:
  1. "Module Status Board"
     - Type: Board
     - Group by: Module Phase
     - Sort: By launch date
     - Color: By health status

  2. "At Risk Modules"
     - Type: List
     - Filter: Health = Red OR Blockers = Yes
     - Sort: By days to launch (ascending)
     - Highlight: Critical items

  3. "Module Timeline"
     - Type: Timeline (Gantt)
     - Show: All module tracker tasks
     - Color: By assigned LD
     - Dependencies: Show cross-module dependencies

Client Management Views:
  1. "Open Issues"
     - Type: List
     - Filter: Status = Open OR In Progress
     - Sort: By severity, then days open
     - Group by: Issue type

  2. "Weekly Reports Archive"
     - Type: List
     - Filter: Task name contains "Week"
     - Sort: By date (descending)
     - Show: Report status

Team & Resources Views:
  1. "Resource Availability"
     - Type: Board
     - Group by: Availability status
     - Sort: By utilization %
     - Show: Current allocations

  2. "LD/LT Pairs"
     - Type: List
     - Group by: Module assigned
     - Show: LD, LT, Module, Dates

Finance & Operations Views:
  1. "Outstanding Invoices"
     - Type: List
     - Filter: Invoice status != Paid
     - Sort: By due date
     - Highlight: Overdue (red)

  2. "Programme P&L"
     - Type: List
     - Group by: Budget item type
     - Show: Running totals
     - Calculate: Revenue - Costs = Profit

Portfolio Views:
  1. "All Programmes"
     - Type: Board
     - Group by: Programme status
     - Sort: By client name
     - Color: By health status

  2. "Programme Timeline"
     - Type: Timeline
     - Show: Programme start → end dates
     - Show: Module milestones
     - Color: By client
```

### 8.3 Dashboard Integration

**Future Integration Options** (beyond Asana):

```yaml
Power BI / Tableau Dashboard:
  Purpose: Advanced analytics and executive reporting
  Data Source: Asana API export + Clockify + Accounting system
  Refresh: Daily or real-time
  Views:
    - Portfolio health overview
    - Revenue vs costs trend
    - Resource utilization heatmap
    - Module delivery timeline
    - Client satisfaction scores
    - Profitability by client

Google Data Studio:
  Purpose: Lighter-weight alternative to Power BI
  Data Source: Asana API → Google Sheets → Data Studio
  Refresh: Daily
  Views: Simplified versions of Power BI views

Asana Reporting (Native):
  Purpose: Built-in Asana dashboards (Premium/Business feature)
  Configuration: Within Asana UI
  Views:
    - Portfolio progress charts
    - Custom field reports
    - Workload charts
    - Burn-up/burn-down for modules

Custom Dashboard (API-built):
  Purpose: Tailored to LDS specific needs
  Technology: React/Next.js frontend + Python backend
  Data Source: Real-time Asana API
  Features:
    - Real-time module status
    - Interactive timeline
    - Drag-and-drop resource planning
    - What-if scenario modeling
```

### 8.4 Client-Facing Views

**Consideration**: What should clients see in Asana?

**Option A: Full Visibility**
```yaml
Client Access: Guest on Programme project
Can See:
  - Module Development projects (their modules)
  - Programme Oversight (status tracker)
  - Client Management (weekly reports, issue log)
Cannot See:
  - Team & Resources (internal)
  - Finance & Operations (confidential)
  - Other clients' programmes

Pros: Maximum transparency, self-service status
Cons: Requires client training, may expose internal discussions
```

**Option B: Limited Visibility**
```yaml
Client Access: Guest on specific projects only
Can See:
  - Client Management project (reports, feedback)
  - Selected deliverable tasks (as they're ready)
Cannot See:
  - Module Development internal workflow
  - Programme Oversight
  - Resource/Finance projects

Pros: Simpler, less overwhelming, maintains working space
Cons: Less transparency, more status requests
```

**Option C: No Asana Access** (Current State)
```yaml
Client Access: None (status via weekly report in shared drive)
Can See:
  - Weekly reporting spreadsheet in Google Drive
  - Deliverables as they're shared
Cannot See:
  - Anything in Asana

Pros: Simplest, no client training, maintains privacy
Cons: Manual reporting burden, less real-time visibility
```

**Recommendation**: Start with Option C (current state), offer Option B to interested clients, reserve Option A for strategic clients with sophisticated PM practices.

---

## 9. Technical Specifications

### 9.1 Hierarchy Specifications

**Asana Hierarchy Limits** (as of 2025):
```yaml
Portfolio:
  Max Projects per Portfolio: 250
  Nesting: Portfolios cannot contain portfolios
  Custom Fields: Yes (portfolio-level)

Project:
  Max Tasks per Project: No hard limit (thousands possible)
  Max Sections per Project: No hard limit (hundreds possible)
  Nesting: Projects cannot contain projects
  Custom Fields: Yes (project-level and inherited)

Task:
  Max Subtasks per Task: No hard limit
  Nesting Depth: Subtask → Sub-subtask → 1 level only (2 levels max)
  Dependencies: Unlimited (practically <100 per task)
  Assignees: 1 per task (workaround: use subtasks for multi-assign)

Custom Fields:
  Max per Organization: 2000 (Premium/Business)
  Types: Text, Number, Dropdown, Multi-select, Date, Person, Formula
  Formulas: Basic calculations supported (sum, count, etc.)
```

**LDS Architecture Limits** (planned):
```yaml
Portfolio Level:
  Total Portfolios: 1 (start), up to 3 (if scale)
  Programmes per Portfolio: 20+ (no expected bottleneck)

Programme Level:
  Projects per Programme: 8 (fixed) + N modules (variable)
  Modules per Programme: Typically 5-15, max ~20
  Total Projects: 8 + 20 = 28 max (well within limits)

Project Level:
  Tasks per Module Project: 72 (fixed template)
  Sections per Module: 12 (fixed template)
  Dependencies per Module: 52 (fixed template)

Total System Load (at scale):
  Programmes: 20
  Modules: 20 programmes × 10 modules avg = 200 modules
  Module Tasks: 200 × 72 = 14,400 tasks
  Total Projects: 20 × 8 + 200 = 360 projects

Assessment: Well within Asana limits, no performance concerns expected
```

### 9.2 Custom Field Technical Specs

**Field Type Decisions**:

```yaml
Text Fields:
  Use for: Names, codes, descriptions, notes
  Examples: Programme Name, Module Code, Blocker Description
  Limitations: No character limit, but keep <500 chars for display

Number Fields:
  Use for: Counts, percentages, metrics, calculations
  Examples: Module Number, Utilization %, Days to Launch
  Limitations: Integers or decimals, no currency symbol (use Currency type)

Currency Fields:
  Use for: Financial values
  Examples: Budget, Invoice Amount, Day Rate
  Format: £ (GBP)
  Limitations: No automatic calculations (use external or Formula field)

Date Fields:
  Use for: Milestones, deadlines, anchors
  Examples: Launch Date, Go Live Date, Invoice Due Date
  Limitations: Date only (not datetime), no timezone

Dropdown (Single-select):
  Use for: Status, phase, category (one value only)
  Examples: Module Phase, Health Status, Pipeline Stage
  Options: Define enum options, can add more later
  Limitations: Single value only, no multi-select

Multi-select:
  Use for: Tags, categories (multiple values)
  Examples: Issue Types (can have Technical + Timeline)
  Limitations: Cannot use in formulas

Person Fields:
  Use for: Assignments, owners, stakeholders
  Examples: LD Assigned, LT Assigned, PM Owner
  Limitations: Must be Asana user, no external contacts

Formula Fields:
  Use for: Calculations from other fields
  Examples: Gross Margin = Revenue - Costs
  Syntax: Limited (sum, count, basic arithmetic)
  Limitations: Cannot reference tasks outside project

Checkbox:
  Use for: Yes/No, True/False
  Examples: Blockers, Client Visibility, Ready for Launch
  Limitations: Binary only
```

**Field Naming Conventions**:
```yaml
Convention: Use descriptive, consistent names
Examples:
  Good: "LD Assigned", "Launch Date", "Health Status"
  Bad: "LD", "Date", "Status" (ambiguous)

Prefixes (if needed for clarity):
  Module_* for module-specific fields
  Programme_* for programme-level fields
  Financial_* for finance fields

Avoid:
  Special characters (except dash, underscore)
  Leading/trailing spaces
  Very long names (>30 chars if possible)
```

### 9.3 Dependency Specifications

**Current Module Template Dependencies**: 52 (fully documented in dependency_mapping.json)

**Cross-Module Dependencies** (new for programme structure):
```yaml
Use Case: Module B cannot start until Module A launches
Implementation:
  - Create dependency between:
      "Module B - Kick off meeting" (dependent)
      "Module A - Go live" (dependency)

Caveat: Cross-project dependencies supported but harder to manage
Recommendation: Model in Programme Oversight with manual enforcement initially
```

**Programme-Level Dependencies**:
```yaml
Use Case: Programme closeout depends on all modules complete
Implementation:
  - Model as tasks in Programme Oversight
  - Create dependencies within Programme Oversight project
  - Use automation to check module completion

Example:
  "Programme Closeout Ready" (dependent)
  "Module 1 Complete", "Module 2 Complete", ... (dependencies)
```

**Dependency Best Practices**:
```yaml
Within Project (Module Template):
  - Use liberally (52 dependencies in module is fine)
  - Ensure logical flow (storyboard → build → review)
  - Test dependency chain doesn't block incorrectly

Cross-Project (Programme Level):
  - Use sparingly (complex to manage)
  - Document clearly (why is this dependency needed?)
  - Consider alternatives (custom field status checks)

Maintenance:
  - Version control dependency mappings (JSON files)
  - Test changes in pilot before production
  - Document rationale for complex dependencies
```

### 9.4 Performance Specifications

**API Performance Targets** (from earlier section, summarized):
```yaml
Module Creation: <5 minutes (API-driven)
Date Updates: <2 minutes for 72 tasks
Status Aggregation: <30 seconds per module
Weekly Report: <1 minute per programme
Webhook Response: <5 seconds per event

API Rate Limits: 150 requests/minute (respect Asana limits)
Concurrent Operations: 10+ parallel API calls (async)
Cache TTL: 1 hour (project structure), 1 day (custom field defs)
```

**Asana UI Performance** (user experience):
```yaml
Project Load Time: <2 seconds (for 72-task module)
Board View Render: <3 seconds (for 20 modules)
Timeline View: <5 seconds (for programme timeline)
Search: <1 second (within project)
Filter Application: <1 second

Expected: Performance remains good even with 200 modules in portfolio
```

---

## 10. Implementation Roadmap

### 10.1 Timeline Summary

**Total Duration**: 12 weeks (3 months)

```yaml
Weeks 1-2: Foundation & Date Implementation
Weeks 3-4: Custom Fields & Module Automation
Weeks 5-6: Pilot Programme & Testing
Weeks 7-8: Production Rollout & Training
Weeks 9-12: Complete Migration & Advanced Features
```

### 10.2 Detailed Weekly Plan

**Week 1: Foundation Setup + Date Logic**
```yaml
Monday-Tuesday:
  - Create "LDS Operations" portfolio
  - Create pilot programme structure
  - Create 8 workflow project templates (empty)
  - Configure programme-level custom fields

Wednesday-Friday:
  - Build date calculation engine (backward from Launch Date)
  - Implement holiday skip logic
  - Create set_module_dates.py script
  - Test date calculations on pilot module

Deliverables:
  - Portfolio + pilot programme created ✓
  - Date automation working ✓
  - Holiday logic tested ✓

Success Criteria:
  - Can set all 72 task dates from Launch Date in <2 min
  - Christmas and academic breaks skipped correctly
```

**Week 2: Date API Implementation + Custom Field Design**
```yaml
Monday-Tuesday:
  - Implement Asana API calls for task date setting
  - Test date API on pilot module
  - Validate dependencies still work after date changes
  - Document date setting process

Wednesday-Friday:
  - Design complete custom field taxonomy (prioritize essential fields)
  - Create custom fields in Asana workspace
  - Map custom fields to hierarchy levels
  - Document custom field purposes and values

Deliverables:
  - Date API functional ✓
  - Essential custom fields created ✓
  - Custom field documentation ✓

Success Criteria:
  - API sets dates reliably (>99% success)
  - Custom fields accessible at correct hierarchy levels
```

**Week 3: Custom Field Automation + Module Template Enhancement**
```yaml
Monday-Wednesday:
  - Implement custom field write operations via API
  - Build field propagation logic (programme → module)
  - Create populate_custom_fields.py script
  - Test on pilot module

Thursday-Friday:
  - Enhance module template with custom fields
  - Add programme-level linking
  - Update module template documentation
  - Test template duplication with custom fields

Deliverables:
  - Custom field automation working ✓
  - Enhanced module template ✓
  - Field propagation tested ✓

Success Criteria:
  - Custom fields auto-populate on module creation
  - Programme-level fields cascade correctly
```

**Week 4: Programme Instantiation Automation**
```yaml
Monday-Wednesday:
  - Build create_programme.py script
  - Implement 8-project creation logic
  - Build create_module_from_template.py script
  - Test full programme creation

Thursday-Friday:
  - Create Programme Oversight tracker automation
  - Implement module → tracker linking
  - Build setup validation checks
  - Document automation usage

Deliverables:
  - Programme creation automation ✓
  - Module instantiation automation ✓
  - Setup validation working ✓

Success Criteria:
  - Full programme created in <5 minutes
  - All projects linked correctly
  - Validation catches errors
```

**Week 5: Pilot Programme Population**
```yaml
Monday:
  - Populate Client Onboarding project (pilot data)
  - Populate Programme Oversight project (with sample modules)

Tuesday:
  - Create 2-3 test module projects in pilot programme
  - Populate Team & Resources project (current team)

Wednesday:
  - Configure Client Management project (sample reports, issues)
  - Configure Finance project (sample budget, invoices)

Thursday:
  - Test data flow between all 8 projects
  - Validate links and custom fields
  - Identify any issues or gaps

Friday:
  - Document pilot programme structure
  - Create lessons learned document
  - Prepare for team demo

Deliverables:
  - Fully populated pilot programme ✓
  - Workflow integration tested ✓
  - Lessons documented ✓

Success Criteria:
  - All 8 workflows represented
  - Data flows correctly
  - Team can navigate structure
```

**Week 6: Status Aggregation + Weekly Reporting**
```yaml
Monday-Tuesday:
  - Implement status aggregation logic
  - Build aggregate_status.py script
  - Test module status → tracker updates

Wednesday-Thursday:
  - Build weekly report generation logic
  - Create generate_weekly_report.py script
  - Test report generation on pilot

Friday:
  - Set up scheduled execution (cron/scheduler)
  - Test end-to-end automation flow
  - Document automation workflows

Deliverables:
  - Status aggregation working ✓
  - Weekly reports auto-generated ✓
  - Scheduling configured ✓

Success Criteria:
  - Module status updates within 5 minutes
  - Weekly report generated in <1 minute
```

**Week 7: Production Rollout Preparation**
```yaml
Monday-Tuesday:
  - Create first real client programme
  - Migrate 2-3 existing modules into programme
  - Validate no disruption to ongoing work

Wednesday:
  - Team training session (2 hours)
  - Walk through new structure
  - Demo automation features
  - Q&A and feedback

Thursday-Friday:
  - Create production documentation
  - Write how-to guides
  - Create quick reference materials
  - Set up support process

Deliverables:
  - First real programme in production ✓
  - Team training complete ✓
  - Production documentation ✓

Success Criteria:
  - Modules work normally in new structure
  - Team comfortable with navigation
  - Support process ready
```

**Week 8: Production Expansion**
```yaml
Monday-Tuesday:
  - Create 2nd and 3rd client programmes
  - Migrate additional modules

Wednesday-Thursday:
  - Monitor usage and issues
  - Provide hands-on support
  - Refine based on feedback

Friday:
  - Week 8 retrospective
  - Identify improvements needed
  - Plan remaining migration

Deliverables:
  - 3+ programmes in production ✓
  - Team using system actively ✓
  - Improvement backlog prioritized ✓

Success Criteria:
  - No critical issues blocking work
  - Team adoption >80%
  - Automations functioning reliably
```

**Week 9: Complete Migration + Webhook Setup**
```yaml
Monday-Wednesday:
  - Migrate remaining modules to programmes
  - Create programmes for all active clients
  - Validate complete migration

Thursday-Friday:
  - Implement webhook subscriptions
  - Build webhook handler service
  - Test event-driven status updates

Deliverables:
  - All modules in programme structure ✓
  - Webhook automation functional ✓

Success Criteria:
  - 100% modules migrated
  - Real-time updates working via webhooks
```

**Week 10: Advanced Automations**
```yaml
Monday-Tuesday:
  - Implement resource availability tracking
  - Build capacity alerts

Wednesday-Thursday:
  - Implement escalation notifications
  - Build invoice milestone automation

Friday:
  - Test advanced automations
  - Document new features

Deliverables:
  - Resource management automation ✓
  - Notification service ✓
  - Invoice automation ✓

Success Criteria:
  - Resource conflicts detected automatically
  - Critical issues flagged immediately
  - Invoices generated on milestones
```

**Week 11: Cross-Programme Reporting**
```yaml
Monday-Tuesday:
  - Build portfolio dashboard views
  - Create cross-programme reports

Wednesday-Thursday:
  - Implement financial summary automation
  - Build resource utilization heatmap

Friday:
  - Create executive dashboard
  - Test reporting accuracy

Deliverables:
  - Portfolio reporting functional ✓
  - Executive dashboard ready ✓

Success Criteria:
  - Andrew can view all programmes at-a-glance
  - Financial summaries accurate
  - Resource utilization visible
```

**Week 12: Finalization + Retrospective**
```yaml
Monday-Tuesday:
  - Archive or delete old standalone projects
  - Clean up pilot programme
  - Final documentation updates

Wednesday:
  - Full system test (end-to-end)
  - Validate all workflows functioning
  - Performance testing

Thursday:
  - Team retrospective session
  - Capture lessons learned
  - Celebrate completion

Friday:
  - Final documentation handoff
  - Maintenance plan creation
  - Future enhancements roadmap

Deliverables:
  - Old structure deprecated ✓
  - Complete system operational ✓
  - Retrospective documented ✓
  - Maintenance plan ready ✓

Success Criteria:
  - All workflows operational
  - Team proficient and confident
  - Client-facing work uninterrupted
  - Clear path for future enhancements
```

### 10.3 Resource Requirements

**Development Effort**:
```yaml
Total Development Time: ~160-240 hours (4-6 weeks full-time equivalent)

Breakdown:
  Week 1-2 (Foundation): 40 hours
  Week 3-4 (Automation): 60 hours (most complex API work)
  Week 5-6 (Testing): 30 hours
  Week 7-8 (Rollout): 20 hours
  Week 9-12 (Migration & Polish): 50 hours

Skills Needed:
  - Python development (API integration, date logic, automation)
  - Asana expertise (structure, custom fields, dependencies)
  - Project management (migration planning, change management)
  - Documentation (technical writing, training materials)
```

**Team Involvement**:
```yaml
Andrew (PM):
  - Requirements validation: 5 hours
  - Pilot testing: 5 hours
  - Training delivery: 3 hours
  - Migration oversight: 10 hours
  Total: ~25 hours spread over 12 weeks

LDs/LTs (Team):
  - Training: 2 hours per person
  - Feedback sessions: 2 hours per person
  - Pilot usage: 5 hours per person
  Total: ~10 hours per person

Developer/Implementer:
  - Full implementation: 160-240 hours
  - Can be spread part-time over 12 weeks
  - Or compressed to 4-6 weeks full-time
```

**External Resources** (if needed):
```yaml
Asana Consultant:
  - Optional: Architecture review (4 hours)
  - Optional: Custom field design review (2 hours)
  Cost: ~£500-1000

Training Materials:
  - Video production (if creating videos): ~£500
  - Or: Screen recordings with Loom (free)
```

### 10.4 Success Metrics

**Quantitative Metrics**:
```yaml
Efficiency Gains:
  - Programme creation time: 2+ hours → <5 minutes (96% reduction)
  - Module creation time: 30-45 min → <5 minutes (90% reduction)
  - Weekly report generation: 15-30 min → <1 minute (95% reduction)
  - Date management: 10-15 min/module → 0 minutes (100% elimination)
  - Total time saved: ~2-3 hours per module = 20-30 hours per 10-module programme

Accuracy Improvements:
  - Dependency errors: Manual ~5% → API <1% (80% reduction)
  - Date calculation errors: Manual ~10% → API 0% (100% elimination)
  - Missing custom fields: Manual ~20% → API 0% (100% elimination)

System Adoption:
  - Team using new structure: Target >90% by Week 8
  - Programmes in new structure: Target 100% by Week 9
  - Automation usage: Target 100% of new modules by Week 7
```

**Qualitative Metrics**:
```yaml
Team Satisfaction:
  - Ease of navigation (survey): Target >4/5
  - Confidence in system (survey): Target >4/5
  - Perceived value (survey): Target >4/5
  - Frustration reduction: High → Low

Client Impact:
  - Client visibility (if offered): Improved
  - Reporting timeliness: Improved (always on-time)
  - Issue resolution speed: Improved (earlier detection)
  - Overall client satisfaction: Maintained or improved

Business Impact:
  - Programme management overhead: Reduced
  - Scalability: 10 modules → 20+ modules without additional overhead
  - Profitability visibility: Real-time (vs month-end)
  - Resource utilization optimization: Improved by 10-15%
```

---

## 11. Future Enhancements

**Post-Implementation Roadmap** (beyond Week 12):

### Phase 1: System Integrations (Month 4-6)
```yaml
Clockify Integration:
  - Sync time entries to Finance project
  - Auto-update actual hours on tasks
  - Calculate cost actuals from time entries

Accounting System Integration:
  - Sync invoices from Asana to accounting software
  - Pull payment received status
  - Auto-update Profit First allocations

Google Drive Integration:
  - Link weekly reports to client shared drives
  - Auto-create programme folders
  - Link deliverables to Asana tasks
```

### Phase 2: Advanced Analytics (Month 6-9)
```yaml
Power BI Dashboard:
  - Real-time portfolio health
  - Revenue vs cost trends
  - Resource utilization heatmaps
  - Predictive delivery analytics

Forecasting:
  - Module delivery date predictions
  - Resource capacity forecasting
  - Revenue forecasting
  - Risk probability modeling

Benchmarking:
  - Module velocity tracking
  - Compare actual vs planned timelines
  - Quality metrics over time
  - Client satisfaction trends
```

### Phase 3: AI Enhancements (Month 9-12)
```yaml
Intelligent Automation:
  - AI-suggested resource allocation
  - Predictive risk detection
  - Automated issue categorization
  - Smart weekly report summarization

Chatbot Interface:
  - "What's the status of Module X?"
  - "When is the next milestone?"
  - "Show me at-risk modules"
  - Natural language queries

Content Generation:
  - Auto-draft weekly reports
  - Auto-draft client communications
  - Auto-draft meeting agendas
```

### Phase 4: Client Portal (Month 12-18)
```yaml
External Dashboard:
  - Branded client portal
  - Real-time module status
  - Deliverable downloads
  - Issue submission
  - Feedback forms

Mobile App:
  - On-the-go status checks
  - Push notifications for milestones
  - Quick issue reporting
  - Photo/video uploads
```

---

## 12. Appendices

### Appendix A: Glossary

```yaml
Programme: Client engagement with multiple modules (Asana Portfolio or Project depending on implementation)
Module: 8-week educational unit (Asana Project using current template)
Workflow: One of 8 business processes (Asana Project within Programme)
Portfolio: Top-level Asana container for programmes
LD: Learning Designer (creates educational content)
LT: Learning Technologist (builds digital modules)
SLD: Senior Learning Designer (Nicole - quality assurance)
MA/SME: Module Author / Subject Matter Expert (client-side expert)
PM: Programme Manager (Andrew)
Launch Date: Target date for module completion (anchor for all relative dates)
Go Live Date: Actual date module becomes available to students
Launch Buffer: Time between Ready for Launch and Go Live (typically 10 weeks)
MPD: Module Planning Document (initial specification)
```

### Appendix B: Custom Field Complete List

**See Section 4 for full details. Total: ~80-100 custom fields across all hierarchy levels.**

### Appendix C: API Endpoints Reference

**Key Asana API Endpoints Used**:
```yaml
Projects:
  - GET /projects/{project_gid}
  - POST /projects
  - PUT /projects/{project_gid}
  - POST /projects/{project_gid}/duplicate

Tasks:
  - GET /tasks/{task_gid}
  - POST /tasks
  - PUT /tasks/{task_gid}
  - GET /projects/{project_gid}/tasks

Dependencies:
  - POST /tasks/{task_gid}/addDependencies
  - POST /tasks/{task_gid}/addDependents

Custom Fields:
  - GET /custom_fields/{custom_field_gid}
  - POST /custom_fields
  - GET /workspaces/{workspace_gid}/custom_fields

Webhooks:
  - POST /webhooks
  - GET /webhooks/{webhook_gid}
  - DELETE /webhooks/{webhook_gid}
```

### Appendix D: Migration Checklist

**Pre-Migration**:
- [ ] Pilot programme fully tested
- [ ] Team trained on new structure
- [ ] Documentation complete
- [ ] Rollback plan ready
- [ ] Stakeholder approval obtained

**During Migration** (per programme):
- [ ] Create programme in portfolio
- [ ] Create 8 workflow projects
- [ ] Populate custom fields
- [ ] Migrate or create modules
- [ ] Set up automations
- [ ] Validate all links
- [ ] Test data flow
- [ ] Team validation

**Post-Migration**:
- [ ] Monitor for issues (first week)
- [ ] Gather team feedback
- [ ] Refine based on learnings
- [ ] Document any workarounds
- [ ] Celebrate success

### Appendix E: Support & Maintenance

**Ongoing Maintenance**:
```yaml
Daily:
  - Monitor automation logs
  - Check for failed API calls
  - Respond to team support requests

Weekly:
  - Review system usage metrics
  - Check for performance issues
  - Update documentation as needed

Monthly:
  - Review custom field usage (any unused?)
  - Analyze automation effectiveness
  - Plan incremental improvements

Quarterly:
  - System health review
  - Team feedback session
  - Roadmap review and adjustment
```

**Support Resources**:
```yaml
Documentation:
  - This architecture document
  - Technical Reference Manual (TECHNICAL_REFERENCE.md)
  - Tutorial (TUTORIAL.md)
  - FAQ (FAQ.md)

Training:
  - Initial training session (recorded)
  - Office hours (weekly first month, then monthly)
  - 1-on-1 support as needed

Escalation:
  - Level 1: Team lead / power user
  - Level 2: System implementer / developer
  - Level 3: Asana support (for platform issues)
```

---

## Document Control

**Version History**:
- v1.0 (2025-10-20): Initial comprehensive architecture design

**Authors**:
- Primary: Claude Code (AI Assistant)
- Review: Andrew (PM, Learning Design Solutions)

**Status**: Draft for Review → To be approved before implementation

**Next Steps**:
1. Review with Andrew for feedback
2. Prioritize features (must-have vs nice-to-have)
3. Validate timeline and resource requirements
4. Obtain approval to proceed with Week 1 implementation
5. Begin foundation setup

---

**END OF COMPREHENSIVE ASANA ARCHITECTURE DESIGN**
