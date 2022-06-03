#reminder setup 

#fix the following label and delete this note later :D 
#it has to have the conditional that it only shows up as a prompt if you've seen the random intro topic.
#no need to be bookmarkable or show up in repeat conversation, none of the events on this file.

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hymod_reminders",
            prompt="Can you remind me about drinking water?",
            category=["health"],
            conditional="seen_event('hyMod_intro')"
            pool=True,
            unlocked=True,
            rules={"bookmark_rule": store.mas_bookmarks_derand.WHITELIST}
        )
    )


label hymod_reminders:
    m "[player], of course! Thanks for asking me to!"
    m "Your health is really important to me, you know that."
    m "And this is a huge step on improving it!"

    m "It's usually recommended to grab a glass of water every hour, is that okay with you?{nw}"
    menu:
        m "It's usually recommended to grab a glass of water every hour, is that okay with you?{fast}"

        "Yep!":
            $ interval = store.hyMod_reminder_utils.INTERVAL_HOURLY_1

        "Maybe every 3 hours?":
            $ interval = store.hyMod_reminder_utils.INTERVAL_HOURLY_3

        "How about every 6 hours?":
            $ interval = store.hyMod_reminder_utils.INTERVAL_HOURLY_6

    if interval == store.hyMod_reminder_utils.INTERVAL_HOURLY_1:
        m "Alrighty then! I'll be sure to remind you about it hourly, [mas_get_player_nickname()]~"
    else:
        m "Alrighty then! I'll be sure to remind you about it every few hours, [mas_get_player_nickname()]~"

    python:
        store.hyMod_reminder.addRecurringReminder(
            "hyMod_reminder",
            datetime.timedelta(seconds=3600), interval, store.hyMod_reminder_utils.LATENCY_HOURLY
        )

        mas_hideEVL("hyMod_intro", "EVE", lock=True)
        mas_showEVL("hyMod_reminder_stop", "EVE", unlock=True)

    return "derandom"

#stop reminder
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hyMod_reminder_stop",
            prompt="You no longer need to remind me about hydration.",
            category=["health"],
            pool=True,
            rules={"no_unlock": None, "bookmark_rule": store.mas_bookmarks_derand.WHITELIST}
        )
    )

label hyMod_reminder_stop:
    m 7esb "Okay! I'll stop~"

    python:
        # Same here, DO NOT move this anywhere, this has to be right above the return statement.
        store.hyMod_reminder.stopReminder("hyMod_reminder")
        mas_hideEVL("hyMod_reminder_stop", "EVE", lock=True)
        mas_showEVL("hyMod_intro", "EVE", unlock=True)

    return


init 5 python:
    store.hyMod_reminder.addReminderEvent(
        Event(
            persistent.event_database,
            eventlabel="hyMod_reminder",
            conditional="store.hyMod_reminder.shouldTriggerReminder('hyMod_reminder')",
            action=EV_ACT_QUEUE,
            rules={"force repeat": None}
        )
    )

label hyMod_reminder:
    m "Hey, [player]! It's time to drink water~"
    m "Try to drink a full cup, okay?"
    m "Or at least half~"
    m "Thank you for taking care of yourself, [mas_get_player_nickname()]!"

    # Do not move this anywhere, this must be above the return.
    $ store.hyMod_reminder.extendCurrentReminder()
    return "no_unlock"