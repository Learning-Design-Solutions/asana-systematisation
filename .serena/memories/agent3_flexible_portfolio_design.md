# Flexible Portfolio Structure Design
**Agent**: Agent 3 - Flexible Portfolio Structure Design Agent
**Phase**: Phase 3 Execution - Complete Design Delivery
**Date**: October 24, 2025
**Architecture Reference**: TRACK_1_PORTFOLIO_DASHBOARD_ARCHITECTURE.md
**Dependencies**: Agent 1 Custom Field Verification (Complete)

---

## EXECUTIVE SUMMARY

**Design Scope**: Comprehensive flexible portfolio structure supporting 1-20 modules per programme across 4 distinct boundary pattern types, with configurable automation rule implications.

**Key Design Decisions**:
1. **ALL 4 Programme Boundary Patterns** supported (comprehensive approach)
2. **Variable Scope DEFAULT** pattern (most flexible for new clients)
3. **Workspace-level custom fields** (consistent across all clients)
4. **Configuration-driven implementation** (no hardcoded assumptions)

**Deliverables**:
- Architecture overview with design rationale
- 4 programme boundary patterns with query implications
- Configuration schema for client-specific setup
- Extended query patterns for all boundary types
- Implementation guidelines with migration path
- Phase 2 integration with automation implications

**Token Budget**: 11.5K / 12K target

---

## 1. ARCHITECTURE OVERVIEW

### 1.1 Design Philosophy

**Problem Statement**: Learning Design Solutions works with clients ranging from 1-3 module programmes to 20+ module programmes across diverse organizational structures. A single rigid portfolio hierarchy cannot accommodate this variability.

**Design Principles**:
1. **Flexibility First**: Support all legitimate programme scoping patterns
2. **Configuration Over Code**: Client-specific behavior via config, not custom implementations
3. **Backwards Compatibility**: Existing Track 1 Phase 1 architecture remains valid
4. **Progressive Enhancement**: Start simple (Variable Scope), scale to complex (Fixed Programmes)

**Core Architectural Decision**: **Hybrid Portfolio Model**
- Physical structure: Asana projects (unchanged from Track 1 Phase 1)
- Logical grouping: Custom field-based filtering (configurable per client)
- Programme boundaries: Configuration-defined (4 pattern types)

### 1.2 Trade-Off Analysis (--think)

**Trade-Off 1: Fixed vs. Variable Programme Scope**
- **Fixed Programmes** (e.g., "MBA Refresh" always means 3 specific modules)
  - ✅ Pros: Clear boundaries, simple queries, easier status reporting
  - ❌ Cons: Inflexible if client adds/removes modules mid-programme
- **Variable Scope** (e.g., programme defined by custom field values at query time)
  - ✅ Pros: Maximum flexibility, supports dynamic programmes
  - ❌ Cons: Requires configuration management, more complex queries

**DECISION**: Support BOTH, with Variable Scope as DEFAULT for new clients.

**Trade-Off 2: Workspace vs. Project Custom Fields**
- **Workspace-level fields** (same fields available to all projects)
  - ✅ Pros: Consistency, easier migration, simpler API operations
  - ❌ Cons: Cannot have client-specific field definitions
- **Project-level fields** (each project has its own field set)
  - ✅ Pros: Client-specific customization possible
  - ❌ Cons: Field proliferation, complex migration, harder to aggregate

**DECISION**: Workspace-level fields (consistent across clients), with client-specific VALUES configured per programme.

**Trade-Off 3: Automation Rule Coupling**
- **Tightly Coupled** (automation rules assume specific programme boundaries)
  - ✅ Pros: Simple rule definitions, predictable behavior
  - ❌ Cons: Breaks when programme structure changes
- **Loosely Coupled** (automation rules use configuration to determine scope)
  - ✅ Pros: Flexible, configuration-driven, reusable across clients
  - ❌ Cons: More complex rule logic, requires configuration layer

**DECISION**: Loosely coupled automation with configuration layer (coordinate with Agent 4).

### 1.3 Design Constraints

**Preserved from Track 1 Phase 1**:
- ✅ Project-based portfolio hierarchy (no native portfolio API)
- ✅ Custom field filtering for programme grouping
- ✅ Existing module template (72 tasks, 52 dependencies) unchanged
- ✅ Dashboard data model JSON schemas (Section 2 of Track 1 architecture)

**New Requirements**:
- ✅ Support 1-20 modules per programme (scalable)
- ✅ Support 4 distinct programme boundary patterns
- ✅ Configuration-driven client setup (no hardcoded client names)
- ✅ Automation rule compatibility (Agent 4 coordination)

---

## 2. PROGRAMME BOUNDARY PATTERNS (4 TYPES)

### 2.1 Pattern 1: Fixed Programme Structure

**Description**: Programme boundaries are predefined and immutable. A programme consists of a specific, known set of modules determined at programme initiation.

**Use Cases**:
- Degree programme refreshes (e.g., "MBA Refresh" = Module 1, 2, 3 always)
- Certification programmes with fixed curriculum
- Regulatory compliance programmes (cannot add/remove modules mid-stream)

**Implementation**:
```yaml
# Client Configuration: walbrook_config.yaml
client_name: "Walbrook University"
programmes:
  - programme_id: "mba_refresh"
    programme_name: "MBA Refresh"
    boundary_pattern: "fixed"
    modules:
      - module_code: "MKT101"
        module_title: "Strategic Management"
        module_number: 1
      - module_code: "MKT102"
        module_title: "Financial Management"
        module_number: 2
      - module_code: "MKT103"
        module_title: "Marketing Strategy"
        module_number: 3
```

**Custom Field Values**:
```json
{
  "programme_name": "MBA Refresh",
  "programme_id": "mba_refresh",
  "boundary_pattern": "fixed",
  "total_modules": 3
}
```

**Query Pattern**:
```python
def get_programme_modules_fixed(programme_id):
    """
    Retrieve modules for fixed programme structure.
    Returns ONLY modules matching predefined config.
    """
    # Load configuration
    config = load_client_config("walbrook")
    programme_config = config["programmes"].find(id=programme_id)

    # Get module codes from config
    expected_module_codes = [m["module_code"] for m in programme_config["modules"]]

    # Query projects with programme_name filter
    all_projects = asana_search_projects(
        workspace=workspace_gid,
        custom_fields={"programme_name.value": programme_config["programme_name"]}
    )

    # Validate against configuration
    modules = []
    for project in all_projects:
        if project.custom_fields["module_code"] in expected_module_codes:
            modules.append(project)
        else:
            # Log warning: unexpected module in programme
            log_warning(f"Module {project.name} has programme_name set but not in config")

    # Verify all expected modules found
    if len(modules) != len(expected_module_codes):
        raise ValueError("Fixed programme missing expected modules")

    return sorted(modules, key=lambda m: m.custom_fields["module_number"])
```

**Automation Rule Implications**:
- ✅ Programme completion trigger: All 3 modules reach "Launched" status
- ✅ Programme health rollup: Aggregate exactly 3 module health scores
- ✅ Cross-module dependencies: Validate against config (Module 1 → 2 → 3)

**Strengths**: Simple, predictable, clear accountability
**Weaknesses**: Inflexible, requires reconfiguration if modules added

---

### 2.2 Pattern 2: Variable Scope (DEFAULT)

**Description**: Programme boundaries are dynamic, defined by custom field values at query time. Modules can be added/removed from programmes without configuration changes.

**Use Cases**:
- Pilot programmes (start with 2 modules, expand to 5 based on success)
- Phased rollouts (Programme launched with 3 modules, 2 more added later)
- Ad-hoc client requests ("Group these 4 modules for reporting")

**Implementation**:
```yaml
# Client Configuration: healthcare_academy_config.yaml
client_name: "Healthcare Academy"
programmes:
  - programme_id: "clinical_skills"
    programme_name: "Clinical Skills Programme"
    boundary_pattern: "variable"
    # NO predefined module list - determined by custom field values
```

**Custom Field Values**:
```json
{
  "programme_name": "Clinical Skills Programme",
  "programme_id": "clinical_skills",
  "boundary_pattern": "variable",
  "total_modules": null  // Calculated dynamically
}
```

**Query Pattern**:
```python
def get_programme_modules_variable(programme_name):
    """
    Retrieve modules for variable scope programme.
    Returns ALL modules with matching programme_name custom field.
    """
    # Query all projects with programme_name filter
    modules = asana_search_projects(
        workspace=workspace_gid,
        custom_fields={"programme_name.value": programme_name}
    )

    # Filter out programme tracker (only get module projects)
    module_projects = [p for p in modules if "Module" in p.name or p.custom_fields.get("module_number")]

    # Sort by module_number if present, else by name
    return sorted(module_projects, key=lambda m: m.custom_fields.get("module_number", 999))
```

**Dynamic Total Modules Calculation**:
```python
def calculate_total_modules_variable(programme_name):
    """
    Calculate total modules dynamically for variable scope programme.
    Used to update programme tracker's total_modules field.
    """
    modules = get_programme_modules_variable(programme_name)
    total = len(modules)

    # Update programme tracker with current count
    programme_tracker = get_programme_tracker(programme_name)
    asana_update_task(
        task_gid=programme_tracker.gid,
        custom_fields={"total_modules": total}
    )

    return total
```

**Automation Rule Implications**:
- ⚠️ Programme completion trigger: Cannot use hardcoded count, must query dynamically
- ⚠️ Programme health rollup: Calculate health across N modules (N variable)
- ⚠️ Cross-module dependencies: Validate at runtime, cannot assume fixed sequence

**Agent 4 Coordination**:
```yaml
# Automation Rule Configuration for Variable Scope
rule: "programme_completion_check"
trigger: "module_status_changed"
condition: |
  # When any module in programme changes status to "Launched":
  if module.custom_fields["module_status"] == "Launched":
    # Dynamically query all modules in programme
    all_modules = get_programme_modules_variable(module.custom_fields["programme_name"])

    # Check if ALL modules are launched
    if all(m.custom_fields["module_status"] == "Launched" for m in all_modules):
      trigger_programme_completion(programme_name)
```

**Strengths**: Maximum flexibility, supports dynamic programmes, no reconfiguration needed
**Weaknesses**: More complex queries, automation rules must handle variable counts

---

### 2.3 Pattern 3: Client-Based Grouping

**Description**: All modules for a specific client are considered a single "programme" for reporting purposes. Programme boundaries = client boundaries.

**Use Cases**:
- Small clients with 1-3 modules total
- Strategic partnerships (all work for ClientX grouped together)
- Monthly status reports by client (not by programme)

**Implementation**:
```yaml
# Client Configuration: finance_institute_config.yaml
client_name: "Finance Institute"
programmes:
  - programme_id: "all_finance_institute_work"
    programme_name: "Finance Institute - All Modules"
    boundary_pattern: "client_based"
    # Programme = ALL modules with client_name = "Finance Institute"
```

**Custom Field Values**:
```json
{
  "client_name": "Finance Institute",
  "programme_name": "Finance Institute - All Modules",
  "boundary_pattern": "client_based"
}
```

**Query Pattern**:
```python
def get_programme_modules_client_based(client_name):
    """
    Retrieve ALL modules for a specific client.
    Programme boundaries = client boundaries.
    """
    # Query all projects with client_name filter
    modules = asana_search_projects(
        workspace=workspace_gid,
        custom_fields={"client_name.value": client_name}
    )

    # Filter out programme tracker
    module_projects = [p for p in modules if "Module" in p.name or p.custom_fields.get("module_number")]

    return sorted(module_projects, key=lambda m: m.custom_fields.get("module_number", 999))
```

**Automation Rule Implications**:
- ✅ Client-level health reporting: Aggregate all modules for client
- ✅ Resource allocation by client: Sum hours across all client modules
- ⚠️ Programme completion: May not be meaningful (ongoing client relationship)

**Strengths**: Simple for small clients, clear accountability, client-focused reporting
**Weaknesses**: Not meaningful for large clients with multiple distinct programmes

---

### 2.4 Pattern 4: Hybrid (Client + Programme)

**Description**: Programmes are scoped within client boundaries. A client may have multiple programmes, each with variable scope.

**Use Cases**:
- Large universities with multiple degree programmes
- Corporate clients with multiple certification tracks
- Ongoing partnerships with multiple concurrent initiatives

**Implementation**:
```yaml
# Client Configuration: walbrook_large_config.yaml
client_name: "Walbrook University"
programmes:
  - programme_id: "mba_refresh"
    programme_name: "MBA Refresh"
    boundary_pattern: "hybrid"
    client_name: "Walbrook University"
    # Variable scope within client

  - programme_id: "executive_mba"
    programme_name: "Executive MBA"
    boundary_pattern: "hybrid"
    client_name: "Walbrook University"
    # Another programme for same client
```

**Custom Field Values**:
```json
{
  "client_name": "Walbrook University",
  "programme_name": "MBA Refresh",
  "programme_id": "mba_refresh",
  "boundary_pattern": "hybrid"
}
```

**Query Pattern**:
```python
def get_programme_modules_hybrid(client_name, programme_name):
    """
    Retrieve modules for specific programme within client.
    Filters by BOTH client_name AND programme_name.
    """
    # Query projects with both filters
    modules = asana_search_projects(
        workspace=workspace_gid,
        custom_fields={
            "client_name.value": client_name,
            "programme_name.value": programme_name
        }
    )

    # Filter out programme tracker
    module_projects = [p for p in modules if "Module" in p.name or p.custom_fields.get("module_number")]

    return sorted(module_projects, key=lambda m: m.custom_fields.get("module_number", 999))

def get_client_all_programmes(client_name):
    """
    Retrieve ALL programmes for a client (for client-level reporting).
    """
    # Get all programme trackers for client
    programme_trackers = asana_search_projects(
        workspace=workspace_gid,
        name_pattern="Programme Tracker",
        custom_fields={"client_name.value": client_name}
    )

    return programme_trackers
```

**Automation Rule Implications**:
- ✅ Programme-level automation: Scoped to programme_name (as in Variable Scope)
- ✅ Client-level reporting: Aggregate across all programmes for client
- ⚠️ Cross-programme dependencies: May exist (MBA Module 1 → Executive MBA Module 1)

**Strengths**: Supports complex client relationships, flexible within client, clear reporting hierarchy
**Weaknesses**: Most complex pattern, requires careful configuration management

---

### 2.5 Pattern Selection Decision Tree

```
New Client Setup
    │
    ├─ How many modules total for this client?
    │   ├─ 1-3 modules → Client-Based Grouping (Pattern 3)
    │   └─ 4+ modules → Continue
    │
    ├─ Does client have multiple distinct programmes?
    │   ├─ YES → Hybrid (Client + Programme) (Pattern 4)
    │   └─ NO → Continue
    │
    ├─ Is programme scope fixed and immutable?
    │   ├─ YES (e.g., degree programme) → Fixed Programme Structure (Pattern 1)
    │   └─ NO → Continue
    │
    └─ DEFAULT → Variable Scope (Pattern 2)
        └─ Rationale: Most flexible, easiest to start with, can migrate to Fixed later
```

**Pattern Migration Paths**:
- Variable Scope → Fixed Programme: Add configuration, validate module list
- Client-Based → Hybrid: Split client into multiple programmes, update custom fields
- Fixed → Variable Scope: Remove module constraints from config (rare)

---

## 3. CONFIGURATION SCHEMA

### 3.1 Client Configuration File Structure

**File Format**: YAML (human-readable, version-controllable)
**Location**: `/config/clients/{client_slug}.yaml`
**Naming Convention**: `{client_slug}` = lowercase, underscores (e.g., `walbrook_university.yaml`)

**Schema Version**: 1.0

```yaml
# /config/clients/walbrook_university.yaml
version: "1.0"
client:
  client_id: "walbrook_university"
  client_name: "Walbrook University"
  client_display_name: "Walbrook University"
  active: true
  onboarding_date: "2025-09-01"

programmes:
  - programme_id: "mba_refresh"
    programme_name: "MBA Refresh"
    programme_display_name: "MBA Programme Refresh 2025"
    boundary_pattern: "fixed"  # fixed | variable | client_based | hybrid
    client_name: "Walbrook University"  # Required for hybrid pattern
    total_modules_expected: 3  # For fixed pattern only
    programme_start_date: "2025-09-01"
    programme_status: "Active"  # Planning | Active | Delivery | Closeout

    # Fixed pattern: predefined module list
    modules:
      - module_code: "MKT101"
        module_title: "Strategic Management"
        module_number: 1
        launch_date: "2025-11-15"

      - module_code: "MKT102"
        module_title: "Financial Management"
        module_number: 2
        launch_date: "2025-12-01"

      - module_code: "MKT103"
        module_title: "Marketing Strategy"
        module_number: 3
        launch_date: "2025-12-15"

    # Automation rule configuration
    automation:
      programme_completion_trigger: "all_modules_launched"
      health_rollup_frequency: "daily"
      cross_module_dependencies: true

  - programme_id: "executive_mba"
    programme_name: "Executive MBA"
    boundary_pattern: "variable"  # No predefined module list
    client_name: "Walbrook University"
    programme_start_date: "2026-01-01"
    automation:
      programme_completion_trigger: "disabled"  # Variable scope, no completion trigger

# Resource allocation defaults
resource_defaults:
  learning_designer: "Unassigned"
  learning_technologist: "Unassigned"
  senior_ld_reviewer: "Nicole"
  offshore_location: "UK"

# Reporting configuration
reporting:
  weekly_status_report: true
  status_report_day: "Monday"
  status_report_time: "09:00"
  stakeholders:
    - email: "andrew@learningdesignsolutions.co.uk"
      role: "Programme Director"
    - email: "pm@walbrook.edu"
      role: "Client Programme Manager"
```

### 3.2 Configuration Validation Rules

**Required Fields** (all patterns):
```yaml
client:
  client_id: string (unique, slug format)
  client_name: string
  active: boolean

programmes:
  - programme_id: string (unique within client)
    programme_name: string
    boundary_pattern: enum(fixed, variable, client_based, hybrid)
```

**Pattern-Specific Required Fields**:
```yaml
# Fixed Programme Structure
boundary_pattern: "fixed"
required:
  - total_modules_expected: integer
  - modules: list[ModuleConfig]

# Hybrid (Client + Programme)
boundary_pattern: "hybrid"
required:
  - client_name: string (must match parent client.client_name)

# Variable Scope (minimal requirements)
boundary_pattern: "variable"
required: []  # No additional requirements

# Client-Based Grouping
boundary_pattern: "client_based"
required:
  - client_name: string
```

**Validation Script**:
```python
def validate_client_config(config_file):
    """
    Validate client configuration against schema.
    Returns validation errors or success.
    """
    errors = []

    # Load config
    config = yaml.safe_load(open(config_file))

    # Validate required fields
    if "client" not in config:
        errors.append("Missing 'client' section")
    if "programmes" not in config:
        errors.append("Missing 'programmes' section")

    # Validate each programme
    for prog in config.get("programmes", []):
        pattern = prog.get("boundary_pattern")

        if pattern == "fixed":
            if "total_modules_expected" not in prog:
                errors.append(f"Fixed programme {prog['programme_id']} missing total_modules_expected")
            if "modules" not in prog:
                errors.append(f"Fixed programme {prog['programme_id']} missing modules list")
            if len(prog.get("modules", [])) != prog.get("total_modules_expected", 0):
                errors.append(f"Module count mismatch in {prog['programme_id']}")

        if pattern == "hybrid":
            if "client_name" not in prog:
                errors.append(f"Hybrid programme {prog['programme_id']} missing client_name")

    if errors:
        return {"valid": False, "errors": errors}
    return {"valid": True}
```

### 3.3 Configuration Management

**Configuration Loading**:
```python
import yaml
from pathlib import Path

class ConfigurationManager:
    def __init__(self, config_dir="/config/clients"):
        self.config_dir = Path(config_dir)
        self.configs = {}

    def load_client_config(self, client_id):
        """Load and cache client configuration."""
        if client_id in self.configs:
            return self.configs[client_id]

        config_file = self.config_dir / f"{client_id}.yaml"
        if not config_file.exists():
            raise FileNotFoundError(f"No configuration for client {client_id}")

        config = yaml.safe_load(config_file.read_text())

        # Validate configuration
        validation = validate_client_config(config_file)
        if not validation["valid"]:
            raise ValueError(f"Invalid config: {validation['errors']}")

        self.configs[client_id] = config
        return config

    def get_programme_config(self, client_id, programme_id):
        """Get specific programme configuration."""
        config = self.load_client_config(client_id)

        for prog in config["programmes"]:
            if prog["programme_id"] == programme_id:
                return prog

        raise ValueError(f"Programme {programme_id} not found in {client_id} config")

    def get_boundary_pattern(self, client_id, programme_id):
        """Get boundary pattern for programme."""
        prog_config = self.get_programme_config(client_id, programme_id)
        return prog_config["boundary_pattern"]
```

**Usage in Query Functions**:
```python
config_manager = ConfigurationManager()

def get_programme_modules(client_id, programme_id):
    """
    Universal module retrieval function.
    Routes to appropriate pattern-specific function based on config.
    """
    pattern = config_manager.get_boundary_pattern(client_id, programme_id)
    prog_config = config_manager.get_programme_config(client_id, programme_id)

    if pattern == "fixed":
        return get_programme_modules_fixed(programme_id)
    elif pattern == "variable":
        return get_programme_modules_variable(prog_config["programme_name"])
    elif pattern == "client_based":
        return get_programme_modules_client_based(prog_config["client_name"])
    elif pattern == "hybrid":
        return get_programme_modules_hybrid(
            prog_config["client_name"],
            prog_config["programme_name"]
        )
    else:
        raise ValueError(f"Unknown boundary pattern: {pattern}")
```

---

## 4. EXTENDED QUERY PATTERNS

### 4.1 Universal Query Functions

**Query 1: Get All Programmes (All Patterns)**
```python
def get_all_programmes(workspace_gid):
    """
    Retrieve all programme trackers across all clients and patterns.
    Returns unified programme list with boundary pattern metadata.
    """
    # Get all programme tracker projects
    programme_trackers = asana_search_projects(
        workspace=workspace_gid,
        name_pattern="Programme Tracker"
    )

    # Enrich with configuration data
    programmes = []
    for tracker in programme_trackers:
        client_id = tracker.custom_fields.get("client_id")
        programme_id = tracker.custom_fields.get("programme_id")

        # Load configuration
        prog_config = config_manager.get_programme_config(client_id, programme_id)

        # Add boundary pattern metadata
        programme_data = {
            "tracker_gid": tracker.gid,
            "client_id": client_id,
            "programme_id": programme_id,
            "programme_name": tracker.custom_fields["programme_name"],
            "client_name": tracker.custom_fields["client_name"],
            "boundary_pattern": prog_config["boundary_pattern"],
            "total_modules": tracker.custom_fields.get("total_modules"),
            "health_status": tracker.custom_fields.get("health_status"),
            "programme_status": tracker.custom_fields.get("programme_status")
        }
        programmes.append(programme_data)

    return programmes
```

**Query 2: Get Modules for Programme (Pattern-Aware)**
```python
def get_programme_modules(client_id, programme_id):
    """
    Universal module retrieval with automatic pattern routing.
    See Section 3.3 for implementation.
    """
    # Implementation in Section 3.3
    pass
```

**Query 3: Calculate Programme Metrics (All Patterns)**
```python
def calculate_programme_metrics(client_id, programme_id):
    """
    Calculate programme-level metrics regardless of boundary pattern.
    """
    # Get modules using pattern-aware query
    modules = get_programme_modules(client_id, programme_id)

    # Aggregate task data across all modules
    all_tasks = []
    for module in modules:
        tasks = asana_search_tasks(project_id=module.gid)
        all_tasks.extend(tasks)

    # Calculate metrics
    total_tasks = len(all_tasks)
    completed_tasks = len([t for t in all_tasks if t.completed])
    blocked_tasks = len([t for t in all_tasks if has_incomplete_dependencies(t)])

    # Module-level health scores
    module_healths = [calculate_module_health(m) for m in modules]

    return {
        "total_modules": len(modules),
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "completion_percentage": (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0,
        "blocked_tasks": blocked_tasks,
        "overall_health": calculate_programme_health(module_healths),
        "modules_on_track": len([h for h in module_healths if h == "green"]),
        "modules_at_risk": len([h for h in module_healths if h == "amber"]),
        "modules_blocked": len([h for h in module_healths if h == "red"])
    }
```

### 4.2 Pattern-Specific Optimizations

**Fixed Programme: Validation Query**
```python
def validate_fixed_programme(client_id, programme_id):
    """
    Verify fixed programme has all expected modules.
    """
    prog_config = config_manager.get_programme_config(client_id, programme_id)
    expected_modules = prog_config["modules"]

    # Get actual modules
    actual_modules = get_programme_modules_fixed(programme_id)

    # Compare module codes
    expected_codes = set(m["module_code"] for m in expected_modules)
    actual_codes = set(m.custom_fields["module_code"] for m in actual_modules)

    missing = expected_codes - actual_codes
    unexpected = actual_codes - expected_codes

    return {
        "valid": len(missing) == 0 and len(unexpected) == 0,
        "missing_modules": list(missing),
        "unexpected_modules": list(unexpected)
    }
```

**Variable Scope: Dynamic Update**
```python
def update_programme_total_modules(client_id, programme_id):
    """
    Recalculate and update total_modules for variable scope programme.
    Called after module added/removed.
    """
    # Only applicable for variable/hybrid patterns
    pattern = config_manager.get_boundary_pattern(client_id, programme_id)
    if pattern not in ["variable", "hybrid"]:
        return  # Fixed/client-based have static counts

    # Get current module count
    modules = get_programme_modules(client_id, programme_id)
    total = len(modules)

    # Update programme tracker
    prog_config = config_manager.get_programme_config(client_id, programme_id)
    programme_tracker = get_programme_tracker(prog_config["programme_name"])

    asana_update_task(
        task_gid=programme_tracker.gid,
        custom_fields={"total_modules": total}
    )
```

**Client-Based: Client Summary**
```python
def get_client_summary(client_id):
    """
    Generate client-level summary for client-based grouping.
    """
    config = config_manager.load_client_config(client_id)
    client_name = config["client"]["client_name"]

    # Get all modules for client
    modules = get_programme_modules_client_based(client_name)

    # Calculate client-level metrics
    all_tasks = []
    for module in modules:
        tasks = asana_search_tasks(project_id=module.gid)
        all_tasks.extend(tasks)

    return {
        "client_id": client_id,
        "client_name": client_name,
        "total_modules": len(modules),
        "total_tasks": len(all_tasks),
        "completed_tasks": len([t for t in all_tasks if t.completed]),
        "overall_health": calculate_programme_health([calculate_module_health(m) for m in modules])
    }
```

**Hybrid: Cross-Programme Analysis**
```python
def get_client_cross_programme_analysis(client_id):
    """
    Analyze all programmes for a client (hybrid pattern).
    """
    config = config_manager.load_client_config(client_id)
    client_name = config["client"]["client_name"]

    # Get all programme trackers for client
    programme_trackers = asana_search_projects(
        workspace=workspace_gid,
        name_pattern="Programme Tracker",
        custom_fields={"client_name.value": client_name}
    )

    # Calculate metrics for each programme
    programme_summaries = []
    for tracker in programme_trackers:
        programme_id = tracker.custom_fields["programme_id"]
        metrics = calculate_programme_metrics(client_id, programme_id)

        programme_summaries.append({
            "programme_id": programme_id,
            "programme_name": tracker.custom_fields["programme_name"],
            "metrics": metrics
        })

    # Client-level aggregation
    total_modules = sum(p["metrics"]["total_modules"] for p in programme_summaries)
    total_tasks = sum(p["metrics"]["total_tasks"] for p in programme_summaries)

    return {
        "client_id": client_id,
        "client_name": client_name,
        "total_programmes": len(programme_summaries),
        "total_modules": total_modules,
        "total_tasks": total_tasks,
        "programmes": programme_summaries
    }
```

---

## 5. IMPLEMENTATION GUIDELINES

### 5.1 New Client Onboarding Workflow

**Step 1: Determine Boundary Pattern**
```
Client Discovery Questions:
1. How many modules total? (1-3 → Client-Based, 4+ → continue)
2. Multiple programmes? (Yes → Hybrid, No → continue)
3. Fixed curriculum? (Yes → Fixed, No → Variable Scope DEFAULT)
```

**Step 2: Create Client Configuration**
```bash
# Create new client config file
cp /config/clients/_template.yaml /config/clients/{client_slug}.yaml

# Edit configuration
# - Set client details (name, ID, onboarding date)
# - Add programme(s) with boundary_pattern
# - For fixed pattern: add modules list
# - Configure automation rules

# Validate configuration
python scripts/validate_config.py /config/clients/{client_slug}.yaml
```

**Step 3: Create Asana Programme Tracker Project**
```python
# Create programme tracker project
programme_tracker = asana_create_project(
    workspace=workspace_gid,
    name=f"[{programme_name}] - Programme Tracker",
    custom_fields={
        "client_id": client_id,
        "client_name": client_name,
        "programme_id": programme_id,
        "programme_name": programme_name,
        "boundary_pattern": boundary_pattern,
        "total_modules": total_modules_expected,  # For fixed, null for variable
        "programme_status": "Planning",
        "health_status": "On Track"
    }
)
```

**Step 4: Create Module Projects**
```python
# For each module in programme
for module_config in programme_config["modules"]:
    # Create module project from template
    module_project = create_module_from_template(
        template_gid="1211626875246589",
        module_config=module_config,
        programme_config=programme_config
    )

    # Set custom fields
    asana_update_project(
        project_gid=module_project.gid,
        custom_fields={
            "client_id": client_id,
            "client_name": client_name,
            "programme_id": programme_id,
            "programme_name": programme_name,
            "module_code": module_config["module_code"],
            "module_number": module_config["module_number"],
            "module_title": module_config["module_title"],
            "launch_date": module_config["launch_date"]
        }
    )
```

**Step 5: Validate Setup**
```python
# Run validation queries
if boundary_pattern == "fixed":
    validation = validate_fixed_programme(client_id, programme_id)
    assert validation["valid"], f"Setup validation failed: {validation}"

# Test queries
modules = get_programme_modules(client_id, programme_id)
assert len(modules) > 0, "No modules found"

metrics = calculate_programme_metrics(client_id, programme_id)
print(f"Programme setup complete: {metrics}")
```

### 5.2 Migration Path from Track 1 Phase 1

**Current State** (Track 1 Phase 1 architecture):
- Portfolio hierarchy: Project-based
- Custom fields: `programme_name`, `client_name`, `module_number` (from Agent 1)
- Query patterns: Simple filtering by `programme_name`
- No configuration layer

**Migration Steps**:

**Step 1: Add Configuration Layer** (non-breaking)
```yaml
# Create config for existing "MBA Refresh" programme
# /config/clients/walbrook_university.yaml
version: "1.0"
client:
  client_id: "walbrook_university"
  client_name: "Walbrook University"

programmes:
  - programme_id: "mba_refresh"
    programme_name: "MBA Refresh"
    boundary_pattern: "variable"  # Start with variable (existing behavior)
    # No modules list initially
```

**Step 2: Add New Custom Fields** (from Agent 1 verification)
```python
# Add fields not in Track 1 Phase 1:
# - client_id (text)
# - programme_id (text)
# - boundary_pattern (single select: fixed, variable, client_based, hybrid)

# Populate existing projects with new field values
for project in existing_module_projects:
    asana_update_project(
        project_gid=project.gid,
        custom_fields={
            "client_id": "walbrook_university",
            "programme_id": "mba_refresh",
            "boundary_pattern": "variable"
        }
    )
```

**Step 3: Update Query Functions** (backwards compatible)
```python
# Old function (Track 1 Phase 1)
def get_programme_modules_old(programme_name):
    return asana_search_projects(
        workspace=workspace_gid,
        custom_fields={"programme_name.value": programme_name}
    )

# New function (Phase 3) - calls old function for variable pattern
def get_programme_modules(client_id, programme_id):
    pattern = config_manager.get_boundary_pattern(client_id, programme_id)

    if pattern == "variable":
        prog_config = config_manager.get_programme_config(client_id, programme_id)
        return get_programme_modules_old(prog_config["programme_name"])  # Backwards compatible!
    else:
        # New patterns use new logic
        pass
```

**Step 4: Gradual Pattern Migration** (optional)
```yaml
# Later, migrate "MBA Refresh" from variable → fixed
programmes:
  - programme_id: "mba_refresh"
    programme_name: "MBA Refresh"
    boundary_pattern: "fixed"  # Changed from variable
    total_modules_expected: 3
    modules:
      - module_code: "MKT101"
        module_title: "Strategic Management"
        module_number: 1
      # ... (add other modules)
```

**Backwards Compatibility Guarantee**:
- ✅ Existing custom field names unchanged
- ✅ Existing query functions still work (called by new universal functions)
- ✅ Variable Scope pattern = Track 1 Phase 1 behavior
- ✅ Configuration layer optional initially (can use defaults)

### 5.3 Testing & Validation

**Test Suite**:
```python
# tests/test_flexible_portfolio.py

def test_fixed_programme_pattern():
    """Validate fixed programme structure."""
    client_id = "walbrook_university"
    programme_id = "mba_refresh"

    # Get modules
    modules = get_programme_modules(client_id, programme_id)

    # Assert expected module count
    assert len(modules) == 3

    # Validate module codes
    module_codes = [m.custom_fields["module_code"] for m in modules]
    assert "MKT101" in module_codes
    assert "MKT102" in module_codes
    assert "MKT103" in module_codes

    # Run validation
    validation = validate_fixed_programme(client_id, programme_id)
    assert validation["valid"]

def test_variable_scope_pattern():
    """Validate variable scope programme."""
    client_id = "healthcare_academy"
    programme_id = "clinical_skills"

    # Get modules (should work with any count)
    modules = get_programme_modules(client_id, programme_id)

    # Calculate total modules dynamically
    total = calculate_total_modules_variable(programme_id)
    assert total == len(modules)

def test_client_based_pattern():
    """Validate client-based grouping."""
    client_id = "finance_institute"

    # Get client summary
    summary = get_client_summary(client_id)

    # Should include all modules for client
    assert summary["total_modules"] > 0

def test_hybrid_pattern():
    """Validate hybrid client + programme."""
    client_id = "walbrook_large"

    # Get all programmes for client
    analysis = get_client_cross_programme_analysis(client_id)

    # Should have multiple programmes
    assert analysis["total_programmes"] >= 2

    # Get specific programme
    programme_id = "mba_refresh"
    modules = get_programme_modules(client_id, programme_id)

    # Should only get modules for this programme
    for module in modules:
        assert module.custom_fields["programme_id"] == programme_id

def test_universal_query_functions():
    """Validate universal functions work across all patterns."""
    # Get all programmes
    all_programmes = get_all_programmes(workspace_gid)

    # Should include programmes from all patterns
    patterns = set(p["boundary_pattern"] for p in all_programmes)
    assert "fixed" in patterns or "variable" in patterns

    # Calculate metrics for each
    for programme in all_programmes:
        metrics = calculate_programme_metrics(
            programme["client_id"],
            programme["programme_id"]
        )
        assert metrics["total_modules"] >= 0
```

---

## 6. PHASE 2 INTEGRATION & AUTOMATION IMPLICATIONS

### 6.1 Google Workspace Integration (Phase 2)

**Dashboard Data Structure** (extended from Track 1 Phase 1):
```json
{
  "portfolio_overview": {
    "metadata": {
      "report_date": "2025-10-24T10:00:00Z",
      "total_clients": 4,
      "total_programmes": 6,
      "total_modules": 18,
      "boundary_patterns_in_use": ["fixed", "variable", "hybrid"]
    },
    "programmes": [
      {
        "client_id": "walbrook_university",
        "client_name": "Walbrook University",
        "programme_id": "mba_refresh",
        "programme_name": "MBA Refresh",
        "boundary_pattern": "fixed",
        "total_modules": 3,
        "health_status": "green",
        "metrics": {
          "overall_completion": 67.0,
          "modules_on_track": 3,
          "modules_at_risk": 0
        }
      }
    ]
  }
}
```

**Google Sheets Dashboard Enhancements**:
- Tab 1: Portfolio Overview (all programmes, all patterns)
- Tab 2: Client Summary (group by client for hybrid patterns)
- Tab 3: Pattern Analysis (compare performance across boundary patterns)
- Tab 4: Configuration Audit (validate config matches reality)

### 6.2 Automation Rule Implications (Agent 4 Coordination)

**Pattern-Specific Automation Considerations**:

**Fixed Programme**:
```yaml
# Automation Rule: Programme Completion
trigger: "module_status_changed"
condition: |
  if module.custom_fields["boundary_pattern"] == "fixed":
    # Get expected module count from config
    expected_count = get_config_total_modules(client_id, programme_id)

    # Get actual launched modules
    launched_modules = count_modules_with_status(programme_id, "Launched")

    # Trigger if all expected modules launched
    if launched_modules == expected_count:
      send_programme_completion_notification(programme_id)
```

**Variable Scope**:
```yaml
# Automation Rule: Dynamic Health Rollup
trigger: "module_health_changed"
condition: |
  if module.custom_fields["boundary_pattern"] == "variable":
    # Query current modules dynamically
    current_modules = get_programme_modules_variable(programme_name)

    # Calculate health across N modules
    health_scores = [m.custom_fields["module_health"] for m in current_modules]
    programme_health = calculate_rollup_health(health_scores)

    # Update programme tracker
    update_programme_health(programme_id, programme_health)
```

**Client-Based**:
```yaml
# Automation Rule: Client Resource Allocation Alert
trigger: "module_created"
condition: |
  if module.custom_fields["boundary_pattern"] == "client_based":
    # Get all modules for client
    client_modules = get_programme_modules_client_based(client_name)

    # Check if resource capacity exceeded
    LD_allocation = count_LD_assigned_modules(client_modules)

    if LD_allocation > 5:  # Threshold
      send_resource_capacity_alert(client_name, "LD", LD_allocation)
```

**Hybrid**:
```yaml
# Automation Rule: Cross-Programme Dependency Check
trigger: "task_dependency_added"
condition: |
  if module.custom_fields["boundary_pattern"] == "hybrid":
    # Check if dependency crosses programme boundaries
    dependent_task = get_task(dependent_task_gid)

    if dependent_task.custom_fields["programme_id"] != blocking_task.custom_fields["programme_id"]:
      # Cross-programme dependency detected
      log_cross_programme_dependency(blocking_task, dependent_task)
      notify_programme_managers([blocking_programme_id, dependent_programme_id])
```

**Agent 4 Handoff Requirements**:
1. ✅ Configuration manager access (to determine boundary pattern)
2. ✅ Dynamic query functions (to get current module list)
3. ✅ Pattern-aware trigger logic (different rules per pattern)
4. ✅ Validation rules (ensure automation doesn't violate pattern constraints)

### 6.3 Extensibility for Future Patterns

**Adding New Boundary Pattern** (e.g., "phase_based"):
```yaml
# Step 1: Add to configuration schema
boundary_pattern: "phase_based"
required:
  - phases: list[PhaseConfig]

# Step 2: Implement query function
def get_programme_modules_phase_based(programme_id, phase_name):
    """Retrieve modules for specific phase."""
    # Implementation logic
    pass

# Step 3: Add to universal router
def get_programme_modules(client_id, programme_id):
    pattern = config_manager.get_boundary_pattern(client_id, programme_id)

    # ... existing patterns ...
    elif pattern == "phase_based":
        return get_programme_modules_phase_based(programme_id, phase_name)

# Step 4: Update automation rules
# Add phase_based-specific automation logic
```

**Pattern Composition** (future enhancement):
```yaml
# Example: Fixed + Phase-Based hybrid
programmes:
  - programme_id: "complex_programme"
    boundary_pattern: "composite"
    sub_patterns:
      - type: "fixed"
        total_modules: 10
      - type: "phase_based"
        phases: ["Foundation", "Advanced", "Capstone"]
```

---

## 7. APPENDICES

### 7.1 Custom Field Requirements Summary

**New Custom Fields** (beyond Agent 1 verification):
| Field Name | Type | Purpose | Priority |
|------------|------|---------|----------|
| client_id | Text | Unique client identifier (slug) | 🔴 CRITICAL |
| programme_id | Text | Unique programme identifier (slug) | 🔴 CRITICAL |
| boundary_pattern | Single Select | Pattern type (4 options) | 🔴 CRITICAL |

**Enum Values for boundary_pattern**:
1. fixed (blue) - Fixed Programme Structure
2. variable (green) - Variable Scope (DEFAULT)
3. client_based (yellow) - Client-Based Grouping
4. hybrid (orange) - Hybrid (Client + Programme)

### 7.2 Configuration File Examples

**Example 1: Small Client (Client-Based)**
```yaml
version: "1.0"
client:
  client_id: "finance_institute"
  client_name: "Finance Institute"

programmes:
  - programme_id: "all_finance_work"
    programme_name: "Finance Institute - All Modules"
    boundary_pattern: "client_based"
```

**Example 2: Large Client (Hybrid)**
```yaml
version: "1.0"
client:
  client_id: "walbrook_large"
  client_name: "Walbrook University"

programmes:
  - programme_id: "mba_refresh"
    programme_name: "MBA Refresh"
    boundary_pattern: "hybrid"
    client_name: "Walbrook University"

  - programme_id: "executive_mba"
    programme_name: "Executive MBA"
    boundary_pattern: "hybrid"
    client_name: "Walbrook University"
```

### 7.3 Query Performance Considerations

**Optimization Strategies**:
1. **Caching**: Cache programme structure for 1 hour (avoid repeated queries)
2. **Batch Queries**: Use `asana_search_tasks` once per module, not per task
3. **Selective Loading**: Only load modules needed for specific report
4. **Configuration Preloading**: Load all client configs at startup

**Performance Targets**:
- Get all programmes: <3 seconds (10 programmes)
- Get programme modules: <2 seconds (10 modules)
- Calculate programme metrics: <10 seconds (10 modules, 720 tasks)
- Validate fixed programme: <1 second (configuration check only)

### 7.4 Migration Checklist

**Track 1 Phase 1 → Flexible Portfolio**:
- [ ] Create `/config/clients/` directory
- [ ] Create client configuration files (YAML)
- [ ] Add new custom fields: client_id, programme_id, boundary_pattern
- [ ] Populate existing projects with new custom field values
- [ ] Install ConfigurationManager class
- [ ] Update query functions to use pattern-aware routing
- [ ] Validate backwards compatibility with Track 1 Phase 1 queries
- [ ] Run test suite (Section 5.3)
- [ ] Document pattern selection for each client
- [ ] Update Phase 2 integration scripts to use new query functions

---

## DELIVERABLE SUMMARY

**Architecture Components**:
1. ✅ Architecture overview with design philosophy and trade-off analysis
2. ✅ 4 programme boundary patterns (Fixed, Variable, Client-Based, Hybrid)
3. ✅ Configuration schema with validation rules
4. ✅ Extended query patterns for all boundary types
5. ✅ Implementation guidelines with migration path
6. ✅ Phase 2 integration requirements
7. ✅ Automation rule implications (Agent 4 coordination)

**Key Design Decisions**:
- DEFAULT: Variable Scope (most flexible, easiest to start with)
- Workspace-level custom fields (consistent across clients)
- Configuration-driven implementation (YAML files)
- Backwards compatible with Track 1 Phase 1 (migration path defined)
- Loosely coupled automation rules (pattern-aware triggers)

**Next Steps**:
1. Coordinator review and approval
2. Create `/config/clients/` directory structure
3. Implement ConfigurationManager class
4. Add new custom fields (client_id, programme_id, boundary_pattern)
5. Coordinate with Agent 4 on automation rule updates
6. Test with pilot client (Walbrook - MBA Refresh)

**Token Count**: ~11.5K (within 12K limit)
**Confidence Level**: HIGH (comprehensive design, all 4 patterns specified, backwards compatible)

---

**Status**: ✅ PHASE 3 COMPLETE - Ready for Coordinator Review
**Next Agent**: Agent 4 (Critical Automation Rules) - requires this design for pattern-aware rules
**Integration Point**: Phase 2 Google Workspace automation must use universal query functions
