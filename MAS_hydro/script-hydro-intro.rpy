#ALL EVENTS HERE MUST BE BOOKMARKABLE

#dialogue about hydration
#fix the labels here if necessary, this event needs to be random with no conditionals, and repeatable

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
#fix the labels here if necessary, this event needs to be random with the conditional of seeing intro, and repeatable
    
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
    m "[Player]! Here is your 'Monika's health tip of the day'!"
    m "The topic of today is tips for drinking enough water!"
    m "We've already discussed the importance of drinking lots of water, so here we go..."
    m "The first one is trying to carry a water bottle with you wherever you go."
    m "Maybe buying a cute one helps with that, [player]!"
    m "If you have water with you, you have no excuse not to drink it! Ahahaha~"
    m "The second tip is focusing on fluids." 
    m "You don’t exactly have to drink plain water to meet your hydration needs."
    m "Tea, milk and broth would suffice, per example!"
    m "You can also add some flair to your water by squeezing in fresh lemon or lime juice."
    m "The third tip would be to skip sugary drinks." 
    m "While you can get fluid from soda, juice, and alcohol, these beverages have high calorie contents." 
    m "Also! Drink water while you’re out to eat instead of ordering another beverage."
    m "You can save the extra money, and also lower the calorie intake of your meal!"
    m "My final tip: if you’re working out hard, and consequently sweating a lot..."
    m "Consider drinking a sports drink that has electrolytes to help replace the ones you lose through sweating."
    m "Don't forget! It's still smart to choose water whenever possible."
    m "I hope these tips help you, [player]!"
    m "And don't forget, I can always remind you to drink water regularly!"
    m "Your lovely girlfriend will always take care of you."
    m "But make sure to take care of yourself too, okay? "
    extend "Ahahaha~" 
    m "I love you, [mas_get_player_nickname()]!"
    return "love"
    
#dialogue about signs of dehydration
#fix the labels here if necessary, this event needs to be random with the conditional of seeing intro, and repeatable

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hyMod_signs",
            prompt="Signs of dehydration",
            category=["health"],
            conditional="seen_event('hyMod_intro')"
            action=EV_ACT_RANDOM,
        )
    )

label hyMod_signs:
    m "[Player], have you noticed the signs your body show when something isn't right?"
    m "When we are in need of something, our bodies scream, demanding what isn't there."
    m "Speaking of which, do you know the signs of dehydration?"
    m "According to studies, some of them are headaches and fatigue."
    m "Some worst symptoms can be confusion, mood changes, overheating, and many more!"
    m "And don't forget! You can always pay attention to your urine color to be sure if you're drinking enough water."
    m "Aim for pale, clear urine!"
    extend " ...Well, that was weird. Ahahaha~"
    m "I'm just trying to help, [player]!" 
    m "I worry a lot about your health."
    m "Please stay safe for me, okay?"
    m "If you're thristy, don't hesitate in drinking some water."
    m "If you're not thirsty but remember that you haven't had a drink in a while, make sure to drink some water too!"
    m "Just don't drink too much water, neither too little!"
    return
