import unittest
import warnings
import sys
import os

sys.path.append("../")
from Code.recommenderapp.movierecommender.search import Search

warnings.filterwarnings("ignore")


class TitleSearchTests(unittest.TestCase):
    def testSearchRomanceInTitle(self):
        search_word = "romance"
        search = Search()
        filtered_dict = search.resultsTop5(search_word)
        expected_resp = [
            "Romancing the Stone (1984)",
            "True Romance (1993)",
            "Romance & Cigarettes (2005)",
            "Romance on the High Seas (1948)",
            "An American Romance (1944)",
        ]
        self.assertEqual(filtered_dict, expected_resp)

    def testSearchToyInTitle(self):
        search_word = "toy"
        search = Search()
        filtered_dict = search.resultsTop5(search_word)
        expected_resp = [
            "Toy Story (1995)",
            "Toy Story 2 (1999)",
            "Toy Story 3 (2010)",
            "Toy Story 4 (2019)",
            "Toy Soldiers (1991)",
        ]
        self.assertEqual(filtered_dict, expected_resp)

    def testSearchLoveInTitle(self):
        search_word = "love"
        search = Search()
        filtered_dict = search.resultsTop5(search_word)
        expected_resp = [
            "Love & Human Remains (1993)",
            "Love Affair (1994)",
            "Love and a .45 (1994)",
            "Love in the Afternoon (1957)",
            "Love Bug, The (1969)",
        ]
        self.assertEqual(filtered_dict, expected_resp)

    def testSearchChristmasInTitle(self):
        search_word = "christmas"
        search = Search()
        filtered_dict = search.resultsTop5(search_word)
        expected_resp = [
            "Christmas Carol, A (1938)",
            "Christmas Story, A (1983)",
            "Christmas Vacation (1989)",
            "How the Grinch Stole Christmas (2000)",
            "I'll Be Home for Christmas (1998)",
        ]
        self.assertEqual(filtered_dict, expected_resp)

    def testSearchWarInTitle(self):
        search_word = "war"
        search = Search()
        filtered_dict = search.resultsTop5(search_word)
        expected_resp = [
            "War of the Worlds (2005)",
            "War Horse (2011)",
            "WarGames (1983)",
            "Warriors (1994)",
            "Cold War (2018)",
        ]
        self.assertEqual(filtered_dict, expected_resp)

    def testSearchAmericanInTitle(self):
        search_word = "american"
        search = Search()
        filtered_dict = search.resultsTop5(search_word)
        expected_resp = [
            "American Beauty (1999)",
            "American History X (1998)",
            "American Hustle (2013)",
            "American Psycho (2000)",
            "American Sniper (2014)",
        ]
        self.assertEqual(filtered_dict, expected_resp)

    def testSearchWorldInTitle(self):
        search_word = "world"
        search = Search()
        filtered_dict = search.resultsTop5(search_word)
        expected_resp = [
            "War of the Worlds (2005)",
            "World War Z (2013)",
            "World Is Not Enough, The (1999)",
            "Jurassic World (2015)",
            "Master of the World (1961)",
        ]
        self.assertEqual(filtered_dict, expected_resp)

    def testSearchNightInTitle(self):
        search_word = "night"
        search = Search()
        filtered_dict = search.resultsTop5(search_word)
        expected_resp = [
            "Night at the Museum (2006)",
            "Night of the Living Dead (1968)",
            "Saturday Night Fever (1977)",
            "Date Night (2010)",
            "Nightmare Before Christmas, The (1993)",
        ]
        self.assertEqual(filtered_dict, expected_resp)

    def testSearchStarInTitle(self):
        search_word = "star"
        search = Search()
        filtered_dict = search.resultsTop5(search_word)
        expected_resp = [
            "Star Wars (1977)",
            "Star Trek: The Motion Picture (1979)",
            "Star Trek II: The Wrath of Khan (1982)",
            "Star Wars: Episode V - The Empire Strikes Back (1980)",
            "Star Wars: Episode VI - Return of the Jedi (1983)",
        ]
        self.assertEqual(filtered_dict, expected_resp)

    def testSearchLifeInTitle(self):
        search_word = "life"
        search = Search()
        filtered_dict = search.resultsTop5(search_word)
        expected_resp = [
            "Life of Brian (1979)",
            "Life Aquatic with Steve Zissou, The (2004)",
            "Life Is Beautiful (1997)",
            "Tree of Life, The (2011)",
            "Life and Nothing But (1989)",
        ]
        self.assertEqual(filtered_dict, expected_resp)

    def testSearchGirlInTitle(self):
        search_word = "girl"
        search = Search()
        filtered_dict = search.resultsTop5(search_word)
        expected_resp = [
            "Girl with a Pearl Earring (2003)",
            "Girl, Interrupted (1999)",
            "Girl Next Door, The (2004)",
            "Girl on the Train, The (2016)",
            "Gone Girl (2014)",
        ]
        self.assertEqual(filtered_dict, expected_resp)

    def testSearchKingInTitle(self):
        search_word = "king"
        search = Search()
        filtered_dict = search.resultsTop5(search_word)
        expected_resp = [
            "Lion King, The (1994)",
            "King Kong (1933)",
            "King's Speech, The (2010)",
            "King Arthur (2004)",
            "King of Comedy, The (1982)",
        ]
        self.assertEqual(filtered_dict, expected_resp)

    def testSearchSecretInTitle(self):
        search_word = "secret"
        search = Search()
        filtered_dict = search.resultsTop5(search_word)
        expected_resp = [
            "Secret Life of Bees, The (2008)",
            "Secret Garden, The (1993)",
            "Secret Window (2004)",
            "Secret in Their Eyes, The (2009)",
            "Secret of Kells, The (2009)",
        ]
        self.assertEqual(filtered_dict, expected_resp)

    def testSearchFutureInTitle(self):
        search_word = "future"
        search = Search()
        filtered_dict = search.resultsTop5(search_word)
        expected_resp = [
            "Back to the Future (1985)",
            "Back to the Future Part II (1989)",
            "Back to the Future Part III (1990)",
            "Futureworld (1976)",
            "Future Shock (1972)",
        ]
        self.assertEqual(filtered_dict, expected_resp)

    def testSearchManInTitle(self):
        search_word = "man"
        search = Search()
        filtered_dict = search.resultsTop5(search_word)
        expected_resp = [
            "Spider-Man (2002)",
            "Man on Fire (2004)",
            "Demolition Man (1993)",
            "Rain Man (1988)",
            "Invisible Man, The (1933)",
        ]
        self.assertEqual(filtered_dict, expected_resp)

    def testSearchWomanInTitle(self):
        search_word = "woman"
        search = Search()
        filtered_dict = search.resultsTop5(search_word)
        expected_resp = [
            "Pretty Woman (1990)",
            "Woman Under the Influence, A (1974)",
            "Woman in the Dunes (1964)",
            "Single White Woman (1992)",
            "My Fair Woman (1995)",
        ]
        self.assertEqual(filtered_dict, expected_resp)

    def testSearchTimeInTitle(self):
        search_word = "time"
        search = Search()
        filtered_dict = search.resultsTop5(search_word)
        expected_resp = [
            "Time Machine, The (1960)",
            "Time After Time (1979)",
            "Out of Time (2003)",
            "Time Bandits (1981)",
            "About Time (2013)",
        ]
        self.assertEqual(filtered_dict, expected_resp)

    def testSearchMagicInTitle(self):
        search_word = "magic"
        search = Search()
        filtered_dict = search.resultsTop5(search_word)
        expected_resp = [
            "Magic Mike (2012)",
            "Practical Magic (1998)",
            "Magic in the Moonlight (2014)",
            "Magic Flute, The (1975)",
            "Magic Sword, The (1962)",
        ]
        self.assertEqual(filtered_dict, expected_resp)

    def testSearchBeautifulInTitle(self):
        search_word = "beautiful"
        search = Search()
        filtered_dict = search.resultsTop5(search_word)
        expected_resp = [
            "Beautiful Mind, A (2001)",
            "Life Is Beautiful (1997)",
            "Beautiful Thing (1996)",
            "Beautiful Girls (1996)",
            "Beautiful Creatures (2013)",
        ]
        self.assertEqual(filtered_dict, expected_resp)

    def testSearchLostInTitle(self):
        search_word = "lost"
        search = Search()
        filtered_dict = search.resultsTop5(search_word)
        expected_resp = [
            "Lost in Translation (2003)",
            "Lost World: Jurassic Park, The (1997)",
            "City of Lost Children, The (1995)",
            "Land of the Lost (2009)",
            "Lost Boys, The (1987)",
        ]
        self.assertEqual(filtered_dict, expected_resp)

if __name__ == "__main__":
    unittest.main()