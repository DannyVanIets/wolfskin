## The file for act 3.
 # I should not be doing this at 6:24AM
 # The Final Canopy

transform ilona_final_canopy:
    zoom 0.75
    xpos 240
    yoffset -100

transform edwin_final_canopy:
    zoom 0.75
    xpos 420
    yoffset -100

label act3:

    # Show the intro of the act.
    # Makes sure that skipping is stopped, also autosaves.
    $ renpy.choice_for_skipping()

    $ quick_menu = False

    window hide

    scene bg fluffies
    with fade

    call screen intro(3)

    $ quick_menu = True

# SCENE 35-39

    play music 'audio/music/He Who Seeks Hope - Theme Of Edwin -.ogg' fadein 5.0 volume 0.5

    scene bg moon with dissolve

    ed "I retired to my bedroom after Uldin's story about the werewolf attack. I couldn't take much more of it. After that, I fell into a deep and dreamless sleep."

    ed "I first noticed the wolfskin was gone when I heard the scream. The faint scent of perfume made me think it must have been Salome's doing."

    scene bg bedroom night dark
    with dissolve

    il "Did you hear me knocking on your door?"

    show edwin_night wolf sad neutral at center with dissolve:
        zoom 0.5

    ed "I didn't know if you were alone — I heard Kellac's voice on the other side. I kept quiet knowing I couldn't risk opening the door with my arms transformed."

    scene bg hallway night dark with dissolve

    il "So, when Kellac and I left to seek help, you moved to the master bedroom."

    ed "Yes. If the wolfskin had been taken, it surely would be there. I was only thinking of saving my own life."

    $ renpy.pause(1.0)

    scene bg master door night with fade

    stop music fadeout 2.0

    ed "When I broke down the door, Salome was on the ground, barely conscious anymore. The room was full of smoke and ash. She still had some lycan features: fangs, and claws… "

    scene bg masters chamber night with dissolve

    show bw_sa_murder at center:
        zoom 0.7 xzoom-1
    with dissolve

    ed "Her voice was thin, high and frail. Her body seemed so small. I've never seen burns that horrible."

    ed "I asked to have the wolfskin back, but she ignored my plea. With the last of her strength, she begged me to kill her."

    "Ilona remains silent for a long while. The fatigue is starting to set in, and she feels ready to crumble."

    il "How did you do it? Kellac ruled her death as complications from her burn wounds."

    scene bg black
    show bw_sa_murder at center:
        zoom 0.7 xzoom-1
    with dissolve

    ed "I tried to think of the most merciful way to give her peace. I truly did pity her - we suffered the same curse, and I felt my sorrow in her."

    hide bw_sa_murder with fade

    $ renpy.pause(1.0)

    play sound 'audio/sfx/zap bone break.mp3' volume 0.2

    scene bg gore with dissolve

    $ renpy.pause(2.0)

    play music 'audio/ambience/dark forest.mp3' volume 0.2 fadein 4.0

    ed "I held her close and crushed the bones in her neck, hoping for an instant death."

    il "You're certain you killed her? She wasn’t already dead before that?"

    ed "When a bearer of the wolfskin dies, they revert to human form. She no longer had any bestial features when I was done."

    il "And as you searched for the wolfskin, we found you."

    ed "Yes. How you found it in the chest in Salome's room, I don't know."

    stop music fadeout 3.0

    "Ilona and Edwin fall silent. Even though he had killed Salome, he was not the one who orchestrated the murder on Uldin."


    play music 'audio/music/Echoing - Theme Of Fleur -.ogg' volume 0.1

    scene bg forest day
    with dissolve

    $ renpy.pause(1.0)

    scene bg forest sunset
    with longdissolve

    $ renpy.pause(1.0)

    show lost_fl at center:
        zoom 0.7 xzoom-1
    with dissolve

    il "Fleur still hasn't been found. People fear she's actually been kidnapped, or taken by the fae."

    scene bg black
    show lost_fl at center:
        zoom 0.7 xzoom-1
    with dissolve

    ed "Do you think that could be the case?"

    il "Her location was not accounted for during or after the murder. Part of me believes she's more than just a witness."

    ed "Then you believe her to be an accomplice… Or, if she were the murderer… Hmm…"

    "Edwin considers this for a moment."

    ed "If she wore the wolfskin, perhaps."

    show effigy at center:
        zoom 0.7 xzoom-1
    with longdissolve

    ed "But if she truly is lost, she'd be suffering the same consequences as I did. It's excruciating to go through."

    ed "When I was first given the wolfskin, I foolishly tried to part with it and leave it behind. In retribution for not heeding the curse, I was left howling in pain."

    scene bg gore
    show lost_fl at center:
        zoom 0.7 xzoom-1
    with longdissolve

    ed "If she's still missing and guilty, she'd need to have incredible fortitude to remain silent for such a long time."

    il "Then maybe Fleur was just an accomplice — unwillingly, perhaps? I strongly believe that she helped Salome."

    ed "That's probably the safest assumption, until she is found."

    stop music fadeout 2.0

    scene bg dungeon
    show edwin_dim distant:
        zoom 0.6 yoffset 20 xpos 800
    show ilona_dim pensive sad at left:
        zoom 0.6 yoffset 20 xpos 200
    with longfade

    il "If only we had been honest and asked to stay together…"

    show edwin_dim fury yell furrow with dissolve
    ed "No. Had they sought the wolfskin while we were together, they might have killed you to get their hands on it. It would have been just as easy to frame me for that."

    ed "This may have been for the best."

    show ilona_dim talk
    show edwin_dim neutral
    with dissolve
    il "Let's not think about that now. I'm as involved in this as you are, regardless."

    show ilona_dim neutral
    show edwin_dim sad talk
    with dissolve
    ed "Ilona, listen to me. The people here… They appreciate you. I meant to bring this up in the morning, when we saw each other again."

    show edwin_dim fury with dissolve
    ed "You… You should stay here. Let them dispose of me. Live, and survive."

    show ilona_dim aaaa yell open tears with dissolve
    il "And watch you {i}die{/i}? Do you really think I would be happy with something like that?"

    show edwin_dim distant -furrow
    show ilona_dim talk
    with dissolve
    ed "I'm going to get what's coming to me, sooner or later."

    show edwin_dim angry furrow
    ed "Your hurt and pain will heal. You can recover. If you're with me, you won't be able to walk a righteous path. But if you leave me here, at least one of us will survive."

    play music 'audio/music/Ilonas_Theme_backing.mp3' volume 0.3 fadein 2.0

    show ilona_dim cry talk
    show edwin_dim neutral
    with dissolve
    il "Enough! I was well aware of the consequences when I left the priory with you!"

    show ilona_dim baby yell
    il "I'm not trying to find a way to break your curse so I can return to the priory, or to repent for my sins."

    show ilona_dim wail with dissolve
    il "I'm doing it so we can live together without the constant fear of being hunted down!"

    show edwin_dim fear -furrow blush talk
    show ilona_dim talk
    with dissolve
    ed "I-Ilona… You really want…"

    show ilona_dim open neutral sad
    with dissolve
    il "I can't do that if you offer yourself up to be killed."

    "Edwin goes to reach for her face, but pauses."
    show edwin_dim sad smile:
        ease 0.7 xpos 740
    " He slips off his glove first, and brushes away Ilona's tears with his thumb."

    show edwin_dim anxious grin with dissolve
    ed "Then we need to survive and break the curse. We'll travel to my homeland, and you can meet my family. We'll live in a valley by a lake, and you… you won't have to feel lonely ever again."

    show edwin_dim sad smile
    show ilona_dim cry baby happy
    with dissolve
    "He smiles warmly at her. Her tears subside as he wipes them away. She touches the hand at her cheek, finally laughing lightly at his comment."

    show ilona_dim glance smile blush with dissolve
    il "Let's not get ahead of ourselves yet. We need to figure out a plan first. Now that you have your wolfskin back, you could easily break through the chains… We could escape."

    show edwin_dim glance talk -blush with dissolve
    ed "It'll be difficult… but I can try. The walls are high, but I could scale them if I transform. If you could survey the town's layout looking for a part of the wall that could give me some footing, that would help us."

    show ilona_dim -blush neutral solemn with dissolve
    il "Understood. I should go — someone might be searching for me."

# SCENE 40
    hide edwin_dim
    hide ilona_dim
    with dissolve

    stop music fadeout 4.0

    play sound 'audio/sfx/zap chain move.mp3' volume 0.3

    $ renpy.pause(2.0)

    "Ilona ties the chains around Edwin again. His possession of the wolfskin should remain a secret until the time comes to escape, and he partially transforms to appear as he did before."

    play sound 'audio/sfx/metal door.wav' volume 0.4

    "Once confirming that nobody is at the door to the dungeon, she exits outside. The door to the dungeon shuts with a metallic groan."

    ## MANSE

    scene bg chapel
    with longfade

    play sound 'audio/ambience/wind and trees.ogg' volume 0.4

    "The wind howls, and she draws her nun's habit closer to her body. The ruins of the chapel loomed towards her, as though the remaining structure would threaten to collapse."

    show anari grin at center:
        zoom 0.7 yoffset 300
    with dissolve

    an "What are you doing here, Ilona? Praying for help now of all times?"

    hide anari with dissolve

    "Ilona's heart leaps when she hears Anari speak so suddenly."

    show ilona shock sweat at less_left:
        zoom 0.5
    show anari look at right:
        zoom 0.5
    with dissolve

    show ilona closed happy annoyed with dissolve
    il "…Indeed. I was praying for your success in finding Fleur. Are there any new leads?"

    show anari look grin
    an "No, but there's still time before sundown. We'll search the forest. I had to personally oversee another crucial job."

    show ilona pensive smile
    il "What might that be?"

    play music [ "<silence 2.0>", "audio/ambience/dark ambience.ogg" ] volume 0.4
    show anari nii smile with dissolve
    an "Making sure there's enough firewood to build a pyre."

    show ilona talk open with dissolve
    il "…!"

    show anari blank grin
    an "Edwin is a {i}huge{/i} man. Wouldn't it be terrible to burn him at the stake only to leave the job half-finished? And he can turn into a werewolf… What if he transforms as he burns up?"

    show ilona aaaa neutral
    il "You may think him a monster, but sometimes you speak like one."

    show anari open worry smile with dissolve
    an "It's not like I'm the one who murdered two people. But I'm sure you've had more than enough time to learn how your beloved little werewolf took care of that through your investigation."

    show ilona smile
    il "You shouldn't let your guard down; I have a better understanding of the situation now."

    show anari angry grin with dissolve
    an "Good. This should be entertaining."

    stop music fadeout 4.0

    play sound 'audio/sfx/footsteps slow leather tile.wav'

    ## KELLAC'S ROOM

    scene bg kellacs room
    with longfade

    "With that remark, Anari leaves. In the remaining time, Ilona reconvenes with Kellac. Eisleigh's condition is now stable and she is resting, the bleeding ceased."

    scene bg forest day
    with fade

    "As part of the investigation, Ilona and Kellac join the search party for Fleur."
    scene bg belorov day
    with dissolve
    extend " While doing so, Ilona searches for an escape route, and any part of the wall that may look like it could be scalable."

    $ renpy.pause(1.0)

    scene bg town plaza day
    with dissolve

    "Eventually, Kellac takes his leave to watch over Eisleigh to make sure her condition remains stable; leaving Ilona in the town square."

# SCENE 40

    ## TOWN PLAZA: SUNSET
    scene bg town plaza sunset with longdissolve

    "The day grows darker as the sun dips below the horizon. Edwin is brought out from the dungeon, his wolf-like arms bound in chains."


    play music 'audio/music/March Of The Huntress - Theme Of Anari -.ogg' fadein 3.0 volume 0.4
    play sound 'audio/sfx/footsteps slow trainers.wav'
    $ renpy.pause(2.0)

    show edwin_sunset wolf distant at less_right with dissolve:
        zoom 0.5

    "Anari is waiting, and several of the townsfolk look to the pyre. There is an air of formality surrounding Anari. Clad in her red hunting garments, the vibrant colour is illuminated by the glow of the sun."

    hide edwin_sunset with dissolve

    show anari_sunset talk angry at center:
        zoom 0.7 yoffset 220
    with dissolve

    an "We will begin the proceedings against Edwin, who was apprehended this morning."

    an "He has made his companionship with the nun, Ilona, clear. Ilona has been harboring him with the knowledge that he is a werewolf."

    show anari_sunset scary neutral with dissolve
    an "Edwin was found on scene, holding Salome's lifeless body."

    show anari_sunset closed neutral with dissolve
    stop music fadeout 3.0
    an "I'll start first with some important information. We could not locate Fleur, but we found this envelope in the forest. The seal on it was still intact."

    play sound 'audio/sfx/gynation paper.wav'

    "Anari's face is grim. She pulls out a letter, the seal on it broken. She reads the brief message out loud for all to hear."

    play music '<from 65 to 128>audio/music/Echoing - Theme Of Fleur -.ogg' fadein 4.0 noloop

    hide anari_sunset with dissolve

    scene bg forest night with fade

    $ renpy.pause(2.0)

    show lost_fl at center:
        zoom 0.7 yoffset 140
    with longdissolve

    fl "{i}By the time you receive this letter, I will be reunited with who I consider to be my true family.{/i}"

    fl "{i}I could only choose one or the other, and so I have decided to take a test of faith to prove my worthiness: I will strike terror into the one who has abandoned me.{/i}"

    fl "{i}In doing so, I have let fate decide my hand, and this was the result - to reunite me with the fair ones forevermore."
    extend " - Fleur Belorovna{/i}"

    hide lost_fl
    show bg black
    with fade

    show bg town plaza sunset
    show anari_sunset neutral angry glance at center:
        zoom 0.7 yoffset 220
    with longfade

    an "We are certain that this is her hand-writing."

    show anari_sunset open worry neutral sweatdrop with dissolve
    an "Fleur is… no longer with us. She has been taken by the fair folk. We couldn't find any trace of her, not even her footprints, or any clues towards her disappearance."

    show anari_sunset closed talk -sweatdrop with dissolve
    an "…With that matter settled, let's proceed with Edwin. The nun Ilona has prepared a defence. Please, rise."

    hide anari_sunset with dissolve

# SCENE 41

    "The words were stuck in Ilona's throat. She thinks deeply about the contents of Fleur's letter, but it truly sounds like the young girl mysteriously vanished. Though part of her couldn't accept that explanation so easily."

    "{i}I could only choose one or the other, and so I have decided to take a test of faith to prove my worthiness.{/i}"

    show ilona_sunset pensive solemn at left:
        zoom 0.5
    show anari_sunset neutral at right:
        zoom 0.5
    with dissolve

    "Ilona decides that they should at least begin with what they know from the investigation, and think about Fleur's letter along the way."

    show ilona_sunset glance talk
    il "This murder had at least two conspirators involved: Salome and Fleur."

    show anari_sunset angry look smile
    an "Hoh? Go on."

    show ilona_sunset aaaa open talk
    il "Both Salome and Fleur conspired together to drug the guests at the banquet, by poisoning the sugar with a powerful soporific."

    il "This was given to Uldin by Kellac last night as part of his medicine to aid his sleeplessness. Kellac has confirmed three doses of this medicine disappeared from his dispensary."

    show ilona_sunset glance
    il "During the banquet, Fleur and Salome were able to figure out Edwin's true nature, and thought to drug him by lacing the sugar with the soporific. When Edwin was asleep, they were able to steal a cursed item from him, and assume the form of a werewolf."

    play music 'audio/music/Wail of the Moon.ogg' volume 0.4 fadein 2.0

    show anari_sunset open talk angry
    an "All I care about are the deaths themselves at the end of the day. So? Who was the one that murdered Uldin?"

    scene bg black with longfade
    "Ilona thinks carefully about the course of events, and what she really saw."

    show bw_sa_murder at center:
        zoom 0.7 xzoom-1
    with dissolve

    "(The corpse of Salome, burned beyond recognition… )"

    hide bw_sa_murder with fade

    "(Her voice was thin, high and frail. Her body seemed smaller, possibly due to the burns…)"

    show lost_fl at center with dissolve:
        zoom 0.7

    "(“If she wore the wolfskin....”)"

    "A theory appears before her, dispelling the illusion of what she saw. If she is right, then this would explain the tragedy of last night in its entirety."

    hide lost_fl with fade

    show bg masters chamber night
    show bw_sa_murder at center:
        zoom 0.7 xzoom-1
    with dissolve

    stop music fadeout 4.0

    il "How were you able to identify the burned corpse in the Master's chamber?"

    an "Her skin was charred beyond recognition, so we had to resort to what remained of her hair and her ring to determine it was Salome."

    il "Did Salome have any identifying features on her body? Anything that could be used to set her apart?"

    an "Nothing that I know of, apart from the mole near her eye… And as I said, her face has been horribly burned — "

    $ renpy.pause(2.0)

    scene bg black
    show bw_sa_murder at center:
        zoom 0.7 xzoom-1
    with dissolve

    il "Then, here's my answer for who murdered Uldin: the culprit was Fleur."
    show bw_murder_fl at center:
        zoom 0.7 xzoom-1
    hide bw_sa_burder
    with vpunch
    play music 'audio/music/Chaos and Torment.ogg' volume 0.5
    extend " The corpse of Salome has been misidentified."

    scene bg town plaza sunset
    show ilona_sunset pensive annoyed at left:
        zoom 0.5
    show anari_sunset blank fury yell sweatdrop at right:
        zoom 0.5
    with vpunch

    an "What? How dare you doubt Kellac's judgement?  You must be truly grasping at straws to make such bold claims!"

    show ilona_sunset talk
    il "You said the corpse's face, hair and body were burned to an unrecognizable state. The only identifiers we had were Salome's ring, and her nightgown - all clothing and effects."

    il "I insist: this is Fleur's body."

    show ilona_sunset neutral
    show anari_sunset talk scary
    with dissolve
    an "Say we believe for one second we mistook one corpse for another — why Fleur? Why would she ever want to murder her own father?!"

    show ilona_sunset glance talk
    il "I don't have all the details… This is only a theory if the letter's contents can be believed. Her letter read: I will strike terror into the one who has abandoned me."

    il "Fleur's letter talks about choosing her true family. Uldin is not frequently in this town, is he? He has essentially abandoned his daughter."

    scene bg hall night
    with dissolve

    il "Only the guests were drugged that night — but not Uldin, herself or her mother. She needed him awake to scare him. As luck would have it, Edwin had the cursed item needed for transformation into a werewolf."

    show salome_bw closed angry smile at less_left
    show fleur_bw sorry happy at less_right
    with dissolve

    il "Her mother was assisting her in this plot. Fleur never intended to kill, she only wished to scare Uldin, perhaps to convince him to change his behaviour."

    scene bg moon
    with fade

    il "She assumed the form of a werewolf, Uldin's worst fear."

    il "She wore her mother's ring, perhaps to prove she had permission if found wandering at night… As you know, Fleur is fond of pranks and tricks. What better night than All Hallow's Eve?"

    an "I refuse to believe this… This is all far too absurd."

    il "A werewolf has considerable strength, even more than a beast, but it doesn't make you impervious to all attacks."

    scene bg gore with fade

    il "Terrified by such a horrible sight, Uldin did not hesitate to burn Fleur with magic, and driven mad by the pain, she killed him by biting his throat."

    scene bg town plaza sunset
    show ilona_sunset pensive annoyed smile at left:
        zoom 0.5
    show anari_sunset look fury neutral sweatdrop at right:
        zoom 0.5
    with dissolve

    il "You may have believed she was taken by the fair folk, but this would explain why you were unable to find her; or even to glimpse any trace of her - she was already dead."

    show anari_sunset yell with dissolve
    an "Then how do you explain Fleur's letter? Or the wooden effigy of her that appeared in her bed?!"

    show ilona_sunset happy annoyed open -sweat with dissolve
    il "I've already laid the evidence bare: there was more than one conspirator. Even taking the cursed item out of the equation, Salome was surely aware that there was a sedated monster in her house. And I strongly believe that she encouraged Fleur to do this 'prank' on her father."

    scene bg masters chamber night with fade
    show bw_murder_fl at center:
        zoom 0.5
    show salome_bw pensive angry smallgrin at extra_right:
        xzoom-1
    with dissolve

    il "Salome must have screamed to clear suspicion from herself, and hid in the master's chamber. At that point, Edwin was looking for his stolen item. He broke down the door and found Fleur's body."

    hide salome_bw with dissolve
    $ renpy.pause(2.0)
    show edwin_bw wolf fear talk sweat at easeinleft_transform:
        zoom 0.5 xzoom-1
    $ renpy.pause(2.0)

    scene bg town plaza sunset
    show ilona_sunset annoyed at left:
        zoom 0.5
    show anari_sunset look fury yell sweatdrop at right:
        zoom 0.5
    with dissolve

    an "How dare you — You have no idea how much Salome loved her daughter! She'd never abandon her like that!"

    show ilona_sunset pensive talk
    il "I wouldn't be so quick to discount the possibility. We found a chest made for Fleur in Salome's room. When Eisleigh opened it, she suffered a horrific injury from a trap. Perhaps Salome had the trap for some time, and her target was Fleur."

    show anari_sunset blank cringe shadow with dissolve
    "Anari remains silent, but her glare is penetrating and cold. Despite this, Ilona continues."

    show ilona_sunset talk
    il "She waited patiently until the manse was empty. After we escorted Edwin to the dungeon and gathered in the town square, Salome was able to move again. She locked the wolfskin away in a chest in her room, and trapped it with a device."

    show ilona_sunset closed relaxed
    il "Salome placed the statue in Fleur's bed to make it seem like she was spirited away by the fair folk. This statue fits the description of this receipt I found in Salome's room. Here."

    play sound 'audio/sfx/gynation paper.wav'
    scene cg open chest with fade

    "Ilona hands Anari the paper she found in the chest. Upon realizing that it explains the existence of the wooden statue of Fleur, she looks thoroughly displeased, nearly crumpling the document."

    il "Fleur must have had some suspicion this plan was risky, so she wrote a short letter. If she succeeded in her prank, all she had to do was destroy it."

    il "In fact, since the letter was found still sealed, I would suspect Salome encouraged Fleur to write it. To make Fleur's disappearance seem more credible, she placed it in the forest after her escape."

    scene bg town plaza sunset
    show ilona_sunset aaaa smile at left:
        zoom 0.5
    show anari_sunset glance neutral shadow at right:
        zoom 0.5
    with dissolve

    il "Not only did Salome orchestrate this parricide. She survived."

    stop music fadeout 2.0

    show anari_sunset fury closed -shadow with dissolve
    "Anari crosses her arms, and her brows knit together as she takes in Ilona's theory."

    show anari_sunset grin glance with dissolve
    an "You're forgetting something. You never explained what Edwin did in that room when he found the burned body. If I were him, I'd hide rather than stay out in the open. Why was he holding the body in his arms?"

    show ilona_sunset pensive neutral sweat with dissolve
    "Ilona freezes, her legs shaking. The words are caught in her throat again. As she sees this, Anari chuckled to herself."

    an "You really are awful at keeping secrets. There's no need to talk — I can already tell just by looking at you."

    "Ilona’s proposition is met with mumblings, grumblings, dissatisfied grunts and a few voices of support from the townsfolk. However, it’s all drowned out in the eyes and minds of both Ilona and Anari-"

    play music 'audio/music/Ilona Theme.mp3' volume 0.5 fadein 1.0

    "Ilona is shivering, as the warm rays of sun accentuate the bags under her eyes. Tired. Broken. But still standing."

    show anari_sunset open talk with dissolve
    "It’s impossible to say what Anari might be thinking right now. Her posture unflinching, the totality of her being in complete focus. She asks the crowd to simmer down, her usual aura of conceit fading away."

    show anari_sunset neutral with dissolve
    "There is now only one question that remains - and a clocktower that's ticking away, endlessly."

    an "So where is she? Where is Salome?"

    show ilona_sunset glance talk
    il "That, I can't tell you. I'm certain that my theory is correct, however."

    show ilona_sunset open
    il "I do not care what happens next, Anari. Whether you believe me or not is irrelevant. I've only tried to make sense of what I could from this tragedy."

    show ilona_sunset closed solemn happy
    il "You cannot make me feel guilt for harbouring Edwin as a werewolf. He is not defined by his curse, and I want you to see that."

    show ilona_sunset talk relaxed -sweat
    il "I have provided evidence and my theory, as you asked. Nothing I do now can change your mind. I accept it, regardless of the outcome."

    show anari_sunset look talk
    an "Sister, I would like to believe you. More than anyone else, believe it or not. Why, however…"

    show anari_sunset angry smile
    show ilona_sunset neutral
    with dissolve
    an "Well, maybe I can tell you some other time. If we even get a chance that is. In your mind, you may be right..."

    show anari_sunset fury with dissolve
    an "But unless you bring Salome to me, I will not be convinced. The ‘righteousness’ that you preach is meaningless without tangible proof. So, where is Salome? We searched everywhere in this town for her daughter."

    show ilona_sunset sad open talk
    il "I can only speculate at this point. Are there any secret or hidden passages in Belorov?"

    stop music fadeout 2.0

    show anari_sunset nii raised smile with dissolve
    an "That would be far too convenient, wouldn't it? You are right: nothing you do will change my mind. I have been burned by blindly trusting others in the past more times and in worse ways than you could ever imagine."

    show anari_sunset relaxed
    an "If I am wrong, so be it. When my time comes, I’ll gladly accept my penance."

    an "There's one thing that's certain: your arrival into this town brought with it the destruction of this family."

    show anari_sunset scary fury cringe
    an "If it weren't for you and Edwin, this tragedy would never have happened."

    show ilona_sunset aaaa talk
    il "You're blaming us for being caught in a plot that we had no part in? You have done nothing but look for reasons to kill Edwin all along. For all I know, maybe you planned for this to happen, to usurp power in Belorov."

    show anari_sunset nii grin
    an "Hahahahaha! I didn't know nuns could tell jokes. As if I would ever wish for such a thing."

    play music 'audio/music/War Of The Huntress - VS Anari -.ogg' volume 0.5

    show anari_sunset glance fury smile
    an "You should learn to choose your words more wisely, Sister. It's unbecoming of a holy woman… but I had the nagging suspicion you were a heretic from the first moment I saw you. Someone like you could never win."

    hide ilona_sunset
    show anari_sunset fury open smile at center:
        zoom 0.8 yoffset 450
    with dissolve

    "With a signal of Anari's hand, two town guards move in on Ilona and grip her arms tightly; drawing them behind her back. The men tried to bind Ilona's hands together with thick rope."

    hide anari_sunset
    show ilona_sunset closed aaaa yell tears at center:
        zoom 0.8 yoffset 450
    with dissolve

    il "Aaaaaaaahh! Let me go!"

    play sound 'audio/sfx/zap clothes rustle.mp3'

    $ renpy.pause(1.5, hard=True)

    play sound 'audio/sfx/werewolf breath.mp3'

    "Ilona struggles and tries to shake the men off, but the guards do not relent. One grabs her by the hair. Edwin cannot abide by this any longer."

    # Show CG wolf
    scene edwolf unleashed with vpunch
    $ renpy.pause(1.5, hard=True)

    "He transforms, the chains snapping off him as he transforms into a massive wolf-man."

    "He rushes at the guards with a growl, knocking them over by slamming against them. He throws them off with both fang and claw, prying Ilona away from them."

    scene bg town plaza sunset
    show anari_sunset fury glance grin kill at center:
        zoom 0.7 yoffset 220
    with fade

    "Anari strings her bow, and takes an arrow from her quiver. She trains it on the werewolf."

    an "I won't let you escape."

    hide anari_sunset with dissolve

    play sound 'audio/sfx/arrow whistle.mp3'

    "When she releases the bowstring, a piercing, otherworldly whistle cries out from her weapon. The arrow grazes Edwin's fur as he transforms from half-man, half-wolf, into an enormous grey wolf."

    ## TOWN WALL
    scene bg black with fade

    "He continues to run on all fours, with only Ilona to guide him. Anari scowls, and then goes to climb a tower to gain a higher vantage point."

    scene edwolf protecc with dissolve

    il "The gates will be already closed by now. There's a part of the wall that was hastily patched up. You should be able to climb through there."

    "Edwin takes a running leap, and latches his claws into the stone wall. He shifts back into his half-wolf form and starts climbing."

# SCENE 44
    play sound 'audio/sfx/Gravel Floor Fall 1.mp3' volume 0.3

    with vpunch

    "The looming stone wall in front of them is a substantial hurdle to overcome. The town guards mobilise, firing arrows that torrent Edwin and Ilona. Edwin does his best to throw off their aim."

    show bg belorov sunset
    show anari_sunset fury scary neutral kill at center:
        zoom 0.85 yoffset 420
    with fade

    "There is one he cannot escape from. Anari's skill with a bow is frightening, her gaze ever calm and steady."

    scene bg wound1
    play sound 'audio/sfx/arrow whistle.mp3'

    $ renpy.pause(0.6, hard=True)
    stop sound

    scene bg wound2
    play sound 'audio/sfx/zap arrow.mp3'

    "Two arrows finally meet its target. They pierce his side, fired in rapid succession."

    scene bg wound3
    play sound 'audio/sfx/arrow whistle.mp3'

    $ renpy.pause(0.4, hard=True)
    stop sound

    scene bg wound4
    play sound 'audio/sfx/zap arrow.mp3'

    $ renpy.pause(0.2, hard=True)
    stop sound

    scene bg wound5
    play sound 'audio/sfx/zap arrow.mp3'

    extend " Then three more pierce his ribs. This isn’t a problem for the werewolf, as he brushes aside the pain. He’s taken greater beatings than this."

    scene edwolf claws with longfade

    "However, he’s not invincible; a few more well placed shots and he’s down, along with Ilona."

    show ilona_sunset glance aaaa talk at center:
        zoom 0.5 xzoom -1
    with dissolve

    il "Stay with me Edwin! Don’t lose sight of our escape. I’ll do my best to heal your wounds with- Ah!"

    play sound 'audio/sfx/arrow whistle.mp3'

    $ renpy.pause(0.5, hard=True)

    play sound 'audio/sfx/zap bone break.mp3' volume 0.7

    scene bg blood

    "An arrow pierces the hand with which Ilona was trying to use to heal. Her hand twists and contorts, reflexingly convulsing due to the writhing pain."

    ed "Ilona! Ho-hold on, we’re almost there!"

    scene cg_repeating_edwolf_edgewolf_blurry with dissolve:
        # Makes you able to use subpixels, handy for positioning.
        subpixel True
        # Keep this as it is, really annoying to change. It tells where to position the image and how far you want to zoom in.
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 1.02
        # Tells where you will circle around in the image and how far.
        alignaround(.5, .6)
        # Linear is how fast you want the circling to be, lower it to make it faster. yalign is the same as like xpos, don't bother changing that. Circles is the amount of circles it will do before repeating.
        linear 10.0 yalign 1.0 clockwise circles 1
        repeat

    "Time seems to move too slowly. How much more pain can they accept? Edwin grimaces past the pain of his sustained wounds."

    "There’s no question about it - Ilona knows Anari could never miss her mark, not with a target so large. She’s missing their vitals on purpose."

    "A good look at Anari leaves nothing more than questions. Does she want to let them leave? Or capture and burn them at the stake alive?"
    $ renpy.pause(0.3)
    play sound 'audio/sfx/arrow whistle.mp3'

    $ renpy.pause(0.5, hard=True)

    play sound 'audio/sfx/zap bone break.mp3' volume 0.7

    scene bg gore with hpunch

    stop music fadeout 3.0

    "Her intentions remain unclear, as one final arrow impales Ilona in the back, shooting through her cleanly."

    "With a light scream, Ilona loses her footing. There's only one hand she could use to hold onto the rough stone wall, and her fingers are slipping. Blood stains her white dress from the hole it left behind, and she can feel it drip down on the wall."

    ed "Ilona! No!"

    play music 'audio/music/Rising.ogg'

    "Edwin is quick to react, as he pulls her over while climbing over the wall; carrying her carefully, as though holding an injured bird."

    # mirror image of wall to give impression they climbed over it
    scene bg belorov sunset:
        xzoom -1
    with longfade

    "The stone wall they escaped over is dyed red with their blood. Yet they make it out of Belorov, despite their injuries."

    "Edwin marches on, with Ilona in his arms. It’s too dangerous to be out in the open. They search for a place to rest, as dusk waits."

    ## FOREST
    scene bg road sunset with dissolve:
        xzoom-1

    "Ilona heals the wound that pierced her abdomen through, and the blood slows. However, the wound does not close completely. The other arrows stuck in them would prove more dangerous to deal with, with no surgical equipment to use."

    il "Edwin, set me down. You're more injured than I am."

    play sound 'audio/sfx/werewolf breath.mp3'

    ed "Ilona, my darling-"

    il "{i}Darling?{/i}"

    play sound 'audio/sfx/zap clothes rustle.mp3'

    show ilona_sunset shock sad talk blush blood:
        zoom 0.5 yoffset 0 xcenter 700
    show edwin_sunset fear blush talk blood at center behind ilona_sunset:
        zoom 0.5
    with dissolve

    "At the awkward exchange, Edwin gingerly sets Ilona down on the ground. He reverts to human form, his ears and face red. Ilona tries to heal what open wounds that Edwin has."

    show edwin_sunset sad smile
    ed "Yes, I've —  I’ve been waiting to call you that for so long."

    show edwin_sunset closed
    ed "What a fool I was to keep what I felt about you hidden…"

    show edwin_sunset distant talk -blush
    ed "The time I spent without you, in that cell. It was excruciating. And that’s when I realised, how much I want you by my side."

    show ilona_sunset glance happy
    il "My, the exhaustion must be getting to you. So you weren't joking about wanting me to meet your family…"

    show edwin_sunset glance neutral
    ed "…"

    show ilona_sunset closed happy solemn
    il "...Thank you. It- it means a lot to me. Could we rest for a while?"

    show edwin_sunset talk
    ed "I don't hear anyone pursuing us. Just for a moment, then…"

    play sound 'audio/sfx/Footsteps Slow Trainers.wav'

    scene bg valley sunset with dissolve

    $ renpy.pause(2.0)

    "They walk for a while to search for a resting place, seeing the valley unfold before them."

    # The scrolling bg
    scene valley_scroll
    show ilona_sunset blood:
        zoom 0.5 yoffset 0 xcenter 700
    show edwin_sunset blood at center behind ilona_sunset:
        zoom 0.5 xzoom -1
    with longfade

    ed "I’m sorry."

    show ilona_sunset open with dissolve
    il "About what?"

    show edwin_sunset angry furrow talk with dissolve
    ed "You’re right about me not saying what it is that I want to say, burying it so deep within the abyss that I can’t even reach it."

    show edwin_sunset distant neutral
    ed "Even if I want to… Just maybe, if I’d come clean to the people that we met thus far, and to you, about the wolfskin; the incessant nightmares that I’ve been having...."

    $ renpy.pause(2.0)

    show edwin_sunset sad talk -furrow with dissolve
    ed "I couldn't even trust you to watch me transform..."

    $ renpy.pause(2.0)

    show ilona_sunset pensive smile with dissolve
    il "It’s okay. We can start over."

    show edwin_sunset neutral with dissolve
    ed "If I’d had the courage to ask for your assistance, we could have found an alternative."

    show ilona_sunset solemn neutral with dissolve
    il "We must be strong and keep our past behind us. What’s done is done."

    $ renpy.pause(4.0)

    il "Besides, I’m here for you now. And you are for me. I’m sure that God has tested our resolve more than enough."

    show edwin_sunset closed smile
    ed "I would like to believe that."

# keep the xalign values for the bg to scroll in the correct direction
# Increase linear value for slower scrolling
    image valley_scroll:
        "images/bg/bg valley sunset long.png"
        xalign 0.0
        linear 340.0 xalign 1.0
        repeat

    scene bg valley sunset with dissolve
    show ilona_sunset closed sad blood at ilona_final_canopy
    show edwin_sunset closed blood behind ilona_sunset at edwin_final_canopy
    # image to give the canopy shading
    show valleytree
    with longfade

    "Eventually, they stop to sit under the shade of a tree, basking in its shadow. Their breath is ragged, but in sync with each other's. Ilona rests her head on Edwin’s shoulders."

    "Edwin and Ilona stay silent, listening to the breathing of the other. They both feared when they would only hear silence. The grievous wounds would prove to both of them that they were alive."

    show edwin_sunset glance talk
    ed "Evil breeds evil, indeed. Wherever I go, something always goes wrong."

    show edwin_sunset anxious
    ed "I’ve noticed hints of it. Even in these past few days - mind you, that banquet was all too much for someone like me to begin with. I used to enjoy these things, but now, I..."

    show ilona_sunset pensive
    il "I know."

    show edwin_sunset open neutral
    ed "Everybody had something to hide. That fear only led to mistrust, and this to violence… We were all alone, yet turning against each other."

    ed "I know I’m in no position to say this, but I see the absurdity of it all now. There is no point in hiding. It does no good."

    show ilona_sunset talk open
    il "It's hard sometimes to be vulnerable, isn't it? To feel exposed, when you have no one you can trust, nobody to confide in."

    il "And you cannot close this distance with others, because you always second guess intentions… There’s nothing worse than feeling alone in the world."

    show edwin_sunset distant talk
    ed "Is that why Salome did what she did?"

    show ilona_sunset pensive neutral
    il "I do not know, but I pity her…"

    scene bg black with longdissolve

    "Ilona hears Edwin's breathing slow. Ilona is too weary to use any more healing magic. They can’t remove the arrows that pierced them, or the two of them would surely bleed out and die."

    ed "…"

    il "Edwin?"
    $ renpy.pause(3.0)
    ed "…"

    scene bg valley sunset
    show ilona_sunset pensive solemn neutral blood:
        zoom 0.75 xpos 240 yoffset -100
    show edwin_sunset closed blood behind ilona_sunset:
        zoom 0.75 xpos 420 yoffset -100
    # image to give the canopy shading
    show valleytree
    with longfade

    il "Ed…"
    $ renpy.pause(3.0)
    show edwin_sunset anxious smile with dissolve
    ed "Yes, love. I'm still here. What is it?"

    show ilona_sunset sad with dissolve
    il "Is it okay if I close my eyes for a while? I don’t think I’ll be able to hold out for any longer…"

    show edwin_sunset sad smile
    ed "You may. I'll keep watch, so you can rest."

    scene bg black with longdissolve

    il "I wonder — what your family is like…"

    ed "It's a big family… They'll definitely welcome you…"

    il "That sounds… nice…"

    ## SKY
    scene bg sky sunset
    with longfade

    "Edwin watches the brilliance of the sky and clouds, gradually darkening. With Ilona by his side, he relishes in the peace and comfort."

    ed "Ilona, love…"
    $ renpy.pause(3.0)
    il "I'm here. Did you need anything?"

    ed "I-I just… I just wanted to say how much I owe to you."

    il "You're always thanking me…"
    $ renpy.pause(3.0)
    il "Ed…"

    ed "Yes?"

    il "Do you think you could hold me? I want to lie down…"

    ed "Of course… I'll lie down with you. We should be safe here…"

    il "Thank you…"

    play sound 'audio/sfx/zap clothes rustle.mp3' volume 0.2

    # CG lying on grass (eyes open)
    scene final open with longdissolve
    $ renpy.pause(1.5, hard=True)

    "Ilona lays her head against Edwin's chest, and he gently wraps his arms around her. He heaves a contented sigh, yet the arrows piercing him dig into his weary body."

    "Edwin thinks of the time they met, reading aloud poetry and ballads together. He strokes her hair, speaking softly in a murmur. He can feel his hands wet with the blood from her wounds."

    # despite the beautiful poem, it should be delivered clumsily as possible (I mean, he's dying, or close to death). "though words are withering" should be admitted through gritted teeth.

    scene final open talk with dissolve
    ed "Should our journey end, so just it be."
    extend "\nI am lost no more, I lay to rest."

    scene final closed with dissolve
    ed "The sun bestows its blessings over me,"
    extend "\nWhile you wait beside."

    scene final open talk with dissolve
    ed "I flourish with the bountiful verdure"
    stop music fadeout 5.0
    extend "\nThough words are withering,"

    ed "In all uncertainty we usher,"

    ed "I bid you know: I love you."

    ed "I-I love…"

    # CG lying on grass (eyes closed)
    scene final closed with longdissolve
    $ renpy.pause(4, hard=True)

    # Go to the credits.
    jump credits_from_script

#####   ALTERNATING LINES FOR THE LAST POEM  ########
#
#    Ilona & Edwin:
#       "We are found."
#
#    il "Praying deep in dead of night,"
#    il "You have found your path."
#
#    ed "Praying still, no end in sight,"
#    ed "A pure heart perseveres."
#
#    il "Praying, no desire, delight,"
#    il "A serene soul you see."
#
#    Ilona & Edwin:
#       "Bring back those melancholy hearts,"
#       "Cleanse these with your soul unbound."
#
#     ed "Out of sorts, but not far gone,"
#     ed "With you, nothing lost is found."
#
######################################################
