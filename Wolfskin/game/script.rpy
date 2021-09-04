# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define il = Character("Ilona")
define ed = Character("Edwin")
define an = Character("Anari")
define fl = Character("Fleur")
define ke = Character("Kellac")
define ei = Character("Eisleigh")
define sa = Character("Salome")
define ul = Character("Uldin")

# Hold at black for a bit.
define fadehold = Fade(0.5, 2.0, 0.5)

# long fade
define longfade = Fade(1.5, 0.0, 1.5)

style say_label:
    outlines [ ( 0, "#000000", 1, 1) ]

style say_dialogue:
    outlines [ ( 0, "#000000", 1, 1) ]

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg black
    with fade

    centered "I am lost. {p=0.8}Pray, that I shall find my path.{p=0.8}Pray, that I shall not lose heart.{p=0.8}Let me see, for who I really am.{p=0.8}This, the only wish I have.{p=0.8}{p=0.8}Before I’ve wronged,{p=0.8}So far gone."

    scene bg forest night
    with fadehold

    play music 'audio/ambience/bbc woods night.mp3' volume 0.01

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

    "The moonlight beams over them, slightly wavering with each breath they take. Ilona wishes that the moonlight would never leave them... it’s best if they rest here for a while."

    il "Edwin…"

    ed "…"

    il "Ed…"

    ed "Yes, I’m here. Please forgive my wandering mind."

    ed "...What could I ever do without you? I feel like I have never thanked you for-"

    "His eyes flicker for a moment. Eventually, they press on. They sight a lonely settlement on the horizon; stone walls surrounding its perimeter."

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
    If you want my answer as a former nun… You and I have sinned. But I’ve never met someone in this world who is not free from sin.

    I’ll shoulder the blame with you. I’ll find a cure.

    You said that you were a beast, through and through.

    You're not. You’re-
    """

    "Edwin immediately lets go of her hand, intertwined seconds ago, but now balled into a fist. The rustling of dry leaves brought with it a heavily armed guard and an archer under a cloak."

    # This ends the game.

    return
