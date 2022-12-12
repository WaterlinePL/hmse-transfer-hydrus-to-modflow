import sys

from hmse_job_utils.data_passing import pass_data_from_hydrus_to_modflow

SIMULATION_ROOT = "/workspace"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <project id>")
        exit(1)

    project_id = sys.argv[1]

    pass_data_from_hydrus_to_modflow(project_id)
