
import unittest


from quad_solver.quad_solver import validate_input



good_values = [
  (
    "1 2 3",
    { 'valid' : True, 'a' : 1.0, 'b' : 2.0, 'c' : 3.0 }
  ),
  (
    "-1 -2 -3",
    { 'valid' : True, 'a' : -1.0, 'b' : -2.0, 'c' : -3.0 }
  ),
  (
    "1.004 2.004 3.004",
    { 'valid' : True, 'a' : 1.004, 'b' : 2.004, 'c' : 3.004 }
  ),
  (
    "-1.004 -2.004 -3.004",
    { 'valid' : True, 'a' : -1.004, 'b' : -2.004, 'c' : -3.004 }
  ),
]


bad_values = [
  (
    "",
    { 'valid' : False, 'a' : 0.0, 'b' : 0.0, 'c' : 0.0 }
  ),
  (
    "   ",
    { 'valid' : False, 'a' : 0.0, 'b' : 0.0, 'c' : 0.0 }
  ),
  (
    "a b c",
    { 'valid' : False, 'a' : 0.0, 'b' : 0.0, 'c' : 0.0 }
  ),
  (
    "2 3",
    { 'valid' : False, 'a' : 0.0, 'b' : 0.0, 'c' : 0.0 }
  ),
  (
    "1 2 3 4",
    { 'valid' : False, 'a' : 0.0, 'b' : 0.0, 'c' : 0.0 }
  ),
]




class TestValidateInput( unittest.TestCase ):


  def test_good_values( self ):

    for ( input, expect_result ) in good_values :

      print( input )

      actual_result = validate_input( input )

      print( f"expect_valid : { expect_result[ 'valid' ] }, actual_valid : { actual_result[ 'valid' ] }" )


      self.assertEqual( expect_result[ 'valid' ], actual_result[ 'valid' ] )

      self.assertEqual( expect_result[ 'a' ], actual_result[ 'a' ] )
      self.assertEqual( expect_result[ 'b' ], actual_result[ 'b' ] )
      self.assertEqual( expect_result[ 'c' ], actual_result[ 'c' ] )

    # loop through good values

    return
  # test_good_values



  def test_bad_values( self ):

    for ( input, expect_result ) in bad_values :

      print( input )

      actual_result = validate_input( input )

      print( f"expect_valid : { expect_result[ 'valid' ] }, actual_valid : { actual_result[ 'valid' ] }" )


      self.assertEqual( expect_result[ 'valid' ], actual_result[ 'valid' ] )

      self.assertEqual( expect_result[ 'a' ], actual_result[ 'a' ] )
      self.assertEqual( expect_result[ 'b' ], actual_result[ 'b' ] )
      self.assertEqual( expect_result[ 'c' ], actual_result[ 'c' ] )

    # loop through good values

    return
  # test_bad_values


# TestValidateInput






if ( __name__ == "__main__" ):

  unittest.main()



