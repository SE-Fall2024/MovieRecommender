import unittest
import warnings

import sys
import os


from Code.recommenderapp.movierecommender.routes import get_movie_info


warnings.filterwarnings("ignore")


class Tests(unittest.TestCase):
    def testToyStory(self):
        result = get_movie_info("Toy Story (1995)")
        self.assertTrue(result['imdbRating']=='8.3')


    def testJumanji(self):
        result = get_movie_info("Jumanji (1995)")
        self.assertTrue(result['imdbRating']=='7.1')

    def testOld(self):
        result = get_movie_info("Grumpier Old Men (1995)")
        self.assertTrue(result['imdbRating']=='6.7')

    def testExhale(self):
        result = get_movie_info("Waiting to Exhale (1995)")
        self.assertTrue(result['imdbRating']=='6.0')

    def testFather(self):
        result = get_movie_info("Father of the Bride Part II (1995)")
        self.assertTrue(result['imdbRating']=='6.1')

    def testAntz(self):
        result = get_movie_info("Antz (1998)")
        self.assertTrue(result['imdbRating']=='6.5')
  
    def testShrek(self):
        result = get_movie_info("Shrek (2001)")
        self.assertTrue(result['imdbRating']=='7.9')

    def testLammbock(self):
        result = get_movie_info("Lammbock (2001)")
        self.assertTrue(result['imdbRating']=='7.2')

    def testLiving(self):
        result = get_movie_info("Desperate Living (1977)")
        self.assertTrue(result['imdbRating']=='7.0')
    def testMogambo(self):
        result = get_movie_info("Mogambo (1953)")
        self.assertTrue(result['imdbRating']=='6.6')

    def testCamelot(self):
        result = get_movie_info("Camelot (1967)")
        self.assertTrue(result['imdbRating']=='6.5')

    def testFire(self):
        result = get_movie_info("Man on Fire (2004)")
        self.assertTrue(result['imdbRating']=='7.7')

    def testArrival(self):
        result = get_movie_info("Arrival, The (1996)")
        self.assertTrue(result['imdbRating']=='6.1')

    def testPulse(self):
        result = get_movie_info("Pulse (2006)")
        self.assertTrue(result['imdbRating']=='4.7')

    def testStealth(self):
        result = get_movie_info("Stealth (2005)")
        self.assertTrue(result['imdbRating']=='5.1')

    def testSoldier(self):
        result = get_movie_info("Universal Soldier: Day of Reckoning (2012)")
        self.assertTrue(result['imdbRating']=='5.1')

    def testChitty(self):
        result = get_movie_info("Chitty Chitty Bang Bang (1968)")
        self.assertTrue(result['imdbRating']=='6.9')

    def testMichael(self):
        result = get_movie_info("Michael (1996)")
        self.assertTrue(result['imdbRating']=='5.7')
      
    def testMelancholia(self):
        result = get_movie_info("Melancholia (2011)")
        self.assertTrue(result['imdbRating']=='7.1')

    def testWhite(self):
        result = get_movie_info("White Oleander (2002)")
        self.assertTrue(result['imdbRating']=='7.1')
   
  

if __name__ == "__main__":
    unittest.main()
