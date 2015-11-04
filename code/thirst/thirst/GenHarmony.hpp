//
//  GenHarmony.hpp
//  thirst
//
//  Created by Ilya Rostovtsev on 11/2/15.
//  Copyright © 2015 Ilya Rostovtsev. All rights reserved.
//

#ifndef GenHarmony_hpp
#define GenHarmony_hpp

#include <memory>
#include <vector>
#include <math.h>
#include "Roughness.hpp"
#include "Random.hpp"

class GenHarmony
{
  public:
    GenHarmony( unsigned long numPartials, float lowNote, float highNote, bool instantiate = false );
    friend std::ostream& operator<<( std::ostream& lhs, const GenHarmony& rhs );
    inline float getFitness() const { return fitness; }
    
    void normalizeAmplitudes();
    void computeFitness( float target );
    inline float roughness() const { return Roughness::Df( aggregate ); }
    std::shared_ptr< GenHarmony > crossover( const std::shared_ptr< GenHarmony > partner ) const;
    void mutate( float mutationRate );
    
  private:
    inline float ftom( float frequency ) {
        return 69.f + 12.f * ( log( frequency / 440.f ) / log( 2.f ) );
    }
    
  private:
    std::vector< std::pair< float, float > > aggregate;
    float freqRange[ 2 ];
    float fitness;
};

#endif /* GenHarmony_hpp */
