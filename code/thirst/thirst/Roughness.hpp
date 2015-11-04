//
//  Roughness.hpp
//  thirst
//
//  Created by Ilya Rostovtsev on 11/2/15.
//  Copyright © 2015 Ilya Rostovtsev. All rights reserved.
//

#ifndef Roughness_hpp
#define Roughness_hpp

#include <vector>

struct Roughness {
    static void normalizeAmplitudes( std::vector< std::pair< float, float > >& aggregate );
    static float Df( const std::vector< std::pair< float, float > >& aggregate );
    static float d( float f1, float f2, float amp1, float amp2 );
};

#endif /* Roughness_hpp */
