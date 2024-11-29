import os
import shutil
from datetime import datetime

def clean_directory(path):
    """Remove all contents of the specified directory if it exists."""
    if os.path.exists(path):
        try:
            shutil.rmtree(path)
            print(f"Cleaned existing directory: {path}")
        except Exception as e:
            print(f"Error cleaning directory {path}: {e}")
            return False
    return True

def create_structure(base_path, structure_dict, reset=False):
    """
    Create the directory structure.
    
    Args:
        base_path (str): Base path where to create the structure
        structure_dict (dict): Dictionary defining the structure
        reset (bool): If True, will remove existing structure before creating new one
    """
    # Get the BHE directory path
    bhe_path = os.path.join(base_path, "BHE")
    
    # If reset is True and BHE directory exists, remove it
    if reset and os.path.exists(bhe_path):
        if clean_directory(bhe_path):
            print(f"Reset: Removed existing BHE directory at {bhe_path}")
        else:
            print("Failed to reset directory structure. Please check permissions and try again.")
            return False

    # Create the structure
    try:
        for name, content in structure_dict.items():
            path = os.path.join(base_path, name)
            if isinstance(content, dict):
                # It's a directory
                os.makedirs(path, exist_ok=True)
                create_structure(path, content)
            else:
                # It's a file
                # Only write if file doesn't exist or reset is True
                if not os.path.exists(path) or reset:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Created/Updated file: {path}")
                else:
                    print(f"Skipped existing file: {path}")
        return True
    except Exception as e:
        print(f"Error creating structure: {e}")
        return False

# Define the directory structure based on BHE.md
structure = {
    "BHE": {
        "README.md": "# BloodHound Enterprise (BHE)\n\nWelcome to the BHE project repository.",
        "Meetings": {
            "DE_Team": {
                f"{datetime.now().strftime('%Y-%m-%d')}_Meeting_Notes.md": """# DE Team Meeting Notes

## Date: {date}

### Attendees
- [List of attendees]

### Agenda
1. [Agenda item 1]
2. [Agenda item 2]

### Discussion Points
- 

### Action Items
- [ ] Action 1
- [ ] Action 2

### Next Steps
- 

### Notes
- """.format(date=datetime.now().strftime('%Y-%m-%d'))
            },
            "GCID_Team": {
                f"{datetime.now().strftime('%Y-%m-%d')}_Meeting_Notes.md": """# GCID Team Meeting Notes

## Date: {date}

### Attendees
- [List of attendees]

### Agenda
1. [Agenda item 1]
2. [Agenda item 2]

### Discussion Points
- 

### Action Items
- [ ] Action 1
- [ ] Action 2

### Next Steps
- 

### Notes
- """.format(date=datetime.now().strftime('%Y-%m-%d'))
            },
            "SpecterOps": {},
            "ECS": {},
            "HXM": {},
            "DA": {},
            "Other_Stakeholders": {}
        },
        "Todos": {
            "YYYY-MM-DD_Todos.md": "# Todo List\n\n## Outstanding Items\n- [ ] Item 1\n- [ ] Item 2"
        },
        "Assignments": {
            "Assignments_Table.md": "# Assignments\n\n| Task | Assignee | Due Date | Status |\n|------|----------|-----------|--------|\n| | | | |"
        },
        "Documentation": {
            "Project_Plan.md": "# Project Plan\n\n## Overview\n\n## Timeline\n\n## Deliverables",
            "Requirements.md": "# Requirements\n\n## Functional Requirements\n\n## Non-Functional Requirements",
            "Design_Documents": {}
        }
    }
}

if __name__ == "__main__":
    # Set the base path where you want to create the BHE directory
    base_path = r'C:\Users\s\Desktop\Project_PA'  # Note the 'r' prefix for raw string
    
    # Ask user if they want to reset the structure
    while True:
        response = input("Do you want to reset the existing structure? (yes/no): ").lower()
        if response in ['yes', 'no']:
            break
        print("Please enter 'yes' or 'no'")
    
    reset = response == 'yes'
    
    if create_structure(base_path, structure, reset):
        print("\nDirectory structure created successfully!")
        if reset:
            print("The structure was reset and recreated.")
        else:
            print("New files were added while preserving existing ones.")
    else:
        print("\nFailed to create directory structure. Please check the errors above.") 