init -990 python in mas_submod_utils:
    Submod(
        author="my-otter-self",
        name="MAS Hydration Reminder Submod",
        description="Reminders about hydration and many more!",
        version="1.0.0"
    )

init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="MAS Hydration Reminder Submod",
            user_name="my-otter-self",
            repository_name="mas_reminders",
            submod_dir="/Submods/MAS Self Harm Submod",
            extraction_depth=3,
            redirected_files=(
                "README.md",
                "LICENSE.txt"
            )
        )
