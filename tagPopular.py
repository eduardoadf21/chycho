
from db import get_database

chychoVault = get_database()
posts = chychoVault["posts2"]


titles = ("An Exercise for the Mind: a 10 by 10 Math Puzzle: a Pattern Recognition Game: Meditation on an Open Maze",
      "Best Explanation of Quantum Field Theory That You Will Ever Hear, Provided by Sean Carroll in Less than 2 Minutes at the 46th Annual Fermilab Users Meeting",
      "It’s Not Just the Mainstream Media That Is Scripted to Manufacture Consent, so Are Our Politicians",
      "Schooling Superman on Totalitarianism: Superman and The Flash have a discussion about gun control while playing chess",
      "The Surveillance State Killed BlackBerry, and the Same Fate Awaits Other Tech Giants (Update 5)",
      "Anomalies, Prisons, and Geophysics: How Governments Use Data and How to Stop Them",
      "Why is Math Important? Because the language of mathematics plays a vital role in our evolution",
      "A Brief Summary of America’s War on Drugs",
      """System of A Down: Hypnotize (Review of System of a Down's "Hypnotize")""",
      "The future of Africa looks bleak, here is why",
      "Some advice to those who have lost loved ones",
      "Happy 420! (Almost everything you wanted to know about Cannabis)",
      "Paradigm Shift in Education: Krishnamurti on the Educator, RAW on Ignorance, Gato on the System, and Hamming on Learning",
      "Sharing a Story from My Father: In Commemoration of the Armenian Genocide",
      "The Dominoes Are Falling, the Tides Are Turning, the War on Drugs Is Ending, but Prohibitionists Just Won’t Give up the Ghost: How to End Prohibition",
      "The Seduction of Dice, The Philosophy of Craps",
      "Some Primary Lessons from Some Amazing Teachers",
      "Coming Out of the Dark Ages, Psychedelic Science, and Freedom Over Consciousness: Introduction to the Benefits of Cannabis, Psilocybin, Ayahuasca, LSD, DMT, and Ibogaine",
      "Canadians Can Grow Tobacco for Personal Use; We Should Be Able to Do the Same with Cannabis",
      "Commodification of Water, the Quintessential Issue of Our Time",
      "World War III began in May 2006: Building the New Map of the Middle East in Real Time",
      "Target is Still Iran: Clear Cutting the Middle East and the Coming Blood Bath (Mapping World War III) ")

for title in titles:
    posts.find_one_and_update({'title': {"$regex": title}},{'$set':{'tag':'popular'}})