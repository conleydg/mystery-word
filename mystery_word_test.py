import unittest
from mystery_word import *

class make_something_up(unittest.TestCase):

    # def test_assert_true(self):
    #     self.assertTrue(my_module.is_true())
   #
   # def test_assert_equal(self):
   #      self.assertEqual(my_module.get_one(), 1)

   # def test_assert_equal(self):
   #     self.assertEqual((len(mystery_word.chose_word_difficulty_based('easy', ['abcd', 'abce', 'aadf'], ['qwertyr', 'qazxswe'], ['qazwsxedc', 'cdewsxzaq']))), 4)

    def test_assert_the_truth(self):
       self.assertTrue(True)

    def test_hit(self):
       self.assertTrue(is_guess_hit_or_miss('a', 'apple'))

    def test_miss(self):
       self.assertFalse(is_guess_hit_or_miss('f', 'apple'))

    def test_word_list_easy(self):
        self.assertEqual(chose_word_difficulty_based('easy', ['easy word'], ['normal word'], ['hard word']), 'easy word')

    def test_word_list_normal(self):
        self.assertEqual(chose_word_difficulty_based('normal', ['easy word'], ['normal word'], ['hard word']), 'normal word')

    def test_word_list_hard(self):
        self.assertEqual(chose_word_difficulty_based('hard', ['easy word'], ['normal word'], ['hard word']), 'hard word')

    def test_word_list_not_equald(self):
        self.assertNotEqual(chose_word_difficulty_based('hard', ['easy word'], ['normal word'], ['hard word']), 'easy word')

    def test_win(self):
        self.assertTrue(win_or_lose('hello', ['h', 'e', 'l', 'o']))

    def test_win_without_finishing(self):
        self.assertFalse(win_or_lose('hello', ['h', 'e', 'l']))





if __name__ == '__main__':
    unittest.main()
