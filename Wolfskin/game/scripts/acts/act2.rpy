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

    scene bg forest night
    with fade

# SCENE 16

    play music 'audio/music/Haunting.ogg'

    "Ilona takes a look once more at the corpses of Salome and Uldin."

    "Kellac examined the bodies when Edwin was being escorted to the dungeon."

    "According to Anari, his role as a physician was extensive and he treated many people during the war."

    "This also meant that he's seen many corpses, making him considerably accurate in determining the time of death."

    "The methods and reasons for their death are clear. To do a further examination, Kellac would have to perform an autopsy."

    "From what is seen, Uldin died of blood loss from a wound to his neck, and Salome shows signs of burns surpassing the third degree."

    "There's swelling at her neck and spine; possibly a fracture. Both of them died at around the same time, shortly before they entered the room to witness the gruesome scenario."

    il "(Could Salome have survived that attack, even for just a moment?)"

    "Ilona looks around the room, seeing the scorched walls and destroyed tapestries and paintings."

    il "(Apparently, Uldin was capable of using fire magic.{p}Did Salome get caught in his attack? I can't really imagine that happening.)"

    "Ilona tries to find anything else in the room that could have been used. On the nightstand, there's a candle turned over. Droplets of now hard wax marred the wood surface. "

    "The burns scorching the wall and room seem too significant to come from just a candle. Near the bed, and on the floor are traces of fur. Some of it is burnt."

    an "Anything out of place?"

    il "There's traces of fur, but that's about it. What about the other rooms?"

    an "Eisleigh told me there was something that felt out of place in Fleur's room.{p}I'll also let you look through Salome's room."

    stop music fadeout 3.0

# SCENE 17

    "Ilona decides to look in Salome's room first, the room closest to the master's chambers. The room is bright, orderly and spacious; and partly serves as the lady's study."

    "The most prominent part of the room is a writing table, items left strewn upon it as though she was in the middle of an important task."

    il "She asked you to go over the events of the day with her, after she met with us. I assume you came to her room, Anari?"

    an "Correct. I gave my report about seeing you and Edwin for the lady's record-keeping.{p}The one thing that's not where it should be is the chest. Though…"

    il "What is it? Please, don't hold back."

    an "I don't think it has anything to do with the murders. That chest is meant for Fleur when she is married. Salome had it made recently."

    an "It's natural she might have moved it since I was last here. She does worry about Fleur's future, after all… Salome was still considering which items should go inside. "

    "It surprises Ilona that Anari became so candid at this moment. Salome and Anari were closer in age, and it made sense that Anari acted as Salome's confidant."

    "They then move to investigate Fleur's room. Ilona couldn't help but be curious about what Anari said earlier. Opening the young girl's room, both of them notice a distinct lump in the bed."

    "Ilona looks to Anari. They agree silently to move closer."

    "Anari did not pay any heed to the room's whimsical decor, but Ilona can't help but steal glances at the spectacle of floral and woodland motifs in her belongings as they pass through."

    "Last night, Ilona never thought too much of Fleur's fascination with strange and mythic tales, especially regarding the fair folk."

    "She thought it to be just a passing interest. Her room speaks otherwise; the girl seems utterly devoted to tales of fantasy."

    "When they reach the bed, Ilona isn't sure what to expect. Anari remains behind her, and nods for Ilona to pull back the covers. Ilona could see something that looked like it's carved from wood…"

    "It resembles a wood statue, or an effigy."

    # TO DO: Implement Fleur's Theme

    "The face looks eerily like Fleur, her expression mysterious; neither happy or sad. The rest of the body looks as though it remains trapped inside a still-living tree."

    an "Impossible…"

    "Anari does not say anything else, but moves back from the effigy. Her hand is balled into a fist, and is shaking, either from rage or fear."

    an "I-I've seen quite enough. I don't want to remain in this ghastly room."

    "She turns immediately on her heel. The sudden reaction surprises Ilona, and she is unsure whether to follow or not."

    "Finding nothing else of note in the room, Ilona rejoins Anari. She finds Anari with her back pressed to the wall, steadily taking deep breaths."

    "For a woman who seemed to fear nothing, Ilona couldn't fathom why Anari looked so scared at that moment."

# SCENE 18

    il "Anari… you don’t look too well. I think we should pause our investigation for the moment."

    il "Umm… would you like some tea?"

    an "...Tea?"

    an "Sister, does it look like I’m in the mood for some tea right now? In the middle of this mess? Is there something wrong with your head, Sister? Have you forgotten the situation we find ourselves in?…"

    an "Or are you trying to lace my drink with-"

    il "I can assure you, it’s none of that. I want to find the culprit as much as you do. But I’ll need your help for that."

    il "I only wish to see that you’re in good health to proceed, soI thought we could take a quick break-"

    an "With some tea, I get it. Very well, I must tell you that I despise the leavesfrom this country, so you'd better make a damn fine cup."

    il "Are there any to your taste?"

    # TO DO: Implement a continous Clock Sound Tick Tock Tick Tock. No Music

    an "…Fine black tea, with bitter orange. I think Uldin still had some in his pantry."

    "Both of them fall silent. There is nobody in the house who can say what to do with Uldin's possessions… Anari isn't even sure if he left a will."

    "Uldin isn't around anymore to enjoy what he had in life, that is certain."

    "Anari goes into the pantry and finds some tea bricks sealed in a container. She was sure that last night, Salome and Fleur did talk about this kind of tea."

    "Ilona, feeling some remorse as though the two of them were bandits, prepares the deceased man's tea according to Anari's instruction. Trying her best to be hospitable, Ilona also serves it with milk and sugar, as Fleur did."

    il "Here you go. Please, have some."

    "Ilona serves tea to Anari. As expected, Anari does not take any of the milk or sugar. In contrast, Ilona puts a generous amount of both in hers. The taste was far too bitter for her to enjoy so early in the morning."

    "Anari leans back in her chair, closing her eyes and taking in the aroma. She takes a sip before putting her tea cup down elegantly, without even the slightest clatter."

    "Ilona follows suit, but she is not nearly as graceful. Anari rubs her temples with the tips of her fingers, before speaking again."

    an "Not bad. Tell me, are all nuns this annoying?"

    il "Pardon me?"

    an "Whatever you're trying to do is futile. Re-examining the corpses or the rooms won't change anything — Edwin was the one who killed them."

    il "What makes you so sure of that?"

    an "I heard the details from Kellac and Eisleigh."

    "Anari details how the events played out: Salome screamed. It was heard by Kellac and Ilona, sleeping on the floor below. Edwin was not in his room."

    "Therefore, Edwin was already inside the master's chambers at the time of the murder."

    "It took some time to make it to the servants quarters and the other guest lodgings, which are on the opposite end of the manse."

    an "Everyone's locations were accounted for:"

    an "I was on patrol as the head of the town guard.{p}Kellac was the first one to react to the scream, followed by you.{p}Eisleigh was in her room."

    an "Each of us were able to confirm each others' locations at the time of the murder. The only one who couldn't be found was Edwin."

    il "How do you suppose that everyone is saying the absolute truth?"

    il "Kellac could have acted as if he had witnessed the murder. We have no account of what he was doing before that."

    il "There was also nobody around to confirm that Eisleigh was not at the crime scene, and I found her alone."

    il "And finally, where was Fleur? You do understand where I’m coming from, yes?"

    an "...I do. You’re smarter than you look, nun."

    an "Indeed, Fleur was missing at the time of the murder. Nobody had seen her enter, or exit the manse. I'll give you that much, but I highly doubt she could be the murderer. She's far too frail."

    il "The door was destroyed in the time it took for Eisleigh and I to return. How do you explain that?"

    an "Does the door being destroyed really mean anything? It doesn't change the fact that Edwin was at the crime scene. Transformed."

    il "…"

    an "Let me cue you in on this: out of everyone around here, you and Edwin are the most suspicious."

    an "The two of you are outsiders, whereas we’ve all known each other for a long time."

    an "I don't plan on letting my bias against the two of you get the better of me, however. Let's start at the beginning: what could be the motivation for the murder?."

    an "Kellac was an associate of Uldin and I during the war. He’s selfless, to the point of stupidity. I guess serving as a medic will do that to you."

    an "It’s hard to admit this, but I consider Kellac to be a close friend. He is a kind-hearted man."

    an "But that is no reason for letting him off the hook. He simply… has no reason for murder."

    il "Please explain."

    an "He’s as kind as he is weak, so I doubt he could overpower both Uldin and Salome. Anything he could have ever needed, whether coin or rare books on magic, he could have simply asked Uldin."

    an "And Uldin wouldn't have hesitated, because they share quite the history."

    an "Although, one thing I can tell you for sure is: Kellac is hiding something. Before he settled here, he had done nothing but walk and regret for five years, or so he says. It keeps him up at night."

    an "Whether it’s related to this case, I do not know."

    il "Hmm… I see."

    il "What about Eisleigh? I honestly don’t know much about her."

    an "She acted as an assistant to Salome; to help with keeping the town running, organization and tasks."

    an "She's been doing her fair share of blunders lately, but I know she takes her job seriously…  Perhaps she's just daydreaming more."

    an "I'm not saying that she's incompetent, let me get that straight. As long as her clumsiness doesn't get in my way."

    an "Though, I don't know much about her either to determine her motivation."

    il "Is she close with Fleur? They are almost the same age."

    an "Not really, Eisleigh and Fleur seem to be in their own heads. Eisleigh, with the study of magic as an apprentice, and Fleur, being a little troublemaker and a prankster."

    an "My niece still plays jokes and tricks, even at her age. It's all childish nonsense…"

    an "Fleur…"

    "Anari was confident up until this point, calm and refined. Now, dread and restlessness begins to take over."

    "Yet she could not overlook the superstitions, even for someone as experienced of a hunter. The wooden effigy of Fleur, her disapearance, the uncertainty behind the murder tarnishes Anari's unshakeable visage."

    "Moreover, Ilona’s demeanour and her relationship with Edwin…"

    il "Are you feeling alright, Anari-"

    an "Don't you dare patronize me, woman! Who do you think you are, prying so brazenly? Take your high and mighty Servant of God tripe elsewhere!"

    an "Trying to save that monster lover of yours… Are you out of your mind?"

    il "I do not know what has gotten into you all of a sudden, but I do not appreciate being spoken to like this."

    il "I showed compassion for you, when time is of the essence — instead of listening to you berate me, I should be finding the murderer!"

    "Silence looms over, waiting to be broken. Anari glares, her hand instinctively touches one of her arrows. She grimaces, and folds her arms across her body."

    il "I’m sorry. I didn’t - I didn't mean to lash out at you like that. It’s just... I want to find the culprit behind this mess."

    an "It’s fine."

    an "If the ‘I’ standing here was the Anari a couple of years back, you would have been mutilated by now."

    an "However, I did step out of line. Who you choose to be with is none of my business. I know violence for the sake of it won’t solve anything."

    an "Though we may not see eye to eye on everything, nun, I quite like you now. The tea must have swayed my opinion, I'm sure."

    an "Since we’re on good terms now-"

    il "(Are we?)"

    an "-and I can’t bear to see you with such a sad face, I’ll let you in on a secret: there is a cure for lycanthropy. You may yet be rid of the beast that lies within your dear beloved."

    an "For your and Edwin’s sake, I suggest you use it."

    il "Which is?"

    an "It’s for the lycan to die, of course!"

    il "…"

    an "Ahahahahaha, the look on your face. Brilliant."

    an "Now now, don’t give me that look. I was only kidding.{p}Partly."

    an "Anyhow, enough chit-chat. I must go and make preparations to lead the search party for Fleur."

    il "I should take my leave, as well. There is much to consider after what we’ve seen today."

    an "Indeed. {w}I can’t wait to hear what kind of answer you will give at sundown. Heh."

    il "I can't ever tell if you're on my side."

    an "I wonder, too."

# SCENE 25

    "Anari leads her out of the room, and back into the town square."

    "Ilona can feel her body covered in a light sweat. She can feel her heart leaping frantically inside her chest, just reminiscing about the conversation she had with Anari."

    "Kellac is waiting at the square, and he exchanges some words with Anari. Their voices are indistinct and quiet."

    "Her own heart sounds louder in her ears, so much that it’s making her weak and dizzy… Her extremities are tingling."

    play sound 'audio/sfx/heartbeat.mp3' loop

    # TO DO: Implement high pitched ambience?

    "It is taking everything for her to stay conscious. Anari glances at Ilona, before smiling to herself and walking away. Ilona sees a figure move in front of her, clad in black robes…"

    ke "Where to?"

    il "…"

    "She can barely recognize the voice. Ilona's vision blurs and the ground beneath her feet feels unsteady."

    ke "Ilona?"

    stop sound

    play sound 'audio/sfx/Gravel Floor Fall 1.mp3'

# Note for SFX: (vpunch effect + sound of collapsing?)

    ke "Hey! Is everything alright? Stay with me!"

# TRANSITION TO BLACK.

    "When Ilona opens her eyes again, she's in an unfamiliar bed and room. The air is heavy with an medicinal smell, suffocatingly so."

    "She feels far too conscious of her body. Her mouth feels dry, and her heart still feels like it's beating too fast."

    il "Did-? Was I…?"

    ke "Take it easy. You're safe — we're still in the manse."

    il "Just how long was I out for?"

    ke "It's almost midday."

    "Ilona grimaces. Too much time was lost. She moves her arms slowly, her body heavy. Sensation comes back into the tips of her fingers, and the unpleasant tingling stops. The smell of herbal medicine starts to become more bearable to her senses."

    ke "It wasn't an ordinary fainting spell. You should have regained consciousness faster if it was simply fatigue and stress."

    ke "I've taken precautions, and treated you for poisoning."

    il "Then, do you think — Did Anari try to poison me?"

    ke "…I suppose you can't really rule out that possibility.{p}Did you eat or drink anything with her?"

    il "Only tea, but I was the one who suggested and prepared it."

    il "I didn't see her slip anything in my drink. In fact, she was convinced I was trying to poison her…"

    ke "She's not the type to take such a cowardly approach."

    ke "She may seem cruel, but I don't think she would go that far to sabotage your efforts and put a stop to you."

    il "It seems you and Anari know each other well. I don't have much time, but I need to ask:"

    il "She had an extreme reaction upon seeing a wooden statue resembling Fleur. What could have terrified her so much about it?"

    ke "Truth be told, I don't really know much about her history, only rumours. She must think that the statue has to do something with the fae — Something in her past made her be wary of them."

    ke "Fleur admires the fair folk. The wooden statue is too elaborate to be one of Fleur's pranks, especially with the death of her parents…"

    il "So her aversion to seeing the statue has to do with her trauma, and distaste for Fleur's fae-related tricks?"

    ke "Something like that. Anari hates being pitied, and she doesn't show pity for anyone else either."

    ke "She would be terrified at the thought of Fleur being spirited away by the fair folk. {w}It's not something that she could ever accept - That's probably why she is leading the search."

    "Ilona shifts her body off the bed, able to move freely again. Kellac invites her to take a seat at the hall, and Ilona does so. He pours her some clear water. The smell of a simmering stew wafts from the kitchen."

    ke "About the tea you had with Anari — was there anything odd about it? {w}I'm asking because before the banquet, I gave Uldin his medicine, a powerful soporific."

    ke "There were three less doses in the pantry when I checked."

    il "Then, you think someone last night—"

    "There's a light knock on the door. Kellac tells them to enter, it's Eisleigh."

    ei "Oh, Ilona — I heard you fainted in the town square. I was worried."

    ke "Ah, yes! I invited Eisleigh over for lunch. Ilona, you probably haven't eaten at all yet, have you? You should try to eat, even if it's just a little."

    il "…"

    ke "…I guess it's hard to trust anyone after what you've been through."

    il "No, it's fine… I'll eat with you. You're right, I probably can't do much if I don't take care of myself."

    "Kellac serves Eisleigh and Ilona a rustic stew, with dark bread and clear water on the side. During the time eating together, Eisleigh asks about the investigation, and Ilona repeats Anari's reasoning surrounding Eisleigh and Kellac."

    "Ilona would have thought that Anari's defense was unbreakable, but there was actually one new thing they learnt about last night…"

    il "So are you considering the possibility someone tried to drug us during the banquet?"

    ke "That's what I feared, at least. Anari and I left before that, so I don't really have a clear picture of what exactly happened."

    "Ilona stares at an empty teacup in the room, and then realizes something — if the tea she served Anari was different, but she used the same sugar from last night—"

    il "The sugar — it must have been tampered with! Last night, I didn't add any to my tea because I didn't want to be rude, but I took some when I had tea with Anari."

    ei "I remember Fleur was reallyinsistent on putting sugar in my tea. I did think that was weird."

    ke "How much sugar did you put in your tea this morning, Ilona?"

    il "Four spoonfuls…"

    ei "Uhh, that sure is a lot…"

    ke "Goodness, no wonder you were out for so long! I'm surprised Anari didn't get on your case for adding tea to your cup of sugar."

    ei "I think we can confirm this theory to be true then: someone was trying to put us into a deep sleep - and there's a chance they were trying to target Edwin specifically."

    il "Then that would implicate Salome, or Fleur, most likely. They were the ones who prepared the tea last night."

    ei "It's not like I can deny it, but..."

    ke "Uldin could be involved, too."

    ke "The truth is… the medicine he uses is made to look inconspicuous on purpose."

    ke "I never inquired too closely about it, but he comes from a rather unscrupulous family; it wouldn't surprise me if he was aware of this plot."

    "Kellac seems to know the most about Uldin's family and his circumstances, so Ilona asked for more information."

    "Uldin suffered from insomnia, and slept in separate arrangements so as to not disturb his wife. Last night was also one of the rare occasions when Uldin was back in town, as he travelled frequently for his research; studying magic."

    "On the topic of magic, Eisleigh recalls something that she needed to discuss."

    ei "Could you tell us more about how Edwin is able to transform into a werewolf? Have you ever seen him do it?"

    il "No, I haven't. When he transforms, even when I ask it of him, he tells me to look away or to close my eyes."

    ke "Wait, why do you ask him to transform? What do you do when he's a werewolf?"

    il "It's… a secret."

    ei "Secret… Wait, that's precisely it!"

    "Everyone else looks at Eisleigh in alarm."

    play music 'audio/music/Wail of the Moon.ogg'

    ei "I heard of shapechangers before while studying cursed objects. They would use either an ointment, or the pelt of an animal, to assume the form of a beast."

    ei "If the curse was tied to his body, he wouldn't fear you witnessing his transformation."

    ei "But what if it was an item? If he feared betrayal, he wouldn't even show it to an ally."

    ei "Besides, there's always a risk involved in keeping that item safe — so it is better that only the bearer knows of it, because it could get lost, destroyed, or..."

    il "… stolen."

    "Both Kellac and Ilona look at Eisleigh with tense faces. Ilona isn't sure what to be more surprised at: Eisleigh's incredible reasoning and knowledge, or that someone would go as far as to steal an item uncertain to be in Edwin's possession."

    ei "There is a high chance that this cursed item still exists. Had it been destroyed, he would have died along with it."

    ei "This would give us a reason as to why Edwin was drugged last night: Uldin and Salome are sharp, and they might have caught onto Edwin being a werewolf early on."

    il "If we return this item to Edwin, would it restore the transformed arms back to human form?"

    ei "It's entirely possible, if that's what controls the transformation. A cursed item like that can generally only be bound to one person."

    ei "Someone else could have also used it, but… Uldin would understand the consequences of such a thing. I highly doubt it would be him."

    ke "Even so, finding this item might lead us to  finding the true culprit, or at least help make sense of this tragedy…"

    ke "You might not be able to convince everyone that Edwin is innocent, otherwise."

    il "Yes, Anari wouldn't accept it so easily... What would it take to convince her of Edwin's innocence?"

    ke "Short of having the culprit confess their crime, or finding Fleur in hope for an answer… I don't know."

# SCENE 32

    "The three of them start their search for the cursed item. Based on Anari's report, Kellac confirms with Ilona that nobody was able to enter or exit the town after Ilona and Edwin entered."

    "Eisleigh was eager to help out in any way possible, now that there was a chance of witnessing or finding a cursed magical object."

    ei "Kellac knows this, but I am not meant to have a copy of the master key."

    ei "I used to be a thief before I came here. The reason why I was an assistant to this household, was because I tried to steal one of Uldin's rare books…"

    ei "However, I've put the past well behind me. Uldin made me his friend instead of punishing me, and I'm thankful for that."

    "Ilona can’t help but find this suspicious. They start their search around Uldin's chambers. Once again, they see the mutilated corpse of Uldin, and the corpse of Salome, burned beyond recognition…"

    "Despite thoroughly searching the bodies, the trio was unable to find the wolfskin or anything else of importance."

    "They move onto Salome's room. Nothing appears to have been touched since the last time Ilona was here with Anari. Like Anari, Eisleigh comments that the chest was moved and then moves to inspect it."

    ei "This chest… Last time I saw it, it wasn’t locked. Salome was still re-arranging it to look nice."

    ei "Let me try opening it…"

    "Eisleigh pulls out a set of various different keys and picks, agitating each in the keyhole, to no avail."

# SCENE 33

    il "I thought you said you put the past behind you."

    ei "I did, but I thought the tools might come to be useful one day. We're doing a good thing, aren't we? Lockpicking is not inherently evil."

    ke "Full of surprises, eh? I trust you're not making excuses now."

    ei "Of course not, I merely-{p}Ah-ha! I got it!"

    "She jammed the lockpick into the keyhole and wriggled it around. A faint 'click' was heard."

    stop music fadeout 1.0

    "…{p}…{p}……"

    "……{p}Five stabs pierce the soft flesh of Eisleigh's hand."

    ke "Eisleigh!"

    ei "Aaaaaaaaghh! It… It hurts… It won't stop bleeding!"

    "Kellac fumbles through his thick, heavy cloak, drawing out a clean cloth for use as a compress."

    ei "We need to do something!"

    ke "There should still be some medical supplies in my room. Let's move there."

    il "Do you need my help? I know some healing magic-"

    ke "It’s all right. I’ve got this."

    ke "I just need to slow the bleeding and elevate the injury site. Don't touch anything else in this room. I'll be back soon."

    "Kellac and Eisleigh make their descent down the stairs. All that remains near the chest is the blood that poured out from Eisleigh's hand, the set of lockpick and Ilona."

    "The hairs on Ilona’s arms raise, and she can feel her heart beat faster. She puts her hand on her chest, as though uttering a short prayer."

    il "Breathe. If the chest was a trap, then there has to be something in there that someone doesn’t want found."

    "Despite her best instincts, Ilona picks up the lockpicks Eisleigh used. She spots a thin tool and uses it to pry the wood chest open…"

    "The trap was already disengaged; the danger gone. She sighs with relief."

    "Nestled underneath delicate pieces of jewelry and other finery, lay the red and glistening gold of a sash; with bloodstained, hoary fur on the other side."

    play music 'audio/music/Haunting.ogg'

    il "This must be it…"

    il "Ilona touches the wolfskin. She thinks back to meeting Salome, and the dissonance between that friendly encounter and the thought of Salome as a cold-blooded killer."

    il "(Salome seemed so kind and caring. Could someone like that really be a murderer?)"

    "A slip of paper falls out with the wolfskin, the contents addressed to a sculptor. According to the paper, the deposit was paid for, but the project was never finished and was thus refunded. A note explains that the item was delivered yesterday."

    il "(It looks like Salome bought something, but the final product was never finished? This could be important - I’d better hold onto this.)"

    il "(What about this chest? Did Fleur witness the murder? Did she take the wolfskin and leave it as a message in her mother's room?)"

    il "(But the chest is trapped, and placed in the open… That doesn't make sense. Why would she want us to find it, only to hurt us?)"

# SCENE 34

    "Ilona makes her way to where Edwin is imprisoned. The dungeons are behind the ruins of the chapel, which is on the south-east side of the manse."

    "She inserts the lockpicks into the keyhole. Ilona had only witnessed Eisleigh do it once, and apparently it’s not as easy as it looks."

    "After what seems like an eternity, the door opens with a loud click and a metallic groan."

    "Fearing that Anari, or someone else, would hear her in the dungeon, she hesitates. If she stayed behind… There was no knowing what the others would do if they laid their eyes on the wolfskin."

    "Kellac and Eisleigh might have seemed cooperative until now, but that could change if they lusted after its power for themselves."

    "Now is her only chance to return it to him privately."

    stop music fadeout 1.0

    il "I must have courage. I know that I made the right decision."

    il "If this can ease his spirits, even just a little, then it will have been worth it."

    il "(We're so close. Salome must be the one who did it… If I can just get Edwin to confirm it, then I won't have any fear.)"

    "Edwin is sitting in the darkness. His eyes make out the figure in white, clutching the wolfskin in her hand."

    ed "Ilona? You shouldn't be here. Wait, you found the…"

    il "I was alone when I took it. Nobody wore it, either."

    ed "…Thank goodness you're okay. Where did you find it?"

    il "Salome's bedroom. Inside a chest meant for Fleur."

    ed "What? That's—"

    "Edwin falters, lost for words."

    play music 'audio/music/He Who Seeks Hope - Theme Of Edwin -.ogg'

    "Ilona kneels down, returning the wolfskin to Edwin. She asks where he normally would wear it. After he tells her, she ties it to the inside of a thick leather piece around his waist."

    "The chains fall to the floor, unbinding his once girthy wolf-like arms, now restored to human form."

    ed "You've saved my life once again… Thank you."

    il "Please, there's no need to thank me. It's given me a chance to talk to you again… Do you think you can tell me more about the murder?"

    ed "Of course — though you probably know more about it than I do."

    il "If I think of who could have been present in the Master's chambers at the time, only two people remain. Did Salome murder Uldin? I've gathered that they must have died from the wounds they inflicted on each other. Am I correct?"

    ed "From what I could tell, yes. But I… I’ve already put you through too much. You have to stop this investigation. There’s no use in getting your hopes up."

    il "...What? I don't understand. We're so close to finding out the truth! What is there left to hide?"

    ed "… If I were to live my life honestly... If I were not a monster… You wouldn't have to keep living a lie."

    il "Earlier today, I saw you holding Salome's corpse in your arms. What happened?"

    ed "I hid the answer from you for a reason. Please, don’t pry any further…"

    il "...You really did kill her."

    "His eyes are empty and cold. At his loss for words, Ilona's heart sinks. Her hands tremble, and she lowers her head."

    il "No… There’s no way… I… You couldn’t have…"

    ed "I should've said something sooner rather than have you go through all of this. I'm sorry."

    il "I believed you were innocent…!"

    ed "If it truly were that simple, then… Well, I wouldn’t have been locked up."

    "She chokes back her tears, before gathering her composure and speaking again."

    il "Tell me everything. Even if the truth will damn us both… I need to know."

    # Go to act 3.
    jump act3
