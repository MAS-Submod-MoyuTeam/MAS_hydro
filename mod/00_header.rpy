init -990 python in mas_submod_utils:
    Submod(
        author="otter",
        name="MAS Hydration Reminder Submod",
        description="Reminders about hydration and many more!",
        version="1.0.0"
    )

init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="MAS Hydration Reminder Submod",
            user_name="my-otter-self",
            repository_name="MAS_hydro",
            submod_dir="/Submods/MAS Hydration Reminder Submod",
            extraction_depth=3,
            redirected_files=(
                "README.md",
                "LICENSE.txt"
            )
        )
