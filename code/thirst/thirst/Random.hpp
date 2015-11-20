//
//  Random.hpp
//  thirst
//
//  Created by Ilya Rostovtsev on 11/2/15.
//  Copyright © 2015 Ilya Rostovtsev. All rights reserved.
//

#ifndef Random_hpp
#define Random_hpp

#include <stdio.h>
#include <random>

class Random
{
  public:
    Random() : Random( 0.f, 16000.f ) {}
    Random( float flow, float fhigh )
        : gen{rd()}, fdist{flow, fhigh}, udist{0., 1.}
    {
    }
    inline float randFreq() { return fdist( gen ); }
    inline float randAmp() { return udist( gen ); }
    inline float randInt( int max )
    {
        std::uniform_int_distribution<> disI{0, max};
        return disI( gen );
    }
    inline void setBounds( float flow, float fhigh )
    {
        fdist = std::uniform_real_distribution<>{flow, fhigh};
    }

  private:
    std::random_device rd;
    std::mt19937 gen;
    std::uniform_real_distribution<> fdist;
    std::uniform_real_distribution<> udist;
};

#endif /* Random_hpp */
