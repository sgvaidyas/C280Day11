def horοsocope1():
    print(
        "\033[1;36mGeneral Day Horoscope\n\033[1;35mIn the morning, the Cancer moon squares Jupiter in Aries, augmenting optimism. \nEmotional comfort may be sought through the discovery of new spiritual insights or education. \nAlthough we derive pleasure in the familiar, under this influence, we are curious about how different cultures live. ")
    n = input("\n\033[1;34mPlease type your zodiac sign:").lower()
    horoDictionary = {
        "aries": "A sweet connection between Mercury and Pluto will give you an opportunity to sort through your psyche, \nallowing you to move past any triggers you don't feel like confronting. Plan on nurturing your body this evening\nwhen the sun enters Virgo and the sector of your chart that governs wellness."
        ,
        "taurus": "Don't be afraid to let your wacky woo side out. You'll notice a shift later tonight when the sun enters efficient Virgo\ninspiring you to get organized within your personal projects throughout the next several weeks"
        ,
        "gemini": "You'll have a chance to shake off this funk when Mercury blows a kiss to Pluto this afternoon, helping you reconnect with\nyour heart's strength. The vibe will shift later tonight when the sun enters Virgo, shifting your focus toward household affairs."
        ,
        "cancer": "Your love life will benefit from some intense energy as Mercury blows a kiss to Pluto, helping you and your sweetheart\nengage in serious conversation without having to endure heaviness or discomfort. Virgo season emerges later tonight\nbringing clarity to your mind in the weeks ahead."
        ,
        "leo": "You will feel more grounded in the present as the afternoon rolls around, allowing you to get back on task if\nyou floated through the morning. Find an excuse to celebrate yourself before evening settles in and the sun\nmove out of your sign and into Virgo"
        ,
        "virgo": "You'll notice an elevation in your mood and energy levels later tonight when the sun enters your sign, blessing\nyour aura with some extra support from beyond the veil throughout the next several weeks. Use this luminary placement to\nmanifest your wildest dreams, trusting that the stars will align to assist these dreams."
        ,
        "libra": "Luckily, a helpful alliance between Mercury and Pluto will provide you with some cosmic support when it comes to\nnurturing yourself, as long as you're willing to release and move past any discomfort or negativity that finds you. "
        ,
        "scorpio": "Luckily, a desire to interact with others can help keep you in the moment, as a sweet alliance between Mercury and\nPluto triggers your social side. The vibe will shift later tonight when Virgo season emerges, which is poised to\nselevate your popularity and usher in new connections throughout the next four weeks. "
        ,
        "segittarius": " A philosophical element will also come into play right now as the sun takes its final steps through Leo and the\nspiritual sector of your chart. Keep your eyes peeled for signs and synchronicities from beyond the veil as the\nstars align to usher you toward enlightenment. "
        ,
        "capicorn": "You'll notice a vibe shift later tonight when the sun enters Virgo, activating the sector of your chart that governs higher\nthinking and spirituality throughout the next four weeks, helping to elevate your psychic abilities and manifestation skills. "
        ,
        "aquarius": "Meanwhile, a sweet connection between Mercury and Pluto will bring through profound moments of clarity, so\nyou should try to keep a journal handy to document these bouts of brilliance. Virgo season makes its debut\nlater tonight, bringing with it major shifts and changes in the coming weeks. "
        ,
        "pisces": "A sweet aspect between Mercury and Pluto will intensify any flirtations you've been nurturing, allowing you to\nreach new depths within your developing connections. You'll notice a shift later tonight when the sun enters\nVirgo and the sector of your chart that governs matters of the heart, bringing through romance in the coming weeks. "
        }
    if n in horoDictionary:
        print(horoDictionary.get(n))
    else:
        print("\033[1;34mYou must have missed typed it.\nTry again...")

    print("\033[1;31m\nQuote of the day:\nA rose does not answer its enemies with words, but with beauty.")


if __name__ == '__main__':
    horοsocope1()
