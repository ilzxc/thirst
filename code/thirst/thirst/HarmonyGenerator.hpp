//
//  HarmonyGenerator.hpp
//  thirst
//
//  Created by Ilya Rostovtsev on 11/2/15.
//  Copyright © 2015 Ilya Rostovtsev. All rights reserved.
//

#ifndef HarmonyGenerator_hpp
#define HarmonyGenerator_hpp

#include <memory>
#include <vector>
#include <math.h>
#include "Random.hpp"

class GenHarmony;

class HarmonyGenerator {
  public:
    HarmonyGenerator( std::vector< std::pair< float, float > > source, int numSolutions = 1, float mutationRate = 0.001f, int numGenerators = 200 );
    
    void setup();
    void update();
    inline float mtof( float midi ) { return ( pow( 2, ( ( midi - 69 ) / 12) ) * 440.0 ); }
    inline bool isDone() { return numSolutions == runCounter; }
    
  private:
    std::vector< float > getFitnesses();
    std::vector< int > scaledFitnesses( const std::vector< float >& fitnesses );
    int scale( float input, float in_min, float in_high, float out_min, float out_high );
    
  private:
    const float mutationRate = 0.f;
    const int numSolutions = 0;
    const int numGenerators = 0;
    int generation;
    int runCounter;
    unsigned long numPartials;
    float lowFreq, highFreq;
    float targetRoughness;
    Random rand;
    std::vector< std::shared_ptr< GenHarmony > > armonie;
};

#endif /* HarmonyGenerator_hpp */
