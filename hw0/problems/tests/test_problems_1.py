import unittest
import sys
sys.path.append("..")

from problems_1.p1_a import (find_index, categorize_number, reverse_list, 
                            process_numbers, string_lengths, even_values_keys, 
                            square_evens, long_strings, convert_to_celsius)
from problems_1.p1_b import (add_element, insert_element_at, remove_element, pop_element_at)
from problems_1.p1_c import (get_keys, get_values, get_items, get_value)
from problems_1.p1_d import (square_all, filter_even, product_of_all)
from problems_1.p1_e import (factorial_rec, factorial_reduce)
from problems_1.p1_advanced import (manage_queue, factorial_dp, linear_search, binary_search)
from io import StringIO


class TestProblem1A(unittest.TestCase):
    """Test cases for Problem 1A functions"""
    
    def test_find_index_found(self):
        """Test find_index when value is found"""
        self.assertEqual(find_index([1, 2, 3, 4], 3), 2)
        self.assertEqual(find_index(['a', 'b', 'c'], 'a'), 0)
        self.assertEqual(find_index([5], 5), 0)
    
    def test_find_index_not_found(self):
        """Test find_index when value is not found"""
        self.assertEqual(find_index([1, 2, 3, 4], 5), -1)
        self.assertEqual(find_index([], 1), -1)
        self.assertEqual(find_index([1, 2, 3], 'a'), -1)
    
    def test_find_index_duplicates(self):
        """Test find_index returns first occurrence"""
        self.assertEqual(find_index([1, 2, 2, 3], 2), 1)
    
    def test_categorize_number_negative(self):
        """Test categorize_number for negative numbers"""
        self.assertEqual(categorize_number(-5), 'negative')
        self.assertEqual(categorize_number(-1), 'negative')
        self.assertEqual(categorize_number(-100), 'negative')
    
    def test_categorize_number_zero(self):
        """Test categorize_number for zero"""
        self.assertEqual(categorize_number(0), 'zero')
    
    def test_categorize_number_positive(self):
        """Test categorize_number for positive numbers"""
        self.assertEqual(categorize_number(1), 'positive')
        self.assertEqual(categorize_number(100), 'positive')
        self.assertEqual(categorize_number(5.5), 'positive')
    
    def test_reverse_list_normal(self):
        """Test reverse_list with normal lists"""
        self.assertEqual(reverse_list([1, 2, 3, 4]), [4, 3, 2, 1])
        self.assertEqual(reverse_list(['a', 'b', 'c']), ['c', 'b', 'a'])
    
    def test_reverse_list_empty(self):
        """Test reverse_list with empty list"""
        self.assertEqual(reverse_list([]), [])
    
    def test_reverse_list_single(self):
        """Test reverse_list with single element"""
        self.assertEqual(reverse_list([1]), [1])
    
    def test_process_numbers_no_negative(self):
        """Test process_numbers with no negative numbers"""
        import sys
        from io import StringIO
        captured_output = StringIO()
        sys.stdout = captured_output
        process_numbers([1, 2, 3, 4])
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "1\n2\n3\n4")
    
    def test_process_numbers_with_negative(self):
        """Test process_numbers stops at negative number"""
        import sys
        from io import StringIO
        captured_output = StringIO()
        sys.stdout = captured_output
        process_numbers([1, 2, -1, 3])
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "1\n2")
    
    def test_process_numbers_with_zero(self):
        """Test process_numbers skips zero"""
        import sys
        from io import StringIO
        captured_output = StringIO()
        sys.stdout = captured_output
        process_numbers([1, 0, 2, 3])
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "1\n2\n3")
    
    def test_string_lengths_normal(self):
        """Test string_lengths with normal input"""
        result = string_lengths(['hello', 'world', 'test'])
        expected = {'hello': 5, 'world': 5, 'test': 4}
        self.assertEqual(result, expected)
    
    def test_string_lengths_empty(self):
        """Test string_lengths with empty list"""
        self.assertEqual(string_lengths([]), {})
    
    def test_string_lengths_empty_strings(self):
        """Test string_lengths with empty strings"""
        result = string_lengths(['', 'a', ''])
        expected = {'': 0, 'a': 1}
        self.assertEqual(result, expected)
    
    def test_even_values_keys_normal(self):
        """Test even_values_keys with normal input"""
        data = {'a': 2, 'b': 3, 'c': 4, 'd': 5}
        result = even_values_keys(data)
        self.assertEqual(set(result), {'a', 'c'})
    
    def test_even_values_keys_no_evens(self):
        """Test even_values_keys with no even values"""
        data = {'a': 1, 'b': 3, 'c': 5}
        result = even_values_keys(data)
        self.assertEqual(result, [])
    
    def test_even_values_keys_all_evens(self):
        """Test even_values_keys with all even values"""
        data = {'a': 2, 'b': 4, 'c': 6}
        result = even_values_keys(data)
        self.assertEqual(set(result), {'a', 'b', 'c'})
    
    def test_square_evens_normal(self):
        """Test square_evens with normal input"""
        result = square_evens([1, 2, 3, 4, 5, 6])
        self.assertEqual(result, [4, 16, 36])
    
    def test_square_evens_no_evens(self):
        """Test square_evens with no even numbers"""
        result = square_evens([1, 3, 5])
        self.assertEqual(result, [])
    
    def test_square_evens_all_evens(self):
        """Test square_evens with all even numbers"""
        result = square_evens([2, 4, 6])
        self.assertEqual(result, [4, 16, 36])
    
    def test_long_strings_normal(self):
        """Test long_strings with normal input"""
        result = long_strings(['hello', 'hi', 'python', 'test', 'programming'])
        self.assertEqual(set(result), {'python', 'programming'})
    
    def test_long_strings_none_long(self):
        """Test long_strings with no long strings"""
        result = long_strings(['hi', 'bye', 'ok'])
        self.assertEqual(result, [])
    
    def test_long_strings_all_long(self):
        """Test long_strings with all long strings"""
        result = long_strings(['python', 'programming', 'computer'])
        self.assertEqual(set(result), {'python', 'programming', 'computer'})
    
    def test_convert_to_celsius_normal(self):
        """Test convert_to_celsius with normal temperatures"""
        result = convert_to_celsius([32, 50, 100])
        expected = ['0.0°C Freezing', '10.0°C', '37.8°C']
        self.assertEqual(result, expected)
    
    def test_convert_to_celsius_below_freezing(self):
        """Test convert_to_celsius with below freezing temperatures"""
        result = convert_to_celsius([0, 20])
        expected = ['-17.8°C Freezing', '-6.7°C Freezing']
        self.assertEqual(result, expected)


class TestProblem1B(unittest.TestCase):
    """Test cases for Problem 1B functions"""
    
    def test_add_element(self):
        """Test add_element function"""
        lst = [1, 2, 3]
        add_element(lst, 4)
        self.assertEqual(lst, [1, 2, 3, 4])
    
    def test_insert_element_at_middle(self):
        """Test insert_element_at in middle"""
        lst = [1, 2, 4]
        insert_element_at(lst, 3, 2)
        self.assertEqual(lst, [1, 2, 3, 4])
    
    def test_insert_element_at_beginning(self):
        """Test insert_element_at at beginning"""
        lst = [2, 3, 4]
        insert_element_at(lst, 1, 0)
        self.assertEqual(lst, [1, 2, 3, 4])
    
    def test_remove_element_exists(self):
        """Test remove_element when element exists"""
        lst = [1, 2, 3, 4]
        remove_element(lst, 2)
        self.assertEqual(lst, [1, 3, 4])
    
    def test_remove_element_not_exists(self):
        """Test remove_element when element doesn't exist"""
        lst = [1, 2, 3, 4]
        remove_element(lst, 5)
        self.assertEqual(lst, [1, 2, 3, 4])  # List should remain unchanged
    
    def test_remove_element_duplicates(self):
        """Test remove_element removes only first occurrence"""
        lst = [1, 2, 2, 3]
        remove_element(lst, 2)
        self.assertEqual(lst, [1, 2, 3])
    
    def test_pop_element_at_valid_index(self):
        """Test pop_element_at with valid index"""
        lst = [1, 2, 3, 4]
        result = pop_element_at(lst, 1)
        self.assertEqual(result, 2)
        self.assertEqual(lst, [1, 3, 4])
    
    def test_pop_element_at_invalid_index(self):
        """Test pop_element_at with invalid index"""
        lst = [1, 2, 3]
        result = pop_element_at(lst, 5)
        self.assertIsNone(result)
        self.assertEqual(lst, [1, 2, 3])  # List should remain unchanged


class TestProblem1C(unittest.TestCase):
    """Test cases for Problem 1C functions"""
    
    def test_get_keys_normal(self):
        """Test get_keys with normal dictionary"""
        data = {'a': 1, 'b': 2, 'c': 3}
        result = get_keys(data)
        self.assertEqual(set(result), {'a', 'b', 'c'})
    
    def test_get_keys_empty(self):
        """Test get_keys with empty dictionary"""
        result = get_keys({})
        self.assertEqual(result, [])
    
    def test_get_values_normal(self):
        """Test get_values with normal dictionary"""
        data = {'a': 1, 'b': 2, 'c': 3}
        result = get_values(data)
        self.assertEqual(set(result), {1, 2, 3})
    
    def test_get_values_empty(self):
        """Test get_values with empty dictionary"""
        result = get_values({})
        self.assertEqual(result, [])
    
    def test_get_items_normal(self):
        """Test get_items with normal dictionary"""
        data = {'a': 1, 'b': 2}
        result = get_items(data)
        self.assertEqual(set(result), {('a', 1), ('b', 2)})
    
    def test_get_items_empty(self):
        """Test get_items with empty dictionary"""
        result = get_items({})
        self.assertEqual(result, [])
    
    def test_get_value_key_exists(self):
        """Test get_value when key exists"""
        data = {'a': 1, 'b': 2}
        result = get_value(data, 'a')
        self.assertEqual(result, 1)
    
    def test_get_value_key_not_exists_default_none(self):
        """Test get_value when key doesn't exist with default None"""
        data = {'a': 1, 'b': 2}
        result = get_value(data, 'c')
        self.assertIsNone(result)
    
    def test_get_value_key_not_exists_custom_default(self):
        """Test get_value when key doesn't exist with custom default"""
        data = {'a': 1, 'b': 2}
        result = get_value(data, 'c', 'default')
        self.assertEqual(result, 'default')


class TestProblem1D(unittest.TestCase):
    """Test cases for Problem 1D functions"""
    
    def test_square_all_normal(self):
        """Test square_all with normal input"""
        result = square_all([1, 2, 3, 4])
        self.assertEqual(result, [1, 4, 9, 16])
    
    def test_square_all_empty(self):
        """Test square_all with empty list"""
        result = square_all([])
        self.assertEqual(result, [])
    
    def test_square_all_negative(self):
        """Test square_all with negative numbers"""
        result = square_all([-2, -3, 2])
        self.assertEqual(result, [4, 9, 4])
    
    def test_filter_even_normal(self):
        """Test filter_even with normal input"""
        result = filter_even([1, 2, 3, 4, 5, 6])
        self.assertEqual(result, [2, 4, 6])
    
    def test_filter_even_no_evens(self):
        """Test filter_even with no even numbers"""
        result = filter_even([1, 3, 5])
        self.assertEqual(result, [])
    
    def test_filter_even_all_evens(self):
        """Test filter_even with all even numbers"""
        result = filter_even([2, 4, 6])
        self.assertEqual(result, [2, 4, 6])
    
    def test_filter_even_empty(self):
        """Test filter_even with empty list"""
        result = filter_even([])
        self.assertEqual(result, [])
    
    def test_product_of_all_normal(self):
        """Test product_of_all with normal input"""
        result = product_of_all([2, 3, 4])
        self.assertEqual(result, 24)
    
    def test_product_of_all_single(self):
        """Test product_of_all with single element"""
        result = product_of_all([5])
        self.assertEqual(result, 5)
    
    def test_product_of_all_with_zero(self):
        """Test product_of_all with zero"""
        result = product_of_all([1, 2, 0, 4])
        self.assertEqual(result, 0)


class TestProblem1E(unittest.TestCase):
    """Test cases for Problem 1E functions"""
    
    def test_factorial_rec_zero(self):
        """Test factorial_rec with 0"""
        self.assertEqual(factorial_rec(0), 1)
    
    def test_factorial_rec_positive(self):
        """Test factorial_rec with positive numbers"""
        self.assertEqual(factorial_rec(1), 1)
        self.assertEqual(factorial_rec(3), 6)
        self.assertEqual(factorial_rec(5), 120)
    
    def test_factorial_reduce_zero(self):
        """Test factorial_reduce with 0"""
        self.assertEqual(factorial_reduce(0), 1)
    
    def test_factorial_reduce_positive(self):
        """Test factorial_reduce with positive numbers"""
        self.assertEqual(factorial_reduce(1), 1)
        self.assertEqual(factorial_reduce(3), 6)
        self.assertEqual(factorial_reduce(5), 120)
    
    def test_factorial_methods_consistency(self):
        """Test that both factorial methods give same results"""
        for n in range(6):
            self.assertEqual(factorial_rec(n), factorial_reduce(n))


class TestProblem1Advanced(unittest.TestCase):
    """Test cases for Problem 1 Advanced functions"""
    
    def test_manage_queue_example(self):
        """Test manage_queue with the provided example"""
        operations = [("enqueue", "Alice"), ("enqueue", "Bob"), ("enqueue", "Charlie"), 
                     ("dequeue",), ("jump", "Eve"), ("remove", "Bob")]
        result = manage_queue(operations)
        self.assertEqual(result, ["Eve", "Charlie"])
    
    def test_manage_queue_enqueue_only(self):
        """Test manage_queue with only enqueue operations"""
        operations = [("enqueue", "Alice"), ("enqueue", "Bob"), ("enqueue", "Charlie")]
        result = manage_queue(operations)
        self.assertEqual(result, ["Alice", "Bob", "Charlie"])
    
    def test_manage_queue_dequeue_only(self):
        """Test manage_queue with enqueue then dequeue operations"""
        operations = [("enqueue", "Alice"), ("enqueue", "Bob"), ("dequeue",), ("dequeue",)]
        result = manage_queue(operations)
        self.assertEqual(result, [])
    
    def test_manage_queue_dequeue_empty(self):
        """Test manage_queue dequeue on empty queue"""
        operations = [("dequeue",)]
        result = manage_queue(operations)
        self.assertEqual(result, [])
    
    def test_manage_queue_remove_existing(self):
        """Test manage_queue remove existing person"""
        operations = [("enqueue", "Alice"), ("enqueue", "Bob"), ("enqueue", "Charlie"), 
                     ("remove", "Bob")]
        result = manage_queue(operations)
        self.assertEqual(result, ["Alice", "Charlie"])
    
    def test_manage_queue_remove_nonexistent(self):
        """Test manage_queue remove non-existent person"""
        operations = [("enqueue", "Alice"), ("enqueue", "Bob"), ("remove", "Charlie")]
        result = manage_queue(operations)
        self.assertEqual(result, ["Alice", "Bob"])
    
    def test_manage_queue_jump_single_person(self):
        """Test manage_queue jump with single person in queue"""
        operations = [("enqueue", "Alice"), ("jump", "Bob")]
        result = manage_queue(operations)
        self.assertEqual(result, ["Alice", "Bob"])
    
    def test_manage_queue_jump_multiple_people(self):
        """Test manage_queue jump with multiple people in queue"""
        operations = [("enqueue", "Alice"), ("enqueue", "Bob"), ("enqueue", "Charlie"), 
                     ("jump", "Dave")]
        result = manage_queue(operations)
        self.assertEqual(result, ["Alice", "Dave", "Bob", "Charlie"])
    
    def test_manage_queue_jump_empty_queue(self):
        """Test manage_queue jump on empty queue"""
        operations = [("jump", "Alice")]
        result = manage_queue(operations)
        self.assertEqual(result, [])
    
    def test_manage_queue_complex_operations(self):
        """Test manage_queue with complex sequence of operations"""
        operations = [
            ("enqueue", "Alice"), 
            ("enqueue", "Bob"), 
            ("enqueue", "Charlie"),
            ("jump", "Dave"),
            ("dequeue",),
            ("enqueue", "Eve"),
            ("remove", "Charlie"),
            ("jump", "Frank")
        ]
        result = manage_queue(operations)
        # Alice dequeued, so queue becomes: [Dave, Bob, Charlie] -> [Dave, Bob] -> [Dave, Bob, Eve] -> [Dave, Frank, Bob, Eve]
        self.assertEqual(result, ["Dave", "Frank", "Bob", "Eve"])
    
    def test_factorial_dp_zero(self):
        """Test factorial_dp with 0"""
        self.assertEqual(factorial_dp(0), 1)
    
    def test_factorial_dp_positive(self):
        """Test factorial_dp with positive numbers"""
        self.assertEqual(factorial_dp(1), 1)
        self.assertEqual(factorial_dp(3), 6)
        self.assertEqual(factorial_dp(5), 120)
        self.assertEqual(factorial_dp(6), 720)
    
    def test_factorial_dp_memoization(self):
        """Test factorial_dp memoization works"""
        # Clear memo to ensure clean test
        factorial_dp.__defaults__[0].clear()
        
        # First call should calculate and store
        result1 = factorial_dp(5)
        # Second call should use memoized value
        result2 = factorial_dp(5)
        
        self.assertEqual(result1, 120)
        self.assertEqual(result2, 120)
        # Check that 5 is in memo
        self.assertIn(5, factorial_dp.__defaults__[0])
    
    def test_linear_search_found(self):
        """Test linear_search when target is found"""
        lst = [1, 3, 5, 7, 9, 11]
        self.assertEqual(linear_search(lst, 5), 2)
        self.assertEqual(linear_search(lst, 1), 0)
        self.assertEqual(linear_search(lst, 11), 5)
    
    def test_linear_search_not_found(self):
        """Test linear_search when target is not found"""
        lst = [1, 3, 5, 7, 9, 11]
        self.assertEqual(linear_search(lst, 4), -1)
        self.assertEqual(linear_search(lst, 12), -1)
        self.assertEqual(linear_search(lst, 0), -1)
    
    def test_linear_search_empty_list(self):
        """Test linear_search with empty list"""
        self.assertEqual(linear_search([], 1), -1)
    
    def test_linear_search_single_element(self):
        """Test linear_search with single element"""
        self.assertEqual(linear_search([5], 5), 0)
        self.assertEqual(linear_search([5], 3), -1)
    
    def test_linear_search_duplicates(self):
        """Test linear_search returns first occurrence"""
        lst = [1, 3, 5, 3, 7]
        self.assertEqual(linear_search(lst, 3), 1)
    
    def test_binary_search_found(self):
        """Test binary_search when target is found"""
        lst = [1, 3, 5, 7, 9, 11, 13, 15]
        self.assertEqual(binary_search(lst, 5), 2)
        self.assertEqual(binary_search(lst, 1), 0)
        self.assertEqual(binary_search(lst, 15), 7)
        self.assertEqual(binary_search(lst, 9), 4)
    
    def test_binary_search_not_found(self):
        """Test binary_search when target is not found"""
        lst = [1, 3, 5, 7, 9, 11, 13, 15]
        self.assertEqual(binary_search(lst, 4), -1)
        self.assertEqual(binary_search(lst, 16), -1)
        self.assertEqual(binary_search(lst, 0), -1)
        self.assertEqual(binary_search(lst, 8), -1)
    
    def test_binary_search_empty_list(self):
        """Test binary_search with empty list"""
        self.assertEqual(binary_search([], 1), -1)
    
    def test_binary_search_single_element(self):
        """Test binary_search with single element"""
        self.assertEqual(binary_search([5], 5), 0)
        self.assertEqual(binary_search([5], 3), -1)
    
    def test_binary_search_two_elements(self):
        """Test binary_search with two elements"""
        self.assertEqual(binary_search([3, 7], 3), 0)
        self.assertEqual(binary_search([3, 7], 7), 1)
        self.assertEqual(binary_search([3, 7], 5), -1)
    
    def test_search_algorithms_consistency(self):
        """Test that linear and binary search give same results on sorted lists"""
        lst = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        test_values = [1, 5, 9, 15, 19, 2, 6, 10, 20, 0]
        
        for value in test_values:
            linear_result = linear_search(lst, value)
            binary_result = binary_search(lst, value)
            self.assertEqual(linear_result, binary_result, 
                           f"Mismatch for value {value}: linear={linear_result}, binary={binary_result}")


if __name__ == '__main__':
    unittest.main()