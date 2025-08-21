import os
import subprocess
import sys
import difflib
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text

class DirUtils:
    console = Console()  # Rich console for pretty output

    @staticmethod
    def find_root_directory(start_dir):
        """Find the first existing directory with a known name starting from the start_dir."""
        current_dir = os.path.abspath(start_dir)
        while True:
            if os.path.isdir(current_dir):
                return current_dir
            parent_dir = os.path.dirname(current_dir)
            if parent_dir == current_dir:
                break
            current_dir = parent_dir
        raise FileNotFoundError(f"Root directory not found starting from '{start_dir}'.")

    @staticmethod
    def get_directories(parent_dir):
        """Get a list of directories in the parent directory."""
        return sorted([d for d in os.listdir(parent_dir) if os.path.isdir(os.path.join(parent_dir, d))])

    @staticmethod
    def count_files(directory_path):
        """Count files in a directory."""
        return len([f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))])

    @staticmethod
    def display_directories(parent_dir, level_name):
        """Display the list of directories under a given level."""
        directories = DirUtils.get_directories(parent_dir)
        table = Table(title=Panel(f"Available {level_name}", style="bold green"), 
                      header_style="bold yellow", 
                      show_header=True, 
                      title_justify="center")

        table.add_column("Index", style="cyan")
        table.add_column("Directory", style="magenta")

        for index, directory in enumerate(directories):
            table.add_row(str(index + 1), directory)

        DirUtils.console.print(table)
        return directories

    @staticmethod
    def open_directory(path):
        """Open the directory in the file explorer."""
        if os.name == 'nt':  # Windows
            os.startfile(path)
        elif os.name == 'posix':  # macOS and Linux
            subprocess.run(['open', path] if sys.platform == 'darwin' else ['xdg-open', path])

    @staticmethod
    def clear_screen():
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def find_matches(query, choices):
        """Find matches for a query in a list of choices, case-insensitive, and include substring matches."""
        query = query.lower()
        choices_lower = [choice.lower() for choice in choices]
        
        # Find matches based on fuzzy matching
        fuzzy_matches = difflib.get_close_matches(query, choices_lower, n=10, cutoff=0.5)
        
        # Find matches based on substring inclusion
        substring_matches = [choice.lower() for choice in choices if query in choice.lower()]
        
        # Combine fuzzy matches and substring matches, ensuring unique results
        combined_matches = set(fuzzy_matches + substring_matches)
        
        # Map combined matches back to original choices
        result_matches = []
        for match in combined_matches:
            if match in choices_lower:
                result_matches.append(choices[choices_lower.index(match)])
            else:
                # If the match is from substring_matches, directly append
                result_matches.extend([choice for choice in choices if match in choice.lower()])
        
        return list(set(result_matches))

    @staticmethod
    def prompt_for_choice(prompt, choices):
        """Prompt the user for a choice and return the best match or handle multiple matches."""
        while True:
            # Style prompt text with rich's Text object
            styled_prompt = Text(prompt, style="bold white on blue")
            choice = Prompt.ask(styled_prompt).strip()
            
            if choice.lower() == 'back':
                return None
            elif choice.lower() == 'open':
                return 'open'
            
            matches = DirUtils.find_matches(choice, choices)
            if not matches:
                DirUtils.console.print("[bold red]No matching item found. Please try again.[/bold red]")
            elif len(matches) == 1:
                return matches[0]
            else:
                DirUtils.console.print("[bold yellow]Multiple matches found:[/bold yellow]")
                table = Table(header_style="bold yellow", show_header=True, title_justify="center")

                table.add_column("Index", style="cyan")
                table.add_column("Match", style="magenta")

                for i, match in enumerate(matches):
                    table.add_row(str(i + 1), match)

                DirUtils.console.print(table)
                
                while True:
                    # Style the prompt for choices with rich's Text object
                    styled_choice_prompt = Text("Enter the number of your choice, or 'back' to go back", style="bold white on blue")
                    match_choice = Prompt.ask(styled_choice_prompt).strip()
                    if match_choice.lower() == 'back':
                        return None
                    if match_choice.isdigit():
                        index = int(match_choice) - 1
                        if 0 <= index < len(matches):
                            return matches[index]
                    DirUtils.console.print("[bold red]Invalid choice. Please try again.[/bold red]")
