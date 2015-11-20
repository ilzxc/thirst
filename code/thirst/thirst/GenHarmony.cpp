//
//  GenHarmony.cpp
//  thirst
//
//  Created by Ilya Rostovtsev on 11/2/15.
//  Copyright © 2015 Ilya Rostovtsev. All rights reserved.
//

#include "GenHarmony.hpp"
#include <algorithm>

using namespace std;

#define frequency first
#define amplitude second

GenHarmony::GenHarmony( unsigned long numPartials, float lowNote,
                        float highNote, bool instantiate )
    : freqRange{lowNote, highNote}
{
    aggregate.reserve( numPartials );

    Random rand{lowNote, highNote};

    if ( instantiate ) {
        for ( auto i = 0; i < numPartials; ++i ) {
            aggregate.push_back(
                pair< float, float >{rand.randFreq(), rand.randAmp()} );
        }
        sort( aggregate.begin(), aggregate.end(),
              [=]( const pair< float, float >& a,
                   const pair< float, float >& b ) -> bool {
                  return a.first < b.first;
              } );
    } else {
        for ( auto i = 0; i < numPartials; ++i ) {
            aggregate.push_back( pair< float, float >{0.f, 0.f} );
        }
    }
}

std::ostream& operator<<( std::ostream& lhs, const GenHarmony& rhs )
{
    string result = "";
    for ( const auto& partial : rhs.aggregate ) {
        result += " " + to_string( partial.frequency ) + " " +
                  to_string( partial.amplitude );
    }
    result += ";";
    lhs << result;
    return lhs;
}

void GenHarmony::normalizeAmplitudes()
{
    vector< float > amps;
    amps.reserve( aggregate.size() );
    for ( auto& partial : aggregate )
        amps.push_back( partial.amplitude );

    const float multiplier = 1.f / *max_element( amps.begin(), amps.end() );
    for ( auto& partial : aggregate ) {
        partial.amplitude *= multiplier;
    }
}

void GenHarmony::computeFitness( float target )
{
    fitness = abs( roughness() - target );
}

shared_ptr< GenHarmony >
GenHarmony::crossover( const shared_ptr< GenHarmony > partner ) const
{
    Random rand;
    auto child = make_shared< GenHarmony >( aggregate.size(), freqRange[ 0 ],
                                            freqRange[ 1 ] );
    int midpoint = rand.randInt( static_cast< int >( aggregate.size() ) );
    for ( auto i = 0; i < midpoint; ++i )
        child->aggregate[ i ] = aggregate[ i ];
    for ( auto i = midpoint; i < aggregate.size(); ++i )
        child->aggregate[ i ] = partner->aggregate[ i ];
    return child;
}

void GenHarmony::mutate( float mutationRate )
{
    Random rand{freqRange[ 0 ], freqRange[ 1 ]};
    for ( auto& partial : aggregate ) {
        if ( rand.randAmp() < mutationRate ) {
            partial.frequency = rand.randFreq();
        }
        if ( rand.randAmp() < 0.5f ) {
            partial.amplitude = rand.randAmp();
        }
    }
}
