from booklover import BookLover
import unittest

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self):
        # add a book and test if it is in `book_list`.
        lover = BookLover("Ben Pelczynski", "mdg7wj@virginia.edu", "Mystery")
        lover.add_book("Redwall", 5)
        self.assertTrue("Redwall" in lover.book_list.book_name.values)
        
    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        lover = BookLover("Ben Pelczynski", "mdg7wj@virginia.edu", "Mystery")
        lover.add_book("Redwall", 5)
        lover.add_book("Redwall", 5)
        self.assertEqual(len(lover.book_list), 1)
        
    def test_3_has_read(self):
        # pass a book in the list and test if the answer is `True`.
        lover = BookLover("Ben Pelczynski", "mdg7wj@virginia.edu", "Mystery")
        lover.add_book("Redwall", 5)
        self.assertTrue(lover.has_book("Redwall"))
        
    def test_4_has_read(self):
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        lover = BookLover("Ben Pelczynski", "mdg7wj@virginia.edu", "Mystery")
        lover.add_book("Redwall", 5)
        self.assertFalse(lover.has_book("Chain Gang All-Stars"))
        
    def test_5_num_books_read(self):
        # add some books to the list, and test num_books matches expected.
        lover = BookLover("Ben Pelczynski", "mdg7wj@virginia.edu", "Mystery")
        lover.add_book("Redwall", 5)
        lover.add_book("The 7½ Deaths of Evelyn Hardcastle", 4)
        lover.add_book("Three Assassins", 2)
        self.assertEqual(lover.num_books_read(), 3)
        
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3.
        lover = BookLover("Ben Pelczynski", "mdg7wj@virginia.edu", "Mystery")
        lover.add_book("Redwall", 5)
        lover.add_book("The 7½ Deaths of Evelyn Hardcastle", 4)
        lover.add_book("Three Assassins", 2)
        self.assertTrue(x > 3 for x in lover.fav_books().book_rating.values)
        
if __name__ == '__main__':
    unittest.main(verbosity=3)
    
#--------------------------------------------------------------------------------------------------------------------