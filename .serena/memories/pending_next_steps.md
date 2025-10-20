# Pending Next Steps - Asana Systematisation Project

**Updated**: 2025-10-14
**Status**: Waiting on inputs

## Immediate Next Actions

### 1. Integrate Andrew's Feedback
**Status**: ⏳ Blocked - Waiting for Andrew's review
**Document**: Module Development Template Specification v2.0
**Context**: 
- Andrew needs to review the specification
- 22 clarification questions pending resolution
- Placeholder emails need finalization
- Holiday scheduling conflicts to address

**When feedback received**:
- Review all comments and questions
- Update specification document
- Resolve clarification points
- Finalize placeholder details
- Update CSV import file if structural changes needed

### 2. Review Updated Project Template in Asana
**Status**: ⏳ Ready for review
**Project**: 1211626875246589 (Template TEST - Project Plan)
**Context**:
- All 52 dependencies now in place via API
- Need to verify template structure and flow
- Check for empty placeholder tasks (need deletion)
- Validate dependency chains work correctly
- Test workflow enforcement

**Review Checklist**:
- [ ] Open project in Asana Timeline view
- [ ] Verify all dependency chains visible
- [ ] Test that dependencies block task completion
- [ ] Check cascading build pattern (Week N → Week N+1)
- [ ] Verify batched review dependencies (Weeks 1-2, Weeks 3-8)
- [ ] Identify and delete empty placeholder tasks
- [ ] Add start dates (manual or API - decision needed)
- [ ] Convert to Asana Template when ready

## Follow-up Actions After Review

### If Template Structure Good
1. Convert Project 1211626875246589 to Asana Template
2. Test template duplication with dummy module
3. Verify dependencies copy correctly
4. Document template usage instructions

### If Changes Needed
1. Document required changes
2. Determine if CSV re-import needed or manual fixes
3. Re-apply dependencies if structure changes
4. Re-verify before template conversion

## Outstanding Issues from Analysis

From CSV_Import_Analysis_and_Fixes.md:

### Still Need to Address
1. **Start Dates**: All tasks missing start dates
   - Option A: Add manually in Timeline view (~15 min)
   - Option B: Add via API (can use same MCP approach)
   
2. **Empty Placeholder Tasks**: ~10 tasks with name=""
   - Need to identify and delete
   - Search for tasks with empty names
   
3. **Template Conversion**: Final step
   - Project Settings → Convert to Template
   - Set template name and description
   - Test duplication

### Decision Points
- **Start dates**: Manual vs API approach?
- **Template variants**: When to create variants?
- **Automation**: Which processes to automate next?

## Longer-Term Roadmap

### Phase 1: Template Stabilization (Next 1-2 weeks)
- Complete Andrew's feedback integration
- Finalize base template
- Test with real module
- Create usage documentation

### Phase 2: Template Variants (Next month)
- Identify variant requirements
- Create 12-week module variant
- Create accelerated variant
- Test all variants

### Phase 3: Automation (Next quarter)
- Automate date calculations
- Build template generation tool
- Integration planning (Clockify, CRM)

## References
- **API Implementation**: asana_api_dependency_implementation memory
- **Project Context**: asana_project_context memory
- **CSV Analysis**: CSV_Import_Analysis_and_Fixes.md
- **Specification**: Asana_Module_Development_Template_Spec_v2.md
