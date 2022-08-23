import random
signs = {1:'Aquarius',2:'Pisces',3:'Aries',4:'Taurus',5:'Gemini',
         6:'Cancer',7:'Leo',8:'Virgo',9:'Libra',10:'Scorpio',11:'Sagittarius',12:'Capricorn'}

choice = int(input('Select when you were born:\n1. Jan 20 - Feb 18\n2. Feb 19 - Mar 20\n3. Mar 21 - Apr 19\n4. Apr 20 - May 20\n5. May 21 - Jun 20\n6. Jun 21 - Jul 22\n7. Jul 23 - Aug 22\n8. Aug 23 - Sep 22\n9. Sep 23 - Oct 22\n10. Oct 23 - Nov 21\n11. Nov 22 - Dec 21\n12. Dec 22 - Jan 19\n'))

sentences = ['The love of your life is right in front of your eyes.',
             'Behind this fortune is the love of my life.',
             'You have a secret admirer.',
             'Love, because it is the only true adventure.',
             'The love of your life will appear in front of you unexpectedly!',
             'An old love will come back to you.',
             'Your love life will soon be happy and harmonious.',
             'Follow what calls you.',
             'You\'re intoxicating when you do what you love.',
             'Be passionate and totally worth the chaos.',
             'You will know it when you see it. It will know you when it sees you.',
             'Do what you love. The rest will fall into place.',
             'Follow what you love and see what turns up.',
             'The middle of the process is no place to determine the end of it.',
             'You should definitely go for it.',
             'Enter unknown territory.',
             'Everything that is was first a dream.']

length = len(sentences)

print(f'Today\'s horoscope for {signs[choice]} is:\n {sentences[random.randint(0,length-1)]}')
