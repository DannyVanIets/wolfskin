## The file for act 2.

label act2:

    # Show the intro of the act.
    # Makes sure that skipping is stopped, also autosaves.
    $ renpy.choice_for_skipping()

    $ quick_menu = False

    window hide

    scene bg fluffies
    with fade

    call screen intro(2)

    $ quick_menu = True

# SCENE 16
    stop music fadeout 3.0

    ## MASTER'S CHAMBER : MORNING TIME

    # FIXME shorter fade after all?
    scene bg masters chamber
    with longfade

    # TODO show Ilona and Kellac

    "Ilona takes a look once more at the corpses of Salome and Uldin."

    "Kellac examined the bodies when Edwin was being escorted to the dungeon."

    "According to Anari, his role as a physician was extensive and he treated many people during the war."

    "This also meant that he's seen many corpses, making him considerably accurate in determining the time of death."

    "The methods and reasons for their death are clear. To do a further examination, Kellac would have to perform an autopsy."

    # Show Uldin and Salome because the text is about them as victims
    show bw_ul_murder at left_center:
        zoom 0.5
    show bw_sa_murder at right_center:
        zoom 0.5 xzoom-1
    with dissolve

    play music 'audio/music/mastered/Haunting.ogg' fadein 2.0 volume 0.5

    "From what Ilona can see, Uldin died of blood loss from a wound to his neck, and Salome shows signs of burns surpassing the third degree."

    "There's swelling at her neck and spine; possibly a fracture. Both of them died at around the same time, shortly before they entered the room to witness the gruesome scenario."

    hide bw_ul_murder
    hide bw_sa_murder
    with dissolve

    show ilona_dim aaaa pensive at left:
        zoom 0.5
    show anari_dim look neutral at right:
        zoom 0.5
    with dissolve

    il "(Could Salome have survived that attack, even for just a moment?)"

    "Ilona looks around the room and sees the scorched walls and destroyed tapestries and paintings."

    il "(Apparently, Uldin was capable of using fire magic. Did Salome get caught in his attack? I can't really imagine that happening.)"

    show ilona_dim at gocenter_transform

    $ renpy.pause(1.0)

    show ilona_dim at centertoleft_transform:
        xzoom-1

    $ renpy.pause(1.0)

    "Ilona tries to find anything else in the room that could have been used. On the nightstand, there's a candle turned over. Droplets of now-hard wax mar the wood surface. "

    "The burns scorching the wall and room seem too significant to come from just a candle. Near the bed and on the floor are traces of fur. Some of it is burnt."

    show anari_dim talk angry closed with dissolve
    an "Anything out of place?"

    show ilona_dim open annoyed with dissolve:
        xzoom 1
    il "There's traces of fur, but that's about it. What about the other rooms?"

    show anari_dim open neutral with dissolve
    an "Eisleigh told me there was something that felt out of place in Fleur's room. I'll also let you look through Salome's room."

# SCENE 17

    ## SALOME'S BEDROOM

    scene bg salomes bedroom
    with longfade

    "Ilona decides to look in Salome's room first, the room closest to the master's chambers. The room is bright, orderly and spacious; and partly serves as Salome's study."

    "The most prominent part of the room is a writing table, items left strewn upon it as though she was in the middle of an important task."

    show ilona_dim at left:
        zoom 0.5
    show anari_dim look neutral at right:
        zoom 0.5
    with dissolve

    il "She asked you to go over the events of the day with her, after she met with us. I assume you came to her room, Anari?"

    show anari_dim neutral at right
    an "Correct. I gave my report about seeing you and Edwin for the lady's record-keeping. The one thing that's not where it should be is the chest. Though???"

    # Let Anari turn around to the right facing the chest
    show anari_dim angry neutral at right_center with dissolve:
        xzoom -1

    show ilona_dim talk
    il "What is it? Please, don't hold back."

    show anari_dim talk
    show ilona_dim neutral
    with dissolve
    an "I don't think it has anything to do with the murders. That chest is meant for Fleur when she is married. Salome had it made recently."

    # Anari turns back to face Ilona
    show anari_dim relaxed with dissolve:
        xzoom 1

    an "It's natural she might have moved it since I was last here. She did worry about Fleur's future, after all??? Salome was still considering which items should go inside. "

    "It surprises Ilona that Anari is suddenly so candid. Salome and Anari were closer in age, and it made sense that Anari acted as Salome's confidant."

    stop music fadeout 3.0

    ## FLEUR'S BEDROOM

    scene bg fleur bedroom
    with longfade

    "They then move to investigate Fleur's room. Ilona couldn't help but be curious about what Anari said earlier. Opening the young girl's room, both of them notice a distinct lump in the bed."

    "Ilona looks at Anari. They agree silently to move closer."

    "Anari does not pay any heed to the room's whimsical decor, but Ilona can't help but steal glances at the spectacle of floral and woodland motifs in her belongings as they pass through."

    "Last night, Ilona never thought too much of Fleur's fascination with strange and mythic tales, especially regarding the fair folk."

    "She thought it to be just a passing interest. Her room speaks otherwise; the girl seems utterly devoted to tales of fantasy."

    "When they reach the bed, Ilona isn't sure what to expect."

    "Anari remains behind her and nods, indicating for Ilona to pull back the covers. Ilona can see something that looks like it is carved from wood."

    play music 'audio/music/mastered/Echoing_Fleur_Theme.ogg' volume 0.5

    # wood effigy
    show effigy at center with longdissolve:
        zoom 0.5

    "It resembles a wood statue, or an effigy."

    "The face looks eerily like Fleur, her expression mysterious ??? neither happy nor sad. The rest of the body looks as though it remains trapped inside a still-living tree."

    show ilona_dim glance annoyed sweat at left:
        zoom 0.5
    show anari_dim blank fury yell fear at right:
        zoom 0.5
    with dissolve

    an "Impossible???"

    "Anari does not say anything else, but moves back from the effigy. Her hand is balled into a fist, and is shaking either from rage or fear."

    show anari_dim cringe

    an "I-I've seen quite enough. I don't want to remain in this ghastly room."

    hide anari_dim with dissolve
    show ilona_dim shock sad talk

    play sound 'audio/sfx/footsteps slow leather tile.wav'

    "She turns immediately on her heel. The sudden reaction surprises Ilona, and she is unsure whether to follow or not."

    ## HALLWAY

    scene bg hallway
    with longfade

    show ilona_dim at less_left:
        zoom 0.5
    show anari_dim closed talk angry shadow at extra_right:
        zoom 0.5
    with longdissolve

    stop sound fadeout 3.0
    "Finding nothing else of note in the room, Ilona rejoins Anari. She finds Anari with her back pressed to the wall, steadily taking deep breaths."

    "For a woman who seemed to fear nothing, Ilona can???t fathom why Anari looked so scared at that moment."

# SCENE 18

    il "Anari??? you don???t look too well. I think we should pause our investigation for the moment."

    show ilona_dim glance solemn with dissolve
    il "Umm??? would you like some tea?"

    show anari_dim look cringe with dissolve
    an "...Tea?"

    # Anari moves slightly to the left (from wall) to show outburst
    show anari_dim fury:
        ease 0.5 xcenter 1500

    an "Does it look like I???m in the mood for some tea right now? In the middle of this mess? Is there something wrong with your head, Sister? Have you forgotten the situation we find ourselves in?"

    show anari_dim blank yell
    an "Or are you trying to lace my drink with-"

    show ilona_dim pensive annoyed talk
    il "I can assure you, it???s none of that. I want to find the culprit as much as you do. But I???ll need your help for that."

    il "I only wish to see that you???re in good health to proceed, so I thought we could take a quick break-"

    show anari_dim open talk angry with dissolve
    an "With some tea, I get it. Very well, I must tell you that I despise the leaves from this country, so you'd better make a damn fine cup."

    show ilona_dim relaxed open neutral
    il "Are there any to your taste?"

    stop music fadeout 3.0

    show anari_dim worry neutral -shadow with dissolve
    an "???Fine black tea, with bitter orange. I think Uldin had some in his pantry."

    scene bg black with fade

    "Both of them fall silent. There is nobody in the house who can say what to do with Uldin's possessions??? Anari isn't even sure if he left a will."

    "Uldin isn't around anymore to enjoy what he had in life, that is certain."

    "Anari goes into the pantry and finds some tea bricks sealed in a container. She was sure that last night, Salome and Fleur did talk about this kind of tea."

    "Ilona, feeling some remorse as though the two of them were bandits, prepares the deceased man's tea according to Anari's instruction."

    "Trying her best to be hospitable, Ilona also serves it with milk and sugar, as Fleur did."

    play music 'audio/sfx/zapsplat clock.mp3' loop volume 0.1

    scene bg hall day
    show ilona_dim at left:
        zoom 0.5
    show anari_dim angry neutral at right:
        zoom 0.5
    with dissolve

    show ilona_dim smile pensive
    il "Here you go. Please, have some."

    "Ilona serves tea to Anari. As expected, Anari does not take any of the milk or sugar."
    play sound 'audio/sfx/zapsplat tea.mp3' volume 0.2
    extend " In contrast, Ilona puts a generous amount of both in hers. The taste was far too bitter for her to enjoy so early in the morning."

    show anari_dim closed raised neutral
    "Anari leans back in her chair, closing her eyes and taking in the aroma. She takes a sip before putting her tea cup down elegantly, without even the slightest clatter."

    show anari_dim angry
    "Ilona follows suit, but she is not nearly as graceful. Anari rubs her temples with the tips of her fingers before speaking again."

    show anari_dim smile
    an "Not bad. Tell me, are all nuns this annoying?"

    show ilona_dim annoyed neutral
    il "Pardon me?"

    show anari_dim look
    an "Whatever you're trying to do is futile. Re-examining the corpses or the rooms won't change anything ??? Edwin was the one who killed them."

    show ilona_dim aaaa pensive talk
    il "What makes you so sure of that?"

    an "I heard the details from Kellac and Eisleigh."

    scene bg masters chamber night
    with dissolve
    show salome_sil at right:
        xzoom-1
    with longdissolve
    "Anari details how the events played out: Salome screamed."
    scene bg door night dark
    show kellac_night at left:
        zoom 0.7 yoffset 300
    show ilona_night at right:
        zoom 0.7 xzoom-1 yoffset 300
    with dissolve
    extend " It was heard by Kellac and Ilona who were sleeping on the floor below. Edwin was not in his room."

    scene bg masters chamber night
    show salome_sil at right:
        xzoom-1
    show edwin_sil wolf at center:
        zoom 0.5 xzoom-1
    with dissolve

    $ renpy.pause(1.0)

    show salome_bw closed sad neutral at right:
        xzoom-1
    show edwin_bw fury furrow yell wolf at center:
        zoom 0.5 xzoom-1
    with longdissolve
    "Therefore, Edwin was already inside the master's chambers at the time of the murder."

    scene bg hallway night dark
    with dissolve
    "It would take some time for a person sleeping below the master's chambers to make it to the servants' quarters, which is on the opposite end of the manse."

    "Since Anari was on duty for her job as the head of the town guard, she could not possibly be at the crime scene during the murder."

    scene bg hall day
    show ilona_dim at left:
        zoom 0.5
    show anari_dim look neutral at right:
        zoom 0.5
    with dissolve

    stop music fadeout 5.0

    an "Everyone's locations were accounted for:"

    an "I was on patrol as the head of the town guard. Kellac was the first one to react to the scream, followed by you. Eisleigh was in her room."

    show anari_dim open angry smile
    an "Each of us were able to confirm each others' locations at the time of the murder. The only one who couldn't be found was Edwin."

    show ilona_dim closed talk
    il "How do you suppose that everyone is saying the absolute truth?"

    play music 'audio/music/mastered/Administer_Justice_Theme_Of_Ilona.ogg' volume 0.3 loop

    il "Kellac could have acted as if he had witnessed the murder. We have no account of what he was doing before that."

    il "There was also nobody around to confirm that Eisleigh was not at the crime scene, and I found her alone."

    show ilona_dim angry aaaa talk
    il "And finally, where was Fleur? You do understand where I???m coming from, yes?"

    show ilona_dim neutral
    show anari_dim look angry neutral
    an "...I do. You???re smarter than you look, nun."

    an "Indeed, Fleur was missing at the time of the murder. Nobody had seen her enter, or exit the manse. I'll give you that much, but I highly doubt she could be the murderer. She's far too frail."

    show ilona_dim glance annoyed talk
    il "The door was destroyed in the time it took for Eisleigh and I to return. How do you explain that?"

    show ilona_dim neutral
    show anari_dim open smile sweatdrop
    an "Does the door being destroyed really mean anything? It doesn't change the fact that Edwin was at the crime scene. Transformed."

    il "???"

    show anari_dim -sweatdrop
    an "Let me cue you in on this: out of everyone around here, you and Edwin are the most suspicious."

    an "The two of you are outsiders, whereas we???ve all known each other for a long time."

    show anari_dim look talk
    an "I don't plan on letting my bias against the two of you get the better of me, however. Let's start at the beginning: what could be the motivation for the murder?"

    an "Kellac was an associate of Uldin and I during the war. He???s selfless, to the point of stupidity. I guess serving as a medic will do that to you."

    an "It???s hard to admit this, but I consider Kellac to be a close friend. He is a kind-hearted man."

    show anari_dim closed relaxed neutral
    an "But that is no reason for letting him off the hook. He simply??? has no reason for murder."

    show ilona_dim talk solemn
    il "Please explain."

    show ilona_dim neutral
    show anari_dim talk
    an "He???s as kind as he is weak, so I doubt he could overpower both Uldin and Salome. Anything he could have ever needed, whether coin or rare books on magic, he could have simply asked Uldin."

    an "And Uldin wouldn't have hesitated, because they share quite the history."

    show anari_dim open
    an "Although, one thing I can tell you for sure is: Kellac is hiding something. Before he settled here, he had done nothing but walk and regret for five years, or so he says. It keeps him up at night."

    show anari_dim look neutral
    an "Whether it???s related to this case, I do not know."

    show ilona_dim open neutral
    il "Hmm??? I see."

    show ilona_dim talk
    il "What about Eisleigh? I honestly don???t know much about her."

    show anari_dim talk
    show ilona_dim neutral
    an "She acted as an assistant to Salome; to help with keeping the town running, organization and tasks."

    an "She's been doing her fair share of blunders lately, but I know she takes her job seriously???  Perhaps she's just daydreaming more."

    show anari_dim open worry smile
    an "I'm not saying that she's incompetent, let me get that straight. As long as her clumsiness doesn't get in my way."

    an "Though, I don't know much about her either to determine her motivation."

    show ilona_dim talk
    il "Is she close with Fleur? They are almost the same age."

    show anari_dim closed
    an "Not really, Eisleigh and Fleur seem to be in their own heads. Eisleigh, with the study of magic as an apprentice, and Fleur, being a little troublemaker and a prankster."

    stop music fadeout 3.0

    show anari_dim angry glance smile
    an "My niece still plays jokes and tricks, even at her age. It's all childish nonsense???"

    show anari_dim neutral fear with dissolve
    an "Fleur???"

    $ renpy.pause(1.0)

    scene bg fleur bedroom with dissolve

    "Anari is confident up until this point ??? calm and refined. Now, dread and restlessness begin to take over."

    show effigy at center with dissolve:
        zoom 0.5

    "Yet she could not overlook the superstitions of the fae, even for someone as rational as her."

    "The wooden effigy of Fleur, her disappearance, and the uncertainty behind the murder tarnishes Anari's unshakeable visage."

    "Moreover, Ilona???s demeanour and her relationship with Edwin???"

    scene bg hall day
    show ilona_dim sad pensive at left:
        zoom 0.5
    show anari_dim angry glance neutral fear at right:
        zoom 0.5
    with dissolve

    il "Are you feeling alright, Anari-"

    show anari_dim yell blank
    an "Don't you dare patronize me, woman! Who do you think you are, prying so brazenly? Take your high and mighty Servant of God tripe elsewhere!"

    show anari_dim blank cringe
    an "Trying to save that monster lover of yours??? Are you out of your mind?"

    show ilona_dim aaaa angry neutral with dissolve
    il "I do not know what has gotten into you all of a sudden, but I do not appreciate being spoken to like this."

    show ilona_dim closed yell with dissolve
    il "I showed compassion for you, when time is of the essence ??? instead of listening to you berate me, I should be finding the murderer!"

    show ilona_dim neutral
    show anari_dim neutral -fear
    with dissolve
    "Silence looms over, waiting to be broken. Anari glares, her hand instinctively touching one of her arrows. She grimaces and folds her arms across her body."

    play music 'audio/sfx/zapsplat clock.mp3' loop volume 0.3

    show ilona_dim pensive sad with dissolve
    il "I???m sorry. I didn???t - I didn't mean to lash out at you like that. It???s just... I want to find the culprit behind this mess."

    show anari_dim open relaxed talk with dissolve
    an "It???s fine."

    an "If the ???I??? standing here was the Anari a couple of years back, you would have been mutilated by now."

    an "However, I did step out of line. Who you choose to be with is none of my business. I know violence for the sake of it won???t solve anything."

    show anari_dim look smile
    an "Though we may not see eye to eye on everything, nun, I quite like you now. The tea must have swayed my opinion, I'm sure."

    show anari_dim nii
    an "Since we???re on good terms now-"

    show ilona_dim glance annoyed
    il "(Are we?)"

    an "-and I can???t bear to see you with such a sad face, I???ll let you in on a secret: there's a cure for lycanthropy. You may yet be rid of the beast that lies within your dear beloved."

    show anari_dim look
    an "For your and Edwin???s sake, I suggest you use it."

    il "Which is?"

    stop music fadeout 2.0

    $ renpy.pause(2.0)

    show anari_dim blank fury grin with vpunch
    an "It???s for the lycan to die, of course!"

    show ilona_dim shock sad talk sweat with dissolve
    il "???"

    show anari_dim nii angry with dissolve
    an "Ahahahahaha, the look on your face. Brilliant."

    show anari_dim look worry smile with dissolve
    an "Now now, don???t give me that look. I was only kidding. Partly."

    show anari_dim relaxed with dissolve
    an "Anyhow, enough chit-chat. I must go and make preparations to lead the search party for Fleur."

    show ilona_dim glance solemn with dissolve
    il "I should take my leave, as well. There is much to consider after what we???ve seen today."

    show anari_dim angry grin
    an "Indeed. I can???t wait to hear what kind of answer you will give at sundown. Heh."

    show ilona_dim pensive neutral -sweat
    il "I can't ever tell if you're on my side."

    show anari_dim open grin
    an "I wonder, too."

# SCENE 25

    ## TOWN SQUARE

    scene bg town plaza morning
    with longfade

    "Anari leads her out of the room and back into the town square."

    scene bg_repeating_town_plaza_blurry

    play sound 'audio/sfx/heartbeat.mp3' loop volume 0.2
    "Ilona is covered in a light sweat. She can feel her heart leaping frantically inside her chest just by thinking about the conversation she had with Anari."
    show slow_eyeblink_filter
    "Kellac is waiting at the square and he exchanges some words with Anari. Their voices are indistinct and quiet."

    "Ilona???s own heart sounds louder in her ears, so much that it???s making her weak and dizzy??? Her extremities are tingling."

    scene bg_repeating_town_plaza_kellac_blurry with fade
    queue music 'audio/music/mastered/Fade_Away.ogg' volume 0.2

    "It is taking everything for Ilona to stay conscious. Anari glances at her before smiling to herself and walking away. Ilona sees a figure move in front of her, clad in black robes???"

    ke "Where to?"

    il "???"

    scene bg_transition_blurry_kellac_extreme

    "She can barely recognise the voice. Ilona's vision blurs and the ground beneath her feet feels unsteady."
    show slow_eyeblink_filter
    ke "Hey! Is everything alright? Stay with me!"

    stop sound

    # TRANSITION TO BLACK.
    scene bg black
    with fade

    stop music fadeout 2.0

    ke "Ilona?"

    # NOTE for SFX: (vpunch effect + sound of collapsing?)
    with vpunch
    play sound 'audio/sfx/Gravel Floor Fall 1.mp3' volume 0.6

    $ renpy.pause(2.0)

    ## KELLAC'S ROOM : NOON TIME
    with logodissolve

    scene bg kellacs room
    with longfade

    play music 'audio/ambience/bbc fire.mp3' volume 0.3
    show slow_eyeblink_filter
    "When Ilona opens her eyes again, she's in an unfamiliar bed and room. The air is heavy with a medicinal smell  ??? suffocatingly so."

    "She feels far too aware of her body. Her mouth feels dry, and her heart still feels like it's beating too fast."

    show ilona_dim closed sad talk at left with dissolve:
        zoom 0.5

    il "Did-? Was I????"

    show kellac_dim raised smile at less_right with dissolve:
        zoom 0.5 xzoom -1

    ke "Take it easy. You're safe ??? we're still in the manse."

    show ilona_dim open neutral
    il "Just how long was I out for?"

    show kellac_dim relaxed talk with dissolve
    ke "It's almost midday."

    show ilona_dim glance annoyed sweat with dissolve
    "Ilona grimaces. Too much time was lost. She moves her arms slowly, her body heavy."

    "Sensation comes back into the tips of her fingers and the unpleasant tingling stops. The smell of herbal medicine starts to become more bearable to her senses."

    show kellac_dim anger neutral with dissolve
    ke "It wasn't an ordinary fainting spell. You should have regained consciousness faster if it was simply fatigue and stress."

    ke "I've taken precautions, and treated you for poisoning."

    il "Then, do you think ??? Did Anari try to poison me?"

    show kellac_dim glance
    ke "???I suppose you can't really rule out that possibility. Did you eat or drink anything with her?"

    show ilona_dim open
    il "Only tea, but I was the one who suggested and prepared it."

    il "I didn't see her slip anything in my drink. In fact, she was convinced I was trying to poison her???"

    show kellac_dim closed relaxed talk
    ke "She's not the type to take such a cowardly approach."

    ke "She may seem cruel, but I don't think she would go that far to sabotage your efforts and put a stop to you."

    stop music fadeout 5.0

    show ilona_dim relaxed -sweat
    il "It seems you and Anari know each other well. I don't have much time, but I need to ask:"

    show ilona_dim sad
    il "She had an extreme reaction upon seeing a wooden statue resembling Fleur. What could have terrified her so much about it?"

    show kellac_dim anger neutral with dissolve
    ke "Truth be told, I don't really know much about her history, only rumours. She must think that the statue has to do something with the fae ??? Something in her past made her be wary of them."

    ke "Fleur admires the fair folk. The wooden statue is too elaborate to be one of Fleur's pranks, especially with the death of her parents???"

    il "So her aversion to seeing the statue has to do with her trauma, and distaste for Fleur's fae-related tricks?"

    show kellac_dim glance talk with dissolve
    ke "Something like that. Anari hates being pitied, and she doesn't show pity for anyone else either."

    ke "She would be terrified at the thought of Fleur being spirited away by the fair folk. It's not something that she could ever accept - That's probably why she is leading the search."

    scene bg black with fade

    "Ilona shifts her body off the bed, able to move freely again. Kellac invites her to take a seat, and Ilona does so. He pours her some clear water. The smell of a simmering stew wafts from the kitchen."

    scene bg kellacs room
    show ilona_dim at left:
        zoom 0.5
    show kellac_dim glance anger neutral at less_right:
        zoom 0.5 xzoom -1
    with longdissolve

    play music 'audio/music/mastered/The_Town.ogg' volume 0.5 fadein 1.0

    show kellac_dim relaxed talk open with dissolve
    ke "About the tea you had with Anari ??? was there anything odd about it? I'm asking because before the banquet, I gave Uldin his medicine, a powerful soporific."

    show kellac_dim anger
    ke "There were three less doses in the pantry when I checked."

    show ilona_dim sad pensive talk with dissolve
    il "Then, you think someone last night???"

    play sound 'audio/sfx/3 knocks.wav' volume 0.3
    "There's a light knock on the door. Kellac tells them to enter. It's Eisleigh."

    play sound 'audio/sfx/wood door open and close.wav' volume 0.5
    show eisleigh_dim worry neutral at extra_right with dissolve

    ei "Oh, Ilona ??? I heard you fainted in the town square. I was worried."

    show kellac_dim nii smile relaxed with dissolve
    ke "Ah, yes! I invited Eisleigh over for lunch. Ilona, you probably haven't eaten at all yet, have you? You should try to eat, even if it's just a little."

    show ilona_dim glance neutral sweat with dissolve
    il "???"

    show kellac_dim open worry neutral with dissolve
    ke "???I guess it's hard to trust anyone after what you've been through."

    show ilona_dim pensive -sweat
    il "No, it's fine??? I'll eat with you. You're right, I probably can't do much if I don't take care of myself."

    scene bg black with fade

    "Kellac serves Eisleigh and Ilona a rustic stew, with dark bread and clear water on the side. During the time eating together, Eisleigh asks about the investigation, and Ilona repeats Anari's reasoning surrounding Eisleigh and Kellac."

    "Ilona thought that Anari's defence was unbreakable, but there was one new thing she learnt about last night???"

    scene bg hall day
    show ilona at left:
        zoom 0.5
    show kellac glance anger neutral at less_right behind eisleigh:
        zoom 0.5 xzoom -1
    show eisleigh worry neutral at extra_right
    with longdissolve

    il "So are you considering the possibility someone tried to drug us during the banquet?"

    show kellac open talk with dissolve
    ke "That's what I feared, at least. Anari and I left before that, so I don't really have a clear picture of what exactly happened."

    show kellac closed
    show ilona glance solemn
    with dissolve
    "Ilona stares at an empty teacup in the room and realizes something ??? if the tea she served Anari was different, but she used the same sugar from last night???"

    show ilona open aaaa talk with dissolve
    il "The sugar ??? it must have been tampered with! Last night, I didn't add any to my tea because I didn't want to be rude, but I took some when I had tea with Anari."

    show eisleigh glance small with dissolve
    ei "I remember Fleur was really insistent on putting sugar in my tea. I did think that was weird."

    show kellac open
    ke "How much sugar did you put in your tea this morning, Ilona?"

    show ilona glance sad smile sweat with dissolve
    il "Four spoonfuls???"

    show eisleigh surprise talk with dissolve
    ei "Uhh, that sure is a lot???"

    show kellac closed relaxed smile sweat with dissolve
    ke "Goodness, no wonder you were out for so long! I'm surprised Anari didn't get on your case for adding tea to your cup of sugar."

    show eisleigh angry glance small with dissolve
    ei "I think we can confirm this theory to be true then: someone was trying to put us into a deep sleep - and there's a chance they were trying to target Edwin specifically."

    show ilona open -sweat
    il "Then that would implicate Salome, or Fleur, most likely. They were the ones who prepared the tea last night."

    show eisleigh closed evil neutral
    ei "It's not like I can deny it, but..."

    show kellac glance anger talk with dissolve
    ke "Uldin could be involved, too."

    ke "The truth is??? the medicine he uses is made to look inconspicuous on purpose."

    show kellac neutral
    ke "I never inquired too closely about it, but he comes from a rather unscrupulous family; it wouldn't surprise me if he was aware of this plot."

    scene bg black with fade

    "Kellac seems to know the most about Uldin's family and his circumstances, so Ilona asked him for more information."

    show uldin_bw at center with dissolve:
    "Uldin suffers from insomnia and slept in separate arrangements so as to not disturb his wife."

    "Last night was also one of the rare occasions when Uldin was back in town, as he travelled frequently for his research studying magic."

    "Salome often handles the day to day affairs of managing Belorov. Uldin came back a day ago, and his return was welcomed back with a feast on All Hallows' Eve."

    hide uldin with dissolve

    stop music fadeout 5.0

    "On the topic of magic, Eisleigh recalls something that she needed to discuss."

    scene bg hall day
    show ilona at left:
        zoom 0.5
    show kellac glance relaxed neutral at less_right behind eisleigh:
        zoom 0.5 xzoom -1
    show eisleigh worry neutral at extra_right
    with fade

    ei "Could you tell us more about how Edwin is able to transform into a werewolf? Have you ever seen him do it?"

    show ilona glance solemn with dissolve
    il "No, I haven't. When he transforms, even when I ask it of him, he tells me to look away or to close my eyes."

    show kellac sweat worry talk with dissolve
    ke "Wait, why do you ask him to transform? What do you do when he's a werewolf?"

    show ilona neutral blush sad with dissolve
    il "It's??? a secret."

    show eisleigh open yell angry with dissolve
    ei "Secret??? Wait, that's precisely it!"

    show kellac -sweat
    show ilona open talk sweat
    with dissolve
    "Everyone else looks at Eisleigh in alarm."

    play music 'audio/music/mastered/Haunting.ogg' fadein 1.0 volume 0.5

    show ilona -sweatdrop
    show eisleigh neutral
    with dissolve
    ei "I heard of shapechangers before while studying cursed objects. They would use either an ointment, or the pelt of an animal, to assume the form of a beast."

    show eisleigh look
    ei "If the curse was tied to his body, he wouldn't fear you witnessing his transformation."

    show eisleigh small glance
    ei "But what if it was an item? If he feared betrayal, he wouldn't even show it to an ally."

    show eisleigh closed
    ei "Besides, there's always a risk involved in keeping that item safe ??? so it is better that only the bearer knows of it, because it could get lost, or destroyed, or..."

    show ilona aaaa neutral
    il "??? stolen."

    show kellac anger neutral
    "Both Kellac and Ilona look at Eisleigh with tense faces. Ilona isn't sure what to be more surprised at: Eisleigh's incredible reasoning and knowledge, or that someone would go as far as to steal an item uncertain to be in Edwin's possession."

    show eisleigh talk open
    ei "There is a high chance that this cursed item still exists. Had it been destroyed, he would have died along with it."

    scene bg moon with dissolve
    ei "This would give us a reason as to why Edwin was drugged last night: Uldin and Salome are sharp, and they might have caught onto Edwin being a werewolf early on."

    il "If we return this item to Edwin, would it restore the transformed arms back to human form?"

    ei "It's entirely possible, if that's what controls the transformation. A cursed item like that can generally only be bound to one person."

    ei "Someone else could have also used it, but??? Uldin would understand the consequences of such a thing. I highly doubt it would be him."

    scene bg hall day
    show ilona pensive aaaa at left:
        zoom 0.5
    show kellac glance anger neutral at less_right behind eisleigh:
        zoom 0.5 xzoom -1
    show eisleigh angry open neutral at extra_right
    with fade

    ke "Even so, finding this item might lead us to  finding the true culprit, or at least help make sense of this tragedy???"

    show kellac closed talk
    ke "You might not be able to convince everyone that Edwin is innocent, otherwise."

    show ilona sad neutral
    il "Yes, Anari wouldn't accept it so easily... What would it take to convince her of Edwin's innocence?"

    show kellac worry open neutral sweat
    ke "Short of having the culprit confess their crime, or finding Fleur in hope for an answer??? I don't know."
    $ renpy.pause(2.0)

    scene bg black with fade

    $ renpy.pause(1.0)

    scene bg fluffies with logodissolve

# SCENE 32

    ## HALLWAY
    scene bg hallway
    with longfade

    play sound 'audio/sfx/stairs ascending slow.wav'
    "The three of them start their search for the cursed item. Based on Anari's report, Kellac confirms with Ilona that nobody was able to enter or exit the town after Ilona and Edwin entered."

    "Eisleigh was eager to help out in any way possible now that there was a chance of witnessing or finding a cursed magical object."

    show ilona at less_left:
        zoom 0.5
    show kellac at extra_left behind ilona:
        zoom 0.5
    show eisleigh open worry neutral at right
    with dissolve

    ei "Kellac knows this, but I am not meant to have a copy of the master key."

    show eisleigh closed
    ei "I used to be a thief before I came here. The reason why I was an assistant to this household, was because I tried to steal one of Uldin's rare books???"

    show eisleigh look smile relaxed
    ei "However, I've put the past well behind me. Uldin made me his friend instead of punishing me, and I'm thankful for that."

    play sound 'audio/sfx/footsteps slow trainers.wav'

    ## MASTER'S CHAMBER
    scene bg masters chamber
    with longfade

    show bw_ul_murder at left_center:
        zoom 0.5
    show bw_sa_murder at right_center:
        zoom 0.5 xzoom-1
    with dissolve

    "Ilona can???t help but find this suspicious."

    "They start their search around Uldin's chambers. Once again, they see the mutilated corpse of Uldin, and the corpse of Salome, burned beyond recognition???"

    "Despite thoroughly searching the bodies, the trio was unable to find the cursed item or anything else of importance."

    stop music fadeout 5.0

    ## SALOME'S BEDROOM
    scene bg salomes bedroom
    with longfade

    "They move onto Salome's room. Nothing appears to have been touched since the last time Ilona was here with Anari. Like Anari, Eisleigh comments that the chest was moved and then moves to inspect it."

    show eisleigh angry small glance at right_center with dissolve:
        xzoom -1

    ei "This chest??? Last time I saw it, it wasn???t locked. Salome was still re-arranging it to look nice."

    ei "Let me try opening it???"

    play sound 'audio/sfx/old keys jingle.mp3'
    "Eisleigh pulls out a set of various different keys and picks, agitating each in the keyhole to no avail."

# SCENE 33

    show ilona happy sad sweat at less_left:
        zoom 0.5
    show kellac at extra_left behind ilona:
        zoom 0.5
    with dissolve

    il "I thought you said you put the past behind you."

    show eisleigh nii grin relaxed
    ei "I did, but I thought the tools might come to be useful one day. We're doing a good thing, aren't we? Lockpicking is not inherently evil."

    show kellac closed raised smile sweat
    ke "Full of surprises, eh? I trust you're not making excuses now."

    show eisleigh angry glance small
    ei "Of course not, I merely-"
    show eisleigh grin nii relaxed
    play sound 'audio/sfx/bolt metal unlock.mp3'
    extend " Ah-ha! I got it!"

    play sound 'audio/sfx/lock metal.mp3' volume 0.3
    "She jams the lockpick into the keyhole and wriggles it around. A faint 'click' is heard."

    ## EISLEIGH'S BLOOD

    $ renpy.pause(0.3)

    scene bg wound1

    play sound 'audio/sfx/stab flesh.mp3' volume 0.8
    "???"

    scene bg wound2
    play sound 'audio/sfx/stab flesh 2.mp3' volume 0.8
    extend "\n???"

    scene bg wound3
    play sound 'audio/sfx/stab flesh.mp3' volume 0.8
    extend "\n??????"

    scene bg wound4
    play sound 'audio/sfx/stab flesh 2.mp3' volume 0.8
    "??????"

    scene bg wound5
    play sound 'audio/sfx/stab flesh.mp3' volume 0.8
    extend "\nFive stabs pierce the soft flesh of Eisleigh's hand."

    play music 'audio/music/mastered/Fade_Away.ogg' volume 0.2 noloop

    ## SALOME'S BEDROOM

    scene bg blood with hpunch

    ke "Eisleigh!"

    ei "Aaaaaaaaghh! It??? It hurts??? It won't stop bleeding!"

    play sound 'audio/sfx/zap clothes rustle.mp3'
    "Kellac fumbles through his thick, heavy cloak, drawing out a clean cloth for use as a compress."

    scene bg salomes bedroom
    with fade

    show kellac sweat yell anger at center behind eisleigh:
        zoom 0.5
    show ilona shock sad talk at left:
        zoom 0.5
    show eisleigh fear worry talk at right_center:
    with dissolve

    ei "We need to do something!"

    show kellac neutral -sweat
    ke "There should still be some medical supplies in my room. Let's move there."

    # Ilona moves slightly to the right
    show ilona pensive neutral:
        ease 0.5 xpos 130

    il "Do you need my help? I know some healing magic-"

    show kellac relaxed closed
    ke "It???s all right. I???ve got this."

    show kellac glance
    ke "I just need to slow the bleeding and elevate the injury site. Don't touch anything else in this room. I'll be back soon."

    hide kellac
    hide eisleigh
    with dissolve

    play sound 'audio/sfx/stairs descending slow.wav'

    "Kellac and Eisleigh make their descent down the stairs. All that remains near the chest is the blood that poured out from Eisleigh's hand, the lockpick set, and Ilona."

    show ilona closed
    "The hairs on Ilona???s arms raise and she can feel her heart beat faster. She puts her hand on her chest, as though uttering a short prayer."

    stop music fadeout 5.0

    show ilona pensive annoyed with dissolve
    il "Breathe. If the chest was a trap, then there has to be something in there that someone doesn???t want found."

    show ilona pensive neutral:
        ease 1.0 xpos 800

    play sound 'audio/sfx/old keys jingle.mp3'
    "Despite her best instincts, Ilona picks up the lockpicks Eisleigh used. She spots a thin tool and uses it to pry the wood chest open???"

    "The trap was already disengaged, the danger gone. She sighs with relief."

    hide ilona

    show bg blood with dissolve

    play music 'audio/sfx/creepy wind a.ogg' volume 0.2 fadein 2.0

    "Nestled underneath delicate pieces of jewelry and other finery lay the red and glistening gold of a sash. It has bloodstained, hoary fur on one side."

    il "This must be it???"

    "Ilona touches the wolfskin. She thinks back to meeting Salome, and the dissonance between that friendly encounter and the thought of Salome as a cold-blooded killer."

    il "(Salome seemed so kind and caring. Could someone like that really be a murderer?)"

    play sound 'audio/sfx/gynation paper.wav'

    "A slip of paper falls out with the wolfskin, the contents addressed to a sculptor."

    "According to the paper, the deposit was paid for, but the project was never finished and was thus refunded. A note explains that the item was delivered yesterday."

    il "(It looks like Salome bought something, but the final product was never finished? This could be important - I???d better hold onto this.)"

    il "(What about this chest? Did Fleur witness the murder? Did she take the wolfskin and leave it as a message in her mother's room?)"

    il "(But the chest is trapped, and placed in the open??? That doesn't make sense. Why would she want us to find it, only to hurt us?)"

# SCENE 34

    ## MANSE
    scene bg chapel
    with longfade

    $ renpy.pause(3.0)

    stop music fadeout 5.0

    play sound 'audio/sfx/footsteps slow trainers.wav' volume 0.4
    "Ilona makes her way to where Edwin is imprisoned. The dungeons are behind the ruins of the chapel, which is on the south-east side of the manse."

    stop sound
    play sound 'audio/sfx/old keys jingle.mp3'
    "She inserts the lockpicks into the keyhole. Ilona had only witnessed Eisleigh do it once, and it???s not as easy as it looks."

    $ renpy.pause(3.0)

    play sound 'audio/sfx/metal door.wav' volume 0.7
    "After what seems like an eternity, the door opens with a loud click and a metallic groan."

    play music 'audio/ambience/janbezo wind.ogg'

    ## DUNGEON
    scene bg dungeon
    with longfade

    "Fearing that Anari, or someone else, will hear her in the dungeon, she hesitates. If she stays behind??? There was no knowing what the others would do if they laid their eyes on the wolfskin."

    "Kellac and Eisleigh may have seemed cooperative up until now, but that could change if they lusted after its power for themselves."

    "Now is Ilona???s only chance to return it to Edwin privately."

    stop music fadeout 1.0

    # close-up of Ilona
    show ilona_dim closed at left with dissolve:
        zoom 0.6

    il "I must have courage. I know that I made the right decision."

    il "If this can ease his spirits, even just a little, then it will have been worth it."

    il "(We're so close. Salome must be the one who did it??? If I can just get Edwin to confirm it, then I won't have any fear.)"

    hide ilona_dim with dissolve

    play sound 'audio/sfx/footsteps slow trainers.wav' volume 0.3

    show edwin_dim wolf distant at right with dissolve:
        zoom 0.6 yoffset 200

    "Edwin is sitting in the darkness. His eyes make out the figure in white, clutching the wolfskin in her hand."

    show edwin_dim fear yell sweat with dissolve
    ed "Ilona? You shouldn't be here. Wait, you found the???"

    play music 'audio/music/mastered/Administer_Justice_Theme_Of_Ilona.ogg' volume 0.5 fadein 1.0
    show ilona_dim pensive solemn at easeinleft_transform:
        zoom 0.6 yoffset 30

    il "I was alone when I took it. Nobody wore it, either."

    show edwin_dim closed talk with dissolve
    ed "???Thank goodness you're okay. Where did you find it?"

    show ilona_dim aaaa with dissolve
    il "Salome's bedroom. Inside a chest meant for Fleur."

    show edwin_dim fury yell with dissolve
    ed "What? That's???"

    show edwin_dim talk with dissolve
    "Edwin falters, lost for words."

    hide ilona_dim
    hide edwin_dim

    show bg black with fade
    "Ilona kneels down, returning the wolfskin to Edwin. She asks where he normally would wear it."
    play sound 'audio/sfx/zap clothes rustle.mp3' volume 0.3 fadeout 1.0

    "After he tells her, she follows his direction and ties it to the inside of a thick leather piece around his waist."

    play sound 'audio/sfx/zap chain drop.mp3' volume 0.3 fadeout 1.0

    "The chains fall to the floor, unbinding his previously thick wolf-like arms  ??? now restored to human form."

    $ renpy.pause(1.0)

    scene bg dungeon
    show edwin_dim wolf distant at right:
        zoom 0.6 yoffset 220
    with fade

    $ renpy.pause(1.0)

    show edwin_dim -wolf with longdissolve

    $ renpy.pause(1.3)

    show edwin_dim open grin with dissolve
    ed "You've saved my life once again??? Thank you."

    show ilona_dim blush glance neutral solemn at left with dissolve:
        zoom 0.6 yoffset 20 xpos 500
    il "Please, there's no need to thank me. It's given me a chance to talk to you again??? Do you think you can tell me more about the murder?"

    show edwin_dim glance talk
    ed "Of course ??? though you probably know more about it than I do."

    show ilona_dim open neutral -blush with dissolve
    il "If I think of who could have been present in the Master's chambers at the time, only two people remain. Did Salome murder Uldin? I've gathered that they must have died from the wounds they inflicted on each other. Am I correct?"

    show edwin_dim angry furrow yell
    ed "From what I could tell, yes. But I??? I???ve already put you through too much. You have to stop this investigation. There???s no use in getting your hopes up."

    stop music fadeout 3.0

    show ilona_dim aaaa open yell with dissolve
    il "...What? I don't understand. We're so close to finding out the truth! What is there left to hide?"

    play music 'audio/ambience/janbezo wind.ogg'

    show edwin_dim talk
    ed "??? If I were to live my life honestly... If I were not a monster??? You wouldn't have to keep living a lie."

    show ilona_dim talk
    il "Earlier today, I saw you holding Salome's corpse in your arms. What happened?"

    show edwin_dim sad -furrow talk
    ed "I hid the answer from you for a reason. Please, don???t pry any further???"

    show ilona_dim pensive annoyed tears with dissolve
    il "...You really did kill her."

    show edwin_dim distant furrow with dissolve
    "His eyes are empty and cold. At his loss for words, Ilona's heart sinks. Her hands tremble, and she lowers her head."

    show ilona_dim baby sad with dissolve
    il "No??? There???s no way??? I??? You couldn???t have???"

    ed "I should've said something sooner rather than have you go through all of this. I'm sorry."

    show ilona_dim cry wail yell aaaa with dissolve
    il "I believed you were innocent!"

    show edwin_dim talk sad -furrow with dissolve
    ed "If it truly were that simple, then??? Well, I wouldn???t have been locked up."

    show ilona_dim cry weep talk sad with dissolve
    "She chokes back her tears before gathering her composure and speaking again."

    show ilona_dim pensive baby talk with dissolve
    il "Tell me everything. Even if the truth will damn us both??? I need to know."

    # Go to act 3.
    jump act3
