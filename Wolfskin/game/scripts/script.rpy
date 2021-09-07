# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define il = Character("Ilona", ctc="ctc_anchored", ctc_position="fixed")
define ed = Character("Edwin", ctc="ctc_anchored", ctc_position="fixed")
define an = Character("Anari", ctc="ctc_anchored", ctc_position="fixed")
define fl = Character("Fleur", ctc="ctc_anchored", ctc_position="fixed")
define ke = Character("Kellac", ctc="ctc_anchored", ctc_position="fixed")
define ei = Character("Eisleigh", ctc="ctc_anchored", ctc_position="fixed")
define sa = Character("Salome", ctc="ctc_anchored", ctc_position="fixed")
define ul = Character("Uldin", ctc="ctc_anchored", ctc_position="fixed")
define unk = Character("???", ctc="ctc_anchored", ctc_position="fixed")
define narrator = Character(name=None, ctc="ctc_anchored", ctc_position="fixed")

# CTC SHENANIGANS

image ctc_anchored:
       "ctc.png"
       yalign 0.93 xalign 0.96 #Adjust these numbers to fit your own textbox
       linear 0.95 alpha 1.0
       linear 0.85 alpha 0.0
       repeat

# Hold at black for a bit.
define fadehold = Fade(0.5, 2.0, 0.5)

# long fade
define longfade = Fade(1.5, 0.0, 1.5)

style say_label:
    outlines [ ( 0, "#000000", 2, 2) ]

style say_dialogue:
    outlines [ ( 0, "#000000", 2, 2) ]

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg black
    with fade

    # Edwin's monologue for the intro in NVL mode
    define nvlNarrator = Character(None, kind=nvl, what_font="CrimsonText-Regular.ttf", what_size=43)

    # NVL mode: Edwin's monologue
    $ quick_menu = False

    window hide

    nvlNarrator """
    I am lost.

    Pray, that I shall find my path.

    Pray, that I shall not lose heart.

    Let me see, for who I really am.

    This, the only wish I have.

    \nBefore I’ve wronged,

    So far gone.
    """

    nvl clear

    $ quick_menu = True

    # Switch to AVD mode.

    scene bg forest night
    with fadehold

    $ renpy.pause(2.0)

    show ilona neutral at left
    with dissolve

    $ renpy.pause(1.0)

    il "We should think of finding shelter soon, before it gets too dark."

    "Ilona waits for Edwin to resume human form, closing her eyes to rest for a moment. There's only the sound of the forest, until Edwin speaks to break their silence."

    ed "Will you please stay with me?"

    il "What? Edwin, please, calm down-"

    ed "... Ilona I-I can’t. Not in a situation like this..."

    il "You’re right, but I need you to slow down. I can’t keep up with you. Moreover, it’s imperative that we don’t look suspicious."

    ed "..."

    il "We have only each other to rely on."

    "As she says this, she places her hands over his. His hands are abnormally cold to touch. Ilona learned this was a sign of his transformation."

    "Even so, she must remain with him."

    "The moonlight beams over them, slightly wavering with each breath they take."

    "She wishes that the moonlight would never leave them... it’s best if they rest here for a while."

    il "Edwin…"

    ed "…"

    il "Ed…"

    ed "Yes, I’m here. Please forgive my wandering mind."

    ed "...What could I ever do without you? I feel like I have never thanked you for-"

    "His eyes flicker for a moment."

    scene bg road
    with longfade

    "Eventually, they press on. They sight a lonely settlement on the horizon; stone walls surrounding its perimeter."

    ed """
    Heh…

    I-I’ve not been myself lately, ever since the incident back at the priory. Tell me, what is it that we’ve done wrong? Is us being together such a bother? You, a nun, and I...

    I understand what I am, a beast through and through. But is that really sin? I’ve always done my best to keep in check, t-to blend and do some good…
    """

    il "I know..."

    ed """
    And that fateful night, lord… I did not know the extent of the hatred that lay within their souls… to go as far as to burn me alive…

    Is there something wrong with me, Ilona? I-I’m so sorry that I’m putting you through this. I’ve been fearing for our lives, always on high alert-
    """

    il """
    If you want my answer as a former nun… You and I have sinned.

    But I’ll shoulder the blame with you. I’ll find a cure.

    You said that you were a beast, through and through.

    You're not. You’re-
    """

    "Edwin immediately lets go of her hand, intertwined seconds ago, but now balled into a fist. The rustling of dry leaves brought with it a heavily armed guard and an archer under a cloak."

    unk "You two have been lingering outside the town wall for a while. No matter, the master of the town expects your attendance at once."

    ed "No, we-"

    il "May we ask, to what purpose do we owe this pleasure? Also, {w=1.0}who are you?"

    unk """
    Sister, all I know is that the master called you. We sighted a nun and a man outside the town walls and informed him of this. From the looks of it, you are in a conspicuous situation. Your legs are trembling.

    It would be best to oblige.
    """

    ed "She simply asked who you are, and what business the master has with us. That’s all, there’s no need to get all feisty."

    unk "Hmph. Fair enough."

    an """
    My name is Anari.

    I could ask you both a bunch of questions. You are not from here, that’s for sure. Now, I’m not going to probe you or anything, because you both look like relatively decent folk. No need to come up with any grand excuses for why you’re here.

    So, let’s get back to it. Will you accept the Master of the town’s call?
    """

    il "...I suppose you won’t give us any other option. Very well, I accept."

    an "A wise judgement. You’re clever for a nun, but you should learn to keep your dog in line."

    ed "...Excuse me?"

    an "I don’t appreciate being called ‘feisty’."

    ed "I meant no offense when I said that, truly. My apologies."

    an "So you do have manners; it would do you well to keep them. Let’s get moving, then. I’ll escort you to the manse. "

    "Anari takes the position of rear guard, as the other guard leads the way forward. Ilona glances back, just once. Anari's bow is by her side and a hand rests on the quiver, ready to fire if the two of them even thought of escaping."

    "She wonders just how much Anari overheard of their conversation... Her arrival seemed too well-timed. Did they give away too much, even when they thought they were alone?"

    "Ilona glances at Edwin, his face inscrutable. And so, they enter the gates."

    # This ends the game.

    return

    # Go to the credits.
    jump credits_from_script
