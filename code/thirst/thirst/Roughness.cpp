//
//  Roughness.cpp
//  thirst
//
//  Created by Ilya Rostovtsev on 11/2/15.
//  Copyright © 2015 Ilya Rostovtsev. All rights reserved.
//

#include "Roughness.hpp"
#include <math.h>

#define frequency first
#define amplitude second

using namespace std;

aggregate_t Roughness::normalizeAmplitudes( const aggregate_t& aggregate )
{
    auto result = aggregate;
    
    vector< float > amps;
    amps.reserve( result.size() );
    for ( auto& partial : result ) amps.push_back( partial.amplitude );
    
    const float multiplier = 1.f / *std::max_element( amps.begin(), amps.end() );
    for ( auto& partial : result ) partial.amplitude *= multiplier;
    
    return result;
}

float Roughness::Df( const aggregate_t& aggregate )
{
    auto sum = 0.f;
    
    for ( const auto& partial1 : aggregate ) {
        for ( const auto& partial2 : aggregate ) {
            sum += d( partial1.frequency, partial2.frequency, partial1.amplitude, partial2.amplitude );
        }
    }
    
    return sum;
}

float Roughness::d( float f1, float f2, float amp1, float amp2 )
{
    constexpr float dStar = 0.24f;
    constexpr float a1 = -3.5f;
    constexpr float a2 = -5.75f;
    constexpr float s1 = 0.0207f;
    constexpr float s2 = 18.96f;
    
    const float fmin = min( f1, f2 );
    const float x = fabs( f2 - f1 );
    const float s = dStar / ( s1 * fmin + s2 );
    
    return min( amp1, amp2 ) * ( exp( a1 * s * x ) - exp( a2 * s * x ) );
}