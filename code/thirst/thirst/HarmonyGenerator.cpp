//
//  HarmonyGenerator.cpp
//  thirst
//
//  Created by Ilya Rostovtsev on 11/2/15.
//  Copyright © 2015 Ilya Rostovtsev. All rights reserved.
//

#include <iostream>
#include "HarmonyGenerator.hpp"
#include "GenHarmony.hpp"
#include "Roughness.hpp"
#include "Random.hpp"

using namespace std;

HarmonyGenerator::HarmonyGenerator( vector< pair< float, float > > source,
                                    int numSolutions, float mutationRate,
                                    int numGenerators )
    : mutationRate{mutationRate}, numSolutions{numSolutions},
      numGenerators{numGenerators}, generation{0}, runCounter{0}, rand{0.f, 1.f}
{
    lowFreq = mtof( 36.f );   // lowest note given the instrumentation (cello C)
    highFreq = mtof( 107.f ); // B-8
    targetRoughness = Roughness::Df( Roughness::normalizeAmplitudes( source ) );
    numPartials = source.size();
    armonie.reserve( numGenerators );
}

void HarmonyGenerator::setup()
{
    generation = 0;
    armonie.clear();

    /// instantiate harmonies:
    for ( auto i = 0; i < numGenerators; ++i ) {
        armonie.push_back(
            make_shared< GenHarmony >( numPartials, lowFreq, highFreq, true ) );
    }
}

void HarmonyGenerator::update()
{
    float sum = 0.f;

    for ( auto& gen : armonie ) {
        gen->normalizeAmplitudes();
        sum += gen->roughness();
        gen->computeFitness( targetRoughness );
    }

    // cout << "Current population average roughness : " << sum / armonie.size()
    // << " / " << targetRoughness << endl;

    auto fitnesses = getFitnesses();

    for ( auto i = 0; i < fitnesses.size(); ++i ) {
        if ( fitnesses[ i ] < 0.0001f ) {
            cout << runCounter << ", ";
            cout << *armonie[ i ] << endl;
            ++runCounter;
            setup();
            return;
        }
    }

    vector< shared_ptr< GenHarmony > > matingPool;
    matingPool.reserve( armonie.size() * ( armonie.size() / 10 ) );
    auto scaled = scaledFitnesses( fitnesses );
    for ( auto i = 0; i < scaled.size(); ++i ) {
        for ( auto j = 0; j < scaled[ i ]; ++j ) {
            matingPool.emplace_back( armonie[ i ] );
        }
    }

    for ( int i = 0; i < armonie.size(); ++i ) {
        int one = rand.randInt( static_cast< int >( matingPool.size() - 1 ) );
        int two = rand.randInt( static_cast< int >( matingPool.size() - 1 ) );
        auto partnerA = matingPool[ one ];
        auto partnerB = matingPool[ two ];
        auto child = partnerA->crossover( partnerB );
        child->mutate( mutationRate );
        armonie[ i ] = child;
    }

    ++generation;
    if ( generation > 1000 ) {
        setup();
    }
}

vector< float > HarmonyGenerator::getFitnesses()
{
    vector< float > result;
    result.reserve( armonie.size() );
    for ( const auto& gen : armonie )
        result.emplace_back( gen->getFitness() );
    return result;
}

vector< int >
HarmonyGenerator::scaledFitnesses( const vector< float >& fitnesses )
{
    vector< int > result;
    result.reserve( armonie.size() );

    float minfit = *min_element( fitnesses.begin(), fitnesses.end() );
    float maxfit = *max_element( fitnesses.begin(), fitnesses.end() );

    for ( const auto& fit : fitnesses )
        result.emplace_back( scale( fit, minfit, maxfit, 1.f, 30.f ) );

    return result;
}

int HarmonyGenerator::scale( float input, float in_low, float in_high,
                             float out_low, float out_high )
{
    auto in_range = in_high - in_low;
    if ( in_range == 0 )
        return rand.randInt( 30 );
    auto out_range = out_high - out_low;
    auto k = ( out_range / in_range );
    return static_cast< int >( ( input - in_low ) * k + out_low );
}