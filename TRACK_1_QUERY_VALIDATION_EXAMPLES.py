"""
Track 1: Portfolio Dashboard Query Validation Examples
========================================================

Purpose: Sample queries demonstrating Phase 1 portfolio dashboard data retrieval
Status: Ready for testing with sample data
Requirements: Asana MCP server configured

Note: Replace placeholder GIDs with actual values from your workspace
"""

# ============================================================================
# CONFIGURATION
# ============================================================================

WORKSPACE_GID = "your_workspace_gid"  # Replace with actual workspace GID

# Programme names (used for filtering)
PROGRAMME_MBA_REFRESH = "MBA Refresh"
PROGRAMME_CLINICAL_SKILLS = "Clinical Skills"

# Expected custom field names
CUSTOM_FIELD_PROGRAMME_NAME = "programme_name"
CUSTOM_FIELD_MODULE_NUMBER = "module_number"
CUSTOM_FIELD_MODULE_TITLE = "module_title"
CUSTOM_FIELD_HEALTH_STATUS = "health_status"

# ============================================================================
# QUERY 1: Get All Programme Trackers
# ============================================================================

def get_all_programmes(asana_mcp):
    """
    Retrieve all programme tracker projects in workspace.

    Returns:
        list: Programme tracker project objects with metadata
    """
    # Search for all projects with "Programme Tracker" in name
    programmes = asana_mcp.asana_search_projects(
        workspace_gid=WORKSPACE_GID,
        # Note: name_pattern may not be available, alternative approach:
        # Search all projects, then filter by naming convention
    )

    # Filter to only programme trackers
    programme_trackers = [
        p for p in programmes
        if "Programme Tracker" in p.get("name", "")
    ]

    # Extract metadata
    programme_data = []
    for prog in programme_trackers:
        programme_data.append({
            "programme_id": prog["gid"],
            "programme_name": get_custom_field_value(
                prog, CUSTOM_FIELD_PROGRAMME_NAME
            ),
            "client_name": get_custom_field_value(
                prog, "client_name"
            ),
            "health_status": get_custom_field_value(
                prog, CUSTOM_FIELD_HEALTH_STATUS
            ),
            "total_modules": get_custom_field_value(
                prog, "total_modules"
            )
        })

    return programme_data


# ============================================================================
# QUERY 2: Get All Modules for a Programme
# ============================================================================

def get_programme_modules(asana_mcp, programme_name):
    """
    Retrieve all module projects linked to a specific programme.

    Args:
        asana_mcp: Asana MCP server instance
        programme_name: Programme identifier (e.g., "MBA Refresh")

    Returns:
        list: Module project objects sorted by module_number
    """
    # Approach: Search all projects, filter by custom field
    # Note: Direct custom field filtering may not be available in MCP
    # Alternative: Get all projects, filter client-side

    all_projects = asana_mcp.asana_search_projects(
        workspace_gid=WORKSPACE_GID
    )

    # Filter to modules for this programme
    module_projects = []
    for project in all_projects:
        # Skip programme trackers
        if "Programme Tracker" in project.get("name", ""):
            continue

        # Check if programme_name custom field matches
        prog_name_value = get_custom_field_value(
            project, CUSTOM_FIELD_PROGRAMME_NAME
        )

        if prog_name_value == programme_name:
            module_projects.append({
                "module_id": project["gid"],
                "module_number": get_custom_field_value(
                    project, CUSTOM_FIELD_MODULE_NUMBER
                ),
                "module_title": get_custom_field_value(
                    project, CUSTOM_FIELD_MODULE_TITLE
                ),
                "project_name": project["name"],
                "launch_date": get_custom_field_value(
                    project, "module_launch_date"
                )
            })

    # Sort by module number
    module_projects.sort(key=lambda m: m.get("module_number", 999))

    return module_projects


# ============================================================================
# QUERY 3: Calculate Programme Completion Percentage
# ============================================================================

def calculate_programme_completion(asana_mcp, programme_name):
    """
    Calculate overall completion percentage for all modules in programme.

    Args:
        asana_mcp: Asana MCP server instance
        programme_name: Programme identifier

    Returns:
        dict: Completion metrics
    """
    # Step 1: Get all modules
    modules = get_programme_modules(asana_mcp, programme_name)

    # Step 2: Get tasks for each module
    total_tasks = 0
    completed_tasks = 0

    module_completions = []

    for module in modules:
        # Query tasks in this module project
        tasks = asana_mcp.asana_search_tasks(
            project_id=module["module_id"]
        )

        # Count total and completed
        module_total = len(tasks)
        module_completed = len([t for t in tasks if t.get("completed", False)])

        total_tasks += module_total
        completed_tasks += module_completed

        module_completions.append({
            "module_number": module["module_number"],
            "module_title": module["module_title"],
            "tasks_total": module_total,
            "tasks_completed": module_completed,
            "completion_pct": (module_completed / module_total * 100) if module_total > 0 else 0
        })

    # Overall programme completion
    overall_completion = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0

    return {
        "programme_name": programme_name,
        "total_modules": len(modules),
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "overall_completion_pct": overall_completion,
        "module_completions": module_completions
    }


# ============================================================================
# QUERY 4: Identify Blocked Tasks Across Programme
# ============================================================================

def identify_blocked_tasks(asana_mcp, programme_name):
    """
    Find all tasks blocked by incomplete dependencies across all modules.

    Args:
        asana_mcp: Asana MCP server instance
        programme_name: Programme identifier

    Returns:
        list: Blocked task details
    """
    modules = get_programme_modules(asana_mcp, programme_name)
    blocked_tasks = []

    for module in modules:
        # Get all tasks in module
        tasks = asana_mcp.asana_search_tasks(
            project_id=module["module_id"]
        )

        # Check each incomplete task for dependencies
        for task in tasks:
            if task.get("completed", False):
                continue  # Skip completed tasks

            # Get full task details (including dependencies)
            task_details = asana_mcp.asana_get_task(
                task_id=task["gid"]
            )

            # Check dependencies
            dependencies = task_details.get("dependencies", [])
            if dependencies:
                # Check if any dependencies are incomplete
                incomplete_deps = []

                for dep_gid in dependencies:
                    dep_task = asana_mcp.asana_get_task(task_id=dep_gid)
                    if not dep_task.get("completed", False):
                        incomplete_deps.append({
                            "task_name": dep_task.get("name"),
                            "task_gid": dep_gid
                        })

                # If task has incomplete dependencies, it's blocked
                if incomplete_deps:
                    blocked_tasks.append({
                        "module_number": module["module_number"],
                        "module_title": module["module_title"],
                        "blocked_task_name": task.get("name"),
                        "blocked_task_gid": task["gid"],
                        "due_date": task.get("due_on"),
                        "incomplete_dependencies": incomplete_deps,
                        "blocker_count": len(incomplete_deps)
                    })

    return blocked_tasks


# ============================================================================
# QUERY 5: Cross-Module Dependency Analysis
# ============================================================================

def analyze_cross_module_dependencies(asana_mcp, programme_name):
    """
    Identify dependencies between tasks in different modules (critical path).

    Args:
        asana_mcp: Asana MCP server instance
        programme_name: Programme identifier

    Returns:
        list: Cross-module dependency relationships
    """
    modules = get_programme_modules(asana_mcp, programme_name)
    cross_module_deps = []

    # Build module ID → module mapping
    module_lookup = {m["module_id"]: m for m in modules}

    for module in modules:
        tasks = asana_mcp.asana_search_tasks(project_id=module["module_id"])

        for task in tasks:
            task_details = asana_mcp.asana_get_task(task_id=task["gid"])

            # Check dependents (tasks that depend on THIS task)
            dependents = task_details.get("dependents", [])

            for dependent_gid in dependents:
                dependent = asana_mcp.asana_get_task(task_id=dependent_gid)

                # Check if dependent is in a DIFFERENT project (cross-module)
                dependent_project_gid = dependent.get("projects", [{}])[0].get("gid")

                if dependent_project_gid != module["module_id"]:
                    # Cross-module dependency detected!
                    dependent_module = module_lookup.get(dependent_project_gid, {})

                    cross_module_deps.append({
                        "blocking_module": module["module_number"],
                        "blocking_task": task.get("name"),
                        "blocking_task_gid": task["gid"],
                        "blocked_module": dependent_module.get("module_number"),
                        "blocked_task": dependent.get("name"),
                        "blocked_task_gid": dependent_gid,
                        "impact": f"Module {dependent_module.get('module_number')} blocked by Module {module['module_number']}"
                    })

    return cross_module_deps


# ============================================================================
# QUERY 6: Module Health Status Calculation
# ============================================================================

def calculate_module_health(asana_mcp, module_id, launch_date):
    """
    Calculate health status for a module based on completion and blockers.

    Args:
        asana_mcp: Asana MCP server instance
        module_id: Module project GID
        launch_date: Target launch date (ISO format)

    Returns:
        dict: Health status and metrics
    """
    import datetime

    # Get all tasks
    tasks = asana_mcp.asana_search_tasks(project_id=module_id)

    # Calculate metrics
    total_tasks = len(tasks)
    completed_tasks = len([t for t in tasks if t.get("completed", False)])
    completion_pct = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0

    # Count blocked tasks
    blocked_count = 0
    for task in tasks:
        if not task.get("completed", False):
            task_details = asana_mcp.asana_get_task(task_id=task["gid"])
            dependencies = task_details.get("dependencies", [])
            if dependencies:
                # Check if any deps incomplete
                for dep_gid in dependencies:
                    dep = asana_mcp.asana_get_task(task_id=dep_gid)
                    if not dep.get("completed", False):
                        blocked_count += 1
                        break

    blocked_pct = (blocked_count / total_tasks * 100) if total_tasks > 0 else 0

    # Calculate expected completion based on timeline
    if launch_date:
        launch = datetime.datetime.fromisoformat(launch_date.replace('Z', '+00:00'))
        today = datetime.datetime.now(datetime.timezone.utc)
        days_to_launch = (launch - today).days

        # Assuming 112 days total timeline (178 - 66 buffer)
        total_timeline = 112
        days_elapsed = total_timeline - days_to_launch
        expected_completion_pct = (days_elapsed / total_timeline * 100) if total_timeline > 0 else 0
    else:
        expected_completion_pct = None
        days_to_launch = None

    # Determine health status
    health_status = "green"
    health_rationale = []

    if blocked_pct > 25:
        health_status = "red"
        health_rationale.append(f"High blocker rate ({blocked_pct:.1f}%)")
    elif blocked_pct > 10:
        health_status = "amber"
        health_rationale.append(f"Moderate blockers ({blocked_pct:.1f}%)")

    if completion_pct < 60:
        health_status = "red"
        health_rationale.append(f"Low completion ({completion_pct:.1f}%)")
    elif completion_pct < 80:
        if health_status != "red":
            health_status = "amber"
        health_rationale.append(f"Below target completion ({completion_pct:.1f}%)")

    if expected_completion_pct and completion_pct < expected_completion_pct:
        if health_status == "green":
            health_status = "amber"
        health_rationale.append(f"Behind schedule (expected {expected_completion_pct:.1f}%)")

    if not health_rationale:
        health_rationale = ["On track"]

    return {
        "health_status": health_status,
        "health_rationale": " | ".join(health_rationale),
        "completion_pct": completion_pct,
        "expected_completion_pct": expected_completion_pct,
        "blocked_count": blocked_count,
        "blocked_pct": blocked_pct,
        "days_to_launch": days_to_launch,
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks
    }


# ============================================================================
# QUERY 7: Resource Utilization Analysis
# ============================================================================

def analyze_resource_utilization(asana_mcp, programme_name):
    """
    Calculate resource allocation across all modules in programme.

    Args:
        asana_mcp: Asana MCP server instance
        programme_name: Programme identifier

    Returns:
        dict: Resource utilization metrics
    """
    modules = get_programme_modules(asana_mcp, programme_name)

    # Resource counters
    resources = {
        "LD": {"modules": 0, "tasks": 0},
        "LT": {"modules": 0, "tasks": 0},
        "SLD": {"modules": 0, "tasks": 0},
        "SME": {"modules": 0, "tasks": 0},
        "PM": {"modules": 0, "tasks": 0}
    }

    for module in modules:
        tasks = asana_mcp.asana_search_tasks(project_id=module["module_id"])

        # Track which resources are assigned to this module
        module_resources = set()

        for task in tasks:
            assignee = task.get("assignee")
            if assignee:
                assignee_name = assignee.get("name", "")

                # Simple heuristic: check if resource type is in assignee name
                # In production, you'd use custom fields or tags
                for resource_type in resources.keys():
                    if resource_type.lower() in assignee_name.lower():
                        resources[resource_type]["tasks"] += 1
                        module_resources.add(resource_type)

        # Count module-level assignments
        for resource_type in module_resources:
            resources[resource_type]["modules"] += 1

    # Identify bottleneck (most heavily utilized resource)
    bottleneck = max(
        resources.items(),
        key=lambda x: x[1]["modules"]
    )[0] if resources else None

    return {
        "programme_name": programme_name,
        "total_modules": len(modules),
        "resource_allocation": resources,
        "bottleneck_resource": bottleneck
    }


# ============================================================================
# QUERY 8: Generate Portfolio Overview
# ============================================================================

def generate_portfolio_overview(asana_mcp):
    """
    Generate complete portfolio overview with all programmes and metrics.

    Args:
        asana_mcp: Asana MCP server instance

    Returns:
        dict: Complete portfolio data structure
    """
    import datetime

    # Get all programmes
    programmes = get_all_programmes(asana_mcp)

    portfolio_data = {
        "metadata": {
            "report_date": datetime.datetime.now().isoformat(),
            "workspace_id": WORKSPACE_GID,
            "total_programmes": len(programmes)
        },
        "programmes": []
    }

    total_modules = 0
    programmes_green = 0
    programmes_amber = 0
    programmes_red = 0

    for prog in programmes:
        prog_name = prog["programme_name"]

        # Get modules
        modules = get_programme_modules(asana_mcp, prog_name)
        total_modules += len(modules)

        # Calculate completion
        completion = calculate_programme_completion(asana_mcp, prog_name)

        # Get blocked tasks
        blocked = identify_blocked_tasks(asana_mcp, prog_name)

        # Determine programme health
        prog_health = prog.get("health_status", "green")
        if prog_health == "red":
            programmes_red += 1
        elif prog_health == "amber":
            programmes_amber += 1
        else:
            programmes_green += 1

        portfolio_data["programmes"].append({
            "programme_id": prog["programme_id"],
            "programme_name": prog_name,
            "client_name": prog["client_name"],
            "health_status": prog_health,
            "total_modules": len(modules),
            "overall_completion": completion["overall_completion_pct"],
            "total_blockers": len(blocked)
        })

    # Cross-programme summary
    portfolio_data["summary"] = {
        "total_modules": total_modules,
        "programmes_green": programmes_green,
        "programmes_amber": programmes_amber,
        "programmes_red": programmes_red
    }

    return portfolio_data


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_custom_field_value(project_or_task, field_name):
    """
    Extract custom field value from project or task object.

    Args:
        project_or_task: Asana object with custom_fields
        field_name: Name of custom field

    Returns:
        Value of custom field or None
    """
    custom_fields = project_or_task.get("custom_fields", [])

    for field in custom_fields:
        if field.get("name") == field_name:
            # Handle different field types
            if field.get("type") == "text":
                return field.get("text_value")
            elif field.get("type") == "number":
                return field.get("number_value")
            elif field.get("type") == "enum":
                enum_value = field.get("enum_value")
                if enum_value:
                    return enum_value.get("name")
            elif field.get("type") == "date":
                return field.get("date_value")

    return None


# ============================================================================
# VALIDATION TEST SUITE
# ============================================================================

def run_validation_tests(asana_mcp):
    """
    Execute all query patterns and validate results.

    Args:
        asana_mcp: Asana MCP server instance

    Returns:
        dict: Test results
    """
    print("=" * 80)
    print("TRACK 1 QUERY VALIDATION TEST SUITE")
    print("=" * 80)

    results = {
        "tests_run": 0,
        "tests_passed": 0,
        "tests_failed": 0,
        "details": []
    }

    # Test 1: Get all programmes
    try:
        print("\nTest 1: Get All Programmes")
        programmes = get_all_programmes(asana_mcp)
        print(f"  Found {len(programmes)} programmes")
        results["tests_run"] += 1
        results["tests_passed"] += 1
        results["details"].append({
            "test": "get_all_programmes",
            "status": "PASS",
            "result": f"Found {len(programmes)} programmes"
        })
    except Exception as e:
        print(f"  FAILED: {str(e)}")
        results["tests_run"] += 1
        results["tests_failed"] += 1
        results["details"].append({
            "test": "get_all_programmes",
            "status": "FAIL",
            "error": str(e)
        })

    # Test 2: Get modules for first programme
    if programmes:
        try:
            print(f"\nTest 2: Get Modules for '{programmes[0]['programme_name']}'")
            modules = get_programme_modules(asana_mcp, programmes[0]['programme_name'])
            print(f"  Found {len(modules)} modules")
            results["tests_run"] += 1
            results["tests_passed"] += 1
            results["details"].append({
                "test": "get_programme_modules",
                "status": "PASS",
                "result": f"Found {len(modules)} modules"
            })
        except Exception as e:
            print(f"  FAILED: {str(e)}")
            results["tests_run"] += 1
            results["tests_failed"] += 1
            results["details"].append({
                "test": "get_programme_modules",
                "status": "FAIL",
                "error": str(e)
            })

    # Test 3: Calculate programme completion
    if programmes:
        try:
            print(f"\nTest 3: Calculate Completion for '{programmes[0]['programme_name']}'")
            completion = calculate_programme_completion(asana_mcp, programmes[0]['programme_name'])
            print(f"  Overall completion: {completion['overall_completion_pct']:.1f}%")
            print(f"  Total tasks: {completion['total_tasks']}")
            results["tests_run"] += 1
            results["tests_passed"] += 1
            results["details"].append({
                "test": "calculate_programme_completion",
                "status": "PASS",
                "result": f"{completion['overall_completion_pct']:.1f}% complete"
            })
        except Exception as e:
            print(f"  FAILED: {str(e)}")
            results["tests_run"] += 1
            results["tests_failed"] += 1
            results["details"].append({
                "test": "calculate_programme_completion",
                "status": "FAIL",
                "error": str(e)
            })

    # Test 4: Identify blocked tasks
    if programmes:
        try:
            print(f"\nTest 4: Identify Blocked Tasks in '{programmes[0]['programme_name']}'")
            blocked = identify_blocked_tasks(asana_mcp, programmes[0]['programme_name'])
            print(f"  Found {len(blocked)} blocked tasks")
            results["tests_run"] += 1
            results["tests_passed"] += 1
            results["details"].append({
                "test": "identify_blocked_tasks",
                "status": "PASS",
                "result": f"{len(blocked)} blocked tasks"
            })
        except Exception as e:
            print(f"  FAILED: {str(e)}")
            results["tests_run"] += 1
            results["tests_failed"] += 1
            results["details"].append({
                "test": "identify_blocked_tasks",
                "status": "FAIL",
                "error": str(e)
            })

    # Test 5: Generate portfolio overview
    try:
        print("\nTest 5: Generate Portfolio Overview")
        portfolio = generate_portfolio_overview(asana_mcp)
        print(f"  Total programmes: {portfolio['metadata']['total_programmes']}")
        print(f"  Green: {portfolio['summary']['programmes_green']}")
        print(f"  Amber: {portfolio['summary']['programmes_amber']}")
        print(f"  Red: {portfolio['summary']['programmes_red']}")
        results["tests_run"] += 1
        results["tests_passed"] += 1
        results["details"].append({
            "test": "generate_portfolio_overview",
            "status": "PASS",
            "result": f"{portfolio['metadata']['total_programmes']} programmes"
        })
    except Exception as e:
        print(f"  FAILED: {str(e)}")
        results["tests_run"] += 1
        results["tests_failed"] += 1
        results["details"].append({
            "test": "generate_portfolio_overview",
            "status": "FAIL",
            "error": str(e)
        })

    # Summary
    print("\n" + "=" * 80)
    print(f"VALIDATION SUMMARY")
    print("=" * 80)
    print(f"Tests Run: {results['tests_run']}")
    print(f"Passed: {results['tests_passed']}")
    print(f"Failed: {results['tests_failed']}")
    print(f"Success Rate: {(results['tests_passed']/results['tests_run']*100) if results['tests_run'] > 0 else 0:.1f}%")
    print("=" * 80)

    return results


# ============================================================================
# USAGE EXAMPLE
# ============================================================================

if __name__ == "__main__":
    print("""
    Track 1 Query Validation Examples
    ==================================

    This script contains sample queries for Phase 1 portfolio dashboard.

    To use:
    1. Configure Asana MCP server
    2. Update WORKSPACE_GID constant
    3. Create sample programmes with custom fields
    4. Run: run_validation_tests(asana_mcp)

    Example:
        from mcp import asana_mcp_server
        asana_mcp = asana_mcp_server()
        results = run_validation_tests(asana_mcp)
    """)
