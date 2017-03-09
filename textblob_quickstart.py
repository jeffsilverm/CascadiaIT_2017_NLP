# /usr/bin/env python3
#
# From https://textblob.readthedocs.io/en/dev/quickstart.html

from textblob import TextBlob

wiki_1 = TextBlob("Python is a high-level, general-purpose programming language.")
print("Wiki 1 tags", wiki_1.tags)

for sent in ["A woman without her man is nothing. ", "A woman, without her man, is nothing.",
             "A woman: without her, man is nothing."]:
    wiki = TextBlob(sent)
    print("Wiki tags: %s : " % sent, wiki.tags)

for sent in [
    "For more information see the Commercial Driver Guide available at www.dol.wa.gov or at any driver licensing office.",
    "You can get an instruction permit or a driver license at any driver licensing office.",
    "Some offices do not offer testing so before you come in be sure the one you plan to visit offers the testing you need.",
    "In an effort to reduce wait times legislation was passed to allow driver training schools licensed by the Department of Licensing and school districts that offer a traffic safety education program under the supervision of the Office of the Superintendent of Public Instruction to administer driver licensing examinations.",
    "A list of approved schools as well as driver licensing offices can be found on our website.",
    "Please contact an approved school for their specific testing requirements.",
    "To be issued an instruction permit you must: ** be at least 15-1/2 years old (or 15 years old if enrolled in an approved driver-training course); ** pass the knowledge test (unless enrolled in an approved driver-training course); ** complete the vision and medical screenings and; ** pay an application/examination fee.",
    "If you pay an application/examination fee and are ( at least 15-1/2 years old or ( 15 years old and enrolled in an approved driver-training course) ) and ( pass the knowledge test or are enrolled in an approved driver-training course) and complete the ( vision and medical screenings) then you will be issued an instruction permit.",
    "If you are under 18 you must also bring your parent or guardian with you to the licensing office when you apply."
    # They must show proof of identity and proof of relationship to you and must also sign a Parental Authorization Affidavit.
    # When last names are different we require more documents 1-3  proving relationship.
    # The permit is valid for one year and you can renew it.
    # If you are enrolled in an approved driver-training course you can get an instruction permit at age 15.
    # You will need a waiver from your school allowing you to apply for the permit up to 10 days before the class starts.
]:
    wiki = TextBlob(sent)
    print("\nWiki tags: %s : " % sent, wiki.tags)
    print("Noun phrase extraction", wiki.noun_phrases)
    print("Parsed", wiki.parse())
    print("n-grams", wiki.ngrams(n=3))
