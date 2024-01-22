from data_maintainer import Data_Maintainer 
import unittest

class test_basics(unittest.TestCase):
    def test_obj_creation(self):
        # test using default file
        obj = Data_Maintainer()
        file = obj.get_data_file()
        self.assertEqual(file, 'gradedata.json')
        
        # test using given file
        obj = Data_Maintainer('other')
        file = obj.get_data_file()
        self.assertEqual(file, 'other')
        

    def test_getters(self):
        dm = Data_Maintainer()

        # test that the getters return the correct attributes
        nats = dm.get_nat_sci()
        nat_sci = set([ 'ANTH', 'ASTR', 'BI', 'CH', 'CIS', 'CIT', 'CPSY', 'ERTH', 'ENVS', 
                                  'GEOG', 'HPHY', 'MATH', 'NEUR', 'PHYS', 'PSY' ])
        self.assertEqual(nats, nat_sci)
        gd = dm.get_grade_data()
        d = None
        self.assertEqual(gd, d)

        # test that the attributes cannot be retrieved without the getters
        with self.assertRaises(AttributeError):
            dm.__natural_sciences
        with self.assertRaises(AttributeError):
            dm.__grade_data
        with self.assertRaises(AttributeError):
            dm.__data_file
        
    def test_setters(self):
        # set data file
        dm = Data_Maintainer()
        dm.set_data_file("non_file")
        file = dm.get_data_file()
        self.assertEqual(file, "non_file")
        # set natural sciences
        nats = dm.get_nat_sci()
        nat_sci = set([ 'ANTH', 'ASTR', 'BI', 'CH', 'CIS', 'CIT', 'CPSY', 'ERTH', 'ENVS', 
                                  'GEOG', 'HPHY', 'MATH', 'NEUR', 'PHYS', 'PSY' ])
        self.assertEqual(nats, nat_sci)
        new_nat = set([ 'ANTH', 'ASTR', 'BI', 'CH', 'CS', 'CIT', 'CPSY', 'ERTH', 'ENVS', 
                                  'GEOG', 'HPHY', 'MATH', 'NEUR', 'PHYS', 'PSY' ])
        dm.set_nat_sci(new_nat)
        nats = dm.get_nat_sci()
        self.assertEqual(nats, new_nat)

class test_validation(unittest.TestCase):
    def test_no_data_file(self):
        dm = Data_Maintainer()
        dm.set_data_file('pi')
        file = dm.get_data_file()
        with self.assertRaises(FileNotFoundError):
            dm.validate_data(file)
        
    def test_wrong_format(self):
        dm = Data_Maintainer()
        dm.set_data_file('gui.py')
        file = dm.get_data_file()
        with self.assertRaises(ValueError):
            dm.validate_data(file)
        
class test_nat_sci_filter(unittest.TestCase):
    def test_compilation(self):
        dm = Data_Maintainer()
        file = dm.get_data_file()
        data = dm.validate_data(file)
        dm.nat_sci_filter(data)

    def test_accuracy(self):
        dm = Data_Maintainer()
        file = dm.get_data_file()
        data = dm.validate_data(file)
        filtered = dm.nat_sci_filter(data)
        # test here that filtered only contains nat sci courses


if __name__ == '__main__' :
    unittest.main()