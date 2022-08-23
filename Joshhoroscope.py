import random
dict = {"Aries": [
    "The moon continues its journey through Cancer this morning, dear Ram, forming a square with expansive Jupiter. \n"
    "This cosmic climate will cause you to feel things on a larger scale, so you may want to find a balance between \n"
    "your heart and sense of logic before taking action or lashing out. Luckily, a sweet connection between Mercury \n"
    "and Pluto will give you an opportunity to sort through your psyche, allowing you to move past any triggers you \n"
    "don't feel like confronting. Plan on nurturing your body this evening when the sun enters Virgo and the sector \n"
    "of your chart that governs wellness. \n",
    "You may get the sense that something is amiss when you awaken this morning, dear Aries, as the Gemini moon forms \n"
    "a harsh t-square with Mercury and Neptune. Try to be cautious of what or who you trust right now, as deception \n"
    "may hang in the air. Luckily, clarity will find you later in the afternoon when Luna blows a kiss to the Leo \n"
    "sun, illuminating the truth while restoring warmth to your heart. You'll feel a shift this evening when the moon \n"
    "enters Cancer, triggering your nurturing and empathic side throughout the next two and a half days. \n",
    "Small blessings and emotional clarity may come through in unexpected ways this morning, dear Aries, \n"
    "as the Cancer moon aspects revolutionary Uranus. Use this energy as a cosmic cue to tap into your gratitude, \n"
    "opening your heart to the beauty that surrounds you. Boredom could cause you to reach for your phone this \n"
    "afternoon, but try not to waste too much time scrolling your social media feeds. Luckily, a dreamy and inspired \n"
    "energy will fill the air later tonight when Luna blows a kiss to Neptune, making it an ideal time to work on \n"
    "creative projects or enjoy a meditation session. \n",
    "The moon moves into fiery Leo this morning, sweet Aries, putting you in a Rambunctious and sassy mood. These \n"
    "vibes are all about embracing your most authentic self, a sentiment seconded by a sweet connection between Venus \n"
    "and the healing asteroid, Chiron. Expressing yourself will play a huge role in any ego-driven healing you may \n"
    "need to embrace right now, as the stars encourage you to unconditionally love yourself. Good vibes will continue \n"
    "to flow well into the evening, thanks to a supportive aspect between Luna and Jupiter, poised to elevate your \n"
    "optimism and strengthen your self-belief.",
    "The Leo moon connects with Chiron and the nodes of fate throughout the first half of the day, dear Aries, \n"
    "asking you to love and appreciate yourself, even if you don't know exactly what the road ahead looks like. \n"
    "Luckily, a sweet alliance between Luna and Venus as evening rolls in will allow you to open your heart and \n"
    "embrace a healthy ego, allowing you to embody confidence without feeling boastful. You'll notice a shift this \n"
    "evening when Mercury enters Libra, bringing a softness to your mind and words throughout the next couple of \n"
    "weeks while elevating your powers of persuasion."],
    "Taurus": [
        "Do your best to stay clear of petty drama and mean-spirited gossip this morning, dear Taurus, as the Gemini \n"
        "moon enters a hash t-square with Mercury and Neptune. This cosmic climate could also stir up insecurities \n"
        "within yourself, making it important that you try not to worry about what others may be thinking or saying \n"
        "about you. Luckily, the vibe will feel much lighter when Luna connects with the Leo sun this afternoon, \n"
        "helping you stabilize your emotions while boosting your ego. Your thoughts will become more profound this \n "
        "evening when the moon enters Cancer, putting you in a sensitive yet logical mood.",
        "You may find yourself in a quiet and cerebral headspace this morning, dear Taurus, as the Cancer moon \n"
        "aspects expansive Jupiter. Try to find healthy distractions if you begin to pick apart your psyche, \n"
        "and avoid fixating on small issues that don't play a significant role in your big picture. A sweet \n"
        "connection between Mercury and Pluto can help you find empowerment through creativity or spirituality,\n "
        "so don't be afraid to let your wacky woo side out. You'll notice a shift later tonight when the sun enters\n "
        "efficient Virgo, inspiring you to get organized within your personal projects throughout the next several \n"
        "weeks.",
        "News you've been waiting for could manifest suddenly this morning, dear Taurus, when the Cancer moon \n"
        "connects with the North Node and Uranus. Pay attention to the subtle signs and synchronicities that surround \n"
        "you right now, as the universe will be eager to enlighten and guide you. Your mystical side will come out to \n"
        "play this evening when Luna blows a kiss to visionary Neptune, activating the sector of your chart that \n"
        "governs spiritually. Use this cosmic climate to embrace the religious or meditative practices of your \n"
        "choosing since connecting with the other side will occur with more fluidity. \n"],
    "Gemini": [
        "There's a risk you could wake up on the wrong side of the bed this morning, dear Gemini, as the moon \n"
        "continues its journey through your sign while forming a harsh t-square with Mercury and Neptune. Don't feel \n"
        "guilty about shutting down emotionally in order to regroup your heart and mind, but try not to lash out at \n"
        "anyone who seeks your advice or attention. Luckily, you'll feel more positive and social later in the \n"
        "afternoon when Luna blows a kiss to the Leo sun, bringing warmth to the atmosphere. Give yourself permission \n"
        "to indulge in a bit of luxury this evening, when the moon makes its way into Cancer and your solar second \n"
        "house.",
        "You may want to steer clear of social media interaction this morning, dear Gemini, or you could begin to \n"
        "detach from the present due to a harsh connection between the Cancer moon and Jupiter. These vibes will also \n"
        "cause you to feel more sensitive to the plights of humanity, which means reading the news could be \n"
        "particularly triggering right now. Luckily, you'll have a chance to shake off this funk when Mercury blows a \n"
        "kiss to Pluto this afternoon, helping you reconnect with your heart's strength. The vibe will shift later \n"
        "tonight when the sun enters Virgo, shifting your focus toward household affairs.",
        "You'll feel vibrationally in sync with the world around you this morning, dear Gemini, thanks to a sweet \n"
        "connection between the Cancer sun and Uranus. Strange synchronicities between your subconscious and the \n"
        "material realms could come into play, making it a good day for documenting any coincidences that find you, \n"
        "as they could be encoded with messages from beyond the veil. Intuitive blocks will temporarily dissolve this \n"
        "evening when Luna blows a kiss to mystifying Neptune, so you may want to indulge in a deep meditation \n"
        "session or pull out your tarot cards for a serious chat between you and the other side."],
    "Cancer": [
        "You may feel a bit overstimulated by the people around you this morning, dear Cancer, as the Gemini moon \n"
        "forms a harsh t-square with Mercury and Neptune. This cosmic climate could also curse you with some \n"
        "temporary brain fog, so you may want to start the day with a grounding meditation session. Luckily, \n"
        "you'll return to your senses later in the afternoon when Luna blows a kiss to Leo. You'll begin to feel more \n"
        "outgoing and like yourself once the moon enters your sign later tonight, reconnecting you with your true \n"
        "identity on an emotional and intellectual level.",
        "New projects or changes within your career could leave you feeling overwhelmed by the number of \n"
        "responsibilities you carry, sweet Crab, as the moon squares off with expansive Jupiter. Trust that you're \n"
        "qualified and capable of handling any professional tasks being thrown your way, but remember that it's okay \n"
        "to turn down work as well. Your love life will benefit from some intense energy as Mercury blows a kiss to \n"
        "Pluto, helping you and your sweetheart engage in serious conversation without having to endure heaviness or \n"
        "discomfort. Virgo season emerges later tonight, bringing clarity to your mind in the weeks ahead."],
    "Leo": [
        "You may feel a bit out of sorts or overstimulated when you wake up, dear Leo, as the Cancer moon squares off \n"
        "with expansive Jupiter. Give yourself permission to indulge in a bit of solitude, putting your phone on do \n"
        "not disturb as you begin the day. Luckily, a sweet connection between Mercury and Pluto will help you feel \n"
        "more grounded in the present as the afternoon rolls around, allowing you to get back on task if you floated \n"
        "through the morning. Find an excuse to celebrate yourself before evening settles in and the sun moves out of \n"
        "your sign and into Virgo. ",
        "The Cancer moon blows a kiss to unpredictable Uranus this morning, which could give you the push needed to \n"
        "set boundaries with difficult people who have been overstepping with you recently. Don't feel bad about \n"
        "drawing lines right now, as the stars encourage you to prioritize your mental and emotional health. A \n"
        "cleansing energy will come into play this evening when Luna blows a kiss to Neptune, making it a great time \n"
        "for a salt bath or purifying meditation. Unfortunately, a harsh opposition between Luna and Pluto could \n"
        "threaten to spoil these peaceful vibes, making it important that you don't surrender to feelings of stress \n"
        "or self-criticism."],
    "Virgo": [
        "You'll form emotional connections with ease today as the moon continues its journey through Cancer and the \n"
        "sector of your chart that governs community. Meanwhile, a sweet alliance between Mercury and Pluto will \n"
        "encourage you to be your most authentic self, allowing you to reveal your true colors without feeling \n"
        "vulnerable or overly exposed. You'll notice an elevation in your mood and energy levels later tonight when \n"
        "the sun enters your sign, blessing your aura with some extra support from beyond the veil throughout the \n"
        "next several weeks. Use this luminary placement to manifest your wildest dreams, trusting that the stars \n"
        "will align to assist these dreams.",
        "Take a moment to check in with your loved ones this morning, dear Virgo, as the Cancer moon shares a sweet \n"
        "connection with Uranus. This cosmic climate will put you in the mood to spread joy, and your nearest and \n"
        "dearest will appreciate being thought of. A dreamy yet flirtatious vibe will fill the air this evening when \n"
        "Luna blows a kiss to Neptune, which may also usher in praise through your social media pages. Just make sure \n"
        "to unplug from your electronic devices as the day comes to a close, or an opposition between the moon and \n"
        "Pluto could sour your online experience. "],
    "Libra": [
        "You might not feel super ready to kick off the workweek when you wake up this morning, dear Libra, \n"
        "as the Cancer moon squares off with expansive Jupiter. This cosmic climate will be especially heavy if you \n"
        "didn't have enough time to fully restore your energy levels over the weekend, making it important that you \n"
        "find ways to integrate self-care into the day. Luckily, a helpful alliance between Mercury and Pluto will \n"
        "provide you with some cosmic support when it comes to nurturing yourself, as long as you're willing to \n"
        "release and move past any discomfort or negativity that finds you. ",
        "Though your spirituality can help carry you through some difficult times, dear Libra, finding a balance \n"
        "between logic and intuition may become a struggle this morning when the Gemini moon enters a harsh t-square\n "
        "with Mercury and Neptune. These sentiments will become exacerbated if you've been putting unreasonable \n"
        "expectations on yourself recently, making it a good time to devote yourself to a bit of self-care and \n"
        "relaxation. A friend may step in to brighten your day later in the afternoon when Luna blows a kiss to the\n "
        "Leo sun, so try not to close off from the people that love you."],
    "Scorpio": [
        "A penchant for daydreaming could cause you to stumble within your tasks and responsibilities this morning, \n"
        "dear Scorpio, as the Cancer moon squares off with Jupiter. This luminary placement is sure to elevate your \n"
        "intuition and connection with the other side, though staying grounded should remain a priority. Luckily, \n"
        "a desire to interact with others can help keep you in the moment, as a sweet alliance between Mercury and \n"
        "Pluto triggers your social side. The vibe will shift later tonight when Virgo season emerges, \n"
        "which is poised to elevate your popularity and usher in new connections throughout the next four weeks.\n ",
        "Flashes of insight may cause you to view the future in a different light this morning, dear Scorpio, \n"
        "as the Cancer moon connects with the North Node and revolutionary Uranus. These vibes will also usher in\n "
        "messages from beyond the veil as the other side guides you toward your highest path. Watch out for emotional \n "
        "exhaustion this afternoon when Luna bounces some unbalanced energy off Saturn, which could be particularly \n"
        "problematic if someone begins to dump their issues onto you. Luckily, you'll have an opportunity to unwind \n"
        "and reconnect with yourself this evening, thanks to a sweet aspect between the moon and Neptune. "],
    "Sagittarius": [
        "You'll have an opportunity to rise above any negative people or situations that have been causing you grief \n"
        "today, dear Archer, as the moon continues its journey through Cancer and your solar eighth house. Meanwhile, \n"
        "a sweet alliance between Mercury and Pluto will help you tap into your self-worth, encouraging you to set \n"
        "boundaries where they're needed. A philosophical element will also come into play right now as the sun takes \n"
        "its final steps through Leo and the spiritual sector of your chart. Keep your eyes peeled for signs and \n"
        "synchronicities from beyond the veil as the stars align to usher you toward enlightenment. \n",
        "The universe will ask you to clean up your act this morning, dear Archer, as the Cancer moon connects with \n"
        "the North Node and revolutionary Uranus. Use the momentum of this cosmic climate to purge your inbox, \n"
        "sort through your desk, wipe down surfaces, and empty the trash, as the universe encourages you to create a \n"
        "clean and neat space to continue the workweek. Plan on spending the evening at home to indulge in some \n"
        "restorative self-care when Luna blows a kiss to mystical Neptune, ushering in a cleansing and supportive \n"
        "energy that's perfect for resetting your heart, mind, and soul. "],
    "Capricorn": [
        "Finding a balance between nurturing both yourself and the people you love could feel like a losing battle \n"
        "this morning as the Cancer moon squares off with expansive Jupiter, highlighting the vast needs of those who \n"
        "fill your heart. Luckily, a sweet connection between Mercury and Pluto will bring some spiritual support \n"
        "your way, allowing you to have meaningful but brief interactions. You'll notice a vibe shift later tonight \n"
        "when the sun enters Virgo, activating the sector of your chart that governs higher thinking and spirituality \n"
        "throughout the next four weeks, helping to elevate your psychic abilities and manifestation skills.",
        "You'll have an opportunity to invest in your relationships without abandoning your identity or independence \n"
        "this morning, dear Sea-Goat, thanks to a sweet connection between the Cancer moon and revolutionary Uranus. \n"
        "These vibes will also give you permission to indulge in your wacky side, so don't hold back if you feel like \n"
        "getting weird. A graceful and airy ambiance will take hold this evening, bringing a lightness to the table \n"
        "that's perfect for poetic conversations and light flirting. Just try not to float too far away during your \n"
        "interactions, or you could end up in murky territory later tonight when the moon opposes Pluto."],
    "Aquarius": [
        "You may need to take extra steps to dodge chatty colleagues or family members this morning, dear Aquarius, \n"
        "as the Cancer moon squares off with expansive Jupiter. This cosmic climate could throw you seriously off \n"
        "schedule if you conversationally procrastinate, making it important that you keep a close eye on the clock. \n"
        "Meanwhile, a sweet connection between Mercury and Pluto will bring through profound moments of clarity, \n"
        "so you should try to keep a journal handy to document these bouts of brilliance. Virgo season makes its \n"
        "debut later tonight, bringing with it major shifts and changes in the coming weeks.",
        "You'll have a chance to fully move on from any drama or trauma that has been weighing on your heart today,\n "
        "dear Aquarius, thanks to a sweet connection between the Cancer moon and revolutionary Uranus this morning. \n"
        "This cosmic climate will snap you out of any unhealthy fog you may have been floating through recently, \n"
        "giving you a chance to reclaim logic and pragmatism. An opportunity to embrace luxury will manifest this \n"
        "evening when Luna aspects dreamy Neptune, making it a great time to escape the mundane world in favor of \n"
        "some serious self-care, relaxation, and perhaps a bit of online shopping."],
    "Pisces": [
        "Resist the urge to overspend this morning, dear Pisces, or a harsh connection between the Cancer moon and \n"
        "Jupiter could cause you to regret it later. Luckily, you'll have an opportunity to find value within \n"
        "yourself instead of material items, as long as you tap into your creativity and let your ego out to play. \n"
        "Meanwhile, a sweet aspect between Mercury and Pluto will intensify any flirtations you've been nurturing, \n"
        "allowing you to reach new depths within your developing connections. You'll notice a shift later tonight \n"
        "when the sun enters Virgo and the sector of your chart that governs matters of the heart, bringing through \n"
        "romance in the coming weeks. ",
        "You may want to get a journaling session in this morning, dear Pisces, as the Cancer moon connects with \n"
        "ingenious Uranus. This cosmic climate will trigger brilliant ideas and new concepts, though failing to \n"
        "document them could cause you to lose them down the line. Your affections will be in high demand this \n"
        "evening when Luna blows a kiss to Neptune, drawing in the adoration of your family and friends. Just try not \n"
        "to give your energy to people who might drain you, or you could begin to feel emotionally and mentally \n"
        "depleted as the day goes to a close."],
}
user_input = input("Enter your zodiac sign \n")
def rand(list):
    num = random.randint(0, len(list) - 1)
    return num
def output_message(input):
    for key, value in dict.items():
        if input == key:
            print("Your horoscope message for {} today is {}".format(input, value[rand(value)]))
output_message(user_input)
