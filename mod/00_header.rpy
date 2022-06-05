init -990 python in mas_submod_utils:
    Submod(
        author="otter",
        name="MAS Hydration Submod",
        description="Reminders about hydration and many more!",
        version="1.0.1"
    )

init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="MAS Hydration Submod",
            user_name="my-otter-self",
            repository_name="mas_hydro",
            submod_dir="/Submods/MAS Hydration Reminder Submod",
            extraction_depth=3,
            redirected_files=(
                "README.md",
                "LICENSE.txt"
            )
        )
