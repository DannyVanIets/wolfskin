## The file for act 1.

## moving sprites are a pain
define midleft= Position(xpos=0.40)

label act1:

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

    show ilona neutral at left with dissolve:
        zoom 0.50 xpos 100

    $ renpy.pause(1.0)

    il "We should think of finding shelter soon, before it gets too dark."

    show ilona shy

    "Ilona waits for Edwin to turn back into a human, closing her eyes to rest for a moment. There's only the sound of the forest, until Edwin speaks to break their silence."

    show edwin anxious at right with dissolve:
        zoom 0.50 xpos 1.0

    ed "I know that I'm asking for too much, but despite everything that's happened… would you please stay with me?"

    show ilona fear

    il "What? Edwin, please, calm down-"

    show edwin sad

    ed "... Ilona I-I can’t. Not in a situation like this..."

    il "You’re right, but I need you to slow down. I can’t keep up with you and that is only going to make us look all the more suspicious."

    ed "..."

    show ilona pensive

    il "We have only each other to rely on."

    show edwin annoyed

    "As she says this, she places her hands over his. His hands are abnormally cold to touch. Ilona learned this was a sign of his transformation."

    "Even so, she must remain with him."

    "The moonlight beams over them, slightly wavering with each breath they take."

    show ilona shy

    il "(If only the moonlight would never leave us. We should rest here for a while.)"

    il "Edwin…"

    ed "…"

    show ilona uwu

    il "Ed…"

    show edwin chuckle

    ed "Yes, I’m here. Please forgive my wandering mind."

    show ilona happy

    show edwin smirk

    ed "...What could I ever do without you? I feel like I have never thanked you for-"

    il "You have thanked me more than enough already, Edwin. I appreciate it… but let's not dwell on it any further. "

    show ilona pensive

    show edwin neutral

    "Their eyes flicker for a moment, and he’s not shivering anymore. "

    scene bg road
    with longfade

    "Eventually, they press on. They sight a lonely settlement on the horizon; stone walls surrounding its perimeter."

    show edwin smirk at right with dissolve:
        zoom 0.50

    ed "Heh…"

    show edwin anxious

    ed """
    I haven't felt like m-myself lately, since the incident back at the priory. Try as I may to blend in, to do good and keep myself in check… I am a beast, through and through.

    What is it that we've done wrong? Is us being together something so heinous? Is my existence such a sin?
    """

    show ilona sad with dissolve:
        zoom 0.50 xpos 50

    il "I know..."

    show edwin annoyed

    ed """
    I did not know the extent of the hatred that lay within their souls until that night… to go as far as to burn me alive…

    Is there something wrong with me, Ilona? I'm always on edge, fearing for our lives… I never meant to put you through this.
    """
    show ilona pensive

    il """
    If you want my answer as a former nun… You and I have sinned.

    You said that you were a beast, through and through.

    You're not. You’re-
    """

    hide ilona

    hide edwin

    "Edwin immediately lets go of her hand, intertwined seconds ago, but now balled into a fist. The rustling of dry leaves brought with it a heavily armed guard and an archer under a cloak. "

    unk """
    That's enough loitering around the town wall looking suspicious, don't you think?

    I've been observing your movements from the battlements for a while now. Be grateful that the town master wishes to have a meeting with you, or else I would have already pierced you with my arrows.
    """

    show edwin serious at right with dissolve:
        zoom 0.50 xpos 1.0

    ed "But, we-"

    show ilona annoyed with dissolve:
        zoom 0.50 xpos 0.75 xzoom -1

    il "May we ask, to what purpose do we owe this pleasure?"

    unk """
    Sister, all I know is that the master called you. I sighted a nun and a man outside the town walls and informed him of this.

    I can tell your legs are shaking even from here… so make sure to comply obediently and I won't ask any difficult questions about you in return.
    """

    ed "She simply asked what business the master has with us. You're acting very feisty for someone who didn't even have the decency to introduce herself."

    unk "Hmph. Fair enough."

    an """
    My name is Anari. Happy now?

    I'm not going to probe you or anything. You may be outsiders, but you look like decent enough folk. No need to come up with any grand excuses for why you’re here.

    So, let’s get back to it. Will you accept the town master's call?
    """

    show ilona annoyedtalk with dissolve:

    il "...I suppose that choice is not truly much of one. I accept."

    show ilona annoyed

    an "A wise judgement. You’re clever for a nun, but you should learn to keep your dog in line."

    show edwin fear

    ed "...Excuse me?"

    an "I don’t appreciate being called ‘feisty’."

    show edwin anxious

    ed "I meant no offense when I said that. My apologies."

    an "So you do have manners; it would do you well to keep them. Let’s get moving, then. I’ll escort you to the manse. "

    """
    Anari takes the position of rear guard, as the other guard leads the way forward. Ilona glances back, just once. Anari's bow is by her side and a hand rests on the quiver, ready to fire if the two of them even thought of escaping.

    Ilona cannot help but wonder just how much Anari overheard of their conversation... Her arrival seemed too well-timed. Did they give away too much, even when they thought they were alone?

    She glances at Edwin, his face inscrutable. And so, they enter the gates.
    """

    ed """
    (When was the last time I felt any hope? Anything besides pain? The swelling in my chest is excruciating…)

    (I truly wouldn't have made it this far on my own. Even if I hide what I am well, people can't help but to be suspicious.)

    (Although - a town full of people not trying to kill me yet is quite an improvement.)
    """
    "It’s almost time to head home for normal folk, but the town is bustling. There's a large bonfire in the square, and there's carved turnips at the doors of all the houses-"

    il "What kind of decorations are these?"

    ed "It’s for... All Hallows’ Eve, a celebration to commemorate the dead."

    il "You mean All Saints’ Eve? Why are the townsfolk celebrating in joy, then?"

    ed "You were raised strictly, Ilona. Father Ivanov never wanted you to know about these pagan festivals."

    ed "Oh!-"

    unk "Young lad, please watch your step. One mistake and this weary old man is done for…"

    ed "I’m so sorry for bumping into you, sir-"

    an "...Kellac, we're the same age."

    ke "Fancy meeting you here, Anari. I didn’t know you like to take strolls. I never knew you had friends either! And who may you be, dear sister?"

    ed "Uh, I’m not sure about that…"

    ke "Pleased to make your acquaintance, anyhow. I’m Kellac, Anari and I go way back."

    an "That we do, and I regret it."

    ke "You’ve just got to love that personality! Don’t take her too seriously, she's always been like that."

    ed "I see… I'm Edwin. Pleased to make your acquaintance. "

    il "As am I. My name is Ilona. Forgive my ignorance, but are you the master of this town?"

    ke "Me? Sorry, but no. I'm just the physician and herbalist. Did the master summon you?"

    il "He did, but I don't know what business we have with him..."

    ke """
    Aha. I should have expected as much; Anari has a habit of leaving out the details and jumping straight to the point.

    I should get going, but we're bound to see each other again soon. Keep well, Anari.
    """

    "Anari only nods curtly, and the group moves along. Further into the town, they find a large house made of timber and stone."

    "Edwin wonders, how should they go about this? It’s best they wait and see what happens once they enter."

    # Go to act 2.
    jump act2
