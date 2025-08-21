import os
from my_modules.dir_utils import DirUtils

def menu(root_dir):
    while True:
        DirUtils.clear_screen()
        categories = DirUtils.display_directories(root_dir, "Categories")
        choice = DirUtils.prompt_for_choice(
            "Enter the name of the category you want to choose, or 'exit' to quit: ",
            categories
        )

        if choice == 'exit':
            return
        elif choice:
            category_path = os.path.join(root_dir, choice)

            while True:
                DirUtils.clear_screen()
                years = DirUtils.display_directories(category_path, "Years")
                year_choice = DirUtils.prompt_for_choice(
                    "Enter the name of the year you want to choose, 'open' to open the category directory, 'back' to go back, or 'exit' to quit: ",
                    years
                )

                if year_choice == 'open':
                    DirUtils.open_directory(category_path)
                    input("Press Enter to return to the year selection...")
                    continue
                elif year_choice in (None, 'back'):
                    break
                elif year_choice == 'exit':
                    return

                year_path = os.path.join(category_path, year_choice)

                while True:
                    DirUtils.clear_screen()
                    months = DirUtils.display_directories(year_path, "Months")
                    month_choice = DirUtils.prompt_for_choice(
                        "Enter the name of the month you want to choose, 'open' to open the year directory, 'back' to go back, or 'exit' to quit: ",
                        months
                    )

                    if month_choice == 'open':
                        DirUtils.open_directory(year_path)
                        input("Press Enter to return to the month selection...")
                        continue
                    elif month_choice in (None, 'back'):
                        break
                    elif month_choice == 'exit':
                        return

                    month_path = os.path.join(year_path, month_choice)

                    while True:
                        DirUtils.clear_screen()
                        dates = DirUtils.display_directories(month_path, "Dates")
                        date_choice = DirUtils.prompt_for_choice(
                            "Enter the name of the date you want to choose, 'open' to open the month directory, 'back' to go back, or 'exit' to quit: ",
                            dates
                        )

                        if date_choice == 'open':
                            DirUtils.open_directory(month_path)
                            input("Press Enter to return to the date selection...")
                            continue
                        elif date_choice in (None, 'back'):
                            break
                        elif date_choice == 'exit':
                            return

                        date_path = os.path.join(month_path, date_choice)
                        DirUtils.open_directory(date_path)
                        input("Press Enter to return to the date selection...")
        else:
            DirUtils.console.print("[bold red]No matching category found.[/bold red]")
            input("Press Enter to continue...")

# Entry point
if __name__ == "__main__":
    try:
        nameOf_directory = input("Type the name or location of directory: ")  # e.g. demo-directory
        root_directory = DirUtils.find_root_directory(nameOf_directory)
        DirUtils.console.print(f"[bold green]Found root directory at: {root_directory}[/bold green]")
        menu(root_directory)
    except FileNotFoundError as e:
        DirUtils.console.print(f"[bold red]{e}[/bold red]")
