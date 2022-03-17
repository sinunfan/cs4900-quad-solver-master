
from math import sqrt




STABILITY_CHANGE_IN_ABC = 0.001

STABILITY_MAX_X_CHANGE = 0.1




def prompt_for_abc():

  print( "please enter a, b, c : " )

  return
# prompt_for_abc



def read_input_for_abc():

  abc_line = input()

  return abc_line
# read_input_for_abc



def validate_input(
  input
):

  results = {
    'valid' : True,
    'a' : 0.0, 'b' : 0.0, 'c' : 0.0
  }


  try :

    tokens = input.split( ' ' )

    if ( len( tokens ) != 3 ) :

      results[ 'valid' ] = False
      return results
    # invalid number of tokens


    results[ 'a' ] = float( tokens[ 0 ] )
    results[ 'b' ] = float( tokens[ 1 ] )
    results[ 'c' ] = float( tokens[ 2 ] )

  # try
  except :

    results[ 'valid' ] = False
  
  # except


  return results
# validate_input



def check_stable(
  a, b, c
):

  normal_result = calculate_roots( a, b, c )
  
  increased_result = calculate_roots( a, b, c )
  
  decreased_result = calculate_roots( a, b, c )
  
  return
# check_stable



def calculate_roots(
  a, b, c
):

  roots = []


  discriminant = b * b - 4 * a * c


  if (
    ( discriminant < 0 )
    or (
      ( a == 0 )
      and ( c == 0 )
    )
  ):

    return roots
  # no real roots



  if ( discriminant > 0 ):

    x1 = (
      ( -b + sqrt( discriminant ) )
      / ( 2 * a ) 
    )

    x2 = (
      ( -b - sqrt( discriminant ) )
      / ( 2 * a ) 
    )

    roots = [ x1, x2 ]

    roots.sort()

  # discriminant > 0
  elif ( ( discriminant == 0 ) and ( a != 0 ) ):

    x1 = (
      -b
      / ( 2 * a ) 
    )

    roots = [ x1, x1 ]

  # discriminant == 0 and a != 0


  return roots
# calculate_roots



# TODO : rename to indicate that it returns a message/string
def display_calculation_results(
  roots
):

  # todo : stuff about stability, formatting


  num_roots = len( roots )

  message = ""

  if ( num_roots == 0 ):

    message = "no real roots"
  
  # num_roots == 0
  elif ( num_roots == 1 ):

    x1 = roots[ 0 ]

    message = "x1 : {}".format( x1 )
  
  # num_roots == 1
  else : # ( num_roots == 2 ):

    x1 = roots[ 0 ]
    x2 = roots[ 1 ]

    message = "x1 : {}, x2 : {}".format( x1, x2 )
  
  # num_roots == 2


  return message
# display_calculation_results




def __main__():
  print( "enter main" )


  while ( True ):
  
    input_results = { 'valid' : False }
    
    while ( input_results[ 'valid'] == False ):

      prompt_for_abc()

      input_results = validate_input( read_input_for_abc() )

    # prompt until valid input is received
      

    a = input_results[ 'a' ]
    b = input_results[ 'b' ]
    c = input_results[ 'c' ]

    calculation_results = calculate_roots( a, b, c )

    message = display_calculation_results( calculation_results )

    print( message )
  
  # main loop

  return
# __main__




if ( __name__ == "__main__" ):

  __main__()

