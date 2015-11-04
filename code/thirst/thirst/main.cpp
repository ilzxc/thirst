//
//  main.cpp
//  thirst
//
//  Created by Ilya Rostovtsev on 11/2/15.
//  Copyright © 2015 Ilya Rostovtsev. All rights reserved.
//

#include <iostream>
#include <vector>
#include <memory>
#include "HarmonyGenerator.hpp"

using namespace std;

vector< pair< float, float > > deinterleave( vector< float > input )
{
    vector< pair< float, float > > result;
    for ( auto i = 0; i < input.size(); i += 2 ) {
        result.emplace_back( pair< float, float >( input[ i ], input[ i + 1 ] ) );
    }
    return result;
}

int main( int argc, const char * argv[] )
{
    if ( argc < 6 ) {
        cerr << "Usage: ./thirst <number solutions> < freq/amp pairs >" << endl;
        return -1;
    }
    
    auto numSolutions = atoi( argv[ 1 ] );
    
    vector< float > input;
    input.reserve( argc - 2 );
    for ( auto i = 2; i < argc; ++i ) {
        input.push_back( atof( argv[ i ] ) );
    }
    
    if ( input.size() % 2 != 0 ) {
        cerr << "Input array is odd, need freq/amp pairs." << endl;
        return -2;
    }
    
    auto source = deinterleave( input );
    
    auto test = make_shared< HarmonyGenerator >( source, numSolutions, source.size() / 0.005f );
    test->setup();
    while ( ! test->isDone() )
        test->update();
    
    return 0;
}
