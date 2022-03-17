
import unittest


from quad_solver.quad_solver import calculate_roots



good_values = [
  # ( a, b, c, expect_roots )
  #( 6, 11, -35 ),
  ( 2, -4, -2, [ -0.41421356237309515, 2.414213562373095 ] ),
  #( -4, -7, 12 ),
  #( 20, -15, -10 ),
  #( 1, -1, -3 ),
  #( 5, -2, -9 ),
  #( 3, 4, 2 ),
  #( -1, 6, 18 ),
  ( 1, -1, -6, [ -2, 3 ] ),
  ( 1, 7, 6, [ -6, -1 ] ),
  ( 1, -5, -6, [ -1, 6 ] ),
]


class TestCalculateRoots( unittest.TestCase ):


  def test_good_values( self ):

    for ( a, b, c, expect_roots ) in good_values :

      print( f'a : { a }, b : { b }, c : { c }' )

      actual_roots = calculate_roots( a, b, c )

      expect_num_roots = len( expect_roots )
      actual_num_roots = len( actual_roots )

      print( f'expect_num_roots : { expect_num_roots }, actual_num_roots : { actual_num_roots }' )


      #self.assertEqual( result[ 'valid' ], True )
      self.assertEqual( expect_num_roots, actual_num_roots )


      if ( actual_num_roots >= 1 ):

        expect_x1 = expect_roots[ 0 ]
        actual_x1 = actual_roots[ 0 ]

        print( f'expect_x1 : { expect_x1 }, actual_x1 : { actual_x1 }' )

        self.assertAlmostEqual( expect_x1, actual_x1 )

      # compare actual and expected x1


      if ( actual_num_roots == 2 ):

        expect_x2 = expect_roots[ 1 ]
        actual_x2 = actual_roots[ 1 ]

        print( f'expect_x2 : { expect_x2 }, actual_x2 : { actual_x2 }' )

        self.assertAlmostEqual( expect_x2, actual_x2 )

      # compare actual and expected x2

    # loop through good values

    return
  # test_good_values


# TestCalculateRoots






if ( __name__ == "__main__" ):

  unittest.main()


