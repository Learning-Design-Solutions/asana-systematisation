# Asana Systematisation Project - Module Development Template Context

## 1. Project Overview
### Goals
- Implement Asana-based project management system for module development workflow
- Replace manual spreadsheet tracking with automated Asana system
- Total timeline: 178 days (112 days to Ready for Launch + 66-day buffer)

### Key Architectural Decisions
- Platform: Asana Premium
- Hierarchy: Portfolio → Project → Section → Task → Subtask
- Unique Characteristics:
  * Week 1 extended to 10 days (vs standard 5-day weeks)
  * Batched academic reviews (Weeks 1-2, then 3-8)
  * Cascading build pattern for resource efficiency

### Technology Stack
- Primary Tool: Asana Premium
- Supporting Tools:
  * Native time tracking
  * CSV import with manual dependency completion
  * Future potential for automation rules

### Team Conventions
- Resource Categories:
  * Internal: LD, LT, SLD
  * External: SME, Academic Reviewer
- Permission Model: Granular access, users see only shared content

## 2. Current State
### Recent Implementations
- CSV Import File: Module_Development_Template_IMPORT.csv
  * 72+ tasks
  * 11 sections
  * Comprehensive custom fields
  * Detailed dependency mapping

### Test Imports
- Project 1211626875246589 (Direct)
  * Subtasks present
  * Missing start dates
  * Incomplete dependencies

### Known Technical Limitations
- Asana CSV Import Constraint: Cannot import dependencies
- Mitigation Options:
  * Manual UI completion (~20 min for 45 relationships)
  * Potential API-based solution

### Performance Baseline
- Template Completion: 49 minutes total manual work
- Total Estimated Effort: 1,364 hours across all roles

## 3. Design Decisions
### Architectural Choices
- Extended Timeline: 17-18 weeks (vs documented 16 weeks)
- Week 1: Extended for LD-SME relationship building
- Task Structure: Separate top-level tasks for resource clarity

### API and Integration Approach
- Asana API Used For:
  * Project analysis
  * Task retrieval
  * Potential future dependency creation

### Custom Fields
- Module Code
- Client Name
- Programme Name
- Launch/Go Live Dates
- Resource Assignments
- Status Tracking
- Review Batch Categorization

### Security Model
- Granular Permissions
- Explicit Content Sharing
- Role-Based Access Control

## 4. Technical Patterns
### Coding Conventions
- File Conversion: LibreOffice (XLSX → CSV)
- Analysis Tools: Asana API
- CSV Format: Matched MBA.csv example structure

### Key Technical Patterns
- Relative Date Calculations from Launch Date
- Dependency Grouping:
  * Critical Path
  * Cascading
  * Within-Task
  * Finalization
- Resource Type Categorization

### Testing Strategy
- Two-Project Test Import Approach
- Comprehensive Comparative Analysis
- Fallback to Manual Processes

## 5. Future Roadmap
### Planned Features
- Solution 1: Manual Dependency Completion
- Automation Rule Configuration
- Portfolio-Level Programme Organization

### Improvement Opportunities
- API-Based Dependency Creation
- Automated Onboarding Workflows
- External Time Tracking Integration (Clockify)

### Technical Debt
- Empty Placeholder Tasks
- Missing Start Dates
- Incomplete Dependency Relationships
- Template Conversion Process

## 6. Critical Files
- Asana_Module_Development_Template_Spec_v2.0.md
- Template_Analysis_-_Actual_Structure.md
- Module_Development_Template_IMPORT.csv
- CSV_Import_Instructions.md
- CSV_Import_Analysis_and_Fixes.md

## Next Decision Point
Approval needed for:
- Solution 1 Implementation (49 min manual completion)
- Alternative Approaches
  * API Development
  * Project 2 Fixes

## Key Metrics
- Total Duration: 178 days
- Estimated Effort: 1,364 hours
- Dependencies: 45 relationships
- Sections: 11
- Tasks: 72+

---

**Last Updated**: 2025-10-14
**Context Version**: 2.0
**Status**: Ready for Review