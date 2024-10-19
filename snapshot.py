import os
import pathlib

def should_ignore(path):
    return 'venv' in path.parts

def create_directory_map(start_path):
    tree = []
    for root, dirs, files in os.walk(start_path):
        path = pathlib.Path(root)
        if should_ignore(path):
            dirs[:] = []  # Don't recurse into this directory
            continue
        level = len(path.relative_to(start_path).parts)
        indent = '  ' * level
        tree.append(f"{indent}{path.name}/")
        for file in files:
            tree.append(f"{indent}  {file}")
    return '\n'.join(tree)

def combine_file_contents(start_path):
    combined_contents = []
    for root, dirs, files in os.walk(start_path):
        path = pathlib.Path(root)
        if should_ignore(path):
            dirs[:] = []  # Don't recurse into this directory
            continue
        for file in files:
            file_path = path / file
            try:
                with file_path.open('r', encoding='utf-8') as f:
                    content = f.read()
                    relative_path = file_path.relative_to(start_path)
                    combined_contents.append(f"###{relative_path}###\n{content}\n")
            except Exception as e:
                combined_contents.append(f"###{file_path.relative_to(start_path)}###\nError reading file: {str(e)}\n")
    return '\n'.join(combined_contents)

def main():
    current_dir = pathlib.Path.cwd()
    
    # Create directory map
    dir_map = create_directory_map(current_dir)
    with open('directory_map.txt', 'w', encoding='utf-8') as f:
        f.write(dir_map)
    print("Directory map has been saved to 'directory_map.txt'")
    
    # Combine file contents
    contents = combine_file_contents(current_dir)
    with open('combined_contents.txt', 'w', encoding='utf-8') as f:
        f.write(contents)
    print("Combined file contents have been saved to 'combined_contents.txt'")

if __name__ == "__main__":
    main()
