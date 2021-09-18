## The file for act 1.

## moving sprites are a pain
define midleft= Position(xpos=0.40)
transform ilona_transform_pos1:
    zoom 0.5
    left
    xpos 300
transform edwin_transform_pos1:
    zoom 0.5
    right
    xpos 1800
transform ilona_move_right:
    ilona_transform_pos1
    linear 0.8 xpos 550

label act1:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg black
    with fade

    # Edwin's monologue for the intro in NVL mode
    define nvlNarrator = Character(None, kind=nvl, what_font="BluuNext-Bolditalic.otf", what_size=50, what_kerning=2)

    # NVL mode: Edwin's monologue
    $ quick_menu = False

    window hide

    nvlNarrator """
    I am lost.

    Pray, that I shall find my path.

    Pray, that I shall not lose heart.

    Pray, I see for who I am.

    This, the only wish I have.

    \nBefore I’ve wronged,

    So far gone.
    """

    nvl clear

    # Switch to AVD mode.

    play music 'audio/music/He Who Seeks Hope - Theme Of Edwin -.ogg'

    scene bg forest night
    with fadehold

    $ renpy.pause(2.0)

    show ilona_night at ilona_transform_pos1
    show expression AlphaMask("canopy", At("ilona", ilona_transform_pos1)) as ilona_mask

    $ renpy.pause(1.0)

    $ quick_menu = True

    il "We should think of finding shelter soon, before it gets too dark."

    show ilona_night closed

    "Ilona waits for Edwin to turn back into a human, closing her eyes to rest for a moment. There's only the sound of the forest, until Edwin speaks to break their silence."

    show edwin_night glance talk at edwin_transform_pos1
    show expression AlphaMask("canopy", At("edwin", edwin_transform_pos1)) as edwin_mask

    ed "I know that I'm asking for too much, but despite everything that's happened… would you please stay with me?"

    show ilona_night sad shock talk

    il "What? Edwin, please, calm down-"

    show edwin_night sad talk

    ed "... Ilona I-I can’t. Not in a situation like this..."

    show ilona_night open sad neutral

    show edwin_night glance neutral

    il "You’re right, but I need you to slow down. I can’t keep up with you and that is only going to make us look all the more suspicious."

    ed "..."

    show ilona_night pensive at ilona_move_right
    show expression AlphaMask("canopy", At("ilona", ilona_move_right)) as ilona_mask

    $ renpy.pause(0.6)

    show ilona_night sad talk

    il "We have only each other to rely on."

    show edwin_night sad neutral

    show ilona_night pensive sad neutral

    "As she says this, she places her hands over his. His hands are abnormally cold to touch. Ilona learned this was a sign of his transformation."

    "Even so, she must remain with him."

    show ilona_night closed relaxed

    "The moonlight beams over them, slightly wavering with each breath they take."

    il "(If only the moonlight would never leave us. We should rest here for a while.)"

    il "Edwin…"

    show edwin_night closed neutral

    ed "…"

    show ilona_night blush smile

    il "Ed…"

    show edwin_night sad grin blush

    ed "Yes, I’m here. Please forgive my wandering mind."

    show edwin_night closed grin

    show ilona_night open

    ed "...What could I ever do without you? I feel like I have never thanked you for-"

    show ilona_night happy

    il "You have thanked me more than enough already, Edwin. I appreciate it… but let's not dwell on it any further. "

    show ilona_night closed smile

    show edwin_night glance smile blush

    "Their eyes flicker for a moment, and he’s not shivering anymore. "

    # foliage masks are not needed anymore
    hide ilona_mask
    hide edwin_mask

    scene bg road
    with longfade

    "Eventually, they press on. They sight a lonely settlement on the horizon; stone walls surrounding its perimeter."

    show edwin_night anxious grin at right with dissolve:
        zoom 0.50

    ed "Heh…"

    show edwin_night anxious talk furrow

    ed "I haven't felt like m-myself lately, since the incident back at the priory. Try as I may to blend in, to do good and keep myself in check… I am a beast, through and through."

    ed "What is it that we've done wrong? Is us being together something so heinous? Is my existence such a sin?"

    show ilona_night sad pensive neutral with dissolve:
        zoom 0.50 xpos 50

    il "..."

    show edwin_night angry furrow

    show ilona_night neutral

    ed "I did not know the extent of the hatred that lay within their souls until that night… to go as far as to burn me alive…"

    ed "Is there something wrong with me, Ilona? I'm always on edge, fearing for our lives… I never meant to put you through this."

    show ilona_night

    show edwin_night neutral

    il "If you want my answer as a {i}former{/i} nun… You and I have sinned."

    il "You said that you were a beast, through and through."

    show ilona_night closed talk

    il "You're not. You’re-"

    hide ilona_night

    hide edwin_night

    with vpunch

    "Edwin immediately lets go of her hand, intertwined seconds ago, but now balled into a fist. The rustling of dry leaves brought with it a heavily armed guard and an archer under a cloak."

    show anari_night angry glance neutral bow with dissolve:
        zoom 0.50 xpos 10 xzoom -1

    unk "That's enough loitering around the town wall looking suspicious, don't you think?"

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

    show anari_night open talk

    an "My name is Anari. Happy now?"

    an "I'm not going to probe you or anything."

    an "You may be outsiders, but you look like decent enough folk. No need to come up with any grand excuses for why you’re here."

    an "So, let’s get back to it. Will you accept the town master's call?"

    show anari_night neutral

    show ilona_night closed talk annoyed

    il "...I suppose that choice is not truly much of one. I accept."

    show ilona_night glance neutral

    show anari_night smile raised

    an "A wise judgement. You’re clever for a nun, but you should learn to keep your dog in line."

    show edwin_night fear talk furrow

    ed "...Excuse me?"

    show anari_night angry neutral

    an "I don’t appreciate being called ‘feisty’."

    show anari_night neutral

    show edwin_night anxious

    ed "I meant no offense when I said that. My apologies."

    show anari_night nii smile relaxed

    an "So you do have manners; it would do you well to keep them. Let’s get moving, then. I’ll escort you to the manse."

    hide anari_night

    hide ilona_night

    hide edwin_night

    with fade

    "Anari takes the position of rear guard, as the other guard leads the way forward."

    "Ilona glances back, just once. Anari's bow is by her side and a hand rests on the quiver, ready to fire if the two of them even thought of escaping."

    "Ilona cannot help but wonder just how much Anari overheard of their conversation... Her arrival seemed too well-timed."

    "Did they give away too much, even when they thought they were alone?"

    "She glances at Edwin, his face inscrutable. And so, they enter the gates."

    scene bg forest day
    with fadehold
    play music 'audio/music/The Town.ogg'

    show edwin closed at right with dissolve:
        zoom 0.50 xpos 1.0

    ed "(When was the last time I felt any hope? Anything besides pain? The swelling in my chest is excruciating…)"

    ed "(I truly wouldn't have made it this far on my own. Even if I hide what I am well, people can't help but to be suspicious.)"

    ed "(Although - a town full of people not trying to kill me yet is quite an improvement.)"

    "It’s almost time to head home for normal folk, but the town is bustling. There's a large bonfire in the square, and there's carved turnips at the doors of all the houses-"

    show ilona glance sad neutral with dissolve:
        zoom 0.50 xpos 0.75 xzoom -1

    # spoken as though Ilona is suspicious of jack o' lanterns
    il "What kind of decorations are these?"

    show edwin glance grin

    ed "It’s for... All Hallows’ Eve, a celebration to commemorate the dead."

    show ilona angry sad talk

    il "You mean All Saints’ Eve? Why are the townsfolk celebrating in joy, then?"

    show edwin closed grin furrow

    show ilona neutral

    # said as though trying not to laugh, mock-seriously
    ed "You were raised strictly, Ilona. Father Ivanov never wanted you to know about these pagan festivals."

    show edwin fear talk
    with hpunch

    show ilona shock sad

    ed "Oh!-"

    show kellac smile at easeinleft_transform:
        zoom 0.50

    # calmly, not overly acted out
    unk "Young lad, please watch your step. One mistake and this weary old man is done for…"

    show edwin closed

    show ilona open solemn

    ed "I’m so sorry for bumping into you, sir-"

    show anari closed talk angry sweatdrop with dissolve:
        zoom 0.50 xpos 540

    # as though tired of an old joke
    an "...Kellac, we're the same age."

    # most of Kellac's lines should be delivered without too much enthusiasm, as though he was an older person or an 'old soul'.
    ke "Fancy meeting you here, Anari. I didn’t know you like to take strolls. I never knew you had friends either! And who may you be, dear sister?"

    ed "Uh, I’m not sure we're friends…"

    ke "Pleased to make your acquaintance, anyhow. I’m Kellac, Anari and I go way back."

    an "That we do, and I regret it."

    ke "You’ve just got to love that personality! Don’t take her too seriously, she's always been like that."

    ed "I see… I'm Edwin. Pleased to make your acquaintance. "

    il "As am I. My name is Ilona. Forgive my ignorance, but are you the master of this town?"

    ke "Me? Sorry, but no. I'm just the physician and herbalist. Did the master summon you?"

    il "He did, but I don't know what business we have with him..."

    ke "Aha. I should have expected as much; Anari has a habit of leaving out the details and jumping straight to the point."

    ke "I should get going, but we're bound to see each other again soon. Keep well, Anari."

    "Anari only nods curtly, and the group moves along. Further into the town, they find a large house made of timber and stone."

    "Edwin wonders, how should they go about this? It’s best they wait and see what happens once they enter."

    an "Sir Uldin, Lady Salome. I've brought to you Sister Ilona, and her companion Edwin."

    ul "So the man was with her after all?"

    # probably not in any need to say this, but the pronunciation of 'blackguard' is spoken like 'bla-grd'
    an "At first, I thought a holy woman was being accosted by some blackguard. To think that he was her travelling companion..."

    ed "I understand I may not have the friendliest appearance… but I have sworn to protect Sister Ilona from harm."

    ul "This is indeed unexpected… Anari's eyes are keen, but perhaps only for hunting her quarry."

    an "True. There's no need to understand the conversations of beasts to hunt them, only their behaviour."

    sa "How amusing... Judging by Anari's report, I would have thought she was describing a saint!"

    il "Thank you for your kind words, but they are far too gracious to be wasted on me... I have not done anything to be deserving of such praise."

    sa "I thought you might be able to join us for tonight's feast for All Hallows' Day, and to perhaps lead us in prayer."

    ul "It’s not every day that you see a nun, and much less in such unlikely company. So, Would you accept our invitation?"

    "Ilona had to consider this carefully. She and Edwin had drawn too much attention already… So it surprised her when Edwin spoke without any fear."

    ed "We will gladly accept."

    sa "Tonight's banquet will begin shortly, but you should still have time to prepare for it. Anari, let us debrief in the meantime."

    # HALL(SCENE 4)

    "It had only been a few days since they were on the run… Ilona could scarcely believe that they were welcomed so readily."

    "They sit at a table laden with food: a rich coloured beetroot soup, mulled wine with spices, pickled vegetables, a glistening whole roasted pheasant and even more dishes than one could name."

    "Seated at the table were two new faces: Fleur, the daughter of Uldin. On Fleur's left side was Eisleigh, an assistant to the house."

    "Uldin plans to rebuild the ruined chapel in Belorov, as Salome is deeply pious. That was why Salome regards the meeting with Ilona as such good fortune."

    "As everyone gathers at the table, Uldin urges Ilona to lead them in prayer before the meal."

    "She speaks a few words of gratitude for the harvest, and for peace and protection. When she lifts her eyes once again, the lively banquet commences."

    ke "The food smells amazing. Was that the pheasant you caught today, Anari?"

    an "The very one. Ahh, a successful hunt and high quality spices can put even someone like me in a good mood."

    ke "You should always be in a good mood, then!"

    an "Heheheh. Fleur, would you like some spiced pheasant?"

    fl "Oh no, thank you, Aunt Anari. You always make it way too spicy… "

    an "That's too bad… I guess you really don't take after Uldin when it comes to food."

    sa "So, what brings you to Belorov, Mister Edwin and Sister Ilona?"

    sa "Our town may not look like much after our chapel was ransacked and destroyed, but it was once breathtaking."

    il "We're… on a pilgrimage. We were just seeking shelter before dark."

    il "I heard about the destruction of a chapel some time ago, but I had no idea it was here."

    sa "Yes, it was the barbarians' doing. Even now, we're still rebuilding the town, but the faithful have moved on from here."

    sa "I miss having someone to share my connection with God, so I am sorry to impose my sudden invitation on you."

    sa "Belorov is home to people of many faiths. Many of us have travelled from afar, like myself."

    il "From what I understand, Edwin was also quite the traveller before we met."

    fl "Do you have any stories, Edwin? I'd love to hear them."

    ed "Haha. To tell you everything that happened would tax my wits."

    fl "Have you seen any mythical creatures in your journeys? Ever met the fair folk??"

    ed "Let me think. There was this one time I had an encounter with a giant… "

    "Edwin regales the table with his tale of encountering a giant when he was atop a mountain. Fleur and Salome listen with rapturous attention."

    "Even Kellac takes an interest in these tales, and starts telling of his own travels. He loses track of time, and he decides that it is getting late, and he needs to head in early."

    "Anari leaves to get some rest for her shift as the town guard. Both of them bid everyone at the table a good night."

    "Even though the party thins out a little, Fleur seems as excitable as when she began. Even Eisleigh, who kept to herself as she ate, joins in on the conversation."

    ei "You've really travelled a long way away if you came from across the sea, Edwin."

    fl "Now I'm wondering, how did you meet Sister Ilona?"

    ed "Oh uh… Heh heh. That's a story for another time. I'm pretty tired…"

    fl "Oh, could it be…? Is the story of how you met Ilona not suitable for my ears? "

    ei "Ahaha, is that it? You might be onto something, Fleur."

    il "…{p}(Girls these days are sharp.)"

    ed "No no, that's not it at all! It's… not that interesting compared to my other stories."

    fl "Hmph, I was under the impression you two shared a forbidden romance."

    sa "Fleur, you shouldn't tease guests. And you really shouldn't encourage her, Eisleigh!"

    fl "Mother, it's All Hallow's Eve! Tricks and pranks are part of the fun. I'm merely teaching Sister Ilona about this part of the festival — She shouldn't be so serious and uptight all the time."

    ul "Well, they said they were on a pilgrimage. If their sins are meant to be forgiven in the end, they should be able to sin along the way all they want!"

    il "..."

    ed "Grk..."

    sa "Not you too, dear… You must have had too much to drink."

    "Salome gives one stern glance to both Fleur and Uldin, and their boisterous laughs subside. Uldin still seems pleased with his comment. When he recalls the looks on Ilona and Edwin's faces, he tries to not burst out laughing again."

    fl "I apologize, Mother. And I apologize to you as well, Edwin and Sister Ilona, for insinuating something I should not have. "

    "Ilona and Edwin sheepishly mumble their acceptance of Fleur's apology. There is still too much attention on them…"

    "Salome asks everyone their preferences for tea to make preparations, and she excuses herself."

    "A brief moment later, Fleur rises from her seat. She helps Salome with preparing the tea, truly apologetic about her earlier behaviour."

    ul "We've arranged separate sleeping quarters for the both of you. Please, don't take our jests seriously."

    ed "You've been most gracious to offer us both this feast and shelter for the night. Thank you again for your hospitality."

    ul "Oh no need, but if you must insist: you’re welcome."

    ul "Please, I know this is all too much for you and Sister Ilona. You’ve met quite a few people already, and it's getting late. If you need to retire for the evening, you are welcome to."

    "At this point, Salome and Fleur have the tea ready, and Eisleigh helps in serving it to the guests, along with servings of milk and sugar at each end of the table."

    "Uldin remarks that this is one of his favourite teas — indeed, the pleasant aroma of black tea is refreshing, and any awkwardness from the conversation before is soon forgotten."

    ul "Though, I must admit I remain curious as to how you two knew each other. Are you religious, Edwin?"

    ed "As much as any other man. Our meeting, well… Ilona pulled me out of a dark place. We bonded over the stories and poems she was recording."

    ed "I did not want to let her travel alone, so I decided to act as her guard on this journey."

    ul "I see. Having a companion to talk about the same texts… That's not so different from me and Eisleigh."

    ei "Well… magical texts; books about curses and spells, rather than stories and poems."

    il "Oh, that's unusual. Both of you practice magic?"

    ul "It's a useful resource, but difficult to master. You did say the two of you are on a pilgrimage… so you might not be aware of recent events."

    ei "There have been sightings of a werewolf in another town."

    ul "Those foul beasts… A werewolf truly must be cursed to succumb to their bloodlust."

    "An oppressive silence lingers, and sweat beads down Edwin’s forehead. Ilona tries to keep a straight face, but her brow twitches."

    "Edwin adds more sugar to his tea, and he takes care to not rattle the crockery as he stirs it with the spoon."

    ul "Please pay no heed to my language, it- It’s just..."

    ul "Belorov was once an old fortress, so we don't have to worry about monster attacks. But in my youth, I experienced an attack first hand..."

    "Uldin details a dramatic hunting trip in his youth, with his older brother and subordinate: a werewolf attacked the tent in the dead of night, but Uldin fended it off with fire magic."

    "His subordinate was torn to pieces, and Uldin's brother had his legs nearly hewn off."

    ul "If it were not for my study of magic, who could say what might have happened?"

    ed "..."

    fl "Edwin, are you okay? You look pale."

    ul "I apologise, I might have gone too far..."

    il "...Do you need any assistance?"

    ed "No, thank you, Ilona. And yes; Fleur, I think I may need to rest for the day. Please excuse me, my mind’s been all over the place."

    ed "I should be back in full spirits by tomorrow."

    ul "Very well. Eisleigh, if you may, show him to his room, please."

    ei "Of course."

    # SCENE 8(EDWIN POV)

    "Eisleigh unlocks the door by the stairs, and opens the guest room. She gives Edwin the key."

    "Having a separated sleeping quarters is more than what he could normally ask for. For this style of house, he would assume that the guests share one large sleeping space."

    "He was prepared to run out of the manse, and to be alone in the darkness of night. Instead, he still has to play the role of an honoured houseguest."

    "Eisleigh bows, and leaves him with only saying a few words of comfort, hoping that he will feel better with rest. He nods, and then closes the door, locking it with the key."

    "The unexpected privacy given to him helps ease his mind and, feeling his skin cool, he wipes the cold sweat from his brow."

    "The chatter of the party is distant, and he has to strain his ears to listen."

    "Now, he is alone."

    "Edwin's towering frame lowers to the ground, and the floorboards creak slightly with his movement."

    "He kneels down by the bed, as though praying. It's as if he only now remembers how to breathe…"

    ed "Lord, please have mercy on my soul…"

    ed "I want to believe that I am human, but the people won't accept me all the same. Am I allowed to surrender at last?"

    # note: please mind the parentheses - they are thoughts, and should not be voiced

    ed "If I were to end it…{p}right here and right now.{p}Wouldn’t that be spectacular?"

    ed "Hah.{p}Hahah{p}Ahahahahahahahahahahahahahhahah!"

    ed "Look at me, a husk of myself. Not even courage remains."

    ed "Pathetic.{p}I should be better than this.{p}Stronger than this."

    ed "What was the point of going through the trials of the military, otherwise?"

    ed "I’ve been through worse."

    ed "That day… I was brave, wasn’t I? I did save my sister from the werewolf attack, didn’t I?"

    ed "(But did I really do it for her?{p}Or did my thirst for blood take over…)"

    ed "(A whiff of blood, and I’m running towards it…)"

    ed "(And he won't leave me alone since then. the Lord of the Forest, he calls himself.)"

    ed "(Penetrating my dreams ever since that day…)"

    ed "(And granting me the curse of the Wolfskin.)"

    "The Wolfskin; a sash of wolf pelt that sits on his waist with intricate designs, foreign to this land. Or to any land, for that matter."

    "The gold glistens, and the red…{p}Well, the red reflects the sheen of madness that rests within."

    ed "(Only the insane ones are bestowed with this torment. Like I…)"

    ed "...What am I doing?"

    ed "Ilona told me once to hold onto hope… What’s done is done."

    ed "(But today was a disaster, how could I lose my composure? I was practically dripping with sweat. I know for a fact that Uldin must have noticed that. Sooner or later, I’m a dead man.)"

    ed "(And I will bring Ilona down with me.)"

    ed "Ilona… my-my darling…"

    ed "I wish I could say these words to your face…"

    ed "What a fool I am for having kept my affection a secret from you..."

    ed "(Because now…)"

    ed "(Now I don’t think I’ll get another chance to say what I want to say… I can feel the hysteria building up within me.)"

    ed "(Expanding like it’s never before.{p}Rising, so far…{p}Far, far away…from my control.)"

    ed "But I promise you this, Ilona:"

    ed "I am not going to hurt you.{p}I am going to do right by you. I am not going to hurt anyone who’s innocent."

    ed "It may seem the other way around, but whatever I do;"

    ed "I will have a damn good reason for it."

    with longfade

    # SCENE 9

    "Ilona stayed after Edwin's exit, to ask Uldin and Eisleigh about the nature of curses, but the conversation following was dense and difficult."

    "At that point, Fleur took her leave, no longer interested in the dry and tiring conversation at hand."

    "Ilona tried her best to keep up. Uldin tried to challenge her with theories that needed to be formed on the spot and, at times, it turned into a messy debate."

    "The rest of the party retired to bed before midnight. When Salome entered, she became the mediator of peace and that was when everyone agreed to call it a night; departing from the main hall on friendly terms."

    "Salome ushered a rather drunk Uldin back to bed. Eisleigh showed Ilona to the room that was prepared for her, and they bid each other a good night."

    "Ilona opens the door, and thinks for a moment if she wants to lock it. Her head is swimming, either from the spiced wine, or the meandering conversation."

    il "(Ed… I wonder how he's doing. That conversation earlier really took a turn for the worse for him.)"

    "His room is on the right side of hers, and Kellac’s on the left."

    "Ilona presses her ear up to the wall separating her and Edwin's room, but hears nothing from the other side."

    il "(Not a sound. He's probably asleep.)"

    il "(I should get some rest too, so we can both leave early tomorrow. The people here are kind, but there's too much risk if we stay… We have to keep moving.)"

    "She thinks of going to see him, to maybe knock on his door and to check up on him."

    "However, in the end she decides not to. Ilona can only trust him to be cautious. She could not continue to worry about him; it would make her restless…"

    "Ilona wonders if she should leave her door unlocked, in case he wants to speak to her."

    "It seems risky, but Ilona is more than used to sleeping in a communal space in the priory… Having a private room felt like an excessive luxury."

    "Though, there are strangers in the house, and some of them are men…"

    "… Edwin would have wanted her door locked. She goes to the door and turns the key in the keyhole, hearing a reassuring click."

    "After a silent prayer, she crawls into bed. Lying there, she feels a sense of unease and restlessness, and also feels strangely awake."

    "Ilona closes her eyes and tries to drift into sleep. Within the peaceful silence of the manse, rest came to her easier than expected."

    with longfade

    "The piercing sound of a howl wakes Kellac first, followed shortly by a woman's loud scream. His door opens with a slam, sensing something is incredibly wrong…"

    "Ilona hears footsteps rush past her room, and her eyes flutter open; registering what woke her. She puts on her habit, covering her head, and hurries out the door, unlocking it first…"

    "Kellac stops on the stairwell when he sees her, turning his head back to see Ilona. Edwin is not with him. She looks to the door next to hers, on the right."

    ke "There's no time to lose! See if you can wake him up, I'm going on ahead!"

    "He runs up the stairs. For a man who always seems so weary, there is a vivacity in his face now that danger is present."

    "Ilona knocks on Edwin's door, trying to hear for any sign of life in the room."

    il "Edwin? It's Ilona!"

    "Silence."

    "She knocks again, this time urgently. Still, there is nothing coming from the other side of the room."

    "She turns the handle. The door is locked, and there is no reply…"

    il "No… Please, no…"

    # SCENE 10

    "Ilona feels her heart lurch."

    "She stumbles up the stairs, finding Kellac at the door to what seems to be the master’s chambers."

    "He knocks urgently, and tries ramming the door with his shoulders, but grunts when the door wouldn't budge."

    ke "It's no use! Damn it! If only I were stronger…"

    ke "I'm going to get Anari! Something's wrong."

    ke "The servants' quarters are on the other side of the house, up the stairs. Get a master key for this door!"

    "Ilona nods and follows Kellac's instructions, passing through the now empty hall and up the stairs."

    "She finds Eisleigh first, and explains the situation."

    "Eisleigh's eyes go wide, and she fumbles in her long green robe, producing a dangling set of keys, nearly dropping them in her haste."

    ei "I- I have a copy of the master key. Come on! There's no time to waste!"

    # TRANSITION TO SCENE 11

    "When they rush back to the masters' chambers, there is no use for the master key. They find the door broken and battered, but no sign of Anari or Kellac yet."

    "Traces of blood are on the door, as with thick shards of wood splintering from its fractures."

    "Ilona and Eisleigh enter the bedroom, stepping over part of the broken door. It smells strongly of blood and burnt hair."

    "They lay their eyes on the blood-soaked bedsheets, and the dead figure of Uldin. His neck is mutilated; torn flesh hangs off of his body, and his eyes are blank."

    "Eisleigh holds a hand over her mouth, and squeezes her eyes shut."

    "A figure of a man hunched over a woman in a dress makes his presence known; he turns to look at them. His yellow eyes give off an eerie glint, as though it were an animal's."

    il "Edwin…"

    ed "Don't come any closer! Stay away…"

    "His voice sounds guttural. It's hard to make out in the darkness, but his arms look huge, and beastly… the fur mixed with the blood of open wounds and bruises."

    "With his body turned away, Ilona couldn't tell who it was in his arms, but she now sees a ring on the hand, and chestnut brown hair…"

    "The sound of footsteps rushes up the stairs again, and Ilona knows immediately who it is."

    an "Get away from him, Ilona!"

    an "I knew there was something wrong with him. I should've shot him dead when I had the chance…"

    "Instead of the cool and elegant Anari that Ilona had seen before, she disguises her sorrow with fury instead."

    "Ilona can’t move. With Anari's arrow trained on them, Kellac rushes in; carrying a healer's kit. Edwin sets the body of the woman down and backs away. Kellac checks the unburned section of her wrist."

    "There is only the sound of Kellac choking back his frustration and dismay."

    ke "I was too late… I'm so sorry… I couldn't save them."

    # SCENE 12 + 13

    "Kellac is on his knees, facing Salome's corpse. All the jovial cheer that he displayed since meeting Ilona vanishes, and he resembles a husk of a man."

    "Anari moves in after seeing that Edwin shows no signs of retaliation."

    an "We need to restrain him. Fleur's gone missing…"

    ed "I didn't do it… I wasn't the one who did this."

    an "An honest man would beg harder for his life. You sound like you've already accepted your execution."

    il "Wait! Please give us a minute. I… I want to talk to Edwin."

    an "…Fine. One minute, and no more. I'm sure you wouldn't be so stupid as to try anything… but be warned."

    "Ilona crouches down beside Edwin. His distant gaze lacks warmth and familiarity."

    il "Edwin, can you hear me?"

    ed "…"

    # choking back tears, but said similarly in the beginning scene
    il "Ed…"

    ed "I-I am so sorry, Ilona. I wasn't able to control it… "

    "Hearing him talk reassures her slightly. Ilona gingerly takes his wolf-like hands into hers. Even though his gaze is cold and stony, the hands still hold warmth."

    il "Do you swear that you didn't kill them?"

    ed "When I entered the room, they were already like this."

    il "Then— You weren't the one—"

    il "Something's wrong. Your hands… they're not turning back—"

    an "Stop — time's up."

    "Anari's voice is enough to cut the two apart, and Ilona lets go of Edwin's hands immediately."

    an "I can't say that I trust you quite yet, Ilona."

    an "You really seem like a clever girl... and who would dare suspect a nun of planning such a gruesome scene?"

    an "Turn yourself in quietly, Edwin, and I'll make sure her interrogation isn't painful."

    "Ilona isn't sure if Edwin obliged so easily because he feared for her safety, or if he truly has given up; like what Anari said earlier. He wordlessly lets Anari bind him with chains."

    "Anari escorts him forcefully out of the mansion, and takes him underground to a dungeon. The only thing Ilona sees before the doors close is Edwin's taciturn and listless expression."

    # TRANSITION TO SCENE 14 + 15

    "With Edwin locked away, the remaining members of the party gather in the town square: Ilona, Eisleigh, Kellac and Anari."

    "Nobody could find Fleur in the manse afterwards, her room and bed empty of her presence."

    "The sun has not risen yet, and the clouds are dark and looming. There's a damp chill in the air."

    ei "What now?"

    an "It's obvious that Edwin is guilty… but I'm not sure what to do with the nun."

    ke "Don't be hasty, Anari. There's a lot we don't know yet."

    ke "Besides, I'm certain I was the first one to wake up. I didn't see Ilona do anything suspicious."

    ei "That matches up with what I saw of her. It just doesn't seem like something Ilona would do from what I know of her..."

    an "What? You think she would let you in on her plots in one night?"

    ei "…That's precisely it. She's awful at keeping secrets."

    ei "If she really was involved, I don't think she would be able to hide it."

    "Anari tries hard to not grumble, though Eisleigh did have a point."

    an "Ilona. Did you know that the man was a werewolf before entering this town?"

    il "…Yes. In my presence, he's more capable of controlling his transformation."

    an "And yet you've been harbouring a monster, regardless of the consequences? Unfathomable…"

    il "I am searching for a way to cure him of his curse. That is all."

    il "Please, I honestly don't think he did it. There must be more to what happened - I can help you find it."

    ke "The town needs to know, we can't hide this for long. Not to mention, Fleur is still missing."

    ke "As long as we keep an eye on Ilona as she investigates, I think it should be safe."

    "Anari sighs at Kellac's advice. Ilona couldn't help but to be thankful for his ability to sway Anari's opinions for even just a moment."

    an "Fine. Let her run around, just make sure someone keeps an eye on her, always."

    an "I'll go first. You two assemble a search party for the forest in the meantime. I'll lead the search once you're ready."

    an "Ilona. You have until sundown. Prove that Edwin is innocent, or I'm going to personally make sure you won't like what’s coming to the two of you."

    with longfade

    # Go to act 2.
    jump act2
