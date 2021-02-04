
import pickle


cset = dict()

try:
    cset = pickle.load(open("conditions.camp", "rb"))
except:
    # Simple Weapons
    cset["Blinded"] = "Incoming Attacks have advantage. Outgoing Attacks have disadvantage. Sight checks always fail."
    cset["Charmed"] = "Cannot attack or otherwise harm the charmer. The charmer has advantage on social checks against the charmed."
    cset["Deafened"] = "Cannot Hear. Automatically fail all hearing-related checks."
    cset["Frightened"] = "Disadvantage to all ability checks and attacks while the source of fear is in line of sight." \
                         "Cannot willingly move closer to the source of fear."
    cset["Grappled"] = "Reduces Speed to 0 until the Grappler is incapacitated or removed."
    cset["Incapacitated"] = "Cannot take actions or reactions."
    cset["Invisible"] = "Cannot be seen without the aid of magic or Special sense. Outgoing attacks have advantage" \
                        "while incoming attacks have disadvantage. Can still be detected by noise."
    cset["Paralyzed"] = "Become Incapacitated, cannot speak, and cannot move. Automatically fail Strength and Dexterity" \
                        "Saving throws. Incoming attacks have advantage, and become critical hits if within 5 feet."
    cset["Petrified"] = "Become Paralyzed by transforming into an inanimate substance. Gain resistance to all types" \
                        "of damage, and immunity to poison, disease and aging (suspended, not neutralized)."
    cset["Poisoned"] = "Disadvantage to all attacks and ability checks."
    cset["Prone"] = "Can only crawl and puts outgoing attacks at disadvantage. Incoming attacks within 5 feet have" \
                    "advantage, but otherwise have disadvantage."
    cset["Restrained"] = "Reduces Speed to 0, advantage on incoming attacks, disadvantage on outgoing attacks and" \
                         "Dexterity saving throws."
    cset["Stunned"] = "Become incapacitated, can only speak falteringly, automatically fail Strength and Dexterity" \
                      "saving throws, and advantage on incoming attacks."
    cset["Unconscious"] = "Become Paralyzed, unaware of your surroundings, drop held items, and fall Prone."

    pickle.dump(cset, open("conditions.camp", "wb"))
