""" calculate how much money a movie makes
-3 vars name, adult, child
-child 6, adult 10
-calc gross total
-20percent
-80 percent of theater makes"""

movie_name = "Descendants 2"
adult = 200
child = 100

"""calculate"""

gross = adult * 10 + child * 6
theater = gross * 0.20
studio = gross * 0.80


def main():
    print(f'Movie Name:       {movie_name:50}')
    print(f'Adult Tickets:    {adult:}')
    print(f'Child Tickets:    {child:}')
    print(f'Theater Profit:   ${theater:,.2f}')
    print(f'Studio Profit:    ${studio:,.2f}')
    print(f'Gross Profit:     ${gross:,.2f}')


main()
