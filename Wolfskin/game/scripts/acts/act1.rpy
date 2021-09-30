## The file for act 1.

transform ilona_transform_pos1:
    zoom 0.5
    xpos 300

transform edwin_transform_pos1:
    zoom 0.5
    right

transform ilona_move_right:
    ilona_transform_pos1
    linear 0.5 xpos 550

# Disables that the poem does not advance automatically.
screen disable_Lmouse():
    key "mouseup_1" action NullAction()

label act1:

    $ quick_menu = False

    window hide

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg black
    with fade

    play music 'audio/ambience/dark forest.mp3' fadein 5.0 fadeout 5.0 volume 0.2

    # Edwin's monologue for the intro in NVL mode
    define nvlNarrator = Character(None, kind=nvl, what_font="BluuNext-Bolditalic.otf", what_size=50, what_kerning=2)

    # Toggle on the auto-play
    $_preferences.afm_enable = True

    # Makes sure that the poem advances automatically. Still possible to instantly see a sentence though!
    show screen disable_Lmouse()

    # NVL mode: Edwin's monologue

    nvlNarrator """
    I am lost.

    Pray, that I shall find my path.

    Pray, that I shall not lose heart.

    Pray, I see for who I am.

    This, the only wish I have.

    \nBefore I’ve wronged,

    So far gone.
    """

    hide screen disable_Lmouse

    nvl clear

    # Toggle off the auto-play
    $_preferences.afm_enable = False

    ## Show the intro of the act.

    scene bg fluffies
    with fade

    call screen intro(1)

    # Switch to AVD mode.

    ## FOREST

    stop music fadeout 3.0

    scene bg forest night
    with fadehold

    $ renpy.pause(2.0)

    play music 'audio/sfx/bbc woodland.ogg' volume 0.17 fadein 3.0

    $ renpy.pause(1.0)

    show ilona_twilight at ilona_transform_pos1
    show expression AlphaMask("canopy", At("ilona", ilona_transform_pos1)) as ilona_mask
    with dissolve

    $ renpy.pause(1.0)

    $ quick_menu = True

    il "We should think of finding shelter soon, before it gets too dark."

    show ilona_twilight closed with dissolve

    "Ilona waits for Edwin to turn back into a human, closing her eyes to rest for a moment. There's only the sound of the forest until Edwin speaks to break their silence."

    show edwin_twilight glance talk at edwin_transform_pos1
    show expression AlphaMask("canopy", At("edwin", edwin_transform_pos1)) as edwin_mask
    with dissolve

    ed "I know that I'm asking for too much, but despite everything that's happened… would you please stay with me?"

    show ilona_twilight sad shock talk with dissolve

    il "What? Edwin, please, calm down-"

    show edwin_twilight fear furrow talk with dissolve

    ed "... Ilona I-I can’t. Not in a situation like this..."

    show ilona_twilight open sad neutral
    show edwin_twilight glance neutral
    with dissolve

    il "You’re right, but I need you to slow down. I can’t keep up with you and that is only going to make us look all the more suspicious."

    ed "..."

    show ilona_twilight pensive at ilona_move_right
    show expression AlphaMask("canopy", At("ilona", ilona_move_right)) as ilona_mask

    $ renpy.pause(0.6)

    show ilona_twilight sad talk with dissolve

    il "We have only each other to rely on."

    show edwin_twilight sad neutral
    show ilona_twilight pensive sad neutral with dissolve

    stop music fadeout 8.0

    "As she says this, she places her hands over his. His hands are abnormally cold to touch. Ilona learned this was a sign of his transformation."

    "She gently caresses his hand and strokes it soothingly."

    "Despite his curse, she must remain with him."

    show ilona_twilight closed relaxed with dissolve

    "The moonlight beams over them, slightly wavering with each breath they take."

    play music 'audio/music/mastered/He_Who_Seeks_Hope_Theme_Of_Edwin.ogg' fadein 5.0 volume 0.5

    il "(If only the moonlight would never leave us. We should rest here for a while.)"

    il "Edwin…"

    show edwin_twilight closed neutral with dissolve

    ed "…"

    show ilona_twilight blush smile with dissolve

    il "Ed…"

    show edwin_twilight sad grin blush with dissolve

    ed "Yes, I’m here. Please forgive my wandering mind."

    show edwin_twilight closed grin
    show ilona_twilight open
    with dissolve

    ed "...What could I ever do without you? I feel like I have never thanked you for-"

    show ilona_twilight happy -blush with dissolve

    il "You have thanked me more than enough already, Edwin. I appreciate it…"

    show ilona_twilight closed smile
    show edwin_twilight glance smile blush
    with dissolve

    "Their eyes flicker for a moment and he’s not shivering anymore. "

    ## OUTSIDE TOWN

    scene bg road:
        xzoom-1
    with longfade

    "Eventually, they press on. They sight a lonely settlement on the horizon; stone walls surround its perimeter."

    show edwin_night closed at right with dissolve:
        zoom 0.50

    ed "Heh…"

    show edwin_night fury talk furrow with dissolve

    ed "I haven't felt like m-myself lately, since the incident back at the priory. Try as I may to blend in, to do good and keep myself in check… I am a beast, through and through."

    show edwin_night stare yell with dissolve

    ed "What is it that we've done wrong? Is us being together something so heinous? Is my existence such a sin?"

    show ilona_night sad pensive neutral with dissolve:
        zoom 0.50 xpos 50

    il "..."

    show edwin_night angry furrow
    show ilona_night neutral
    with dissolve

    show edwin_night glance talk with dissolve

    ed "I did not know the extent of the hatred that lay within their souls until that night… to go as far as to burn me alive…"

    ed "Is there something wrong with me, Ilona? I'm always on edge, fearing for our lives… I never meant to put you through this."

    show edwin_night neutral
    show ilona_night closed talk
    with dissolve

    il "If you want my answer as a former nun… You and I have sinned."

    il "You said that you were a beast, through and through."

    show ilona_night open talk

    il "You're not. You’re-"

    hide ilona_night

    hide edwin_night

    play sound 'audio/sfx/Letting_go_of_your_totally_non-romantic_partners_hand_because_someone_just_saw_you.mp3' volume 0.7

    with vpunch

    stop music fadeout 1.0

    "Edwin immediately releases her hand, intertwined seconds ago, but now balled into a fist. The rustling of dry leaves brings with it a heavily armed guard and an archer wearing a cloak."

    unk "That's enough loitering around the town wall looking suspicious, don't you think?"

    show anari_night angry glance neutral bow with dissolve:
        zoom 0.50 xpos 10 xzoom -1

    queue music 'audio/music/mastered/March_Of_the_Huntress_Theme_Of_Anari.ogg' fadein 2.0 volume 0.35

    unk "I've been observing your movements from the battlements for a while now. Be grateful that the town master wishes to have a meeting with you, or else I would have already pierced you with my arrows."

    show edwin_night sad furrow talk at right with dissolve:
        zoom 0.50 xpos 1.0

    ed "But, we-"

    show ilona_night glance annoyed talk with dissolve:
        zoom 0.50 xpos 0.75 xzoom -1

    il "May we ask, to what purpose do we owe this pleasure?"

    show ilona_night aaaa neutral

    show anari_night open smile

    unk "{i}Sister{/i}, all I know is that the master called you. I sighted a nun and a man outside the town walls and informed him of this."

    unk "I can tell your legs are shaking even from here… so make sure to comply obediently and I won't ask any difficult questions about you in return."

    show edwin_night talk open furrow

    ed "She simply asked what business the master has with us. You're acting very feisty for someone who didn't even have the decency to introduce herself."

    show edwin_night neutral

    show anari_night closed relaxed

    unk "Hmph. Fair enough."

    show anari_night open talk with dissolve

    an "My name is Anari. Happy now?"

    show anari_night smile
    an "I'm not going to probe you or anything."

    an "You may be outsiders, but you look like decent enough folk. No need to come up with any grand excuses for why you’re here."

    show anari_night angry smile
    an "So, let’s get back to it. Will you accept the town master's call?"

    show ilona_night closed talk annoyed

    il "...I suppose that choice is not truly much of one. I accept."

    show ilona_night glance neutral

    show anari_night smile raised nii with dissolve

    an "A wise judgement. You’re clever for a nun, but you should learn to keep your dog in line."

    show edwin_night fear talk furrow

    ed "...Excuse me?"

    show anari_night angry glance neutral with dissolve

    an "I don’t appreciate being called ‘feisty’."

    show anari_night neutral

    show edwin_night anxious

    ed "I meant no offense when I said that. My apologies."

    show anari_night nii smile relaxed with dissolve

    an "So you do have manners; it would do you well to keep them. Let’s get moving, then. I’ll escort you to the manse."

    ## TOWN GATE

    scene bg belorov night
    with longfade

    "Anari takes the position of rear guard, as the other guard leads the way forward."

    stop music fadeout 3.0

    "Ilona glances back, just once. Anari's bow is by her side and a hand rests on the quiver, ready to fire if the two of them even thought of escaping."

    "Ilona cannot help but wonder just how much of their conversation Anari overheard... Her arrival seemed too well-timed."

    "Did they give away too much, even when they thought they were alone?"

    "She glances at Edwin, his face inscrutable. And so, they enter the gates."

    stop music fadeout 3.0

    ## TOWN PLFAZA
    $ quick_menu = False

    show bg fluffies with fade

    with logodissolve

    scene bg town plaza night
    with longfade

    stop sound fadeout 4.0

    play music 'audio/music/mastered/The_Town.ogg' volume 0.7

    $ renpy.pause(3.0)

    show edwin_night closed at right with longdissolve:
        zoom 0.50 xpos 1.0

    $ quick_menu = True
    ed "(When was the last time I felt any hope? Anything besides pain? The swelling in my chest is excruciating…)"

    show edwin_night open
    ed "(I truly wouldn't have made it this far on my own. Even if I hide what I am well, people can't help but to be suspicious.)"

    show edwin_night smile angry furrow
    ed "(Although — a town full of people not trying to kill me yet is quite an improvement.)"

    "The town is bustling despite not being very large. A clock tower stands over the plaza. Small patches of land growing wheat are adjacent to the plaza and there is a stocked stable for horses nearby."

    "There's a large bonfire in the square, and there are carved turnips at the doors of all the houses."

    show ilona_night glance sad neutral with dissolve:
        zoom 0.50 xpos 0.75 xzoom -1

    # spoken as though Ilona is suspicious of jack o' lanterns
    il "What kind of decorations are these?"

    show edwin_night glance grin -furrow with dissolve

    ed "It’s for... All Hallows’ Eve, a celebration to commemorate the dead."

    show ilona_night angry sad talk with dissolve

    il "You mean All Saints’ Eve? Why are the townsfolk celebrating in joy, then?"

    show edwin_night closed grin furrow
    show ilona_night neutral
    with dissolve

    ed "You were raised strictly, Ilona. Father Ivanov never wanted you to know about these pagan festivals."

    play sound 'audio/sfx/Bumping_into_thick_clothed_man.mp3'

    show edwin_night fear talk
    with hpunch

    ed "Oh!-"

    show kellac_night neutral at easeinleft_transform:
        zoom 0.50

    # calmly, not overly acted out
    unk "Young lad, please watch your step. One mistake and this weary old man is done for…"

    show edwin_night closed
    show ilona_night open solemn
    with dissolve

    ed "I’m so sorry for bumping into you, sir-"

    show anari_night closed talk angry sweatdrop with dissolve:
        zoom 0.50 xpos 540

    # as though tired of an old joke
    an "...Kellac, we're the same age."

    show anari_night look neutral -sweatdrop
    show kellac_night nii smile raised
    show edwin_night open neutral -furrow

    # most of Kellac's lines should be delivered without too much enthusiasm, as though he was an older person or an 'old soul'.
    ke "Fancy meeting you here, Anari. I didn’t know you like to take strolls. I never knew you had friends either! And who may you be, dear sister?"

    show edwin_night closed neutral sweat
    show ilona_night annoyed
    with dissolve

    ed "Uh, I’m not sure we're friends…"

    show ilona_night relaxed
    show kellac_night open raised
    show edwin_night open -sweat

    ke "Pleased to make your acquaintance, anyhow. I’m Kellac, Anari and I go way back."

    show anari_night closed angry neutral sweatdrop

    an "That we do, and I regret it."

    show kellac_night nii happy

    ke "You’ve just got to love that personality! Don’t take her too seriously, she's always been like that."

    show edwin_night smile
    show kellac_night smile

    ed "I see… I'm Edwin. Pleased to make your acquaintance."

    show ilona_night happy

    il "As am I. My name is Ilona. Forgive my ignorance, but are you the master of this town?"

    show anari_night look
    show kellac_night talk worry open
    with dissolve

    ke "Me? Sorry, but no. I'm just the physician and herbalist. Did the master summon you?"

    show kellac_night neutral
    show ilona_night sad talk
    show edwin_night neutral sad
    with dissolve

    il "He did, but I don't know what business we have with him..."

    show ilona_night neutral
    show kellac_night smile sweat
    show anari_night -sweatdrop
    with dissolve

    ke "Aha. I should have expected as much; Anari has a habit of leaving out the details and jumping straight to the point."

    show kellac_night raised -sweat
    with dissolve

    ke "I should get going, but we're bound to see each other again soon. Keep well, Anari."

    hide kellac_night with dissolve
    show anari_night closed relaxed
    with dissolve

    "Anari only nods curtly, and the group moves along. Further into the town, they find a large house made of timber and stone."

    play sound 'audio/sfx/footsteps slow leather tile.wav'

    stop music fadeout 3.0

    ## MANSE
    scene bg chapel night
    with longfade

    show edwin_twilight:
        zoom 0.5 xcenter 170 xzoom -1
    show ilona_twilight:
        zoom 0.5 xcenter 370
    show anari_twilight look:
        zoom 0.5 xcenter 850 xzoom -1
    with dissolve

    play sound 'audio/sfx/3 knocks.wav' volume 0.15

    "Anari knocks on the door. It is answered by a man and woman in fine clothing. They step outside of the house."

    queue sound 'audio/ambience/wind and trees.ogg' volume 0.2

    show uldin_twilight:
        xcenter 1500 xzoom -1
    show salome_twilight neutral:
        xcenter 1750 xzoom -1
    with dissolve

    an "Sir Uldin, Lady Salome. I've brought to you Sister Ilona, and her companion Edwin."

    show uldin_twilight closed laugh

    hide anari_twilight with dissolve

    ul "So the man was with her after all?"

    show anari_twilight worry neutral sweatdrop behind uldin_night with dissolve:
        zoom 0.5 xcenter 1100

    an "At first, I thought a holy woman was being accosted by some blackguard. To think that he was her travelling companion..."

    show edwin_twilight glance talk

    ed "I understand I may not have the friendliest appearance… but I have sworn to protect Sister Ilona from harm."

    show uldin_twilight smirk open

    ul "This is indeed unexpected… Anari's eyes are keen, but perhaps only for hunting her quarry."

    show anari_twilight closed relaxed smile -sweatdrop

    an "True. There's no need to understand the conversations of beasts to hunt them, only their behaviour."

    show salome_twilight grin downturn nii
    show edwin_twilight neutral
    with dissolve

    sa "Judging by Anari's report, I would have thought she was describing a saint!"

    show ilona_twilight sad pensive
    with dissolve

    il "Thank you for your kind words, but they are far too gracious to be wasted on me... I have not done anything to be deserving of such praise."

    show salome_twilight smallgrin open

    sa "I thought you might be able to join us for tonight's feast for All Hallows' Eve, and to perhaps lead us in prayer."

    show uldin_twilight laugh
    with dissolve

    ul "It’s not every day that you see a nun, and much less in such unlikely company. So, would you accept our invitation?"

    show ilona_twilight closed annoyed

    "Ilona considers this carefully. She and Edwin had drawn too much attention already. So it surprises her when Edwin speaks without any fear."

    show edwin_twilight talk closed with dissolve
    show anari_twilight look -sweatdrop

    ed "We will gladly accept."

    show ilona_twilight glance solemn sweat
    with dissolve

    sa "Tonight's banquet will begin shortly, but you should still have time to prepare for it. Anari, let us debrief in the meantime."

    ## HALL(SCENE 4)

    stop sound fadeout 5.0

    scene bg hall alt
    with longfade

    play sound 'audio/ambience/bbc fire.mp3' volume 0.1 loop

    "It had only been a few days since they were on the run… Ilona could scarcely believe that they were welcomed so readily."

    "They sit at a table laden with food: a rich coloured beetroot soup, mulled wine with spices, pickled vegetables, a glistening whole roasted pheasant and even more dishes than one could name."

    scene bg hall night
    with fade

    # show Fleur and Eisleigh for their introduction (for only one moment)
    show fleur_dim at left_center with dissolve
    show eisleigh_dim at right_center with dissolve

    "Seated at the table were two new faces: Fleur, the daughter of Uldin. On Fleur's left side was Eisleigh, an assistant to the house."

    hide fleur_dim
    hide eisleigh_dim
    with dissolve

    # show Uldin and Salome to highlight their importance (for only one moment)
    show uldin_dim at left_center
    show salome_dim at right_center
    with dissolve

    "Uldin plans to rebuild the ruined chapel in Belorov, as Salome is deeply pious. This is why Salome regards the meeting with Ilona as such good fortune."

    hide uldin_dim
    hide salome_dim
    with dissolve

    # group shot with all characters shown on screen
    show uldin_dim:
        yalign 1.0 zoom 0.7 xcenter 85
    show salome_dim:
        yalign 1.0 zoom 0.7 xcenter 335
    show fleur_dim look behind anari_dim, salome_dim:
        yalign 1.0 zoom 0.7 xzoom -1 xcenter 585
    show anari_dim look:
        yalign 1.0 zoom 0.35 xzoom -1 xcenter 835

    show eisleigh_dim look behind anari_dim, kellac_dim:
        yalign 1.0 zoom 0.7 xzoom -1 xcenter 1085
    show kellac_dim:
        yalign 1.0 zoom 0.35 xcenter 1335
    show edwin_dim behind kellac_dim, ilona_dim:
        yalign 1.0 zoom 0.35 xzoom -1 xcenter 1585
    show ilona_dim:
        yalign 1.0 zoom 0.35 xzoom -1 xcenter 1835
    with dissolve

    "As everyone gathers at the table, Uldin urges Ilona to lead them in prayer before the meal."

    hide uldin_dim
    hide salome_dim
    hide fleur_dim
    hide anari_dim
    hide eisleigh_dim
    hide kellac_dim
    hide edwin_dim
    with dissolve

    # Close-up of Ilona (praying)
    show ilona_dim closed at center with dissolve:
        zoom 0.8 yoffset 300

    "She speaks a few words of gratitude for the harvest and for peace and protection. When she lifts her eyes once again, the lively banquet commences."

    queue music 'audio/music/mastered/The_Banquet.ogg' fadein 3.0

    hide ilona_dim with dissolve

    # Anari, Kellac and Fleur convo

    show fleur_dim look at extra_left:
        xzoom -1
    show anari_dim look at center:
        zoom 0.5 xzoom -1
    show kellac_dim smile raised at extra_right:
        zoom 0.5 xzoom -1
    with dissolve

    ke "The food smells amazing. Was that the pheasant you caught today, Anari?"

    show anari_dim nii raised

    an "The very one. Ahh, a successful hunt and high quality spices can put even someone like me in a good mood."

    show kellac_dim raised nii happy sweat
    show fleur_dim nii happy

    ke "You should always be in a good mood, then!"

    # Anari switches to left to face Fleur
    show anari_dim look:
        xzoom 1
    show kellac_dim smile open -sweat

    an "Heheheh. Fleur, would you like some spiced pheasant?"

    show fleur_dim sorry happy

    fl "Oh no, thank you, Aunt Anari. You always make it way too spicy… "

    show fleur_dim sorry smile
    show anari_dim worry

    an "That's too bad… I guess you really don't take after Uldin when it comes to food."

    # Salome, Fleur, Ilona, and Edwin convo
    scene bg hall alt
    with fade

    show salome_dim at extra_left
    show ilona_dim:
        zoom 0.5 xzoom -1 xcenter 1750
    show edwin_dim behind ilona_dim:
        zoom 0.5 xcenter 1550
    with dissolve

    sa "So, what brings you to Belorov, Mister Edwin and Sister Ilona?"

    show salome_dim pensive sad neutral with dissolve

    sa "Our town may not look like much after our chapel was ransacked and destroyed, but it was once breathtaking."

    show ilona_dim sad happy

    il "We're… on a pilgrimage. We were just seeking shelter before dark."

    show ilona_dim neutral

    il "I heard about the destruction of a chapel some time ago, but I had no idea it was here."

    show salome_dim parted

    sa "Yes, it was the barbarians' doing. Even now, we're still rebuilding the town, but the faithful have moved on from here."

    sa "I miss having someone to share my connection with God, so I am sorry to impose my sudden invitation on you."

    show salome_dim open relaxed smallgrin

    sa "Belorov is home to people of many faiths. Many of us have travelled from afar, like myself."

    show ilona_dim relaxed smile
    show edwin_dim anxious smile blush

    il "From what I understand, Edwin was also quite the traveller before we met."

    show fleur_dim happy behind salome_dim with dissolve:
        xzoom -1 xcenter 530

    fl "Do you have any stories, Edwin? I'd love to hear them."

    show edwin_dim closed grin

    ed "Haha. To tell you everything that happened would tax my wits."

    show fleur_dim nii
    show salome_dim smile

    fl "Have you met any mythical creatures in your journeys? Ever met the fair folk?? I've always dreamed of finding one!!"

    show edwin_dim anxious smile -blush

    ed "Let me think. There was this one time I had an encounter with a giant… "

    show edwin_dim grin

    "Edwin regales the table with his tale of encountering a giant when he was atop a mountain. Fleur and Salome listen with rapturous attention."

    # Kellac and Anari leaves

    show kellac_dim smile behind fleur_dim with dissolve:
        zoom 0.5 xcenter 800

    "Even Kellac takes an interest in these tales and starts telling of his own travels. He loses track of time and he decides that it is getting late and he needs to head in early."

    show anari_dim with dissolve:
        zoom 0.5 xcenter 1200

    "Anari leaves to get some rest for her shift as the town guard. Both of them bid everyone at the table a good night."

    hide kellac_dim
    hide anari_dim
    with dissolve

    # Uldin, Salome, Fleur, Eisleigh, Edwin, Ilona convo
    scene bg hall night
    with longfade

    show salome_dim:
        xcenter 150
    show fleur_dim behind salome_dim:
        xzoom -1 xcenter 730
    show ilona_dim:
        zoom 0.5 xzoom -1 xcenter 1830
    show edwin_dim behind ilona_dim:
        zoom 0.5 xcenter 1630
    with dissolve

    "Even though the party thins out a little, Fleur seems as excitable as when she began. Even Eisleigh, who kept to herself as she ate, joins in on the conversation."

    show eisleigh_dim glance small behind fleur_dim with dissolve:
        xzoom -1 xcenter 1100

    ei "You've really travelled a long way if you came from across the sea, Edwin."

    show fleur_dim sorry
    show salome_dim neutral
    fl "Now I'm wondering, how did you meet Sister Ilona?"

    show ilona_dim glance
    show edwin_dim fear grin blush
    with dissolve
    ed "Oh uh… Heh heh. That's a story for another time. I'm pretty tired…"

    show fleur_dim wink happy
    with dissolve
    fl "Oh, could it be…? Is the story of how you met Ilona not suitable for my ears?"

    # Eisleigh turns to left briefly to face Fleur
    show eisleigh_dim nii grin:
        xzoom 1

    ei "Ahaha, is that it? You might be onto something, Fleur."

    show eisleigh_dim:
        xzoom -1

    show fleur_dim nii
    show ilona_dim closed aaaa sweat
    with dissolve
    il "…"
    extend "(Girls these days are sharp.)"

    show edwin_dim fear talk blush
    show eisleigh_dim look smile
    with dissolve
    ed "No no no, that's not it at all! It's… not that interesting compared to my other stories."

    show fleur_dim wink smile
    show edwin_dim neutral sweat
    with dissolve
    fl "Hmph, I was under the impression you two shared a forbidden romance. Perhaps the strange forces that wander tonight will tip the scales at last!"

    show salome_dim angry pensive blush
    with dissolve
    sa "Fleur, you shouldn't tease guests. And you really shouldn't encourage her, Eisleigh!"

    # Fleur turns to left to face Salome
    show fleur_dim sorry happy:
        xzoom 1
    show ilona_dim open relaxed -sweat
    fl "Mother, it's All Hallow's Eve! Tricks and pranks are part of the fun. I'm merely teaching Sister Ilona about this part of the festival — She shouldn't be so serious and uptight all the time!"

    show uldin_dim wink laugh worry blush behind fleur_dim, eisleigh_dim with dissolve:
        xzoom 1 xcenter 400

    ul "Well, they said they were on a pilgrimage. If their sins are meant to be forgiven in the end, they should be able to sin along the way all they want!"

    show ilona_dim pensive annoyed blush with dissolve
    il "..."

    show edwin_dim stare talk blush with dissolve
    ed "Grk..."

    show salome_dim sad closed parted sweatblush
    sa "Not you too, dear… You must have had too much to drink."
    show salome_dim angry pensive neutral
    show fleur_dim neutral look
    show uldin_dim glance smirk
    "Salome gives one stern glance to both Fleur and Uldin, and their boisterous laughs subside. Uldin still seems pleased with his comment. When he recalls the looks on Ilona and Edwin's faces, he tries to not burst out laughing again."

    # Fleur turns to right to face Edwin/Ilona
    show fleur_dim look happy with dissolve:
        xzoom -1

    fl "I apologize, Mother. And I apologize to you as well, Edwin and Sister Ilona, for insinuating something I should not have. "

    show ilona_dim pensive solemn
    show edwin_dim anxious

    "Ilona and Edwin sheepishly mumble their acceptance of Fleur's apology. There is still too much attention on them…"

    hide salome_dim with dissolve

    "Salome asks everyone their preferences for tea so she can make preparations, and she excuses herself."

    hide fleur_dim with dissolve

    "A brief moment later, Fleur rises from her seat. She helps Salome to prepare the tea, truly apologetic about her earlier behaviour."

    show uldin_dim wink laugh relaxed with dissolve
    ul "We've arranged separate sleeping quarters for the both of you. Please, don't take our jests seriously."

    show edwin_dim open -blush
    ed "You've been most gracious to offer us both this feast and shelter for the night. Thank you again for your hospitality."

    ul "Oh no need, but if you must insist: you’re welcome."

    show uldin_dim glance with dissolve
    ul "Please, I know this is all too much for you and Sister Ilona. You’ve met quite a few people already, and it's getting late. If you need to retire for the evening, you are welcome to."

    # Tea party : Uldin, Fleur, Eisleigh, Ilona, Edwin convo
    scene bg hall alt
    with longfade

    "Salome and Fleur have the tea ready and Eisleigh helps serve it to the guests and places servings of milk and sugar at each end of the table."

    scene bg hall night
    with fade

    show uldin_dim at extra_right with dissolve:
        xzoom -1

    "Uldin remarks that this is one of his favourite teas — indeed, the pleasant aroma of black tea is refreshing, and any awkwardness from the conversation before is soon forgotten."

    show ilona_dim at less_left:
        zoom 0.5
    show edwin_dim behind ilona_dim:
        zoom 0.5 xzoom -1 xcenter 200
    with dissolve

    ul "Though, I must admit I remain curious as to how you two met each other. Are you religious, Edwin?"

    show edwin_dim glance talk
    ed "As much as any other man. Our meeting, well… Ilona pulled me out of a dark place. We bonded over the stories and poems she was recording."

    ed "I did not want to let her travel alone, so I decided to act as her guard on this journey."

    show uldin_dim closed laugh
    ul "I see. Having a companion to talk about the same texts… That's not so different from me and Eisleigh."

    show eisleigh_dim grin behind uldin_dim:
        xcenter 1300
    show uldin_dim neutral
    with dissolve

    ei "Well… magical texts; books about curses and spells, rather than stories and poems."

    show ilona_dim smile
    il "Oh, that's unusual. Both of you practice magic?"

    show uldin_dim talk
    ul "It's a useful resource, but difficult to master. You did say the two of you are on a pilgrimage… so you might not be aware of recent events."

    show eisleigh_dim angry look talk
    ei "There have been sightings of a werewolf in another town."

    show edwin_dim neutral distant sweat
    show ilona_dim pensive neutral solemn
    with dissolve

    show uldin_dim pensive angry neutral with dissolve
    ul "Those foul beasts… A werewolf truly must be cursed to succumb to their bloodlust."

    stop music fadeout 3.0
    stop sound fadeout 5.0

    "An oppressive silence lingers and sweat beads down Edwin’s forehead. Ilona tries to keep a straight face, but her brow twitches."

    play sound 'audio/sfx/zapsplat tea.mp3' volume 0.2
    "Edwin adds more sugar to his tea, and he takes care to not rattle the crockery as he stirs it with the spoon."

    show uldin_dim laugh
    ul "Please pay no heed to my language, it- It’s just..."

    scene bg hall alt
    with fade

    ul "Belorov was once an old fortress, so we don't have to worry about monster attacks. But in my youth, I experienced an attack first hand..."

    "Uldin details a dramatic hunting trip in his youth, with his older brother and subordinate."

    "A werewolf attacked the tent in the dead of night, but Uldin fended it off with fire magic."

    "His subordinate was torn to pieces, and Uldin's brother had his legs nearly hewn off."

    ul "If it were not for my study of magic, who could say what might have happened?"

    ed "..."

    scene bg hall night
    with fade

    show uldin_dim angry neutral at extra_right:
        xzoom -1
    show ilona_dim pensive sad at less_left:
        zoom 0.5
    show edwin_dim distant sweat behind ilona_dim:
        zoom 0.5 xzoom -1 xcenter 200
    with dissolve

    $ renpy.pause(2.0)

    show fleur_dim sorry parted behind ilona_dim:
        xzoom 1 xcenter 850
    with dissolve

    fl "Edwin, are you okay? You look awfully pale."

    show uldin_dim closed talk
    ul "I apologise, I might have gone too far..."

    # Ilona turns to left (facing Edwin)
    show ilona_dim open:
        xzoom -1
    with dissolve

    show fleur_dim look neutral

    il "...Do you need any assistance?"

    show uldin_dim open relaxed neutral
    show edwin_dim closed talk
    ed "No, thank you, Ilona. And yes; Fleur, I think I may need to rest for the day. Please excuse me, my mind’s been all over the place."

    show edwin_dim glance grin
    ed "I should be back in full spirits by tomorrow."

    show uldin_dim talk
    ul "Very well. Eisleigh, if you may, show him to his room, please."

    show eisleigh_dim closed talk behind uldin_dim with dissolve:
        xcenter 1300

    ei "Of course."

    hide edwin_dim
    hide eisleigh_dim
    with dissolve

    # SCENE 8(EDWIN POV)

    scene bg door night light
    with fade

    play sound 'audio/sfx/wood door open.wav' volume 0.3
    "Eisleigh unlocks the door by the stairs and opens the guest room. She gives Edwin the key."

    scene bg bedroom night light
    with longfade

    show eisleigh_dim closed neutral at extra_left:
        xzoom -1
    with dissolve

    "Having separate sleeping quarters is more than Edwin could normally ask for. In this style of house, he had assumed that the guests share one large sleeping space."

    show eisleigh_dim open neutral with dissolve

    "He was prepared to run out of the manse, and to be alone in the darkness of night."

    "Instead, he has to play the role of an honoured houseguest."

    show eisleigh_dim smile with dissolve

    "Eisleigh bows and leaves him with only a few words of comfort, hoping that he will feel better with rest."

    "He nods and then closes the door, locking it with the key."

    hide eisleigh_dim with dissolve
    play sound 'audio/sfx/wood door close.wav' volume 0.3

    queue sound 'audio/ambience/dark forest.mp3' volume 0.1 fadein 3.0 noloop

    "The unexpected privacy given to him helps ease his mind and, feeling his skin cool, he wipes the cold sweat from his brow."

    "The chatter of the party is distant, and he has to strain his ears to listen."

    "Now, he is alone."

    show edwin_dim closed furrow at less_left with dissolve:
        zoom 0.5 xzoom-1

    "Edwin's towering frame lowers to the ground, and the floorboards creak slightly with his movement."

    "He kneels down by the bed, as though praying. It's as if he only now remembers how to breathe…"

    hide edwin_dim

    show bg black with fade

    ed "Lord, please have mercy on my soul…"

    ed "I want to believe that I am human, but the people won't accept me all the same. Am I allowed to surrender at last?"

    ed "If I were to end it… right here and right now. Wouldn’t that be spectacular?"

    ed "Hah. Hahah."

    scene bg bedroom night light
    show edwin_dim angry furrow laugh at center:
        zoom 0.9 yoffset 860

    extend " Ahahahahahahahahahahahahahhahah!"

    ed "Look at me, a husk of myself. Not even courage remains."

    show edwin_dim stare with dissolve
    ed "Pathetic. I should be better than this. Stronger than this."

    show edwin_dim stare yell with dissolve
    ed "What was the point of going through the trials of the military, otherwise?"

    ed "I’ve been through worse."

    show edwin_dim fury talk with dissolve

    ed "That day… I was brave, wasn’t I? I did save my sister from the werewolf attack, didn’t I?"

    play sound 'audio/sfx/Creepy Wind A.ogg' volume 0.3

    ed "(But did I really do it for her? Or did my thirst for blood take over…)"

    scene bg blood with fade

    ed "(A whiff of blood, and I’m running towards it…)"

    ed "(And he won't leave me alone since then. The Lord of the Forest, he calls himself.)"

    ed "(Penetrating my dreams ever since that day…)"

    ed "(And granting me the curse of the Wolfskin.)"

    "The Wolfskin; a sash of wolf pelt that sits on his waist with intricate designs, foreign to this land. Or to any land, for that matter."

    "The gold glistens, and the red… Well, the red reflects the sheen of madness that rests within."

    ed "(Only the insane ones are bestowed with this torment. Like I…)"

    scene bg bedroom night light
    show edwin_dim sad neutral at center:
        zoom 0.9 yoffset 860
    with fade

    stop sound fadeout 4.0

    ed "...What am I doing?"

    play music 'audio/music/mastered/He_Who_Seeks_Hope_Reprise.ogg' volume 0.7 fadein 1.0 noloop

    ed "Ilona told me once to hold onto hope… What’s done is done."

    ed "(But today was a disaster, how could I lose my composure? I was practically dripping with sweat. I know for a fact that Uldin must have noticed that. Sooner or later, I’m a dead man.)"

    ed "(And I will bring Ilona down with me.)"

    show edwin_dim angry talk furrow with dissolve

    ed "Ilona… my-my darling…"

    ed "I wish I could say these words to your face…"

    show edwin_dim angry

    ed "What a fool I am for having kept my affection a secret from you..."

    hide edwin_dim
    show bg moon with fade

    ed "(Because now…)"

    ed "(Now I don’t think I’ll get another chance to say what I want to say… I can feel the hysteria building up within me.)"

    ed "(Expanding like it’s never before. Rising, so far… Far, far away…from my control.)"

    ed "But I promise you this, Ilona:"

    scene bg bedroom night light
    show edwin_dim angry furrow neutral at center:
        zoom 0.9 yoffset 860
    with fade

    ed "I am not going to hurt you. I am going to do right by you. I am not going to hurt anyone who’s innocent."

    ed "It may seem the other way around, but whatever I do;"

    show edwin_dim fury furrow with dissolve

    ed "I will have a damn good reason for it."

    # SCENE 9

    stop music fadeout 3.0

    scene bg hall night
    with longfade

    show ilona_dim aaaa talk sweat at less_left:
        zoom 0.5
    show fleur_dim parted at extra_left behind ilona_dim:
        xzoom -1
    show eisleigh_dim glance small:
        xcenter 1300
    show uldin_dim angry smirk at extra_right:
        xzoom -1
    with dissolve

    "Ilona stayed after Edwin's exit to ask Uldin and Eisleigh about the nature of curses, but the conversation that followed was dense and difficult."

    play music 'audio/ambience/bbc fire.mp3' volume 0.2 fadein 2.0 noloop

    hide fleur_dim with dissolve

    "By that point, Fleur took her leave, no longer interested in the dry and tiring conversation at hand."

    show ilona_dim angry neutral
    show uldin_dim wink smirk
    with dissolve
    "Ilona tried her best to keep up. Uldin tried to challenge her with theories that needed to be formed on the spot and, at times, it turned into a messy debate."

    scene bg hallway night light
    with longfade

    "The rest of the party retired to bed before midnight."

    "When Salome entered, she became the mediator of peace and that was when everyone agreed to call it a night, departing from the main hall on friendly terms."

    show uldin_dim blush closed laugh:
        xcenter 1700
    show salome_dim pensive sad sweatblush behind uldin_dim:
        xcenter 1350
    with dissolve
    show ilona_dim annoyed glance blush at less_left:
        zoom 0.5 xzoom -1
    show eisleigh_dim grin worry at extra_left behind ilona_dim:
    with dissolve

    "Salome ushered a rather drunk Uldin back to bed. Eisleigh showed Ilona to the room that was prepared for her, and they bid each other a good night."

    scene bg door night light
    with fade

    play sound 'audio/sfx/wood door open and close.wav'

    "Ilona opens the door and wonders for a moment if she wants to lock it. Her head is swimming — either from the spiced wine or the meandering conversation."

    scene bg bedroom night light
    with longfade

    show ilona_dim pensive solemn at center with dissolve:
        zoom 0.5

    stop music fadeout 2.0
    play music 'audio/ambience/janbezo wind.ogg'

    il "(Ed… I wonder how he's doing. That conversation earlier really took a turn for the worse for him.)"

    "His room is on the right side of hers, and Kellac’s on the left."

    show ilona_dim closed
    "Ilona presses her ear up to the wall separating her and Edwin's room, but hears nothing from the other side."

    show ilona_dim pensive
    il "(Not a sound. He's probably asleep.)"

    scene bg bedroom night dark
    with fade

    il "(I should get some rest too, so we can both leave early tomorrow. The people here are kind, but there's too much risk if we stay… We have to keep moving.)"

    "She thinks of going to see him, to maybe knock on his door and to check up on him."

    "However, in the end she decides not to. Ilona can only trust him to be cautious. She could not continue to worry about him; it would make her restless…"

    play sound 'audio/sfx/zap clothes rustle.mp3' volume 0.1

    scene bg door night dark:
        xzoom -1
    with fade

    "Ilona wonders if she should leave her door unlocked, in case he wants to speak to her."

    "It seems risky, but Ilona is more than used to sleeping in a communal space in the priory… Having a private room feels like an excessive luxury."

    "Though, there are strangers in the house, and some of them are men…"

    "… Edwin would have wanted her door locked."
    play sound 'audio/sfx/lock metal.mp3'
    extend " She goes to the door and turns the key in the keyhole, hearing a reassuring click."

    scene bg bedroom night dark
    with fade

    "After a silent prayer, she crawls into bed. Lying there, she feels a sense of unease and restlessness, and also feels strangely awake."

    scene bg black
    with longfade

    "Ilona closes her eyes and tries to drift into sleep. Within the peaceful silence of the manse, rest comes to her easier than expected."

    stop music fadeout 3.0

    $ quick_menu = False
    # NOTE: Here is the huge turning point to the murder
    show bg fluffies with fade

    with logodissolve

    $ renpy.pause(2.0)
    $ quick_menu = True

    scene bg black with fade

    queue music 'audio/music/mastered/Death_Tolls.ogg' volume 0.4

    "The piercing sound of a howl wakes Kellac first, followed shortly by a woman's loud scream."
    play sound 'audio/sfx/Door_Slam.mp3'
    extend " His door opens with a slam, sensing something is incredibly wrong…"

    scene bg bedroom night dark
    with fade

    play sound 'audio/sfx/footsteps hurried.wav'
    "Ilona hears footsteps rush past her room, and her eyes flutter open; registering what woke her."
    play sound 'audio/sfx/zap clothes rustle.mp3' volume 0.2
    extend " She puts on her habit, covering her head, and hurries out the door."

    scene bg hallway night dark
    show kellac_twilight glance anger at center:
        zoom 0.7 yoffset 380
    with dissolve

    "Kellac stops on the stairwell when he sees her, turning his head back to see Ilona. Edwin is not with him. She looks to the door next to hers, on the right."

    show kellac_twilight yell with dissolve
    ke "There's no time to lose! See if you can wake him up, I'm going on ahead!"

    play sound 'audio/sfx/stairs ascending hurried.wav' fadeout 1.0
    hide kellac_twilight with dissolve

    "He runs up the stairs. For a man who always seems so weary, there is a vivacity in his face now that danger is present."

    scene bg door night dark
    with fade

    play sound 'audio/sfx/3 knocks.wav' volume 0.4

    "Ilona knocks on Edwin's door, listening for any sign of life in the room."

    show ilona_twilight sad talk at center:
        zoom 0.7 yoffset 260
    with dissolve

    il "Edwin? It's Ilona!"

    "Silence."

    play sound 'audio/sfx/knockers.wav'
    show ilona_twilight annoyed neutral with dissolve

    "She knocks again, this time urgently. Still, there is nothing coming from the other side of the room."

    play sound 'audio/sfx/zap door handle movement.mp3' volume 0.2
    "She turns the handle. The door is locked, and there is no reply…"

    show ilona_twilight shock sad talk with dissolve
    il "No… Please, no…"

    # SCENE 10
    scene bg hallway night dark
    with fade

    "Ilona feels her heart lurch."

    play sound 'audio/sfx/stairs ascending hurried.wav' fadeout 2.0
    "She stumbles up the stairs, finding Kellac at the door to what seems to be the master’s chambers."

    scene bg master door night
    with fade

    play sound 'audio/sfx/knockers.wav'

    "He knocks urgently, and tries ramming the door with his shoulders, but grunts when the door wouldn't budge."

    show kellac_twilight anger closed grimace sweat at center:
        zoom 0.7 yoffset 380

    ke "It's no use! Damn it! If only I was stronger…"

    show kellac_twilight glance talk
    ke "I'm going to get Anari! Something's wrong."

    scene bg hallway night dark
    with fade

    show ilona_twilight annoyed at left:
        zoom 0.5
    show kellac_twilight anger talk at right:
        zoom 0.5 xzoom -1
    with dissolve

    ke "The servants' quarters are on the other side of the house, up the stairs. Get a master key for this door!"

    play sound 'audio/sfx/footsteps hurried leather tile.wav'
    hide kellac_twilight with dissolve
    hide ilona_twilight with dissolve

    show bg black with fade

    "Ilona nods and follows Kellac's instructions, passing through the now empty hall and up the stairs."

    scene bg hallway night dark
    show ilona_twilight annoyed talk at left:
        zoom 0.5
    show eisleigh_twilight neutral at right
    with fade

    "She finds Eisleigh first, and explains the situation."

    show eisleigh_twilight surprise worry
    show ilona_twilight neutral
    "Eisleigh's eyes go wide and she fumbles in her long green robe, producing a dangling set of keys and nearly dropping them in her haste."

    show eisleigh_twilight surprise worry talk
    play sound 'audio/sfx/old keys jingle.mp3' volume 0.2
    ei "I- I have a copy of the master key. Come on! There's no time to waste!"

    stop music fadeout 3.0
    scene bg master door night
    with longfade

    $ renpy.pause(1.0)

    play sound 'audio/sfx/stairs ascending hurried.wav'

    "When they rush back to the masters' chambers, they realize there is no use for the master key. They find the door broken and battered, but no sign of Anari or Kellac yet."

    scene bg gore
    with fade

    $ renpy.pause(1.0)

    play music 'audio/ambience/Dark Ambience.ogg' volume 0.4

    "Traces of blood are on the door, with thick shards of wood splintering from its fractures."

    scene bg masters chamber night
    with fade

    play sound 'audio/sfx/footsteps slow leather tile.wav'

    "Ilona and Eisleigh enter the bedroom, stepping over part of the broken door. It smells strongly of blood and burnt hair."

    show ilona_twilight shock sad neutral at less_left:
        zoom 0.5
    show eisleigh_twilight fear worry talk at extra_left behind ilona_night:
        xzoom -1
    with dissolve

    "They lay their eyes on the blood-soaked bed sheets and the lifeless figure of Uldin."

    "His neck is mutilated; torn flesh hangs off of his body, and his eyes are blank."

    show eisleigh_twilight closed worry neutral
    "Eisleigh holds a hand over her mouth, and squeezes her eyes shut."

    "A figure of a man is hunched over a woman in a dress and makes his presence known. He turns to look at them."

    "His yellow eyes give off an eerie glint, as though it were an animal's."

    # Use longdissolve to make Edwin appear slower in scene
    show edwin_twilight distant wolf at extra_right:
        zoom 0.5
    with longdissolve

    play music 'audio/music/mastered/Wail_Of_The_Moon.ogg' volume 0.3 fadein 2.0

    il "Edwin…"

    # Ilona moves closer towards Edwin
    show ilona_twilight:
        ease 1.0 xcenter 1000
    # Edwin turns around
    show edwin_twilight stare yell furrow wolf:
        xzoom -1

    ed "Don't come any closer! Stay away…"

    " It's hard to make out in the darkness, but his arms look huge, and beastly… the fur mixed with the blood of open wounds and bruises."

    "With his body turned away, Ilona can’t tell who is in his arms, but she now sees a ring on his hand and chestnut brown hair…"

    play sound 'audio/sfx/footsteps hurried tile trainers.wav'

    "The sound of footsteps is heard again and Ilona knows immediately who it is."

    scene bg hallway night dark
    show anari_twilight fury scary yell kill at center:
        zoom 0.7 yoffset 220
    with dissolve

    stop sound

    an "Get away from him, Ilona!"

    show anari_twilight cringe sweatdrop with dissolve
    an "I knew there was something wrong with him. I should've shot him dead when I had the chance…"

    "This is not the cool and elegant Anari that Ilona had seen before. Instead, she disguises her sorrow with fury instead."

    scene bg masters chamber night
    show kellac_twilight anger at easeinleft_transform:
        zoom 0.8 yoffset 500

    play sound 'audio/sfx/footsteps hurried leather tile.wav'
    "Ilona can’t move. With Anari's arrow trained on them, Kellac rushes in; carrying a healer's kit."
    stop sound

    "Edwin sets the body of the woman down and backs away. Kellac checks the unburned section of her wrist."

    show kellac_twilight closed grimace  with dissolve
    "There is only the sound of Kellac choking back his frustration and dismay."

    show kellac_twilight talk  with dissolve
    ke "I was too late… I'm so sorry… I couldn't save them."

    # SCENE 12 + 13

    hide kellac_twilight with dissolve

    "Kellac is on his knees, facing Salome's corpse."

    "All the jovial cheer that he displayed since meeting Ilona vanishes, and he resembles a husk of a man."

    # Anari moves to the right slightly
    show anari_twilight kill scary angry neutral at easeinleft_transform:
        zoom 0.5 xzoom -1
    play sound 'audio/sfx/footsteps slow trainers.wav'
    "Anari moves in after seeing that Edwin shows no signs of retaliation."

    stop sound
    an "We need to restrain him. Fleur's gone missing…"

    # Edwin turns to left
    show edwin_twilight distant talk wolf at extra_right:
        zoom 0.5 xzoom 1
    with dissolve

    ed "I didn't do it… I wasn't the one who did this."

    show anari_twilight smile with dissolve
    an "An honest man would beg harder for his life. You sound like you've already accepted your execution."

    # Ilona turns to left
    show ilona_twilight sad talk at center with dissolve:
        zoom 0.5 xzoom -1

    il "Wait! Please give us a minute. I… I want to talk to Edwin."

    show anari_twilight neutral
    an "…Fine. One minute, and no more. I'm sure you wouldn't be so stupid as to try anything… but be warned."

    scene bg masters chamber night with dissolve
    show edwin_twilight wolf distant at right:
        zoom 0.8 yoffset 600
    with dissolve

    $ renpy.pause(1.0)

    play sound 'audio/sfx/footsteps slow leather tile.wav' volume 0.7
    # Ilona turns to right and moves towards Edwin (close enough to touch him)
    show ilona_twilight pensive solemn at easeinleft_transform:
        zoom 0.85 yoffset 400

    $ renpy.pause(1.0)

    stop sound

    "Ilona crouches down beside Edwin. His distant gaze lacks warmth and familiarity."

    show ilona_twilight sad talk with dissolve
    il "Edwin, can you hear me?"

    show edwin_twilight yell stare with dissolve
    ed "…"
    $ renpy.pause(2.0)
    show ilona_twilight closed with dissolve
    il "Ed…"
    $ renpy.pause(3.0)
    show edwin_twilight sad talk with dissolve
    ed "I-I am so sorry, Ilona. I wasn't able to control it… "

    "Hearing him talk reassures her slightly. Ilona gingerly takes his wolf-like hands into hers. Even though his gaze is cold and stony, the hands still hold warmth."

    show ilona_twilight open
    il "Do you swear that you didn't kill them?"

    show edwin_twilight talk with dissolve
    ed "When I entered the room, they were already like this."

    show ilona_twilight talk
    il "Then— You weren't the one—"

    show ilona_twilight sweat pensive neutral with dissolve
    il "Something's wrong. Your hands… they're not turning back—"

    an "Stop — time's up."

    play sound 'audio/sfx/Letting_go_of_your_totally_non-romantic_partners_hand_because_someone_just_saw_you.mp3' volume 0.7

    # Ilona turns left (facing Anari)
    show ilona_twilight:
        xzoom -1
    with dissolve

    stop music fadeout 3.0

    "Anari's voice is enough to cut the two apart, and Ilona lets go of Edwin's hands immediately."

    scene bg masters chamber night with dissolve
    show anari_twilight angry scary neutral bow at center:
        zoom 0.7 yoffset 240
    with dissolve

    an "I can't say that I trust you quite yet, Ilona."

    show anari_twilight open smile with dissolve
    an "You seem like a clever girl... and who would dare suspect a nun of planning such a gruesome scene?"

    show anari_twilight neutral
    an "Turn yourself in quietly, Edwin, and I'll make sure her interrogation isn't painful."

    hide anari_twilight with dissolve

    play sound 'audio/sfx/zap chain move.mp3' volume 0.2 fadeout 7.0
    stop music fadeout 2.0
    "Ilona isn't sure if Edwin obliged so easily because he feared for her safety, or if he truly has given up, like Anari said earlier. He wordlessly lets Anari bind him with chains."

    $ renpy.pause(2.0)

    ## MANSE
    scene bg chapel night
    with longfade

    play sound 'audio/sfx/footsteps slow trainers.wav'
    "Anari escorts him forcefully out of the mansion, and takes him underground to a dungeon."

    ## DUNGEON
    scene bg dungeon
    with fade
    extend "\nThe only thing Ilona sees before the doors close is Edwin's taciturn and listless expression."

    play sound 'audio/sfx/metal door.wav' volume 0.7

    show edwin_twilight wolf distant at center:
        zoom 0.5
    with longdissolve


    # TRANSITION TO SCENE 14 + 15

    ## TOWN PLAZA

    scene bg town plaza night
    with longfade

    "With Edwin locked away, the remaining members of the party gather in the town square: Ilona, Eisleigh, Kellac and Anari."

    show ilona_night sad pensive at less_left:
        zoom 0.5
    show kellac_night at extra_left behind ilona_night:
        zoom 0.5
    show eisleigh_night neutral at less_right behind anari_night:
    show anari_night look neutral at extra_right:
        zoom 0.5
    with dissolve

    "Nobody could find Fleur in the manse afterwards, her room and bed empty of her presence."

    "The sun has not risen yet, and the clouds are dark and looming. There's a damp chill in the air."

    queue music 'audio/ambience/wind and trees.ogg' volume 0.3 fadein 2.0

    show eisleigh_night closed worry
    ei "What now?"

    show anari_night angry
    an "It's obvious that Edwin is guilty… but I'm not sure what to do with the nun."

    show kellac_night anger talk
    ke "Don't be hasty, Anari. There's a lot we don't know yet."

    ke "Besides, I'm certain I was the first one to wake up. I didn't see Ilona do anything suspicious."

    show eisleigh_night talk
    show kellac_night neutral
    with dissolve
    ei "That matches up with what I saw of her. It just doesn't seem like something Ilona would do from what I know of her..."

    an "What? You think she would let you in on her plots in one night?"

    show eisleigh_night open grin
    ei "…That's precisely it. She's awful at keeping secrets."

    show eisleigh_night neutral with dissolve
    ei "If she really was involved, I don't think she would be able to hide it."

    show anari_night closed sweatdrop
    "Anari tries hard to not grumble, though Eisleigh does have a point."

    show anari_night look talk -sweatdrop
    an "Ilona. Did you know that the man was a werewolf before entering this town?"

    play music 'audio/music/mastered/Administer_Justice_Instrumental.ogg' volume 0.3 fadein 2.0 noloop

    show ilona_night talk
    il "…Yes. In my presence, he's more capable of controlling his transformation."

    show anari_night cringe with dissolve
    an "And yet you've been harbouring a monster, regardless of the consequences? Unfathomable…"

    show ilona_night closed neutral with dissolve
    il "I am searching for a way to cure him of his curse. That is all."

    show ilona_night open aaaa with dissolve
    il "Please, I honestly don't think he did it. There must be more to what happened - I can help you find it."

    show kellac_night glance sweat
    ke "The town needs to know, we can't hide this for long. Not to mention, Fleur is still missing."

    show kellac_night talk
    ke "As long as we keep an eye on Ilona as she investigates, I think it should be safe."

    show anari_night open neutral
    show kellac_night neutral
    with dissolve
    "Anari sighs at Kellac's advice. Ilona can't help but to be thankful for his ability to sway Anari's opinions for even just a moment."

    show anari_night relaxed neutral with dissolve
    an "Fine. Let her run around, just make sure someone keeps an eye on her, always."

    an "I'll go first. You two assemble a search party for the forest in the meantime. I'll lead the search once you're ready."

    show anari_night scary talk with dissolve
    an "Ilona. You have until sundown. Prove that Edwin is innocent, or I'm going to personally make sure you won't like what’s coming to the two of you."

    # Go to act 2.
    jump act2
