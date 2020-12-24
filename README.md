# Lottery money wasting calculator

Simple script to show how much money you will lose given `n` number of purchased random tickets.

## Running

`python main.py`

## Tweaking

- To change the winnings for number of matches, adjust `winnings` list on line 9.
- To set the number of tickets purchased, change `purchased_tickets` on line 21
- To change the ball range, `max_ball_range` on line 19 (UK Lotto uses 59 balls some use 49 or whatever but the principle is the same)
- To change the winning number set (although redundant as lotteries are by definition random), change `winning` on line 16.

## Caveats

I just made this quickly to explain how lotteries make money to a relative, it's not a profesional job and memory intensive.

This is a basic lottery thing, doesn't take into account any bonusses, "thunderballs" or anything like that, just straight matching.

## Licence

It's a toy, I really don't care what you do with it. Hopefully it's educational.
