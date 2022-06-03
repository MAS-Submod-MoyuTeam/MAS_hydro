#dialogue about hydration

#fix the labels here if necessary, this event needs to be random with no conditionals.

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hyMod_intro",
            prompt="Drinking water",
            category=["health"],
            random=True
        )
    )

label hyMod_intro:
    m "[player], I've been thinking about something."
    m "The importance of drinking water!"
    m "Everyone knows that drinking water as much as you can is very important..."
    m "Some of the benefits of being hydrated include higher energy levels and healthy weight loss."
    m "Some studies even support the idea that drinking water can help with your brain and energy!"
    m "If you don't drink enough water, headaches can happen and your mood can decline."
    m "And I'm not even talking about the amount of health problems that can come with it!"
    m "Constipation, urinary tract infections, kidney stones, skin problems..."
    m "Ouch! I get shivers only to think about those."
    m "What no one tells you though, is that the amount of water you must drink depends on a lot of factors."
    m "Where you live, your diet, the season and your environment and routine, per example."
    m "Oh! I've been rambling too much."
    m "What I really wanted to tell you was that you can tell me if you want me to remind you to drink water on a regular basis."
    m "Just let me know if you need it, okay?"
    m "I just want to take care of you!"
    m "Await for the next 'Monika's health tip of the day'!"
    return
    
# dialogue about tips to drink more water
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hyMod_tips",
            prompt="Tips to drink more water",
            category=["health"],
            conditional="seen_event('hyMod_intro')"
            action=EV_ACT_RANDOM,
        )
    )

label hyMod_tips:
    m ""
